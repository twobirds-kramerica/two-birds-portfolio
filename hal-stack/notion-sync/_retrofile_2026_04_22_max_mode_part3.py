"""Retro-file 2026-04-22 max-mode THIRD HALF (S-042 through S-046) to Notion.

Part 1 (_retrofile_2026_04_22_max_mode.py) filed S-032/033/034 + RI-007 follow-up.
Part 2 (_retrofile_2026_04_22_max_mode_part2.py) filed S-036/037/038/039/040.
This file covers the final 5 sprints shipped in the 17:08-22:40 max-mode window:
    S-042 audit-the-audits (6 AUDIT.md progress headers across 6 repos)
    S-043 TBCC AUDIT header correction (item #5 already shipped)
    S-044 Notion dedupe (archived 3 S-036/037/038 duplicates)
    S-045 Drive upload splitter skeleton (RI-007 structural fix)
    S-046 feedback memory extension (topic-keyword-grep lesson)

Usage (Windows bash, UTF-8 stdout per S-041 lesson):
    PYTHONIOENCODING=utf-8 python hal-stack/notion-sync/_retrofile_2026_04_22_max_mode_part3.py

Exits 0 on all-created; 1 on any failure.
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
        "S-042: Audit-the-audits — PROGRESS UPDATE headers on 6 AUDIT.md files",
        "P2", "Done", "HAL Stack", "Sprint",
        "Extended the S-040 Kevin AUDIT header pattern to 6 more repos. Per-repo "
        "commits: clarity/fe7af3d (2 of 5 Top-5 shipped), career-coach/e76a581 "
        "(3 of 5), aaron-patzalek/4c743cb (3 of 5), two-birds-innovation/92006df "
        "(1 of 5; 4 Aaron-blocked), quality-dashboard/a8620b2 (ALL 5 shipped), "
        "two-birds-command-centre/cf6c177 (4 of 5; #5 meta-description later "
        "found shipped in S-043). Combined with S-040 Kevin header + b4e1e02 "
        "S-030 proposal header, 8 proposal/audit docs now carry SHIPPED-"
        "awareness. RI-003 duplicate-work risk substantially reduced for "
        "future Claude instances."
    ),
    (
        "S-043: TBCC AUDIT header correction — item #5 already shipped in fe605d8",
        "P3", "Done", "Two Birds Command Centre", "Task",
        "two-birds-command-centre main commit d4c3a77. S-042's TBCC header "
        "listed per-page meta description as Open citing the AUDIT text 'was "
        "skipped'. Topic-keyword grep revealed fe605d8 feat(seo) had already "
        "shipped distinct descriptions on all 10 TBCC pages. Corrected to "
        "all-5-closed. Self-reviewed the other 5 S-042 AUDIT headers; all "
        "verified accurate (genuinely-open items are Aaron-input-blocked or "
        "content-design-blocked). Drove the S-046 feedback memory extension."
    ),
    (
        "S-044: Notion dedupe — archived 3 S-036/037/038 duplicates from S-041 crash",
        "P3", "Done", "HAL Stack", "Task",
        "portfolio commit de0276b. _retrofile_2026_04_22_max_mode_part2.py "
        "crashed on Windows cp1252 stdout the first run (S-038 arrow char); "
        "POSTs had succeeded for S-036/037/038 before the crash, UTF-8 retry "
        "created duplicates. New reusable helper "
        "_dedupe_2026_04_22_s036_s037_s038.py: groups pages by title prefix, "
        "keeps oldest per group, archives rest via PATCH {archived: true}. "
        "3/3 archived cleanly. Paper trail now matches ship reality."
    ),
    (
        "S-045: drive-upload-split.py skeleton — RI-007 structural fix",
        "P2", "Done", "HAL Stack", "Sprint",
        "portfolio commit f9544f6. hal-stack/helpers/drive-upload-split.py "
        "(276 lines). Splits JSON-array archives into bounded-size chunks for "
        "per-file MCP upload. Args: --input, --key, --naming template, "
        "--chunk-mb (default 3), --one-record-per-file, --encode-base64, "
        "--dry-run. Emits plan.json for the MCP caller. Dry-run against the "
        "real 82 MB conversations.json validated: 150 records, 28 chunks under "
        "3 MiB cap, 5 records need own-chunks at 3.5-5.7 MiB (long DCC build "
        "sessions). RI-007 no longer a hard blocker — waiting on Aaron's "
        "Drive MCP re-auth with drive.file scope. After re-auth: Claude Code "
        "runs the splitter + loops mcp__claude_ai_Google_Drive__create_file "
        "over plan entries."
    ),
    (
        "S-046: Extend feedback memory with topic-keyword-grep lesson",
        "P3", "Done", "HAL Stack", "Task",
        "Memory file ~/.claude/projects/.../memory/feedback_git_log_grep_proposals.md "
        "gained the S-043 extension. New rule: when verifying AUDIT/proposal "
        "item closure, sprint-ID grep alone isn't sufficient; also grep topic "
        "keywords (e.g. 'meta.description' not just 'S-XXX') and filesystem-"
        "check where relevant. Trust the repo, not the audit narrative. "
        "Memory file is user-scope (not versioned); cross-machine propagation "
        "is a pre-existing HAL Stack architecture gap flagged in SESSION-STATE. "
        "Paper trail for this sprint: commit 091f80b (SESSION-STATE only)."
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
