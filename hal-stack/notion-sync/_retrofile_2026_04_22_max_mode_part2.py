"""Retro-file 2026-04-22 max-mode SECOND HALF (S-036 through S-040) to Notion.

Part 1 (_retrofile_2026_04_22_max_mode.py) filed S-032/033/034 + RI-007
follow-up (4 entries). This file covers the five sprints shipped after
the first wrap:
    S-036 DCC stale preconnect/dns-prefetch cleanup
    S-037 cross-repo preconnect sweep (aaron-patzalek + career-coach)
    S-038 module count truth-up (CLAUDE.md)
    S-039 portfolio root README + voice-check compliance
    S-040 Kevin AUDIT progress-update header

Mirrors the pattern used by _retrofile_2026_04_22_max_mode.py.

Usage:
    python hal-stack/notion-sync/_retrofile_2026_04_22_max_mode_part2.py

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
        "S-036: DCC stale Google Fonts + cdnjs preconnect cleanup (sovereignty polish)",
        "P3", "Done", "DCC", "Sprint",
        "digital-confidence commit b59d6dc (43 files, -161 lines). Removed dead "
        "dns-prefetch + preconnect hints for fonts.googleapis.com, "
        "fonts.gstatic.com, and cdnjs.cloudflare.com. These were added in older "
        "perf sprints (841c26e, 9fad906) when fonts came from Google CDN; after "
        "Merriweather + Source Sans 3 self-hosting they only leaked a DNS/TLS "
        "visit-signal to Google without serving any request. Preserved the "
        "www.googletagmanager.com preconnect (still used by consent-gated GA4 + "
        "Microsoft Clarity). Post-cleanup: 0 stale hints remain on 43 pages."
    ),
    (
        "S-037: Cross-repo preconnect sweep (aaron-patzalek + career-coach)",
        "P3", "Done", "HAL Stack", "Sprint",
        "Portable extension of S-036. aaron-patzalek master commit 8dadf5d (2 "
        "files, -4 lines: patches/career-coach-index.html + "
        "patches/kevins-apartment-index.html). career-coach main commit 80ee1e1 "
        "(1 file, -2 lines: beta/index.html). Scanned 7 sibling repos; 5 were "
        "already clean (clarity, kevins-apartment-search, two-birds-innovation, "
        "two-birds-command-centre, quality-dashboard). Same fonts.googleapis + "
        "fonts.gstatic preconnect pattern removed; Inter and DM Sans + DM Serif "
        "Display fonts remain self-hosted on both repos."
    ),
    (
        "S-038: CLAUDE.md module count truth-up (21 to 27 main modules)",
        "P3", "Done", "DCC", "Task",
        "portfolio commit 37ba935 (CLAUDE.md, 1 file +1/-1). Line 39 claimed "
        "'DCC, 241 pages, 21 modules'. Reality: 27 numbered main modules "
        "(module-1 through module-27-*) + module-2-5.html (half-step) + "
        "module-visual-ai.html (bonus) = 29 module-*.html files. Dropped the "
        "'241 pages' claim (almost certainly stale after the 200-page S-034 "
        "theme-color sweep). Updated one-liner now reads: 'DCC, 27 main "
        "modules (module-1 through module-27) + 2 supplementary (module-2-5 "
        "half-step, module-visual-ai bonus), bilingual EN/FR, deployed on "
        "GitHub Pages'. Prevents future Claude instance from confusion."
    ),
    (
        "S-039: Portfolio root README.md + voice-check compliance",
        "P2", "Done", "HAL Stack", "Sprint",
        "portfolio commits c56b087 (+108 lines new README) and 2120457 "
        "(voice-check compliance, replaced 18 em dashes). No README.md "
        "existed in portfolio root before today. Covers orient-in-60-seconds, "
        "sibling repo landscape, sprint loop + trigger commands (including "
        "just go from S-033), governance references, HAL Stack + Notion sync "
        "pointers, key-files table, session-start checklist, Aaron/Scrappy "
        "Pack/Founding Board context. Does NOT duplicate CLAUDE.md (Claude-"
        "facing) nor hal-stack/README.md (HAL-specific); points at those as "
        "authoritative. Voice-check fully compliant: 0 em dashes, 0 banned "
        "words, no participial openers. Ends with compliance tag."
    ),
    (
        "S-040: Kevin AUDIT.md SHIPPED-header — all 5 Top-5 actions closed",
        "P3", "Done", "Kevin's Apartment Search", "Task",
        "kevins-apartment-search main commit c431ee6 (AUDIT.md, +13 lines at "
        "top). AUDIT was written 2026-04-21 before S-KEVIN-HYGIENE (ccc2cd3) "
        "and S-KEVIN-CSP-READY (815f9fd) landed. All 5 of the §9 Top-5 next-"
        "actions shipped in those two commits (#4 broken-link-check is "
        "superseded by #2 listing-availability probe for Kevin's private-tool "
        "use case). Added PROGRESS UPDATE block at top mapping each to its "
        "closure commit with explicit 're-audit fresh, do not reuse §9 list' "
        "guidance. Same pattern as hal-stack/research/dcc-accessibility-"
        "components-proposal.md (b4e1e02). Closes duplicate-work-risk surface "
        "per feedback_git_log_grep_proposals memory."
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
