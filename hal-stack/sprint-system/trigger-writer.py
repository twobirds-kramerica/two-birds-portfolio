"""Write NEXT-SPRINT-TRIGGER.md after a sprint's FINAL STEP.

Design note: this file is a MARKER, not a mechanism. Writing it does NOT
automatically start a new Claude Code session — that requires either:

  (a) Claude Code's `schedule` skill or `/loop` skill (Anthropic-side,
      authenticated with Aaron's session), OR
  (b) Aaron opening a fresh CC session and reading the trigger file.

The watcher-daemon design from the original S-LOOP-ARCHITECT brief can't
spawn authenticated Claude Code sessions — see SESSION-STATE 02:05 EST.

What this file DOES do: records the intended next sprint so whatever
mechanism picks up the baton has authoritative state. If the queue is
empty, writes QUEUE-EMPTY.md instead and logs it — so subsequent runs
know to stop rather than retry.

USAGE:

    python hal-stack/sprint-system/trigger-writer.py --next S-FOO-BAR
    python hal-stack/sprint-system/trigger-writer.py --next-from-notion  # pulls via next-sprint.py logic
    python hal-stack/sprint-system/trigger-writer.py --empty

Exit codes:
  0 — trigger written
  1 — unable to write (filesystem error)
  2 — --next-from-notion used but Notion unreachable
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent

TRIGGER_PATH = REPO_ROOT / "NEXT-SPRINT-TRIGGER.md"
EMPTY_PATH = REPO_ROOT / "QUEUE-EMPTY.md"
LOG_PATH = HERE / "trigger-writer-log.md"

_nc_spec = importlib.util.spec_from_file_location(
    "notion_client_mod", REPO_ROOT / "hal-stack" / "notion-sync" / "notion-client.py"
)
_nc = importlib.util.module_from_spec(_nc_spec)  # type: ignore
_nc_spec.loader.exec_module(_nc)  # type: ignore


def _timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S EST")


def _session_number() -> int:
    """Monotonic-ish counter based on number of past trigger writes in the log."""
    if not LOG_PATH.exists():
        return 1
    return sum(1 for _ in LOG_PATH.open(encoding="utf-8") if _.startswith("- "))+ 1


def _log(line: str) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not LOG_PATH.exists():
        LOG_PATH.write_text(
            "# Trigger Writer Log\n\nAppend-only log of NEXT-SPRINT-TRIGGER.md writes.\n\n",
            encoding="utf-8",
        )
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def write_trigger(sprint_id: str, notes: str | None = None) -> int:
    session = _session_number()
    body = (
        f"# Next Sprint Trigger\n\n"
        f"**Sprint:** {sprint_id}\n"
        f"**Session:** {session}\n"
        f"**Written:** {_timestamp()}\n\n"
        f"## How to execute\n\n"
        f"Open a Claude Code session and type:\n\n"
        f"    next sprint\n\n"
        f"The `next-sprint.py` script will pick up the locked item from Notion.\n\n"
    )
    if notes:
        body += f"## Notes\n\n{notes}\n"

    try:
        TRIGGER_PATH.write_text(body, encoding="utf-8")
        if EMPTY_PATH.exists():
            EMPTY_PATH.unlink()
        _log(f"- {_timestamp()} session-{session}: {sprint_id}")
        print(f"TRIGGER-WRITER: {TRIGGER_PATH.name} written (session {session}, sprint {sprint_id})")
        return 0
    except Exception as e:
        print(f"TRIGGER-WRITER: write failed: {e}", file=sys.stderr)
        return 1


def write_empty() -> int:
    session = _session_number()
    body = (
        f"# Sprint Queue Empty\n\n"
        f"**Written:** {_timestamp()}\n"
        f"**Session:** {session}\n\n"
        f"`next-sprint.py` returned exit code 3 (no Ready item) — there are no more "
        f"Claude-Code-owned sprints Ready to execute. Loop stops here.\n\n"
        f"To resume: file or promote a sprint in Notion Product Backlog "
        f"(Owner=Claude Code, Status=Ready), then delete this file and run `next sprint`.\n"
    )
    try:
        EMPTY_PATH.write_text(body, encoding="utf-8")
        if TRIGGER_PATH.exists():
            TRIGGER_PATH.unlink()
        _log(f"- {_timestamp()} session-{session}: QUEUE-EMPTY")
        print(f"TRIGGER-WRITER: {EMPTY_PATH.name} written (queue empty, loop stops)")
        return 0
    except Exception as e:
        print(f"TRIGGER-WRITER: write failed: {e}", file=sys.stderr)
        return 1


def _next_from_notion() -> str | None:
    """Query Notion for the next Ready Claude-Code sprint. Returns sprint_id or None."""
    try:
        client = _nc.NotionClient()
        cfg = client.config
        clauses = [
            {"property": "Type", "select": {"equals": "Sprint"}},
            {"property": "Owner", "select": {"equals": "Claude Code"}},
            {"property": "Status", "select": {"equals": "Ready"}},
        ]
        pages = client.query_data_source(
            cfg["product_backlog_data_source"], filter_={"and": clauses}
        )
        if not pages:
            return None
        # Priority sort
        priority_order = {p: i for i, p in enumerate(cfg.get("priority_order", ["P0", "P1", "P2", "P3"]))}

        def rank(page: dict) -> tuple:
            prop = page["properties"].get("Priority", {}).get("select")
            pri = prop["name"] if prop else ""
            title_arr = page["properties"].get("Item", {}).get("title", [])
            title = title_arr[0]["plain_text"].lower() if title_arr else ""
            return (priority_order.get(pri, 99), title)

        pages.sort(key=rank)
        top = pages[0]
        title_arr = top["properties"]["Item"]["title"]
        return title_arr[0]["plain_text"] if title_arr else None
    except Exception as e:
        print(f"TRIGGER-WRITER: Notion query failed: {e}", file=sys.stderr)
        raise


def _cli() -> int:
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--next", dest="next_sprint", help="Sprint ID to write as next")
    g.add_argument("--next-from-notion", action="store_true", help="Pull next Ready sprint from Notion")
    g.add_argument("--empty", action="store_true", help="Write QUEUE-EMPTY.md instead")
    p.add_argument("--notes", default=None)
    args = p.parse_args()

    if args.empty:
        return write_empty()
    if args.next_sprint:
        return write_trigger(args.next_sprint, notes=args.notes)
    if args.next_from_notion:
        try:
            sid = _next_from_notion()
        except Exception:
            return 2
        if sid is None:
            return write_empty()
        return write_trigger(sid, notes=args.notes)
    return 1


if __name__ == "__main__":
    sys.exit(_cli())
