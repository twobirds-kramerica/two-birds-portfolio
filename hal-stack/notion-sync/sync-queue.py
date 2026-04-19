"""Pull open Claude Code sprints from Notion and write them to
hal-stack/sprint-system/sprint-queue-from-notion.md.

Never modifies sprint-queue.md. On Notion failure, logs the error and exits 1
without touching the generated file. The hand-maintained sprint-queue.md is
the local fallback used by callers.
"""
from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Import notion-client.py (module name has a hyphen, so use importlib).
_spec = importlib.util.spec_from_file_location("notion_client", HERE / "notion-client.py")
_nc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_nc)  # type: ignore[attr-defined]

NotionClient = _nc.NotionClient
NotionError = _nc.NotionError
list_claude_code_sprints = _nc.list_claude_code_sprints
log_sync_event = _nc.log_sync_event
load_config = _nc.load_config


REPO_ROOT = HERE.parent.parent
OUTPUT_PATH = REPO_ROOT / "hal-stack" / "sprint-system" / "sprint-queue-from-notion.md"
LOCAL_QUEUE_PATH = REPO_ROOT / "hal-stack" / "sprint-system" / "sprint-queue.md"


def sort_sprints(sprints: list[dict], priority_order: list[str]) -> list[dict]:
    rank = {p: i for i, p in enumerate(priority_order)}
    status_rank = {"Ready": 0, "In Progress": 1, "Review": 2, "Blocked": 3, "Backlog": 4}
    def key(s: dict) -> tuple[int, int, str]:
        return (
            rank.get(s.get("priority") or "", 99),
            status_rank.get(s.get("status") or "", 99),
            (s.get("item") or "").lower(),
        )
    return sorted(sprints, key=key)


def render_markdown(sprints: list[dict], generated_at: str) -> str:
    lines: list[str] = []
    lines.append("<!--")
    lines.append("STATUS: GENERATED — do not edit by hand.")
    lines.append(f"Generated: {generated_at}")
    lines.append("Source: Notion Product Backlog (Type=Sprint, Owner=Claude Code)")
    lines.append("Local fallback queue: hal-stack/sprint-system/sprint-queue.md")
    lines.append("-->")
    lines.append("")
    lines.append("# Sprint Queue (from Notion)")
    lines.append("")
    lines.append(
        "Auto-generated from the Notion Command Center → Product Backlog. "
        "Sorted by priority, then status, then item name."
    )
    lines.append("")
    lines.append("**Status key:** Ready = run anytime | In Progress = active | "
                 "Blocked = waiting | Review = needs check | Backlog = not ready")
    lines.append("")
    lines.append("| Priority | Status | Item | Product | Notion ID |")
    lines.append("|----------|--------|------|---------|-----------|")
    for s in sprints:
        pri = s.get("priority") or "—"
        status = s.get("status") or "—"
        item = (s.get("item") or "(untitled)").replace("|", "\\|")
        product = s.get("product") or "—"
        pid = s.get("id") or "—"
        lines.append(f"| {pri} | {status} | {item} | {product} | `{pid}` |")
    lines.append("")
    lines.append(f"**Total open sprints:** {len(sprints)}")
    lines.append("")
    return "\n".join(lines)


def write_output(content: str) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(content, encoding="utf-8")


def detect_conflicts(sprints: list[dict]) -> list[str]:
    """Surface anything a human should look at. Conservative heuristics."""
    issues: list[str] = []
    seen_titles: dict[str, str] = {}
    for s in sprints:
        title = (s.get("item") or "").strip().lower()
        if not title:
            issues.append(f"Page {s.get('id')} has no title")
            continue
        if title in seen_titles:
            issues.append(
                f"Duplicate title '{s.get('item')}' "
                f"(pages {seen_titles[title]} and {s.get('id')})"
            )
        else:
            seen_titles[title] = s.get("id", "?")
        if not s.get("priority"):
            issues.append(f"Sprint '{s.get('item')}' has no priority set")
        if not s.get("status"):
            issues.append(f"Sprint '{s.get('item')}' has no status set")
    return issues


def main() -> int:
    try:
        cfg = load_config()
    except Exception as e:
        print(f"FAIL: could not load config.json: {e}", file=sys.stderr)
        return 2
    try:
        client = NotionClient(config=cfg)
    except RuntimeError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        log_sync_event(f"sync-queue aborted: {e}")
        return 2
    try:
        sprints = list_claude_code_sprints(client, exclude_done=True)
    except NotionError as e:
        print(f"FAIL: Notion API unreachable: {e}", file=sys.stderr)
        print("Local fallback: use hal-stack/sprint-system/sprint-queue.md.")
        log_sync_event(f"sync-queue: Notion unreachable — {e}")
        return 1

    priority_order = cfg.get("priority_order", ["P0", "P1", "P2", "P3"])
    sprints = sort_sprints(sprints, priority_order)
    generated_at = datetime.now(timezone.utc).astimezone().strftime(
        "%Y-%m-%d %H:%M %Z"
    )
    content = render_markdown(sprints, generated_at)
    write_output(content)

    conflicts = detect_conflicts(sprints)
    log_sync_event(
        f"sync-queue OK — {len(sprints)} sprint(s) written; "
        f"{len(conflicts)} conflict(s)"
    )
    for c in conflicts:
        log_sync_event(f"  conflict: {c}")

    print(f"Wrote {OUTPUT_PATH} ({len(sprints)} sprint(s)).")
    if conflicts:
        print(f"{len(conflicts)} conflict(s) logged to SYNC-LOG.md:")
        for c in conflicts:
            print(f"  - {c}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
