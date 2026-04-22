"""S-R01-PHASE-RETRO-PART2 — second-pass retro-file for sprints 18-43.

The original retro-file (commit deabcae, sprint 19) covered sprints
1-17. Everything shipped after that (sprints 18 through 43, plus
the couple of audits that were shipped earlier but batched into
the AUDIT.md deliverables) needs its own retro-file pass for Notion
paper-trail completeness.

Files 22 Done entries via create_backlog_item. Zero external input
needed; uses the chunking-aware append_to_rich_text + create_page
helpers proven end-to-end today.

Run once:   python _s_retro_file_2026_04_21_part2.py
"""
from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

spec = importlib.util.spec_from_file_location(
    "nc", os.path.join(HERE, "notion-client.py")
)
nc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nc)


# 22 Done entries — sprints 18 through 43, minus the 14 already filed in
# the original retro (S-KEVIN-HYGIENE, S-CLARITY-PORTABILITY, S-NOTION-
# CREATE-PAGE, S-R01-INFRA, S-R01-PHASE-1c-1l). Ordered roughly
# chronologically for Product Backlog readability.
DONE_ENTRIES = [
    dict(
        item="S-R01-SKILL-GRAPH: 351-line onboarding index for 20-row DCC Kids Research DB",
        product="DCC",
        notes=(
            "Shipped 2026-04-21 (commit 421d842). Durable markdown "
            "doc at hal-stack/research/dcc-kids-skill-graph.md. "
            "Seven sections: coverage matrix, three age-spanning "
            "ladders, prerequisite + reinforcement graph, research-"
            "citation roll-up, how-to-use per audience, known follow-"
            "ups, session provenance. Complements Notion per-skill "
            "depth with cross-skill structure."
        ),
    ),
    dict(
        item="S-R01-PHASE-1f-CYBERTIP-PATCH: Cybertip.ca added to sextortion row",
        product="DCC",
        notes=(
            "Shipped 2026-04-21 (commit 9e4be54). Closed P1 Canadian-"
            "specific follow-up flagged in the sextortion row's own "
            "audit. Appended Canadian parallel to en-CA-Content "
            "(+669 chars) + Research-Source (+858 chars) via "
            "append_to_rich_text. Cybertip.ca (Canadian Centre for "
            "Child Protection since 2002) now named alongside Take It "
            "Down and US CyberTipline."
        ),
    ),
    dict(
        item="S-AARON-HYGIENE: personal brand site HAL Stack rigor pass",
        product="Portfolio",
        notes=(
            "Shipped 2026-04-21 (commit 8908c85 on aaron-patzalek). "
            "Self-host Inter (SIL OFL 1.1), CSP tightened (dropped "
            "fonts.googleapis.com + fonts.gstatic.com), deleted 2 "
            "orphan files (css/style.css 619 lines + js/main.js 20 "
            "lines, both unreferenced dead code), new axe-core CI, "
            "9-section AUDIT.md with top-5 follow-ups. Sovereignty: "
            "L1 -> L3."
        ),
    ),
    dict(
        item="S-TBI-HYGIENE: company brand site audit + a11y baseline + OG meta",
        product="Two Birds Innovation",
        notes=(
            "Shipped 2026-04-21 (commit 2bb65d9 on two-birds-"
            "innovation). Skip-link + <main> landmark + aria-label "
            "on nav + aria-expanded sync on nav-toggle (WCAG 2.4.1 + "
            "4.1.2, all missing). Full OG/robots/canonical metadata "
            "block (link previews on LinkedIn/Slack/email were "
            "blank — critical for revenue-adjacent site). New axe-"
            "core CI. 9-section AUDIT.md."
        ),
    ),
    dict(
        item="S-CC-HYGIENE: Career Coach audit + a11y + SEO + axe CI",
        product="Career Coach",
        notes=(
            "Shipped 2026-04-21 (commit 4f37d4f on career-coach). "
            "lang='en' -> 'en-CA', full SEO/social meta block, skip-"
            "link + <main> landmark, axe-core CI, 9-section AUDIT.md. "
            "Key finding: Career Coach is structurally identical to "
            "pre-portability Clarity; S-CLARITY-PORTABILITY Route-B "
            "pattern applies verbatim (60 min). Top-5 filed."
        ),
    ),
    dict(
        item="S-TEMPLATE-HYGIENE: project template codifies today's learnings",
        product="HAL Stack",
        notes=(
            "Shipped 2026-04-21 (commit f38869b on two-birds-project-"
            "template). Highest-leverage change of the day. Every "
            "future Two Birds project started from this template "
            "inherits accumulated HAL Stack rigor defaults. 10 new "
            "files (663 lines): index.html starter, css/tokens.css + "
            "main.css, fonts/inter/, .github/workflows/axe-core.yml, "
            "AUDIT.md.template, expanded CLAUDE.md (Autonomous Dev "
            "Cycles Rule, Standard Defaults, Commit Conventions), "
            "expanded todo.md."
        ),
    ),
    dict(
        item="S-CC-PORTABILITY: Career Coach LLM provider picker wired end-to-end",
        product="Career Coach",
        notes=(
            "Shipped 2026-04-21 (commit 9d7e44e on career-coach). "
            "Applied S-CLARITY-PORTABILITY pattern (clarity/a5a0d4d) "
            "verbatim. Settings UI gets provider <select> with "
            "conditional key field; 4 llmChat call sites updated to "
            "pass provider; redundant hardcoded model override "
            "dropped from salary-negotiation call. Career Coach "
            "L1 -> L3/L4 (Ollama path = zero external API calls)."
        ),
    ),
    dict(
        item="S-CC-FONTS: Career Coach self-hosts DM Sans + DM Serif Display",
        product="Career Coach",
        notes=(
            "Shipped 2026-04-21 (commit 45d3ddd on career-coach). "
            "Vendored 4 DM Sans weights (~30 KB each) + DM Serif "
            "Display Regular (~24 KB) from googlefonts/dm-fonts (SIL "
            "OFL 1.1). ~145 KB total. Google Fonts preconnects + "
            "@import dropped. <link rel='preload'> for DM Sans "
            "Regular + Bold. Combined with S-CC-PORTABILITY, Career "
            "Coach is fully L3/L4-capable."
        ),
    ),
    dict(
        item="S-CROSS-PROMO: Clarity + Career Coach mutual cross-links",
        product="Portfolio",
        notes=(
            "Shipped 2026-04-21 (commits c5b7fe0 on clarity + "
            "da62d75 on career-coach). Clarity results now show "
            "'Other free tools from Two Birds Innovation' block "
            "linking Career Coach + DCC. Career Coach footer adds "
            "bilingual links to Clarity + DCC. Closes funnel gap "
            "identified in both CC AUDIT and TBI AUDIT."
        ),
    ),
    dict(
        item="S-QD-HYGIENE: Build Quality Dashboard audit + a11y baseline",
        product="Portfolio",
        notes=(
            "Shipped 2026-04-21 (commit 1cc4709 on quality-"
            "dashboard). Internal tool, tighter audit scope since "
            "noindex'd + PIN-gated. lang='en' -> 'en-CA', skip-link "
            "+ main landmark, description meta, axe-core CI, 9-"
            "section AUDIT.md. Top-5 small a11y/polish items."
        ),
    ),
    dict(
        item="S-TBC-HYGIENE: two-birds-command-centre multi-page audit (10 pages)",
        product="Portfolio",
        notes=(
            "Shipped 2026-04-21 (commit 20a166d on two-birds-"
            "command-centre). Last substantial untouched repo. "
            "Multi-page shape; idempotent Python injector "
            "(_build/apply-a11y-baseline.py) applied skip-link + "
            "<main> to all 10 pages in one pass. Shared "
            ".skip-link CSS. axe-core CI scans all 10 pages. 9-"
            "section AUDIT.md."
        ),
    ),
    dict(
        item="HAL: append_to_rich_text auto-chunking upgrade",
        product="HAL Stack",
        notes=(
            "Shipped 2026-04-21 (commit 544ba26). append_to_rich_"
            "text now uses _rich_text chunker to split long text "
            "into <=1900-char blocks on paragraph/newline/space "
            "boundaries. Callers pass single string; chunking "
            "invisible. Closes the implicit TODO filed in S-R01-"
            "PHASE-1f-CYBERTIP-PATCH commit message."
        ),
    ),
    dict(
        item="S-PRIMARY-SOURCE: Piaget/Erikson/Vygotsky/Kohlberg appendix on 12 rows",
        product="DCC",
        notes=(
            "Shipped 2026-04-21 (commit fb94e66). WebSearch-"
            "verified primary publications: Piaget 1952 Origins of "
            "Intelligence in Children, Erikson 1950/1963 Childhood "
            "and Society + 1968 Identity Youth and Crisis, Vygotsky "
            "1978 Mind in Society, Kohlberg 1969 Stage and Sequence. "
            "Standardised appendix (~650 chars) appended to "
            "Research-Source on all 12 DCC Kids Research DB rows "
            "citing those frameworks. 12/12 succeeded; real-world "
            "validation of sprint-31's chunking upgrade."
        ),
    ),
    dict(
        item="S-TBI-STYLE-EXTRACT: move Phase-3 inline CSS to style.css",
        product="Two Birds Innovation",
        notes=(
            "Shipped 2026-04-21 (commit 3b06118 on two-birds-"
            "innovation). ~160-line <style> block moved from "
            "index.html head into css/style.css (section-header "
            "comment). Byte-for-byte preserved. Index drops 495 -> "
            "334 lines. Last inline CSS gone; only inline elements "
            "remaining are schema.org JSON-LD blocks."
        ),
    ),
    dict(
        item="S-AARON-NAV-EXTRACT: move inline nav JS to js/main.js",
        product="Portfolio",
        notes=(
            "Shipped 2026-04-21 (commit e6d3148 on aaron-patzalek). "
            "13-line inline <script> extracted to js/main.js (defer-"
            "loaded). aria-expanded now takes explicit 'true'/"
            "'false' strings. js/ recreated after earlier S-AARON-"
            "HYGIENE deletion of orphan main.js."
        ),
    ),
    dict(
        item="S-QD-FOCUS: quality-dashboard :focus-visible for dark theme",
        product="Portfolio",
        notes=(
            "Shipped 2026-04-21 (commit 90ad085 on quality-"
            "dashboard). Consolidated :focus-visible rules covering "
            "a, button, input, select, textarea, [tabindex]. 3px "
            "teal outline on 2px offset; WCAG AA on every surface. "
            ":focus:not(:focus-visible) suppressed on button/a so "
            "ring only shows on keyboard focus."
        ),
    ),
    dict(
        item="S-QD-CACHE: 60s sessionStorage cache on quality-dashboard GitHub API",
        product="Portfolio",
        notes=(
            "Shipped 2026-04-21 (commit 75da12a on quality-"
            "dashboard). All 4 API helpers (fetchJSON, fileExists, "
            "pagesEnabled, fetchIndexHead) wrapped in 60s "
            "sessionStorage cache keyed by URL. 'qd-cache:' "
            "namespace. Reduces ~30+ fetches per page load to ~1 "
            "per URL per minute; stays well under GitHub's 60/hour "
            "unauthenticated rate limit."
        ),
    ),
    dict(
        item="S-QD-EXTRACT+INDICATOR: inline script -> js/dashboard.js + per-card fetch indicator",
        product="Portfolio",
        notes=(
            "Shipped 2026-04-21 (commit 7bce8ef on quality-"
            "dashboard). Two QD AUDIT items in one sprint. 754-line "
            "<script> block extracted to js/dashboard.js; "
            "index.html 1928 -> 1173 lines. New cacheTimestamp() "
            "helper reads the cache ts field added in S-QD-CACHE; "
            "renderCard() shows 'Data fetched: 2m ago' per repo."
        ),
    ),
    dict(
        item="S-KEVIN-CSP-READY: inline CSS+JS+9 onclicks extracted",
        product="Portfolio",
        notes=(
            "Shipped 2026-04-21 (commit 815f9fd on kevins-"
            "apartment-search). Final Tier-2 item. 1027-line CSS "
            "-> css/kevin.css; 1417-line JS -> js/kevin.js; 9 "
            "onclick= attrs -> data-action + data-crit, dispatched "
            "via existing delegated click listener. index.html "
            "2803 -> 359 lines. Kevin's now fully CSP-ready on "
            "the main page."
        ),
    ),
    dict(
        item="S-DCC-VIS-STYLEGUIDE-STABLE: 4th attempt failed; reverted with lessons",
        product="DCC",
        notes=(
            "Attempted + reverted 2026-04-21 (commit 7056da2 on "
            "digital-confidence). Tried waitForSelector + Playwright "
            "mask on kbd-help + S-030. Update mode passed; compare "
            "mode failed with same 'two consecutive stable "
            "screenshots' error as previous 3 attempts. Reverted; "
            "styleguide excluded again. File header documents all "
            "4 techniques tried + 2 honest future-fix options. "
            "Signal: surface is intrinsically pixel-noisy."
        ),
    ),
    dict(
        item="HAL: end-of-session context export + patterns library + CLAUDE.md pointers",
        product="HAL Stack",
        notes=(
            "Sprints 40-42 shipped 2026-04-22 00:04-00:20 EST. "
            "(a) exports/2026-04-21-max-mode-39-sprints.md — 153-"
            "line consolidated session summary. "
            "(b) research/autonomous-dev-patterns-v1.md — 13 "
            "reusable patterns distilled from today's sprints. "
            "(c) portfolio CLAUDE.md updated with pointers to "
            "today's durable artefacts + full notion-sync helper "
            "surface. Every future session sees today's outputs "
            "via auto-load. Commits: 72a880b, 20484dc, 2920f90."
        ),
    ),
    dict(
        item="HAL: session close — RETRO.md overwrite",
        product="HAL Stack",
        notes=(
            "Shipped 2026-04-22 ~00:20 EST (commit f32cef3). "
            "Closes the CLAUDE.md standing rule 'After every "
            "session: overwrite logs/RETRO.md and push.' Previous "
            "content was from 2026-04-16; replaced with today's "
            "42-sprint retro covering what shipped, what didn't "
            "work, what needs Aaron (P0/P1/P2), 8/9 coverage, how-"
            "to-resume, and session provenance."
        ),
    ),
]


def main() -> int:
    client = nc.NotionClient()
    created = []
    failures = []

    print(f"=== Filing {len(DONE_ENTRIES)} DONE entries (retro part 2) ===\n")
    for entry in DONE_ENTRIES:
        print(f"--- {entry['item'][:70]} ---")
        try:
            page = nc.create_backlog_item(
                client,
                item=entry["item"],
                priority="P0",
                status="Done",
                owner="Claude Code",
                type_="Sprint",
                product=entry.get("product"),
                notes=entry.get("notes"),
            )
            pid = page.get("id")
            print(f"OK: {pid}")
            created.append(entry["item"])
        except Exception as e:
            print(f"FAIL: {type(e).__name__}: {e}")
            failures.append((entry["item"], str(e)))
        print()

    print("=" * 70)
    print(f"SUMMARY: {len(created)} filed, {len(failures)} failed")
    if failures:
        for item, err in failures:
            print(f"  FAIL — {item}: {err}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
