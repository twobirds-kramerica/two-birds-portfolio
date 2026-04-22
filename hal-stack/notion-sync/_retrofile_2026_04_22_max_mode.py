"""Retro-file 2026-04-22 max-mode triple-ship to Notion Product Backlog.

S-032 + S-033 + S-034 all shipped 2026-04-22 17:08-17:15 EST during a
short max-mode run that followed a 7-trigger empty-queue loop and
RI-006 circuit-break. Paper-trail-filing them as Done entries, plus
one Backlog entry for RI-007 (Drive MCP re-auth + large-file upload
helper) so it's tracked as a pending follow-up.

Mirrors the pattern used by _retrofile_sprints_48_63.py (the 16-entry
batch from the 2026-04-21 max-mode run).

Usage:
    python hal-stack/notion-sync/_retrofile_2026_04_22_max_mode.py

Exits 0 on all-created; 1 on any failure (and logs to SYNC-LOG.md via helpers).
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
create_backlog_item = mod.create_backlog_item

# (item, priority, status, product, type_, notes)
ENTRIES: list[tuple[str, str, str, str, str, str]] = [
    (
        "S-032: DCC wizard UX proof-of-concept (module-1-wizard parallel URL)",
        "P2", "Done", "DCC", "Sprint",
        "digital-confidence commit 36e3763 (+735 lines, 4 new files). "
        "Ships css/wizard.css (~250 lines, tokens-only, flexbox, 56px tap "
        "targets, WCAG AAA, mobile-first 375/768/1024+), js/wizard.js (~140 "
        "lines vanilla, hash-routed steps, native <dialog> help overlay with "
        "showModal focus-trap, Escape close), _templates/module-base-wizard.html "
        "template with {{PLACEHOLDER}} markers, and module-1-wizard.html as "
        "5-step POC with 3 <details> 'Tell me more' collapsibles. Slide-wizard "
        "COEXISTS with long-scroll (design call made in max mode per governance "
        "doc) — existing module-1.html untouched. Fonts: Merriweather + Source "
        "Sans 3 (NOT Inter as pasted prompt demanded — contradicted sovereignty "
        "rule). Next action: Aaron evaluates live at "
        "twobirds-kramerica.github.io/digital-confidence/module-1-wizard.html "
        "and picks replace/coexist/revert."
    ),
    (
        "S-033: 'just go' trigger phrase — RI-006 Fix #1",
        "P1", "Done", "HAL Stack", "Sprint",
        "portfolio commit d0aa1ff. Adds 'just go' to CLAUDE.md TRIGGER COMMANDS "
        "as single-sprint autonomous authorization in normal mode. Does NOT "
        "chain, does NOT persist beyond single sprint, requires pre-pick "
        "git-log-grep per feedback_git_log_grep_proposals memory. Closes the "
        "governance gap that drove this session's 7-trigger empty-queue loop "
        "(see RELIABILITY-ISSUES.md RI-006). Fires #2 + #3 of RI-006 systemic-"
        "fix options remain as future-enhancement candidates; Fix #1 is the "
        "cheapest sufficient baseline."
    ),
    (
        "S-034: DCC theme-color meta tag Warm Hearth alignment (200 pages)",
        "P3", "Done", "DCC", "Sprint",
        "digital-confidence commit e017ea9 (200 files, +200/-200). sed replace "
        "of <meta name=theme-color content=#1565C0> (legacy cool-blue) with "
        "#2A7B6F (Warm Hearth primary) across all 200 HTML pages. Affects "
        "mobile browser chrome (iOS status bar, Android system bars) — now "
        "matches brand rather than pre-Warm-Hearth palette. No visual change "
        "in page body; tokens.css already serves Warm Hearth there. Post-"
        "replace: 0 stale #1565C0 remaining; 203 pages on #2A7B6F (200 fixed "
        "+ 3 from S-032 wizard POC files)."
    ),
    (
        "RI-007 follow-up: Drive MCP re-auth (drive.file scope) + large-file "
        "upload splitter helper",
        "P2", "Backlog", "HAL Stack", "Task",
        "portfolio commit c3cd602. Drive MCP currently under-scoped — search "
        "and create_file both return 'insufficient authentication scopes'. "
        "Blocker on Aaron's 2026-04-22 'copy conversations.json to Drive' "
        "request. Two-part fix: (1) Aaron re-authorises the Google Drive MCP "
        "in claude.ai settings with drive.file scope minimum. (2) Claude Code "
        "builds hal-stack/helpers/drive-upload-split.py that splits large "
        "archives (like the 82 MB conversations.json) by record/conversation-id "
        "into per-file uploads via create_file, since single-call base64 "
        "arguments can't handle >~5-10 MB. LOE after re-auth: ~30-45 min. "
        "Workaround until then: Drive desktop sync or drive.google.com web "
        "upload."
    ),
]


def main() -> int:
    client = NotionClient()
    failures: list[str] = []
    created_ids: list[str] = []

    for (item, priority, status, product, type_, notes) in ENTRIES:
        try:
            page = create_backlog_item(
                client,
                item=item,
                priority=priority,
                status=status,
                owner="Claude Code",
                type_=type_,
                product=product,
                notes=notes,
            )
            created_ids.append(page.get("id", "?"))
            print(f"OK  {item[:72]}")
        except Exception as e:  # noqa: BLE001
            failures.append(f"{item}: {e}")
            print(f"ERR {item[:72]}: {e}")

    print(f"\nCreated: {len(created_ids)} / {len(ENTRIES)}")
    if failures:
        print("Failures:")
        for f in failures:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
