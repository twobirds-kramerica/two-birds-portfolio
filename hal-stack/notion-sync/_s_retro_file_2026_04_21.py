"""S-R01-PHASE-RETRO — retroactively file today's sprints in the
Product Backlog as Done Notion entries.

2026-04-21 ran ~18 max-mode sprints, most promoted under max-mode.md's
'last resort' / 'empty queue' clauses, so they never received formal
Notion rows. This script uses create_backlog_item (landed earlier
today in S-NOTION-CREATE-PAGE, a3c8f53) to file each shipped sprint
retroactively as a Done entry, plus two named follow-up items as
Backlog.

Proves the tooling by using it. Gives Aaron a clean paper trail.
Demonstrates end-to-end round-trip of the tooling stack: create_page
(generic), create_backlog_item (Product Backlog-specific), and the
already-trusted complete-sprint flow.

Run once:   python _s_retro_file_2026_04_21.py
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


# ===========================================================================
# DONE entries — every shipped sprint today that does not already have a
# Notion row. Each gets the commit hash + a short explainer + the repo
# it landed in. Ordered chronologically so the Product Backlog reads as
# a session log for today.
# ===========================================================================
DONE_ENTRIES = [
    dict(
        item="S-KEVIN-HYGIENE: self-host Leaflet + Inter, AA --grey contrast, listing-availability probe",
        product="Portfolio",
        notes=(
            "Shipped 2026-04-21 via max-mode last-resort clause "
            "(first empty-queue cycle after S-030/S-CLARITY/S-KEVIN/"
            "S-DCC-VISUAL-REGRESSION). Kevin's Apartment Search: "
            "vendored Leaflet 1.9.4 (BSD-2-Clause, ~165 KB) + Inter "
            "v4.0 variable font (SIL OFL 1.1, ~338 KB), removing two "
            "external CDN deps; darkened --grey #888 -> #686868 for "
            "WCAG AA on cream; added listing-availability.yml workflow "
            "(weekly HEAD probe, opens GH issue on 404/410/5xx). "
            "Repo now fully L3-ready. Commit ccc2cd3."
        ),
    ),
    dict(
        item="S-CLARITY-PORTABILITY: wire the 4-provider LLM picker end-to-end",
        product="Clarity",
        notes=(
            "Shipped 2026-04-21 via max-mode last-resort clause "
            "(second empty-queue cycle). Route B from the S-CLARITY "
            "audit was executed: Setup screen gets a provider "
            "<select> for Anthropic / OpenAI / Gemini / Ollama with "
            "conditional API-key field + per-provider placeholder + "
            "'Get a key' link. Activate flow writes llm_provider + "
            "llm_api_key to localStorage. runDiagnostic drops the "
            "hardcoded model override; provider defaults drive. "
            "Footer names active provider dynamically. Updated "
            "llm-provider.js Anthropic default to Sonnet 4.6 for "
            "better diagnostic output. Clarity is now actually "
            "L3/L4-capable (Ollama path = zero external calls). "
            "Commit a5a0d4d."
        ),
    ),
    dict(
        item="S-NOTION-CREATE-PAGE: create_page + build_backlog_properties helpers",
        product="HAL Stack",
        notes=(
            "Shipped 2026-04-21 as meta-tooling foundation to unblock "
            "S-R01-PHASE-1. NotionClient.create_page() POSTs "
            "/v1/pages with the 2025-09-03 data_source_id parent "
            "shape. NotionClient.build_page_body() returns the "
            "request body without sending (offline verification). "
            "build_backlog_properties() hides title/select/"
            "rich_text boilerplate. create_backlog_item() is the "
            "one-call convenience wrapper (this script uses it). "
            "New CLI: --dry-run-create emits JSON body without API "
            "call. Commit a3c8f53."
        ),
    ),
    dict(
        item="S-R01-INFRA: DCC Kids Research DB schema + create_research_row helper",
        product="HAL Stack",
        notes=(
            "Shipped 2026-04-21 as meta-tooling phase 2. Discovered "
            "the DCC Kids Research Database data source "
            "(e184382b-b59a-41e7-9152-d90fbee1abe6) via Notion "
            "search; captured its 22-column schema as 7 module-"
            "level enum constants (RESEARCH_CATEGORIES, "
            "RESEARCH_AGE_RANGES, etc). "
            "build_research_row_properties() validates every "
            "select/multi-select against the captured enums; "
            "create_research_row() is one-call row creation. "
            "--dry-run-create extended to emit both Backlog + "
            "Research-row samples. Commit f549242."
        ),
    ),
    dict(
        item="S-R01-PHASE-1c: 2 research rows (DB 8 -> 10) -- True/story + Tell a grown-up",
        product="DCC",
        notes=(
            "Shipped 2026-04-21 using the freshly-landed helpers. "
            "Two new foundation rows: "
            "(1) '4-6 x Critical-Thinking: True things and story "
            "things' (P0-Core) -- Piaget preoperational + Common "
            "Sense Media + Sharon & Woolley fantasy/reality "
            "research. "
            "(2) '7-9 x Emotional-Safety: Telling a grown-up when "
            "something online feels weird' (P0-Core) -- Piaget "
            "concrete-operational + MediaSmarts Media Safety Tips "
            "for Middle Childhood + Dan Siegel 'Name It to Tame "
            "It' + 2022 MediaSmarts survey stat. "
            "Commit 152c2a5."
        ),
    ),
    dict(
        item="S-R01-PHASE-1d: 2 more research rows (DB 10 -> 12) -- 4-6 maker + 13-15 2FA",
        product="DCC",
        notes=(
            "Shipped 2026-04-21. "
            "(1) '4-6 x Creative-Making: Making my own thing first, "
            "then watching other people\\'s' (P0) -- Scholastic, "
            "NAEYC, Bright Horizons early-childhood creativity + "
            "PMC9590021 Game Program evidence base. "
            "(2) '13-15 x Tech-Safety: Turning on 2FA on accounts "
            "I care about' (P0) -- CISA + NIST SP 800-63B + Common "
            "Sense Education. "
            "Commit 228d77f."
        ),
    ),
    dict(
        item="S-R01-PHASE-1e: coverage grid complete (DB 12 -> 13)",
        product="DCC",
        notes=(
            "Shipped 2026-04-21. Last open cell in the 4 ages x 5 "
            "categories grid filled: '7-9 x Creative-Making: Making "
            "something useful for someone else' (P0). Erikson "
            "industry-vs-inferiority + Harvard Project Zero Agency-"
            "by-Design + Schonert-Reichl PMC3790250. After this "
            "sprint the grid is 20/20; remaining Phase-1 shifted "
            "from 'fill grid' to 'add 2nd rows for depth'. "
            "Commit a068564."
        ),
    ),
    dict(
        item="S-R01-PHASE-1f: sextortion resistance row + rich_text auto-chunk fix (DB 13 -> 14)",
        product="DCC",
        notes=(
            "Shipped 2026-04-21. Single highest-impact protective "
            "row in the DB based on FBI/NCMEC/FinCEN threat data. "
            "'13-15 x Emotional-Safety: What to do if someone "
            "pressures me to send a picture (sextortion)' (P0). "
            "4-step protocol: stop responding / save evidence / "
            "tell an emergency adult / use Take It Down. "
            "Non-shaming; boys 14-17 explicitly named as primary "
            "target. Mid-sprint helper fix: rich_text fields now "
            "auto-chunk >1900 chars (first call hit 3160). "
            "Commit 6e975a4."
        ),
    ),
    dict(
        item="S-R01-PHASE-1g: 10-12 password manager prereq for 2FA (DB 14 -> 15)",
        product="DCC",
        notes=(
            "Shipped 2026-04-21. '10-12 x Tech-Safety: Using a "
            "password manager so every account gets its own "
            "password' (P0). Direct prerequisite for the 13-15 2FA "
            "skill (1d) -- without unique per-account passwords, "
            "2FA only patches the hole the password would have "
            "caused anyway. One-Saturday setup pattern: Bitwarden "
            "or 1Password Families, diceware master, full "
            "existing-account rotation. CISA + NIST SP 800-63B + "
            "Bitwarden family documentation. Commit dcd86a7."
        ),
    ),
    dict(
        item="S-R01-PHASE-1h: 13-15 lateral reading + AI check (DB 15 -> 16)",
        product="DCC",
        notes=(
            "Shipped 2026-04-21. '13-15 x Critical-Thinking: "
            "Reading around something before I believe it "
            "(lateral reading + AI check)' (P0). Stanford SHEG's "
            "lateral-reading technique with a 2026 AI-overlay. "
            "Four-move routine: notice the engineered reaction "
            "/ leave the page / search the claim (not the source) "
            "/ add the AI check. Evidence: SHEG 2019 study -- 6 x "
            "50-min lessons DOUBLED high-schoolers' spotting "
            "accuracy. News Literacy Project Checkology + "
            "RumorGuard for weekly low-pressure practice. "
            "Commit a2509cc."
        ),
    ),
    dict(
        item="S-R01-PHASE-1i: 10-12 credit-when-remixing (DB 16 -> 17)",
        product="DCC",
        notes=(
            "Shipped 2026-04-21. '10-12 x Creative-Making: When "
            "I remix something, I name who made the original' "
            "(P1). Lifetime creator-citizenship habit for the "
            "age when kids actively remix (fan art, meme edits, "
            "Roblox, TikTok, fanfic). Every published remix "
            "names sources in caption/description; introduces "
            "Creative Commons as how creators positively say "
            "'yes, remix me'. Common Sense Ed + CC official "
            "docs + Copyright & Creativity Elementary K-6 "
            "curriculum + Lessig Remix (2008). Commit 31ec2a0."
        ),
    ),
    dict(
        item="S-R01-PHASE-1j: 10-12 stepping out of pile-on (DB 17 -> 18)",
        product="DCC",
        notes=(
            "Shipped 2026-04-21. '10-12 x Emotional-Safety: "
            "Stepping out of a group pile-on (without becoming "
            "the next target)' (P0). Agency-based framing -- "
            "NOT 'be an upstander' (kids reject as preachy). "
            "Three rehearsed moves in increasing difficulty: "
            "(1) don't forward (zero social cost, shrinks "
            "pile-on by one); (2) private DM to target; "
            "(3) change the subject in the group. Works WITH "
            "Kohlberg conventional-morality affiliation peak, "
            "not against it. Empirical anchor: peer intervention "
            "stops bullying within ~10 seconds in most cases "
            "(Olweus/PREVNet/Common Sense synthesis). Kids Help "
            "Phone Canada named as escalation. Commit e428d29."
        ),
    ),
    dict(
        item="S-R01-PHASE-1k: 7-9 app permissions pause-and-show (DB 18 -> 19)",
        product="DCC",
        notes=(
            "Shipped 2026-04-21. '7-9 x Tech-Safety: Pause and "
            "show a grown-up whenever an app asks for something' "
            "(P0). Completes the Tech-Safety ladder across all "
            "4 age brackets: 4-6 secret/share -> 7-9 pause-and-"
            "show -> 10-12 password manager (1g) -> 13-15 2FA "
            "(1d). One rule memorised cold. Zero-punishment "
            "framing (revoke together after tap-throughs); "
            "stickers for noticing, not for saying no; device-"
            "level parental controls essential complement. FTC "
            "COPPA + Common Sense Ed + Apple Kids Category + "
            "MediaSmarts Canada. Commit 96b9364."
        ),
    ),
    dict(
        item="S-R01-PHASE-1l: 13-15 AI tutor vs shortcut -- Phase-1 target MET (DB 19 -> 20)",
        product="DCC",
        notes=(
            "Shipped 2026-04-21. '13-15 x Learning: Using AI as "
            "a tutor that grows me, not a shortcut that hollows "
            "me out' (P0). Defining learning skill for the "
            "current teen generation. Four moves: (1) answer "
            "first, ask AI second (generation effect); (2) ask "
            "AI to critique YOUR reasoning, not provide the "
            "answer (Socratic scaffolding); (3) 'explain like "
            "I'm in grade 8' (cognitive load); (4) protege "
            "test -- close AI, wait 10 min, teach it back out "
            "loud (retrieval practice). Evidence: Dartmouth Nov "
            "2025 'illusion of mastery' + Nature Scientific "
            "Reports 2025 RCT + Khan Academy Khanmigo 2024-25 "
            "(68K -> 700K students). This row hits the original "
            "Phase-1 target of 20+ at exactly 20. Commit 7dca6d2."
        ),
    ),
]


# ===========================================================================
# Follow-up BACKLOG items named in commit messages / audits today but never
# filed in Notion.
# ===========================================================================
BACKLOG_ITEMS = [
    dict(
        item="S-DCC-VIS-STYLEGUIDE-STABLE: make styleguide visual regression work",
        priority="P3",
        product="DCC",
        notes=(
            "Filed retroactively 2026-04-21. During S-DCC-VISUAL-"
            "REGRESSION (8183b1f), styleguide was dropped from the "
            "Playwright visual-regression scan after 3 fix attempts "
            "couldn't quiet a persistent 'failed to take two "
            "consecutive stable screenshots' flake. Styleguide's "
            "dense typography samples + keyboard-helper modal "
            "auto-injection cause sub-pixel rendering non-"
            "determinism that Playwright's stability retries can't "
            "absorb. Fix needs a styleguide-specific approach: "
            "viewport clip + mask known-unstable regions (kbd-"
            "help dialog, font-sample blocks). LOE ~1-2h. Low "
            "priority (styleguide is internal documentation, not "
            "user-facing). Reference: S-DCC-VISUAL-REGRESSION "
            "commit 8183b1f on digital-confidence/main."
        ),
    ),
    dict(
        item="S-KEVIN-CSP-READY: extract inline scripts + styles from Kevin's index.html",
        priority="P2",
        product="Portfolio",
        notes=(
            "Filed retroactively 2026-04-21. Named in the S-KEVIN "
            "audit (AUDIT.md section 4) as a CSP-readiness "
            "follow-up. After S-KEVIN shipped, 11 inline onclick "
            "handlers still remain on Save/Cancel/Reset/Print "
            "buttons (those are actual <button> elements so lower "
            "a11y impact than the 4 criteria-row divs that were "
            "converted in S-KEVIN). Also: inline <script> and "
            "<style> blocks should move to kevin.js + kevin.css. "
            "Pairs with any future host migration away from GitHub "
            "Pages to a CSP-capable provider (Cloudflare Pages, "
            "Netlify, etc). LOE ~1-2h. Low value today, valuable "
            "the moment we migrate."
        ),
    ),
]


def main() -> int:
    client = nc.NotionClient()
    created = []
    failures = []

    print(f"=== Filing {len(DONE_ENTRIES)} DONE entries ===\n")
    for entry in DONE_ENTRIES:
        print(f"--- DONE: {entry['item'][:70]} ---")
        try:
            page = nc.create_backlog_item(
                client,
                item=entry["item"],
                priority="P0",  # historical priority matches the original sprints
                status="Done",
                owner="Claude Code",
                type_="Sprint",
                product=entry.get("product"),
                notes=entry.get("notes"),
            )
            pid = page.get("id")
            url = page.get("url")
            print(f"OK: {pid}")
            created.append((entry["item"], pid, url))
        except Exception as e:
            print(f"FAIL: {type(e).__name__}: {e}")
            failures.append((entry["item"], str(e)))
        print()

    print(f"\n=== Filing {len(BACKLOG_ITEMS)} BACKLOG follow-up items ===\n")
    for entry in BACKLOG_ITEMS:
        print(f"--- BACKLOG ({entry['priority']}): {entry['item'][:70]} ---")
        try:
            page = nc.create_backlog_item(
                client,
                item=entry["item"],
                priority=entry["priority"],
                status="Backlog",
                owner="Claude Code",
                type_="Sprint",
                product=entry.get("product"),
                notes=entry.get("notes"),
            )
            pid = page.get("id")
            print(f"OK: {pid}")
            created.append((entry["item"], pid, page.get("url")))
        except Exception as e:
            print(f"FAIL: {type(e).__name__}: {e}")
            failures.append((entry["item"], str(e)))
        print()

    print("\n" + "=" * 70)
    print(f"SUMMARY: {len(created)} filed, {len(failures)} failed")
    print("=" * 70)
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
