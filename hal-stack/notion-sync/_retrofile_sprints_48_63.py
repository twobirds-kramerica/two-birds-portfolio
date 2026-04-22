"""Retro-file sprints 48-63 (Session 22 continuation) to Notion Product Backlog.

All entries filed as Done with the commit hash in Notes. Mirrors the pattern
used during the first retro sweep (2026-04-21 retro-file-part2).

Usage:
    python hal-stack/notion-sync/_retrofile_sprints_48_63.py

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

# Each entry: (item, priority, product, notes)
# Status is always "Done" since these shipped tonight.
ENTRIES = [
    (
        "S-CC-CSP-READY: extract Career Coach inline script to js/app.js",
        "P2", "Career Coach",
        "Commit 0b53a6e. Applied S-KEVIN-CSP-READY pattern — 1560-line inline "
        "<script> block moved to js/app.js, replaced with src=js/app.js defer. "
        "node --check clean. Career Coach now CSP-ready (zero inline JS)."
    ),
    (
        "S-AARON-ROUTING: Clarity CTA card + contact-form one-liner",
        "P2", "Aaron Patzalek",
        "Commit 7d79fb7 on aaron-patzalek. 'What I'm Building' Clarity card links "
        "to twobirds-kramerica.github.io/clarity/; Contact section gains a short "
        "subtitle framing welcome message types. Closes AUDIT §8 items 2+3."
    ),
    (
        "S-CC-FOCUS-VISIBLE-TBCC: two-birds-command-centre :focus-visible",
        "P3", "Two Birds Command Centre",
        "Part of commit 22781c5. Added explicit :focus-visible styling on "
        "interactive elements. Dark-theme keyboard a11y. Closes AUDIT §8 item 2."
    ),
    (
        "S-TBCC-JSON-SCHEMA-CI: JSON schema validator workflow",
        "P3", "Two Birds Command Centre",
        "Part of commit 22781c5. Added _build/check_data_schemas.py Python "
        "validator + .github/workflows/json-schema-check.yml. All 4 existing "
        "data/*.json files pass schema check. Closes AUDIT §8 item 4."
    ),
    (
        "S-CLARITY-PORTFOLIO-EVIDENCE: factual evidence line under CTA card",
        "P2", "Clarity",
        "Commit e4e79b7. Added one-line factual portfolio evidence (DCC, Kevin, "
        "Career Coach) under CTA byline. Sidesteps 'no testimonials' audit flag "
        "without fabricating social proof. Factual variant of AUDIT §9 item 5."
    ),
    (
        "S-TBI-PORTFOLIO-EVIDENCE: factual evidence line under About",
        "P2", "Two Birds Innovation",
        "Commit d88bc09. Mirrors Clarity portfolio-evidence pattern on TBI About "
        "section. Parallel thread to TBI AUDIT §8 item 4 (case study substitute "
        "until a pilot walkthrough can be written up)."
    ),
    (
        "S-CLARITY-LINK-CHECK: weekly external-link CI workflow",
        "P3", "Clarity",
        "Commit 1f594fe. Sunday 06:00 EST cron checks 3 sibling Two Birds tools "
        "+ 3 LLM provider API-key pages. Opens GitHub issue only on broken link. "
        "Closes Clarity AUDIT §6 Backlog item 1."
    ),
    (
        "S-CC-LINK-CHECK: weekly external-link CI workflow",
        "P3", "Career Coach",
        "Commit 05f439d. Same pattern as DCC/Clarity — Sunday cron on 2 sibling "
        "tools + 3 LLM provider key pages."
    ),
    (
        "S-AARON-LINK-CHECK: weekly external-link CI workflow",
        "P3", "Aaron Patzalek",
        "Commit afe12a4. Checks LinkedIn profile, Formspree endpoint, and "
        "3 sibling Two Birds tools every Sunday."
    ),
    (
        "S-TBI-LINK-CHECK: weekly external-link CI workflow",
        "P3", "Two Birds Innovation",
        "Commit 18c2194. Checks 5 sibling Two Birds tool URLs weekly."
    ),
    (
        "S-QD-LINK-CHECK: weekly external-link CI workflow",
        "P3", "Quality Dashboard",
        "Commit 6b4d772. 7 monitored portfolio URLs — dashboard's primary purpose "
        "now has raw HTTP reachability check alongside commit-freshness view."
    ),
    (
        "S-SEO-SWEEP: sitemap.xml + robots.txt across 6 repos",
        "P2", "HAL Stack",
        "Commits 91ec39b aaron-patzalek, 69b979f TBI, 5108bc8 Clarity, d8cafc3 CC, "
        "05c519d quality-dashboard, 2275a00 kevins. "
        "5 public brand sites get AI-bot friendly robots.txt (11 crawlers allowed) "
        "+ public sitemap. Quality Dashboard + Kevin get Disallow:/ matching their "
        "existing noindex posture. Closes 100% of non-DCC SEO gap."
    ),
    (
        "S-TEMPLATE-SYNC-SEO: project template inherits SEO + link-check baseline",
        "P3", "HAL Stack",
        "Commit 67bbc33 on two-birds-project-template. robots.txt, sitemap.xml, "
        "and broken-external-link-check.yml now ship with the template. Every "
        "future project starts compliant."
    ),
    (
        "S-KEVIN-SEO-FIX: align robots.txt with existing noindex posture",
        "P3", "Kevins Apartment Search",
        "Commit 2275a00. Self-review caught S-SEO-SWEEP regression — Kevin's "
        "index.html has <meta robots content=noindex, nofollow> but sprint 59 "
        "added public robots.txt + sitemap by mistake. Reverted to Disallow:/ "
        "and removed sitemap. Demonstrates working self-review loop."
    ),
    (
        "S-SESSION-LOG-PART2: SESSION-STATE + aaron-todos reconciliation (sprints 48-54)",
        "P3", "HAL Stack",
        "Commit 2cadc33. Reconciled aaron-todos-2026-04-21.md with sprint 52's "
        "partial closure of Clarity portfolio-evidence (testimonial variant still "
        "open). Documented 6 AUDIT top-5 items autonomously closed tonight."
    ),
    (
        "S-SESSION-LOG-PART3: SESSION-STATE final reconciliation (sprints 55-63)",
        "P3", "HAL Stack",
        "Commits 4ee5617 + cf2d02f. Final SESSION-STATE entries documenting "
        "sprints 55-60 (SEO + link-check sweep) and sprints 61-63 (template sync "
        "+ Kevin self-review regression fix). 16-sprint continuation complete."
    ),
]


def main() -> int:
    client = NotionClient()
    filed = 0
    failed: list[str] = []

    print(f"Filing {len(ENTRIES)} backlog entries to Notion Product Backlog...")
    print("Status=Done, Owner=Claude Code, Type=Sprint, Priority=as-listed\n")

    for item, priority, product, notes in ENTRIES:
        try:
            page = create_backlog_item(
                client,
                item=item,
                priority=priority,
                status="Done",
                owner="Claude Code",
                type_="Sprint",
                product=product,
                notes=notes,
            )
            page_id = page.get("id", "?")
            print(f"OK  [{priority}] {item[:70]}")
            print(f"    -> {page_id}")
            filed += 1
        except Exception as exc:
            print(f"FAIL [{priority}] {item[:70]}: {exc}")
            failed.append(item)

    print(f"\n{filed}/{len(ENTRIES)} entries filed.")
    if failed:
        print("Failed:")
        for f in failed:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
