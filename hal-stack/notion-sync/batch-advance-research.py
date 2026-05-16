"""Batch-advance all DCC Research DB rows from Research → Spec.

Usage:
    python hal-stack/notion-sync/batch-advance-research.py [--dry-run]

--dry-run prints what would be updated without touching Notion.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# notion-client.py has a hyphen so it can't be imported as a normal module.
_spec = importlib.util.spec_from_file_location("notion_client", HERE / "notion-client.py")
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

NotionClient = _mod.NotionClient
load_config = _mod.load_config
log_sync_event = _mod.log_sync_event
NotionError = _mod.NotionError

DRY_RUN = "--dry-run" in sys.argv


def main() -> int:
    try:
        cfg = load_config()
    except Exception as e:
        print(f"FAIL: config.json: {e}", file=sys.stderr)
        return 2

    try:
        client = NotionClient(config=cfg)
    except RuntimeError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        return 2

    ds_id = cfg.get("kids_research_data_source")
    if not ds_id:
        print("FAIL: 'kids_research_data_source' missing from config.json", file=sys.stderr)
        return 2

    filter_ = {"property": "Status", "select": {"equals": "Research"}}
    try:
        pages = client.query_data_source(ds_id, filter_=filter_)
    except NotionError as e:
        print(f"FAIL: query error: {e}", file=sys.stderr)
        return 1

    if not pages:
        print("No rows at Status=Research found.")
        return 0

    print(f"Found {len(pages)} row(s) at Status=Research.")
    if DRY_RUN:
        print("[DRY RUN -- no changes written]\n")

    updated = 0
    failed = 0

    for page in pages:
        page_id = page.get("id", "")
        title_prop = page.get("properties", {}).get("Skill / Feature", {})
        parts = title_prop.get("title", [])
        skill = "".join(p.get("plain_text", "") for p in parts).strip() or page_id

        if DRY_RUN:
            print(f"  would update: {skill}")
            updated += 1
            continue

        try:
            client.set_select(page_id, "Status", "Spec")
            log_sync_event(f"batch-advance-research: Research->Spec '{skill}' ({page_id})")
            print(f"  OK: {skill}")
            updated += 1
        except NotionError as e:
            print(f"  FAILED: {skill} -- {e}", file=sys.stderr)
            log_sync_event(
                f"batch-advance-research: FAILED Research->Spec '{skill}' ({page_id}): {e}"
            )
            failed += 1

    print(f"\nDone: {updated} updated, {failed} failed.")
    if not DRY_RUN:
        log_sync_event(f"batch-advance-research: {updated} Research→Spec, {failed} failed.")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
