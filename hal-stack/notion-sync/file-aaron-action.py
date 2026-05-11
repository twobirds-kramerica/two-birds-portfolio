"""File an Aaron-facing action item directly into the Notion Product Backlog.

Usage:
    python file-aaron-action.py "Action description" [P1|P2|P3] [--notes "context"]

Defaults:
    priority = P2
    notes    = (empty)

Creates a Notion backlog item:
    Owner  = Aaron
    Status = Backlog
    Type   = Task
    Item   = <description>

This script is called at the end of every sprint for any item in
"Next recommended action for Aaron" that requires a decision or
explicit human action. Ensures no Aaron-facing item gets buried in
SESSION-STATE and lost between sessions.

Exit codes:
    0 — filed successfully
    1 — Notion API error
    2 — config / auth error
    64 — bad usage
"""
from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

_spec = importlib.util.spec_from_file_location("nc", HERE / "notion-client.py")
_nc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_nc)  # type: ignore[attr-defined]

NotionClient = _nc.NotionClient
NotionError = _nc.NotionError
load_config = _nc.load_config
log_sync_event = _nc.log_sync_event

VALID_PRIORITIES = {"P0", "P1", "P2", "P3"}


def usage() -> int:
    print(
        'Usage: python file-aaron-action.py "Action description" [P1|P2|P3] [--notes "context"]',
        file=sys.stderr,
    )
    return 64


def parse_args(argv: list[str]) -> tuple[str, str, str] | None:
    """Return (description, priority, notes) or None on bad args."""
    args = argv[1:]
    if not args:
        return None

    description = args[0].strip()
    if not description:
        return None

    priority = "P2"
    notes = ""

    i = 1
    while i < len(args):
        arg = args[i]
        if arg.upper() in VALID_PRIORITIES:
            priority = arg.upper()
        elif arg == "--notes" and i + 1 < len(args):
            notes = args[i + 1]
            i += 1
        i += 1

    return description, priority, notes


def file_action(description: str, priority: str = "P2", notes: str = "") -> dict:
    """Create an Aaron action item in the Notion Product Backlog.

    Returns the created page object.
    Raises NotionError on API failure.
    """
    try:
        cfg = load_config()
    except Exception as e:
        raise RuntimeError(f"could not load config.json: {e}") from e

    client = NotionClient(config=cfg)
    data_source_id = cfg["product_backlog_data_source"]

    ts = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M %Z")
    note_text = f"[{ts}] Auto-filed from sprint — Aaron action required."
    if notes:
        note_text += f"\n{notes}"

    properties: dict = {
        "Item":     {"title":  [{"text": {"content": description}}]},
        "Status":   {"select": {"name": "Backlog"}},
        "Priority": {"select": {"name": priority}},
        "Owner":    {"select": {"name": "Aaron"}},
        "Type":     {"select": {"name": "Task"}},
        "Notes":    {"rich_text": [{"text": {"content": note_text}}]},
    }

    page = client.create_page(data_source_id, properties)
    log_sync_event(
        f"file-aaron-action: filed '{description}' [{priority}] → {page.get('id')}"
    )
    return page


def main(argv: list[str]) -> int:
    parsed = parse_args(argv)
    if parsed is None:
        return usage()

    description, priority, notes = parsed

    try:
        page = file_action(description, priority, notes)
    except RuntimeError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        return 2
    except NotionError as e:
        print(f"FAIL: Notion API error: {e}", file=sys.stderr)
        return 1

    pid = page.get("id", "")
    url = page.get("url", "")
    print(f"FILED: [{priority}] {description}")
    print(f"  id : {pid}")
    print(f"  url: {url}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
