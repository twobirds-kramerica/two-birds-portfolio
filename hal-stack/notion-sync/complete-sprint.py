"""Mark a sprint complete in Notion.

Usage:
    python complete-sprint.py <name-or-page-id> [commit-hash]

  - If the first argument looks like a Notion page ID (UUID, with or without
    dashes), it is treated as an ID. Otherwise the Product Backlog is
    searched case-insensitively by title.
  - Sets Status to Done.
  - Appends a timestamped completion line to Notes. Includes commit hash
    if provided.
  - Logs the completion to SYNC-LOG.md.

Exit codes:
  0 — marked complete
  1 — Notion API unreachable
  2 — config or auth error
  3 — no matching sprint found / ambiguous match
  64 — bad usage
"""
from __future__ import annotations

import importlib.util
import re
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


UUID_RE = re.compile(r"^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$", re.I)


def looks_like_page_id(s: str) -> bool:
    return bool(UUID_RE.match(s.strip()))


def find_by_name(client: NotionClient, name: str) -> list[dict]:
    name_lower = name.strip().lower()
    sprints = list_claude_code_sprints(client, exclude_done=False)
    exact = [s for s in sprints if (s.get("item") or "").strip().lower() == name_lower]
    if exact:
        return exact
    return [s for s in sprints if name_lower in (s.get("item") or "").lower()]


def usage() -> int:
    print(
        "Usage: python complete-sprint.py <name-or-page-id> [commit-hash]",
        file=sys.stderr,
    )
    return 64


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        return usage()
    target = argv[1].strip()
    commit_hash = argv[2].strip() if len(argv) > 2 else ""

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

    if looks_like_page_id(target):
        page_id = target
        display_name = f"(page {page_id})"
    else:
        try:
            matches = find_by_name(client, target)
        except NotionError as e:
            print(f"FAIL: Notion API unreachable: {e}", file=sys.stderr)
            log_sync_event(f"complete-sprint: API unreachable looking up '{target}'")
            return 1
        if not matches:
            print(f"No Claude Code sprint matches '{target}'.")
            return 3
        if len(matches) > 1:
            print(f"Ambiguous name '{target}' — {len(matches)} matches:")
            for m in matches:
                print(f"  {m['id']}  [{m.get('priority')}] {m.get('item')}")
            print("Re-run with a more specific name or the Notion page ID.")
            return 3
        page_id = matches[0]["id"]
        display_name = matches[0].get("item") or page_id

    ts = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M %Z")
    note_parts = [f"[{ts}] DONE"]
    if commit_hash:
        note_parts.append(f"commit {commit_hash}")
    note = " — ".join(note_parts)

    try:
        client.set_select(page_id, "Status", "Done")
    except NotionError as e:
        print(f"FAIL: could not set Status=Done: {e}", file=sys.stderr)
        log_sync_event(f"complete-sprint: set Status failed on {page_id} — {e}")
        return 1

    try:
        client.append_to_rich_text(page_id, "Notes", note)
    except NotionError as e:
        print(f"WARN: Status set to Done but note append failed: {e}", file=sys.stderr)
        log_sync_event(f"complete-sprint: note append failed on {page_id} — {e}")

    log_sync_event(f"complete-sprint: {display_name} ({page_id}) → Done; {note}")
    print(f"DONE: {display_name}")
    print(f"  Notion page: {page_id}")
    print(f"  Note appended: {note}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
