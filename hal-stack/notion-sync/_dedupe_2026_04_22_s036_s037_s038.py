"""Dedupe potential duplicate Notion entries for S-036 / S-037 / S-038.

Context: _retrofile_2026_04_22_max_mode_part2.py crashed on Windows cp1252
stdout encoding the first time it ran, but the POST to Notion succeeded for
entries that printed before the crash. Retry with PYTHONIOENCODING=utf-8
succeeded 5/5 — which means S-036 / S-037 / S-038 may each have 2 Notion
pages.

Strategy:
1. Query Product Backlog for pages whose Item title starts with 'S-036:',
   'S-037:', or 'S-038:' (exact title start).
2. For each title-group with >1 page: keep the OLDEST (earliest created_time);
   archive the rest via PATCH pages/{id} {archived: true}.
3. Log the archive events to SYNC-LOG.md.

Usage (Windows bash, UTF-8 stdout to avoid cp1252 issues):
    PYTHONIOENCODING=utf-8 python hal-stack/notion-sync/_dedupe_2026_04_22_s036_s037_s038.py

Exits 0 on clean dedupe; 1 on any API failure.
"""
from __future__ import annotations
import sys
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("notion_client_mod", HERE / "notion-client.py")
assert SPEC and SPEC.loader
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)  # type: ignore

NotionClient = mod.NotionClient
extract_title = mod.extract_title
log_sync_event = mod.log_sync_event

TARGET_PREFIXES = ("S-036:", "S-037:", "S-038:")


def main() -> int:
    client = NotionClient()
    data_source_id = client.config["product_backlog_data_source"]

    # Query with sort by created_time ascending so oldest-first iteration is cheap.
    pages = client.query_data_source(
        data_source_id,
        sorts=[{"timestamp": "created_time", "direction": "ascending"}],
    )

    groups: dict[str, list[dict]] = {"S-036:": [], "S-037:": [], "S-038:": []}
    for p in pages:
        title = extract_title(p, "Item") or ""
        for prefix in TARGET_PREFIXES:
            if title.startswith(prefix):
                groups[prefix].append(p)
                break

    print("Group sizes:")
    for prefix, plist in groups.items():
        print(f"  {prefix}: {len(plist)} pages")
    print()

    to_archive: list[tuple[str, str, str]] = []  # (page_id, prefix, title)
    for prefix, plist in groups.items():
        if len(plist) <= 1:
            continue
        # keep oldest (index 0 after ascending sort); archive the rest
        for dup in plist[1:]:
            pid = dup.get("id", "?")
            title = extract_title(dup, "Item") or ""
            created = dup.get("created_time", "?")
            print(f"Will archive: {prefix} page {pid} created {created}")
            to_archive.append((pid, prefix, title))

    if not to_archive:
        print("No duplicates found. Exiting clean.")
        return 0

    print(f"\nArchiving {len(to_archive)} duplicate pages...")
    failures: list[str] = []
    for pid, prefix, title in to_archive:
        try:
            # Notion archive is a top-level flag on PATCH pages/{id}
            client._request("PATCH", f"pages/{pid}", {"archived": True})
            log_sync_event(
                f"dedupe S-036-038: archived duplicate {prefix} page {pid} "
                f"('{title[:50]}')"
            )
            print(f"  OK  {pid}")
        except Exception as e:  # noqa: BLE001
            failures.append(f"{pid}: {e}")
            print(f"  ERR {pid}: {e}")

    print(f"\nArchived: {len(to_archive) - len(failures)} / {len(to_archive)}")
    if failures:
        print("Failures:")
        for f in failures:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
