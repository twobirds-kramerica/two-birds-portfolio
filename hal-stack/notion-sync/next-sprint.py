"""Lock the next sprint for Claude Code.

Flow:
  1. Pull fresh Notion data via sync-queue.py logic.
  2. Find the highest-priority Ready item where Owner=Claude Code.
  3. Update that item to In Progress in Notion.
  4. Print the sprint details for Claude Code to execute.
  5. On Notion failure, print a clear fallback message pointing at
     hal-stack/sprint-system/sprint-queue.md.

Exit codes:
  0 — a sprint was locked and printed
  1 — Notion API unreachable (fallback path)
  2 — configuration or auth error
  3 — no Ready sprint found
"""
from __future__ import annotations

import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("notion_client", HERE / "notion-client.py")
_nc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_nc)  # type: ignore[attr-defined]

NotionClient = _nc.NotionClient
NotionError = _nc.NotionError
list_claude_code_sprints = _nc.list_claude_code_sprints
log_sync_event = _nc.log_sync_event
load_config = _nc.load_config


REPO_ROOT = HERE.parent.parent
LOCAL_QUEUE_PATH = REPO_ROOT / "hal-stack" / "sprint-system" / "sprint-queue.md"


def pick_next_ready(sprints: list[dict], priority_order: list[str]) -> dict | None:
    rank = {p: i for i, p in enumerate(priority_order)}
    ready = [s for s in sprints if (s.get("status") or "") == "Ready"]
    if not ready:
        return None
    ready.sort(key=lambda s: (
        rank.get(s.get("priority") or "", 99),
        (s.get("item") or "").lower(),
    ))
    return ready[0]


def fallback_notice(reason: str) -> int:
    print(f"Notion API unavailable ({reason}).")
    print("Falling back to local sprint queue:")
    print(f"  {LOCAL_QUEUE_PATH}")
    print("Claude Code: read that file and execute the top non-blocked READY sprint.")
    log_sync_event(f"next-sprint fallback to local — {reason}")
    return 1


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
        return 2

    try:
        sprints = list_claude_code_sprints(client, exclude_done=True)
    except NotionError as e:
        return fallback_notice(str(e))

    next_item = pick_next_ready(sprints, cfg.get("priority_order", ["P0", "P1", "P2", "P3"]))
    if not next_item:
        print("No Ready Claude Code sprints in Notion.")
        print(f"Check hal-stack/sprint-system/sprint-queue.md for local-only items.")
        log_sync_event("next-sprint: no Ready sprint found")
        return 3

    try:
        client.set_select(next_item["id"], "Status", "In Progress")
    except NotionError as e:
        print(f"WARN: found next sprint but failed to mark In Progress: {e}")
        print("Proceeding without status update. Reconcile manually.")
        log_sync_event(
            f"next-sprint: failed to mark {next_item['id']} In Progress — {e}"
        )

    ts = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M %Z")
    note = f"[{ts}] next-sprint: Ready → In Progress"
    try:
        client.append_to_rich_text(next_item["id"], "Notes", note)
    except NotionError as e:
        log_sync_event(
            f"next-sprint: failed to append lock note to {next_item['id']} — {e}"
        )

    log_sync_event(
        f"next-sprint locked: [{next_item.get('priority')}] "
        f"{next_item.get('item')} ({next_item['id']})"
    )

    payload = {
        "action": "next-sprint",
        "locked_at": ts,
        "sprint": {
            "notion_id": next_item["id"],
            "notion_url": next_item.get("url"),
            "item": next_item.get("item"),
            "priority": next_item.get("priority"),
            "product": next_item.get("product"),
            "status": "In Progress",
            "notes": next_item.get("notes"),
        },
    }
    print("=" * 60)
    print(f"SPRINT LOCKED: [{payload['sprint']['priority']}] {payload['sprint']['item']}")
    print("=" * 60)
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
