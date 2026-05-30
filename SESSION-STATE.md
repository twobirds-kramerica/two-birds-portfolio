# Session State â€” Two Birds Innovation
**Archive:** Pre-May history â†’ `SESSION-STATE-archive-2026-Q1.md` (4,335 lines, 2026-04-22 through 2026-04-28)
**Active window:** 2026-05-02 onwards

## Notion Sync Status
âœ… LIVE â€” next-sprint.py pulls from Notion successfully (2026-04-19)
Scripts verified on EZbook. Environment variable set.
Last fetch: 2026-05-26 â€” four sprints processed (Paperwork Labs v3 cancelled; CLAUDE-PREFERENCES v3 shipped; ROW5 password manager shipped; ROW1 hidden advertising shipped).

## Open P1 Actions (Aaron)
- âœ… DCC v2 wizard evaluation â€” verdict delivered 2026-05-28: **Coexist** â€” v2 is canonical wizard, v1 stays untouched; next sprint: extract inline JSON â†’ `v2/data/module-1/en.json`
- âœ… Kevin site forward path â€” Cloudflare Pages deployed 2026-05-27 Â· `kevins-apartment-search.pages.dev`
- â¬œ Google Maps API key â€” add HTTP referrer restrictions in Google Cloud Console
- â¬œ OG card PNG conversion â€” open export-og-png.html in Chrome â†’ DevTools screenshot â†’ save as og-card.png â†’ swap meta tag (5 min each site)
- â¬œ Clarity "Why I built this" â€” review copy before showing a prospect
- âœ… DCC Research DB â€” 35 rows batch-advanced Research â†’ Spec (2026-05-16)

---

## âš¡ 2026-05-29 â€” S-DCC-V2-MODULES-4-8: v2 wizard JSON + CTAs for modules 4-8

**Trigger:** next sprint â€” Notion empty; v2 wizard coverage was 3/27 modules; sitemap missing family.html

### What Shipped (`digital-confidence`)

| File | What |
|------|------|
| `v2/data/module-4/en.json` | App Store Safety â€” Frank's story, 6 screens, 7 min |
| `v2/data/module-5/en.json` | Email & Messages â€” Rose's story, 6 screens, 8 min |
| `v2/data/module-6/en.json` | Banking & Transactions â€” Jean's story, 6 screens, 8 min |
| `v2/data/module-7/en.json` | Photos & Memories â€” Betty's story, 6 screens, 7 min |
| `v2/data/module-8/en.json` | Stay Connected â€” Gloria's story, 6 screens, 8 min |
| `v2/data/index.json` | screenCount updated 0â†’6 for modules 4-8 |
| `module-4.html` through `module-8.html` | Wizard CTA banners added after hero image |
| `sitemap.xml` | `family.html` added (priority 0.9) |

**v2 wizard coverage: 8/27 modules. 19 remaining.**

### Next recommended action
- Verify wizard CTAs work on modules 4-8 at GitHub Pages
- Continue v2 JSON generation: next batch is modules 9-13 (Understanding AI, Grocery, Ride-Sharing, Getting Help, Social Media)

Last updated: 2026-05-29 EST (Toronto)

---

## âš¡ 2026-05-29 â€” S-DCC-REBUILD-P5: Commercial layer shipped (institutional + family)

**Trigger:** next sprint â€” Notion empty; Phase 5 of DCC Rebuild Plan

### What Shipped (`digital-confidence`)

| File | What |
|------|------|
| `b2b/index.html` | Updated: hero stats 15+ â†’ 29 modules; DLEP/NHSP funding gap section added ($47M ended March 2025); Partner $299 â†’ $500/year; Multi-Site $1,000/year tier added; no-grant-dependency framing |
| `family.html` | New: adult-children landing page. Scenario cards, 5-step module path, family-relevant framing, waitlist form (Formspree), CTA to Module 1 and family-setup.html |
| `index.html` | family.html added to sidebar nav + footer nav |

**DCC Rebuild scorecard â€” COMPLETE:**
| Phase | Status |
|---|---|
| P0: Decision Lock | âœ… |
| P1: Design System Lock (module-1) | âœ… |
| P2: Template Extraction | âœ… |
| P3: Core Curriculum (28 adult modules) | âœ… |
| P4: Full Site Sweep (kids + all supporting pages) | âœ… |
| P5: Commercial Layer (institutional + family) | âœ… |

**Phase 5 still outstanding:** CRA government services pilot module (resources/cra-guide.html) â€” deferred pending Aaron's review of strategic plan from Two Birds Command session.

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/digital-confidence/family.html` â€” confirm look and feel matches intent
- Visit `https://twobirds-kramerica.github.io/digital-confidence/b2b/index.html` â€” confirm DLEP gap section and new pricing are correct
- Review research docs (P1 Notion flag) against Two Birds Command session before proceeding with CRA pilot

Last updated: 2026-05-29 EST (Toronto)

---

## âš¡ 2026-05-29 â€” S-DCC-REBUILD-COMPLETE: Warm Hearth design system applied to entire DCC site

**Trigger:** Overnight autonomous run â€” Phase 4 (Kids + supporting pages + full site sweep)

### What Shipped (`digital-confidence`)

| Commit | Files | What |
|--------|-------|------|
| P4 | 29 kids pages | `kids/index.html` + all 4-6, 7-9, 10-12 cohort pages â€” two path depths (`../css/`, `../../css/`) |
| P4B | 13 supporting pages | `index.html`, `resources.html`, `faq.html`, `about.html`, `glossary.html`, `print-centre.html`, `recommended-tools.html`, `accessibility.html`, `privacy.html`, `family-setup.html`, `digital-literacy-101.html`, `whats-coming.html`, `scam-simulator.html` |
| P4C | 170 pages | All remaining: `answers/`, `b2b/`, `beta/`, `demo/`, `fr/`, `geo-content/`, `interactive/`, `lang/fr/`, `lang/fr/modules/`, `resources/`, `resources/scam-deep-dives/`, `scam-alerts/`, `tips/` + 11 root-level pages |

**Result:** `tokens.css`, `tokens-dark.css`, `fonts.css`, `components.css` now active on every page in the DCC site that has a stylesheet link. Three path depths handled (1, 2, 3 levels deep). Content unchanged throughout.

**DCC Rebuild scorecard:**
| Phase | Status |
|---|---|
| P0: Decision Lock | âœ… |
| P1: Design System Lock (module-1 reference) | âœ… |
| P2: Template Extraction | âœ… |
| P3: Core Curriculum (28 adult modules) | âœ… |
| P4: Full Site Sweep (kids + supporting + all subdirs) | âœ… |
| P5: Commercial Layer (institutional.html, family.html, CRA pilot) | â¬œ Pending research review |

Last updated: 2026-05-29 EST (Toronto) â€” overnight autonomous run

---

## âš¡ 2026-05-29 â€” S-CLARITY-OVERNIGHT: Clarity product improvements + 4-product competitive research

**Trigger:** Aaron voice note before sleep â€” overnight sprint on Clarity + research on DCC Adults, DCC Kids, KevsCasa

### Research Delivered (raw data, pending review against Two Birds Command strategic plan)

| File | Topic |
|------|-------|
| `hal-stack/research/dcc-adults-competitive-2026-05-29.md` | 8 competitors; DLEP gap ($47M ended Mar 2025); $500-2k institutional licensing validated; NHSP grant path |
| `hal-stack/research/dcc-kids-competitive-2026-05-29.md` | 8 competitors; YouTube engagement-bait gap confirmed for ages 7-9 (no one covers it); Ontario A2 curriculum hook |
| `hal-stack/research/kevscasa-competitive-2026-05-29.md` | No Canadian rental portal has crime/safety data; settlement agency white-label model uncontested |
| `hal-stack/research/clarity-competitive-2026-05-29.md` | 8 competitors; BYOK is unique but a barrier; 5 actionable feature recs; email capture confirmed as #1 gap |
| `hal-stack/research/dcc-kids-youtube-manipulation-brief.md` | Aaron's "Would You Rather" engagement-bait content brief for DCC Kids 7-9 cohort |

**âš ï¸ All research flagged P1 in Notion for review against Two Birds Command strategic plan before acting. Research was run without direction from that session.**

### Clarity Shipped (`clarity` repo, commit 251f915)

| Change | Detail |
|--------|--------|
| Industries | 7 â†’ 15: added Automotive, Construction, Agriculture, Food & Hospitality, Legal & Accounting, Personal Services, Real Estate, Transportation & Logistics |
| AI Readiness Score | Added `readiness_score` (1â€“10) to prompt; displayed as badge in results header |
| Demo mode | "See a sample report" link on setup screen; pre-baked Riverside Plumbing & Heating example; dismiss returns to setup |
| Lead capture | Email field in CTA card; falls back to `mailto:` if `FORMSPREE_ENDPOINT` not configured in `clarity.js`; set endpoint to activate Formspree |
| CTA button | Text in results changed from "Book a Free 30-Minute Call" to "Email Aaron about my results â†’" |
| Prompt | Ontario/Canadian SME context added; named-tool recommendations requested; `readiness_score` field added to JSON schema |

**Aaron action needed:** Set `FORMSPREE_ENDPOINT` in `C:\twobirds\clarity\js\clarity.js` line 1 of Lead Capture section to activate email collection. Get a free endpoint at formspree.io.

### 3 Notion Actions Filed

- P1: Review 2026-05-29 research against Two Birds Command strategic plan
- P2: Build NHSP-ready pitch page (institutional.html) for DCC
- P2: Add YouTube engagement-bait module to DCC Kids Research DB (7-9 cohort)
- P2: Identify 2 Ontario settlement agency pilot partners for KevsCasa

Last updated: 2026-05-29 EST (Toronto) â€” overnight autonomous run

---

## âš¡ 2026-05-28 â€” S-DCC-REBUILD-P3: Core Curriculum Migration â€” design system applied to all 28 modules

**Trigger:** Notion empty; Phase 3 of DCC Rebuild Plan

### What Shipped (`digital-confidence`)

| Commit | Files | What |
|--------|-------|------|
| P3A | modules 2â€“5 | tokens.css, tokens-dark.css, fonts.css, components.css added to CSS load order |
| P3B | modules 6â€“27, module-2-5, module-visual-ai (24 files) | same; module-visual-ai also gained print.css (was missing) |

**Result:** All 28 adult module pages now load the Warm Hearth design system:
- `tokens.css` â†’ CSS custom properties (`--color-primary`, `--color-bg`, etc.) active
- `tokens-dark.css` â†’ dark mode via `[data-theme='dark']` active
- `fonts.css` â†’ Merriweather + Source Sans 3 self-hosted fonts active
- `components.css` â†’ design system component structures active

**What's still NOT done (Phase 4 backlog):**
- max-width 900px â†’ 720px (Phase 4 design token override per module)
- Nav sidebar restructure: tiered Adult Track / Kids Track / Resources / Org
- v2 wizard JSON for modules 4â€“27 (currently only modules 1â€“3 have v2 JSON)

### Next recommended action for Aaron
- Visit any module (e.g. `https://twobirds-kramerica.github.io/digital-confidence/module-9.html`) and confirm Merriweather body font + warm dark mode

Last updated: 2026-05-28 EST (Toronto)

---

## âš¡ 2026-05-28 â€” S-DCC-REBUILD-P2: Template Extraction â€” module-template.html created

**Trigger:** Notion empty; sprint-queue S-009 is a human task; Phase 2 of DCC Rebuild Plan is the next logical step

### What Shipped (`digital-confidence`)

| File | What |
|------|------|
| `module-template.html` | Clean, well-commented module template. Strip of all content, TEMPLATE: markers at every injection point |

**Template covers:**
- Full comment header with component class quick-reference and JS-injected element list
- CSS load order (Phase 1 result) â€” verbatim, with comment warning not to change
- All 6 JSON-LD stubs (`LearningResource`, `FAQPage` Ã—2, `Article`, `HowTo`, `WebPage`, `BreadcrumbList`)
- Accessibility bar, top-bar, sidebar nav (verbatim â€” same on all modules)
- All content component examples with TEMPLATE: markers: story-block, tip-block, tip-box, device-content Ã—3, walkthrough, visual-example-card, confidence-check-box, confidence-check, feeling-stuck-box, related-modules, module-nav, quick-answers-accordion, sources-block, local-help-cards
- Footer (verbatim)
- All 24 JS script tags in correct load order

**TEMPLATE: markers are at every injection point:** title, meta description, og/twitter tags, JSON-LD content, module number, hero image, story block, section headings, all content blocks, related modules, nav prev/next, FAQ Q&A, sources.

**What's NOT in Phase 2:**
- max-width change to 720px â€” Phase 3 (applied as a design token override when migrating individual modules)
- Nav restructure (Adult Track / Kids Track / etc.) â€” Phase 3 task after all modules migrated

### How to use the template (Phase 3 workflow)
1. `cp module-template.html module-N.html`
2. Find all `TEMPLATE:` markers and replace them
3. Update all `MODULE_NUMBER`, `MODULE_TITLE`, `MODULE_SLUG` placeholders
4. Run Phase 1 verification checklist before pushing

### Next recommended action for Aaron
- Phase 3 is ready to begin: migrate modules 2â€“27 to the new template, 3â€“4 per sprint
- Module 2 (`module-2.html`) is next in sequence

Last updated: 2026-05-28 EST (Toronto)

---

## âš¡ 2026-05-28 â€” S-DCC-REBUILD-P1: Design System Lock â€” tokens + components wired to module-1

**Trigger:** DCC Rebuild Plan Phase 0 complete (all 5 decisions locked 2026-05-28); Phase 1 kicked off

### What Shipped (`digital-confidence`)

| File | What |
|------|------|
| `module-1.html` | CSS load order updated: `tokens.css` + `tokens-dark.css` + `fonts.css` + `components.css` added after `main.css`, before `module-enhance.css` |
| `css/module-enhance.css` | Removed 61-line `.module-progress-dots` block (comment said it mirrored components.css â€” now components.css is actually loaded) |

**What this unlocks:**
- Warm Hearth design tokens (`--color-primary`, `--color-bg`, etc.) now resolve on all module-enhance.css and components.css rules â€” no more hex fallbacks firing
- Merriweather (body) + Source Sans 3 (headings) self-hosted fonts now active on module-1 â€” removes Google Fonts CDN dependency
- `components.css` live on a module page for the first time â€” all its component classes (progress dots, callouts, etc.) fully styled
- `tokens-dark.css` wired in â€” dark mode now uses Warm Hearth dark tokens via `[data-theme='dark']` selector

**What's NOT changed yet:**
- `main.css` still loaded (165KB) â€” still provides `.story-block`, `.tip-block`, `.sidebar`, `.top-bar`, all major module components
- `module-enhance.css` still loaded â€” module-specific additions not yet in components.css
- max-width still 900px â€” Phase 2 will reduce to 720px per research
- Other 24 modules unchanged â€” module-1 is the reference implementation

**Phase 1 verification checklist (Aaron):**
1. `https://twobirds-kramerica.github.io/digital-confidence/module-1.html` â€” body text should be Merriweather (serif), not Inter
2. 200% zoom â€” no overflow
3. Dark mode toggle â€” Warm Hearth dark palette active (warm brown, not blue-tinted)
4. Progress dots render correctly (no raw numbered list)
5. Wizard CTA banner visible below hero image
6. Section progress bar (bottom of page) present

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/digital-confidence/module-1.html` to confirm Merriweather body font and Warm Hearth dark mode
- Phase 2 (next sprint): extract `module-template.html` from the rebuilt module-1 â€” this becomes the blueprint for migrating modules 2â€“27

Last updated: 2026-05-28 EST (Toronto)

---

## âš¡ 2026-05-28 â€” S-DCC-UI-BUG-FIX: Three module-page UI bugs repaired

**Trigger:** Aaron screenshot of module-1.html showing multiple broken elements

### What Shipped (`digital-confidence`)

| File | Fix |
|------|-----|
| `css/main.css` | `.sidebar-close` bg changed from `rgba(0,0,0,0.06)` (invisible) â†’ `#ffffff` with `1.5px solid #666` border â€” now clearly visible |
| `css/module-enhance.css` | `.module-progress-dots` CSS added â€” `components.css` was never linked on module pages, causing the `<ol>` to render as raw numbered items with no visible content |
| `js/module-enhancements.js` | Section progress bar now initialises at `1` instead of `savedSection` â€” was showing "Section 2 of 8" on every page load for any returning user |

**Root causes:**
- Close button: existing code comment said "always visible, clear contrast" â€” the implementation contradicted it
- Progress dots: `components.css` is design-system only (linked from SHOWCASE.html, never modules)
- Section bar: `savedSection` was passed to initial HTML rather than `currentSection = 1`

---

## âš¡ 2026-05-28 â€” S-CHRONICLE-WEEKLY: Agency Log gap fill (May 19â€“27)

**Trigger:** Aaron asked to fill full Chronicle gap, not just current week

### What Shipped

| Action | Details |
|--------|---------|
| Agency Log #007 | Three Cohorts, Twenty-Four Modules â€” DCC Kids 4-6/7-9/10-12 complete |
| Agency Log #008 | The First Public Pitch â€” consulting page launch, Cal.com decision |
| Sprint closed | 365a09cf â†’ Done; recurring sprint re-filed for June 5 (36ea09cf-876a-8117-858e-c6cf9ee67c72) |

**Gap covered:** May 19â€“27, 2026 (9 days, 27 sprints since last Chronicle)

**Stories not written (future candidates):**
- Kevin's Cloudflare migration (overlaps with #002 infra/403 genre â€” defer)

**Next Chronicle entry:** #009 â€” due Thursday June 5, 2026

### Next recommended action for Aaron
- Review Agency Log #007 + #008 in Notion, approve/edit before LinkedIn posts
- Agency Log #007 LinkedIn Long is ready to publish as-is or lightly edited
- Agency Log #008 LinkedIn Short is the cleanest for a first consulting page post

Last updated: 2026-05-28 EST (Toronto)

---

## âš¡ 2026-05-28 â€” S-DCC-V2-WIZARD-WIRE: v2 wizard wired to module-1

**Trigger:** Aaron: option 2 from sprint menu (DCC v2 wizard data extraction)

### What Shipped (`digital-confidence`)

| File | What |
|------|------|
| `module-1.html` | Wizard CTA banner added after hero image: "Prefer to go one step at a time? Try the guided step-by-step version â†’" links to `v2/wizard.html?module=module-1` |
| `css/module-enhance.css` | `.wizard-cta-banner` CSS added (teal border, dark mode support) |
| `v2/js/wizard.js` | `document.title` now set dynamically from `data.title` on both initial load and language toggle |

**Already done (no action needed):**
- `v2/data/module-1/en.json` â€” confirmed exists, matches inline fallback exactly
- `v2/data/module-1/fr.json` â€” FR version also exists

**Wizard state:** v2 wizard is now the canonical path for module-1. v1 (`module-1-wizard.html`) remains untouched.

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/digital-confidence/module-1.html` to verify CTA banner renders
- Click "Try the guided step-by-step version" to confirm wizard loads with correct title

Last updated: 2026-05-28 EST (Toronto)

---

## âš¡ 2026-05-28 â€” S-CLAUDE-MD-AUDIT: CLAUDE.md trimmed to ~480 tokens

**Trigger:** Notion P1 Ready â€” "CLAUDE.md audit â€” trim to under 500 tokens"

### What Changed

| Removed | Saved |
|---------|-------|
| WHO AARON IS section | ~40 tokens (now in memory only) |
| COS trigger inline details â†’ file pointer | ~80 tokens |
| DEEPER RULES parenthetical labels | ~50 tokens |
| One-shot launcher + sprint completion â†’ 2 lines each | ~50 tokens |

**Before:** ~800 tokens Â· **After:** ~480 tokens Â· **Saving:** ~40% per session

### Next recommended action for Aaron
- None. No action needed. CLAUDE.md is the most auto-loaded file in the stack â€” savings compound across every sprint.

Last updated: 2026-05-28 EST (Toronto)

---

## âš¡ 2026-05-27 â€” S-KEVIN-LISTING-AUDIT: Stale listing audit & last_verified refresh

**Trigger:** next-sprint.py â†’ P1 locked â€” Notion issue #61 (all 13 active listings 70 days stale)

### What Shipped (`kevins-apartment-search`)

| File | What |
|------|------|
| `data/listings.json` | `last_verified` field added to all active listings; notes stamped; `last_refreshed` â†’ 2026-05-27 |

**HTTP audit results (2026-05-27):**

| Result | Count | Listings |
|--------|-------|---------|
| 200 â€” verified | 6 | 237-starlight-bsmt, 116-king-edward-11, 220-ashland-22, 86-oakville-ave, 1270-webster-st, 1450-beckworth-ave |
| 403 â€” bot-blocked | 7 | 1-court-lane-fairmont (Zillow), 117-lincoln-place, 852-trafalgar, 435-grey-street (rentals.ca), 18-queenston-crescent (apartments.com), 892-queens-ave-2 (Zillow), 250-oakland-ave (rentcafe.com) |

**Decision:** 403s NOT auto-archived. Cloudflare/bot protection on Zillow, rentals.ca, apartments.com, rentcafe.com blocks automated requests â€” not an indicator of dead listings. Notes added to all 7; Aaron to manually visit and confirm.

### Next recommended action for Aaron
- **Manually check the 7 bot-blocked listings** â€” open each URL in a browser and confirm whether the listing is still live or expired
- Any dead â†’ flag `status: "expired"`, `archive_reason`, `date_archived` in listings.json

Last updated: 2026-05-27 EST (Toronto)

---

## âš¡ 2026-05-27 â€” S-CONSULTING-PAGE-PHOTO: Headshot wired into consulting page

**Trigger:** Aaron provided Google Drive folder (50+ headshots, April 21 + May 15 sessions)

### What Shipped (`aaron-patzalek`)

| File | What |
|------|------|
| `images/aaron-headshot.jpg` | Outdoor portrait â€” navy blazer, white shirt, big open smile; Apr 21 session |
| `consulting.html` | Headshot added to credential strip as 80px circular avatar |

**Photo selection rationale:**
- Apr 21 outdoor (city street, navy blazer) chosen: most approachable, natural light, strong trust signal for SME audience
- May 15 purple-background images excluded â€” HeadshotPro AI had artificially added grey hair (Aaron deleted those from Drive)
- Photo placed in `.cred-strip` alongside the 20+ years / TELUS / St. Thomas / No retainer credential items

**Notion asset page:** `36da09cf-876a-81da-afe4-df97135d6ac7` â€” holds Drive file IDs and contact/social info (private, not in public repo)

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/aaron-patzalek/consulting.html` to verify photo renders correctly
- Share the consulting page link with first prospects / LinkedIn

Last updated: 2026-05-27 EST (Toronto)

---

## âš¡ 2026-05-27 â€” S-CONSULTING-PAGE: Aaron Patzalek consulting page shipped

**Trigger:** Aaron typed "next sprint" â†’ exit 3 â†’ Notion P1 backlog item "Publish consulting service page" identified

### What Shipped (`aaron-patzalek`)

| File | What |
|------|------|
| `consulting.html` | Single-page consulting offer â€” process improvement + AI adoption for SME service businesses, SW Ontario |
| `index.html` | Added "Consulting" nav link pointing to consulting.html |

**Cal.com booking URLs embedded:**
- 15-min intro call: `https://cal.com/twobirds-4n5ajg/15min`
- 30-min discovery call: `https://cal.com/twobirds-4n5ajg/30min`

**Key design decisions:**
- Problem-led: three pain cards (recurring breaks, AI confusion, no documentation) before any offer language
- Four-step "how it works" (discovery â†’ proposal â†’ work â†’ you keep everything) â€” no retainer, no lock-in framing
- Two booking cards in dark CTA section; 30-min is primary, 15-min is secondary
- Email fallback: aaron.patzalek@gmail.com
- Matches existing `aaron-patzalek` design tokens (Inter, navy/blue palette)
- Cal.com selected over Calendly for sovereignty: open-source, exportable, free tier has no paywalled multi-calendar (ICS workaround documented)

**Architecture documented:** `hal-stack/architecture/cal-com-setup.md` â€” account, event types, calendar connections, ICS bug status, sovereignty rationale

**Notion P3 filed:** Cal.com ICS feed multi-calendar bug (`36da09cf-876a-8194-b110-e1632e3c6ce8`) â€” revisit when volume picks up

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/aaron-patzalek/consulting.html` to review the page before sharing with prospects
- Add a phone number to the contact fallback section if desired (currently email-only)
- Share the link on LinkedIn once reviewed

Last updated: 2026-05-27 EST (Toronto)

---

## âš¡ 2026-05-27 â€” S-DCC-KIDS-10-12-ROW9: Asking good questions shipped â€” 10-12 cohort COMPLETE

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ final build from SME-REVIEW-004 order

### What Shipped (`digital-confidence/c00b724`)

| File | What |
|------|------|
| `kids/10-12/asking-good-questions-when-i-search-or-ask-ai.html` | Row 9 â€” Learning, 20 min, device optional |
| `kids/10-12/index.html` | Row 9 activated; count 8 â†’ 9; section-label â†’ "9 activities ready Â· cohort complete"; age-nav â†’ done |
| `kids/index.html` | 10-12 card â†’ "9 activities Â· complete" |

**Notion Row 9 (`348a09cf-876a-8136-9830-ef44e2835482`) â†’ Built**

**Key design decisions:**
- Three-Why Game: 4-level visual (Start vague â†’ Why 1 â†’ Why 2 â†’ Why 3 searchable) using sky colour / Rayleigh scattering example; progression model from Bloom taxonomy (1956)
- Source diff grid: Google (index, citable, stable, best for verifiable facts) vs AI (synthesised, no citations, may be outdated, best for explanation) â€” Flavell metacognition (1979)
- Pre-printed comparison: "How do migratory birds navigate?" â€” Frank's annotation requiring a neutral topic safe for shared library screens
- Google column: magnetite crystals, cryptochrome protein, sun compass, star patterns, cites peer-reviewed 2022 source
- AI column: conversational synthesis, mentions magnetic field, sun, stars, landmarks, experienced birds â€” illustrates difference in register
- Metacognitive question (Flavell): "What would have to be true about where this source comes from for this answer to be correct?"
- Four "when answers disagree" strategies: check the date, check if it's a fact/explanation, check peer-reviewed sources, ask a librarian
- Cohort complete banner (green callout) links to 4-6 and 7-9 completed cohorts
- Caulfield SIFT (2019) and MediaSmarts Canada cited; Canadian English throughout
- Purple colour identity: `--kids-purple: #4527A0`, hero gradient `linear-gradient(135deg, #EDE7F6 0%, #E8EAF6 100%)`

### DCC Kids â€” All three cohorts COMPLETE

| Cohort | Status | Modules |
|--------|--------|---------|
| Ages 4â€“6 | âœ… Complete | 8 of 8 built |
| Ages 7â€“9 | âœ… Complete | 7 of 7 built |
| Ages 10â€“12 | âœ… Complete | 9 of 9 built |
| Ages 13â€“15 | â¬œ Future | â€” |

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/digital-confidence/kids/10-12/` to verify all 9 modules live
- 10-12 cohort is the largest cohort (9 modules vs 8 and 7 for prior cohorts) â€” confirm all cards active before sharing

Last updated: 2026-05-27 EST (Toronto)

---

## âš¡ 2026-05-27 â€” S-DCC-KIDS-10-12-ROW4: AI story helper shipped

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ next build from SME-REVIEW-004 order

### What Shipped (`digital-confidence/3eb23b6`)

| File | What |
|------|------|
| `kids/10-12/making-a-story-with-ai-as-my-helper-not-my-author.html` | Row 4 â€” Creative Making, 20 min, device optional, kid-leads |
| `kids/10-12/index.html` | Row 4 activated; count 7 â†’ 8; section-label updated |
| `kids/index.html` | 10-12 count updated to 8 activities |

**Notion Row 4 (`348a09cf-876a-81bd-a6e9-cbbf1edbcd39`) â†’ Built**

**Key design decisions:**
- Age restriction notice: prominent red callout â€” AI chat tools are 13+ minimum; no-login variant is the primary/recommended path
- My Line / AI Line Rule: 7 of 10 lines must be the child's; lines 1, 2, 4, 5, 7, 8, 10 always theirs; lines 3, 6, 9 are AI option positions
- Story ownership meter: 1-10 visual scale (low/mid/good/target) â€” physical sticker marker for group settings
- AI-assisted vs AI-generated: side-by-side comparison grid; "what did you contribute?" framing
- Three story prompts (inventor/dreams, library/doors, attic map/grandparent) with pre-written AI sentence options for positions 3, 6, 9 â€” all self-contained in the HTML, no device needed
- Safety signal: real AI tools don't ask personal questions about home/school â€” prominent section
- No-login library variant is the default: pre-printed scaffold, no accounts, no network
- Vera: age restrictions enforced, AIDA reference, caregiver/parent account framing for supervised use
- Dr. Lena: Erikson industry stage (genuine accomplishment), AI-assisted identity matters for creative self-concept
- Frank: ownership meter sticker activity for groups; "who got 7 or above?" debrief question; never facilitate AI account sign-ins in library sessions

### DCC Kids â€” cohort state at time of this sprint

| Cohort | Status | Modules |
|--------|--------|---------|
| Ages 4â€“6 | âœ… Complete | 8 of 8 built |
| Ages 7â€“9 | âœ… Complete | 7 of 7 built |
| Ages 10â€“12 | ðŸ”¶ Building | 8 of 9 built |
| Ages 13â€“15 | â¬œ Future | â€” |

Last updated: 2026-05-27 EST (Toronto)

---

## âš¡ 2026-05-27 â€” S-DCC-KIDS-10-12-ROW6: Remix attribution shipped

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ next build from SME-REVIEW-004 order

### What Shipped (`digital-confidence/99c47ec`)

| File | What |
|------|------|
| `kids/10-12/when-i-remix-something-i-name-who-made-the-original.html` | Row 6 â€” Creative Making, 15 min, no screens, kid-leads |
| `kids/10-12/index.html` | Row 6 activated; count 6 â†’ 7; section-label updated |
| `kids/index.html` | 10-12 count updated to 7 activities |

**Notion Row 6 (`349a09cf-876a-8124-a6ff-cdda22772fd9`) â†’ Built**

**Key design decisions:**
- Kohlberg Stage 3 community ethics framing throughout: "attribution is how creative communities sustain themselves" â€” not legalistic
- Six remix types as visual tiles: fan art, memes, TikTok stitches, Roblox mods, music mash-ups, fan fiction
- Three-type copyright explainer: Creative Commons (CC BY), Canadian Copyright Act (fair dealing, not "fair use"), Crown copyright + Open Government Licence
- Vera: Crown copyright explicitly addressed â€” government content is not automatically free; look for the OGL badge
- Simple credit formula: [work description] by [creator], [source], [licence if known] â€” with 5 concrete examples
- Sources Named Running Count activity: TikTok stitch scenario with 5 sources (cooking clip, background music, downloaded font, food blog photo, own commentary) â€” check-off tally format; printable
- FAQ: 4 questions (can't find the original / memes / Roblox-Minecraft / fair dealing vs. fair use)
- Frank: tally gamification, physical worksheet, "Distracted Boyfriend" meme example for FAQ prep
- fr-QC gap noted in facilitator note: French build requires QuÃ©bÃ©cois creator examples before going live

### DCC Kids â€” Three cohorts

| Cohort | Status | Modules |
|--------|--------|---------|
| Ages 4â€“6 | âœ… Complete | 8 of 8 built |
| Ages 7â€“9 | âœ… Complete | 8 of 8 built |
| Ages 10â€“12 | ðŸ”¶ Building | 7 of 9 built |
| Ages 13â€“15 | â¬œ Future | â€” |

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/digital-confidence/kids/10-12/` to verify 7 active modules
- Next build sprint: Row 4 â€” Making a story with AI as my helper (most complex; no-login library variant; platform age restrictions must be addressed)

Last updated: 2026-05-27 EST (Toronto)

---

## âš¡ 2026-05-27 â€” S-DCC-KIDS-10-12-ROW7: Is this an ad? shipped

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ next build from SME-REVIEW-004 order

### What Shipped (`digital-confidence/504c3c9`)

| File | What |
|------|------|
| `kids/10-12/is-this-an-ad-or-did-they-really-mean-it.html` | Row 7 â€” Critical Thinking, 20 min, Internet optional, kid-leads |
| `kids/10-12/index.html` | Row 7 activated; count 5 â†’ 6; section-label updated |
| `kids/index.html` | 10-12 count updated to 6 activities |

**Notion Row 7 (`348a09cf-876a-815b-9435-df11c72e1a24`) â†’ Built**

**Key design decisions:**
- Disclosure Clock: three-zone timeline (first 30 sec âœ… / mid-video âš ï¸ / end of video ðŸš«) â€” makes video-specific timing concrete
- Relationship types grid: cash, gifted product, affiliate link, sponsored experience (all require disclosure) vs no-relationship purchase (doesn't)
- Ad Read Challenge: 5 text/screenshot scenarios distinct from Row 1 â€” caption-only, on-screen overlay, "honest review" title fallacy, end-of-video too-late disclosure, correct gifted disclosure
- Two-viewer compare format (kid-leads pairs, each makes independent call before comparing)
- Library-compatible: all scenarios are text-based, no live video required; optional clip enrichment noted
- Vera: description-only disclosure does not meet Canadian Ad Standards
- Dr. Lena: disappointment when a favourite creator doesn't disclose = the skill working; parasocial trust is real, not a weakness
- Frank: Scenario 3 ("honest review" title, no disclosure) generates strongest group discussion; Disclosure Clock becomes practical with a live device as optional enrichment
- Prereq link to spotting-hidden-advertising.html (soft prerequisite, not hard gate)

### DCC Kids â€” Three cohorts

| Cohort | Status | Modules |
|--------|--------|---------|
| Ages 4â€“6 | âœ… Complete | 8 of 8 built |
| Ages 7â€“9 | âœ… Complete | 8 of 8 built |
| Ages 10â€“12 | ðŸ”¶ Building | 6 of 9 built |
| Ages 13â€“15 | â¬œ Future | â€” |

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/digital-confidence/kids/10-12/` to verify 6 active modules
- Next build sprint: Row 6 â€” When I remix something, I name who made the original (Creative Making; Canadian Copyright Act; fr-QC gap; English build unblocked)

Last updated: 2026-05-27 EST (Toronto)

---

## âš¡ 2026-05-26 â€” S-DCC-KIDS-10-12-ROW1: Spotting hidden advertising shipped

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ next build from SME-REVIEW-004 order

### What Shipped (`digital-confidence/c16f6aa`)

| File | What |
|------|------|
| `kids/10-12/spotting-hidden-advertising.html` | Row 1 â€” Critical Thinking, 20 min, no screens, kid-leads |
| `kids/10-12/index.html` | Row 1 activated; count 4 â†’ 5; section-label updated |
| `kids/index.html` | 10-12 count updated to 5 activities |

**Notion Row 1 (`35ca09cf-876a-8142-ba37-fc1991f4e98e`) â†’ Built**

**Key design decisions:**
- Parasocial trust framing (Horton & Wohl 1956): one-directional emotional bonds with creators make paid recommendations feel like friend advice
- Creator earnings callout: $1Kâ€“$50K per sponsored post; familiarity is the product
- Two-layer taxonomy: obvious ads (banners/skippable) vs paid recommendations (harder to spot)
- Vera annotation: behavioural targeting as a third invisible layer
- Canadian Ad Standards: disclosure must be early and visible, never buried
- Ad Detective Challenge: 5 text-based scenarios, detective-and-witness pair format, printable (no live internet required for library use)
- Trust moment section: Dr. Lena's cognitive dissonance framing ("that disappointment is the lesson working")
- Research: Horton & Wohl (1956), Colliander & DahlÃ©n (2011), Jin & Phua (2014), Ad Standards Canada, MediaSmarts Canada, CRTC

### DCC Kids â€” Three cohorts

| Cohort | Status | Modules |
|--------|--------|---------|
| Ages 4â€“6 | âœ… Complete | 8 of 8 built |
| Ages 7â€“9 | âœ… Complete | 8 of 8 built |
| Ages 10â€“12 | ðŸ”¶ Building | 5 of 9 built |
| Ages 13â€“15 | â¬œ Future | â€” |

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/digital-confidence/kids/10-12/` to verify 5 active modules
- Next build sprint: Row 7 â€” Is this an ad? (multi-age Critical Thinking; kid-leads 10-12 variant)

Last updated: 2026-05-26 EST (Toronto)

---

## âš¡ 2026-05-26 â€” S-DCC-KIDS-10-12-ROW5: Password manager module shipped

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ highest-value build from SME-REVIEW-004 order

### What Shipped (`digital-confidence/f638653`)

| File | What |
|------|------|
| `kids/10-12/using-a-password-manager.html` | Row 5 â€” Tech Safety, family setup, 60-90 min, needs a device |
| `kids/10-12/creating-a-strong-password.html` | "Ready for next step" callout now links to password manager |
| `kids/10-12/index.html` | Row 5 activated; count 3 â†’ 4 |
| `kids/index.html` | 10-12 count updated to 4 activities |

**Notion Row 5 (`349a09cf-876a-811d-b763-c94c8fdef76e`) â†’ Built**

**Key design decisions:**
- Family-account framing throughout: caregiver is account owner (Vera annotation)
- One-time setup framing; child adds and manages at least one vault item themselves (Dr. Lena: skill-transfer requirement)
- Bitwarden (free, open source) and 1Password (paid, strong UX) â€” both presented as valid choices
- Credential-stuffing chain explainer (how one breach cascades to all accounts)
- Vault diagram showing master key â†’ entries
- Diceware passphrase method (4+ random words + number + symbol)
- 6-step family setup guide + printable home checklist
- Library version = 20-min preview-only + printed checklist (Frank annotation); fr-QC gap flagged

### DCC Kids â€” Three cohorts

| Cohort | Status | Modules |
|--------|--------|---------|
| Ages 4â€“6 | âœ… Complete | 8 of 8 built |
| Ages 7â€“9 | âœ… Complete | 8 of 8 built |
| Ages 10â€“12 | ðŸ”¶ Building | 4 of 9 built |
| Ages 13â€“15 | â¬œ Future | â€” |

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/digital-confidence/kids/10-12/` to verify 4 active modules
- Next build sprint: Row 1 â€” Spotting hidden advertising (Critical Thinking; parasocial framing + printed examples)

Last updated: 2026-05-26 EST (Toronto)

---

## âš¡ 2026-05-26 â€” S-CLAUDE-PREFERENCES-V3: CLAUDE-PREFERENCES v3 committed to system-rules

**Trigger:** Aaron typed "next sprint" â†’ Notion locked P2 HAL Stack item

### What Shipped (`two-birds-portfolio/88aa523`)

| File | What |
|------|------|
| `hal-stack/system-rules/CLAUDE-PREFERENCES-2026-05-26.md` | CLAUDE-PREFERENCES v3 â€” fetched from Google Drive ID `1VcKCUzn-qNl7tHFT_CDMdSRBjVpYiVD7`, written and committed |

**v3 change:** Presentation tool rule added (LLM-agnostic). Covers Gamma/Canva data integrity, workflow, and access constraints. Applies to every tool call, every session, every LLM.

**Cancelled same session:** Paperwork Labs brief v3 sprint (`36ba09cf`) â€” superseded by v7 Word doc (Google Drive, built 2026-05-26). Marked Done in Notion, no file committed.

**Note:** The Paperwork Labs v7 Word doc is a separate file. Drive file ID `1VcKCUzn-qNl7tHFT_CDMdSRBjVpYiVD7` is CLAUDE-PREFERENCES, not Paperwork Labs.

### Next recommended action for Aaron
- Type `next sprint` to continue â€” DCC Row 5 (password manager) is next in the build queue

Last updated: 2026-05-26 EST (Toronto)

---

## âš¡ 2026-05-02 â€” S-CONTEXT-EXPORT-2026-04-28 (just-go single sprint)

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 + queue empty â†’ "just go".

### What Shipped

- `hal-stack/context-system/exports/2026-04-28-ci-hardening-claude-md-trim.md` â€” context export covering 2026-04-25 (portfolio CI) + 2026-04-28 (gitleaks + RETRO + CLAUDE.md trim). Includes decisions table, open questions, artifact index, key context for future sessions.
- `hal-stack/context-system/context-index.md` â€” new row added at top of Active Contexts table.
- Notion: `354a09cf-876a-8168-ae44-c03122c57ec1` filed as Done.

### Next recommended action for Aaron
- Check GitHub Actions on `two-birds-portfolio` â€” confirm gitleaks first-run passed clean
- Provide Calendly URL â†’ unlocks P1 revenue sprint (mailto â†’ Calendly on Clarity + TBI, ~30 min)

Last updated: 2026-05-02 at 10:00 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.

---

## âš¡ 2026-05-02 â€” S-CALENDLY (just-go single sprint)

**Trigger:** Aaron provided `https://calendly.com/aaronpatzalek` and typed "just go".

### What Shipped

- `clarity/index.html:762` â€” `href="#"` â†’ `https://calendly.com/aaronpatzalek` on "Book a Free 30-Minute Call" button. `target="_blank" rel="noopener"` already present. Commit `d97607b` on clarity master.
- `two-birds-innovation/index.html:313` â€” `mailto:aaron.patzalek@gmail.com?subject=...` â†’ `https://calendly.com/aaronpatzalek`, `target="_blank" rel="noopener"` added, button text "Email Us" â†’ "Book a Free Call". Commit `d2e788a` on two-birds-innovation master.
- Email address + phone in `contact-details` block kept as secondary contacts on both sites.
- Notion: `354a09cf-876a-8147-b885-e9db2328fbf1` filed as Done (P1).

### Next recommended action for Aaron
- Both repos pushed to GitHub Pages â€” verify the buttons open calendly.com/aaronpatzalek in a new tab
- Next P1 human item: LinkedIn URL for TBI contact section (3 min, ask Aaron to confirm handle)

Last updated: 2026-05-02 at 11:15 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.

---

## âš¡ 2026-05-02 â€” S-TBI-LINKEDIN (just-go single sprint)

**Trigger:** Aaron confirmed "just go". LinkedIn URL sourced from `career-ops/cv.md`.

### What Shipped
- `two-birds-innovation/index.html:318` â€” `https://linkedin.com/in/aaronpatzalek` added to contact-details block alongside email + phone. Commit `4eadbad` on two-birds-innovation master.
- Notion: `354a09cf-876a-81f7-a573-f8ca13d760b5` filed as Done (P1).

### P1 backlog status after today's session
- âœ… Calendly URL wired to Clarity + TBI CTAs
- âœ… LinkedIn link added to TBI contact section
- â¬œ Kevin site forward path (Aaron decision)
- â¬œ Google Maps API key referrer restrictions (Aaron action)
- â¬œ DCC v2 wizard evaluation (Aaron review)

Last updated: 2026-05-02 at 11:30 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.

---

## âš¡ 2026-05-02 (overnight) â€” 3-sprint autonomous run (S-OG-CARDS / S-CLARITY-WHY-BUILT / S-R01-STRETCH)

**Trigger:** Aaron said "go" before sleeping. 3-hour autonomous run, normal mode. Notion queue exit 3, local queue empty. Aaron also corrected two profile errors: "solo parent" â†’ "married, parent of twins"; ADHD never to be mentioned. CLAUDE.md + memory updated (`7f42859`).

### Sprint 1 â€” S-OG-CARDS: OG card images for brand sites (~70 min)
**Commits:** `aaron-patzalek/108ca44`, `two-birds-innovation/0d79577`

Both brand sites previously had blank link previews on LinkedIn, Slack, iMessage, WhatsApp, Discord.

- `aaron-patzalek/images/og-card.svg` (1200Ã—630) â€” dark navy/blue gradient, AP initials badge, name/title/tagline, stats row (20yr, St. Thomas, Canadian-built), Calendly CTA
- `two-birds-innovation/images/og-card.svg` (1200Ã—630) â€” deep space theme, teal accent bar, company name/taglines, service pricing cards (CA$2,500 / CA$4,000), Calendly CTA
- `og:image` meta wired on both sites (TBI had no og:image at all; AP's pointed to a missing .png â†’ updated to .svg + added width/height/alt)
- `images/export-og-png.html` in both repos â€” Chrome DevTools export helper for PNG conversion (needed for full Twitter/X coverage)

**Aaron action needed:** To get full Twitter/X support, open `images/export-og-png.html` in Chrome, F12 â†’ Ctrl+Shift+P â†’ "Capture full size screenshot", save as `og-card.png` in the same folder, then update `og:image` from `.svg` â†’ `.png`.

**Notion:** `355a09cf-876a-810e-81ab-cc9c3c6831d6` (Done, P1)

### Sprint 2 â€” S-CLARITY-WHY-BUILT: "Why I built this" trust section (~35 min)
**Commit:** `clarity/4873edb`

- New `<section class="why-built">` between `</main>` and `<footer>` in Clarity
- Olive-light background, left-border accent, 4 paragraphs of Aaron's origin story
- Content: 20yr PM at TELUS/Staples/Start.ca â†’ watched AI widen enterprise/SME gap â†’ built Clarity to close it â†’ privacy reassurance (your data stays in your browser)
- Byline with name, role, location, TBI link
- CSS in the `<style>` block, matches existing Clarity tokens

**Aaron action needed:** Review copy before promoting to a prospect. The story is accurate based on known context but Aaron should verify the framing works for his voice. Easy to edit in index.html.

**Notion:** `355a09cf-876a-8169-bbbe-c7ce84155165` (Done, P2)

### Sprint 3 â€” S-R01-STRETCH-1m/1n/1o: 3 DCC Research DB depth rows (~80 min)
**Commit:** `portfolio/82da6be`

All 3 at Status=Research. No ADHD in learning_profile per Aaron's instruction.

| ID | Skill | Category | Age |
|----|-------|----------|-----|
| `355a09cf-876a-8198-...` | Reading visual and audio media for signs of AI manipulation (deepfakes) | Critical-Thinking | 13-15 |
| `355a09cf-876a-817c-...` | Big feelings are real; I get to choose what I do next | Emotional-Safety | 4-6 |
| `355a09cf-876a-8171-...` | Following a story back to where it started (source tracing / SIFT) | Critical-Thinking | 10-12 |

Row 1m: C2PA/Content Authenticity Initiative, MIT Media Lab, Sensity AI, Europol 2022, liar's dividend concept.
Row 1n: Siegel & Bryson 'name it to tame it', Kopp 1982, Eisenberg 2000, Radesky 2020 (AAP), Erikson.
Row 1o: SIFT (Caulfield 2019), Stanford SHEG Civic Online Reasoning, RAND Truth Decay, MediaSmarts Canada.

**Notion:** `355a09cf-876a-810a-b36e-e47f646a9539` (Done, P3)

### What was NOT touched
- DCC wizard evaluation â€” still waiting on Aaron's decision (a/b/c from SESSION-STATE 2026-04-22)
- Kevin site forward path â€” Aaron decision still pending
- Google Maps API key referrer restrictions â€” Aaron action still pending
- Career Coach pricing.html â€” blocked on defining what Pro is
- OG card PNG conversion â€” Aaron action (see Sprint 1 above)

### P1 backlog status after overnight run
- âœ… Calendly URL wired to Clarity + TBI CTAs
- âœ… LinkedIn link added to TBI contact section
- âœ… OG cards live on both brand sites (SVG; PNG conversion is a 5-min Aaron task)
- â¬œ Kevin site forward path (Aaron decision)
- â¬œ Google Maps API key referrer restrictions (Aaron action)
- â¬œ DCC v2 wizard evaluation (Aaron review)

Last updated: 2026-05-02 overnight (autonomous run)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.

---

## âš¡ 2026-05-04 (overnight) â€” 2-sprint autonomous run (S-SOLO-PARENT-CLEANUP / S-R01-STRETCH-1p/1q/1r)

**Trigger:** Aaron said "go" before sleeping. Normal mode. Notion queue exit 3.

### Sprint 1 â€” S-SOLO-PARENT-CLEANUP (~20 min)
**Commit:** `portfolio/57132ae`

Corrected "solo parent" â†’ accurate description across all 9 remaining files. The CLAUDE.md fix (`7f42859`) was done 2026-05-02; this sprint finishes the sweep.

| File | Change |
|------|--------|
| README.md | "Solo parent" â†’ "Married, parent" |
| hal-stack/sprint-system/aaron-todos-2026-04-21.md | "Solo parent / St. Thomas" â†’ "Parent of twins / St. Thomas" |
| journey/narrative/chapter-05-the-overnight-builds.md | "A solo parent with twin six-year-olds" â†’ "A parent of twin six-year-olds" |
| hal-stack/personas/advisory/scrappy-pack.md | "solo parent" â†’ "working parent" |
| hal-stack/personas/inner-circle.md | "solo parent of twin 6-year-olds" â†’ "parent of twin 6-year-olds" |
| hal-stack/voice-layer/README.md | "solo parent" â†’ "parent" |
| hal-stack/context-system/context-loader-prompt.md | "solo parent" â†’ "married and a parent" |
| hal-stack/architecture/principles.md | "solo parent" â†’ "parent" |
| sovereignty/05-ip-register.md | "Solo parent building in public" â†’ "Parent and founder building in public" |

One remaining instance in SESSION-STATE.md is the correction log itself â€” intentional.

**Notion:** `356a09cf-876a-812c-aab0-d93c9db68d56` (Done, P1)

### Sprint 2 â€” S-R01-STRETCH-1p/1q/1r: 3 more DCC Research DB rows (~90 min)
**Commit:** `portfolio/1fe9959`

DCC Research DB now has 26 rows (20 coverage + 6 depth). All at Status=Research.

| ID | Skill | Category | Age |
|----|-------|----------|-----|
| `356a09cf-876a-810b-...` | Real, made-up, or somewhere in between â€” sorting what I find online | Critical-Thinking | 7-9 |
| `356a09cf-876a-81b4-...` | Publishing my work responsibly â€” audience, consent, and permanence | Creative-Making | 13-15 |
| `356a09cf-876a-8103-...` | My device has eyes, ears, and a memory â€” and I get to choose who uses them | Tech-Safety | 4-6 |

Row 1p: three-bucket sorting (verified/opinion/invented). Piaget classification, MediaSmarts Break the Fake, Lewandowsky 2012.
Row 1q: publishing framework (audience modelling, consent, screenshot permanence). PIPEDA/CPPA, Solove 2007, Creative Commons, CCCP.
Row 1r: device sensor awareness for youngest group. Camera cover habit, permission-check habit, smart speaker awareness. AAP/CPS, CCCP, Radesky 2020.

**Notion:** `356a09cf-876a-8122-8815-c9124b8b0610` (Done, P3)

### P1 backlog status (unchanged)
- âœ… Calendly URL wired to Clarity + TBI CTAs
- âœ… LinkedIn link added to TBI contact section
- âœ… OG cards live on both brand sites (PNG conversion is a 5-min Aaron task)
- âœ… "solo parent" corrected across entire repo
- â¬œ Kevin site forward path (Aaron decision)
- â¬œ Google Maps API key referrer restrictions (Aaron action)
- â¬œ DCC v2 wizard evaluation (Aaron review)

Last updated: 2026-05-04 overnight (autonomous run)

---

## âš¡ 2026-05-08 â€” S-TIKTOK-VET: TikTok screenshot vetting (49 images)

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ "tiktok-vet" â†’ "tiktok-vet-retry"

### What Shipped

- `C:\mnt\user-data\outputs\TikTok_Vetting_MASTER_TABLE.md` â€” 49 images catalogued across 12 series. Every image read and described: filename, tool, category, description, series, sovereignty tag, cost, HAL Stack fit.
- 6 Notion backlog items created in `dee08637-7122-46cd-bc29-7775ce3ab8f6`:

| Sprint ID | Priority | Status | Item |
|-----------|----------|--------|------|
| S-LOOP-001 | P1 | Ready | /loop automation patterns (Boris Cherny) |
| S-029-EXTENDED | P2 | Backlog | RuFlo vs /loop trade-off analysis |
| S-BIONIC-001 | P2 | Backlog | Bionic Reading mode for DCC |
| S-IMPECCABLE | P2 | Backlog | Impeccable + Taste Skill design vocabulary |
| S-OPEN-DESIGN-001 | P2 | Backlog | Evaluate Open Design (open-source Claude Design) |
| S-PUBLIC-APIS-001 | P2 | Backlog | Catalogue public-apis for Two Birds products |

### Key findings from vetting

- **Series L (Boris Cherny /loop, 10 frames):** He uses /loop for PR babysitting, flaky test detection, Twitter feedback clustering every 30 min, server-side monitoring. "Dozens of loops running." S-LOOP-001 is P1 Ready.
- **Series F (RuFlo, 6 frames):** 60+ agents, Queen hierarchy, WASM 352x faster, #1 GitHub. Sovereign but heavyweight. S-029-EXTENDED = evaluate vs /loop before adopting.
- **Series C (Open Design, 5 frames):** Open-source Claude Design alternative. BYOK, local-first, Apache-2.0, 31 skills, 72 brand outputs. No subscription.
- **Series G (Design Skills, 6 frames):** Impeccable (`npx skills add pbakaus/impeccable`) + Taste Skill (tasteskill.dev, 7.2K stars) â€” design vocabulary for AI harnesses. Directly relevant to DCC + Clarity quality.
- **Series K (Bionic Reading, 1 frame):** 7,778 likes / 2,974 saves. CSS/JS fixation-point technique â€” P2 DCC accessibility enhancement.
- **4 images [REJECTED]:** Wan2GP, Hunyuan, LTX-Video (frame 35) â€” all require local consumer GPU Aaron doesn't have.

### Next recommended action

- Type `next sprint` â†’ S-LOOP-001 is now P1 Ready in Notion.

Last updated: 2026-05-08 (TikTok vetting session)

---

## âš¡ 2026-05-08 â€” loop-pr-babysitter run

### Results

| Check | Result |
|-------|--------|
| Repos ahead of remote | 0 â€” all clean |
| Uncommitted work | two-birds-portfolio: 2 untracked files (`helpers-README.md`, `mcp-write-log.txt`) â€” not blocking |
| Stale branches | 0 â€” all repos are clean single-branch |
| CI: two-birds-portfolio | âœ… PASS (latest: S-LOOP-001 push, today) |
| CI: digital-confidence | âŒ FAIL â†’ âœ… FIXED â€” `build-health-report.yml` commit `5650be6` |

### CI fix applied

**DCC `build-health-report.yml`** â€” `SyntaxError: Invalid or unexpected token`
- **Root cause:** Commit messages with backticks (`` `abc1234` ``) injected directly into JS template literals via `${{ steps.*.outputs.* }}`, breaking JS syntax at YAML-parse time.
- **Fix:** Moved all step outputs to `env:` block; read via `process.env` inside the script. Safe regardless of commit message content.
- **Commit:** `digital-confidence/5650be6`

---

## âš¡ 2026-05-08 â€” S-LOOP-001: /loop automation patterns (Boris Cherny)

**Trigger:** Aaron typed "next sprint" â†’ Notion locked S-LOOP-001 (P1)

### What Shipped

`hal-stack/loop-patterns/` â€” new directory, 5 files:

| File | Loop Job | Recommended Interval |
|------|----------|---------------------|
| `README.md` | Pattern overview, Boris Cherny source, 4 run modes (manual/loop/Task Scheduler/schedule skill) | â€” |
| `loop-pr-babysitter.md` | Scan repos for stale branches, CI failures, uncommitted work; auto-fix mechanical CI errors | Daily or on-demand |
| `loop-backlog-health.md` | Read Notion backlog; flag P1 items going cold, stale Ready items, orphaned In Progress, any P0 not running | Weekly |
| `loop-content-freshness.md` | Run DCC freshness script; check brand site lastmod; flag stale modules; auto-create Notion items for STALE | Weekly |
| `loop-notion-sync-verify.md` | Verify SYNC-LOG freshness, test MCP connectivity, check NOTION_API_KEY; canary for all other loops | Daily (2 AM) |

### Boris Cherny pattern principles documented

1. Cron + repeat â€” every loop has a fixed interval
2. Dozens in parallel â€” each loop is narrow and focused
3. Server-side â€” most valuable loops run without Aaron present
4. 100 agents simultaneously â€” loops spawn agents only when needed
5. Sovereign â€” /loop is built into Claude Code, zero external deps

### Next recommended action for Aaron

- Run `loop-pr-babysitter.md` now (just paste the prompt) â€” clears any CI debt
- Add `loop-notion-sync-verify.md` prompt to `run-overnight-build.bat` for daily 2 AM run
- Next sprint: S-029-EXTENDED (RuFlo vs /loop trade-off) or S-BIONIC-001 (Bionic Reading DCC)

---

## âš¡ 2026-05-08 â€” Automation Governance System Phase 1 (SSOT + Verification + Audit)

**Trigger:** Aaron typed "next sprint" â†’ Notion locked `35ba09cf-876a-81d3-94b7-df95a876fd2f` (P2)

### What Shipped

4 new SSOT files in `.claude/`:

| File | Purpose |
|------|---------|
| `.claude/status-semantics.yaml` | Canonical Notion status strings â€” auto_pick_status, in_progress_status, done_statuses |
| `.claude/sprint-schema.json` | Sprint payload shape + required fields (notion_id, item, priority, status) |
| `.claude/verification-checklist.md` | Pre-flight checks + smoke test commands |
| `.claude/automation-governance.md` | Rules 1-4: Verify, SSOT, Schema, Next-action mandatory |

`hal-stack/notion-sync/next-sprint.py` updated:
- Added `_load_status_semantics()` â€” parses status-semantics.yaml, no external deps
- `pick_next_ready()` now takes `auto_pick_status` param (loaded from SSOT, default "Ready")
- `main()` loads SSOT on startup; uses `auto_pick_status` + `in_progress_status` from YAML
- Hardcoded `"Ready"` and `"In Progress"` strings replaced â€” Rule 2 enforced

Also committed: `hal-stack/sprint-system/helpers-README.md` + `logs/mcp-write-log.txt` (untracked since loop session)

**Notion:** `35ba09cf-876a-81d3-94b7-df95a876fd2f` â†’ Done

### Test
```bash
python hal-stack/notion-sync/next-sprint.py
# Exit 0 = sprint locked from SSOT-driven status check
# Exit 3 = no Ready items (expected if Notion backlog is empty)
```

### Next recommended action for Aaron
- Phase 2 (next week): `audit-sprints.py` nightly enforcement â€” wire into `run-overnight-build.bat`
- Next content sprint: S-BIONIC-001 (Bionic Reading DCC) or S-029-EXTENDED (RuFlo vs /loop)

---

## âš¡ 2026-05-09 â€” S-BIONIC-001: Bionic Reading mode for DCC

**Trigger:** Aaron selected S-BIONIC-001 â†’ Notion locked `35aa09cf-876a-8185-969d-e60660dcf5ea` (P2)

### What Shipped

`digital-confidence/aee6239`

| File | Change |
|------|--------|
| `js/bionic-reading.js` | New standalone module â€” TreeWalker bolds first ~50% of each word; reversible; skips UI chrome; `window.DCC_BionicReading` API; `dc-bionic-reading` localStorage key |
| `css/accessibility.css` | `.bionic-reading b.dc-b { font-weight: 700 }` + dark mode softened to 600 |
| `accessibility/settings.html` | New toggle row in Reading Aids (EN + FR), script tag, `dc-bionic-reading` added to reset array |
| `js/accessibility.js` | `initBionicReading()` injects ð bar button; called in DOMContentLoaded |

### How it works
- Enable: TreeWalker finds text nodes in `main/article/body`, splits each word on midpoint, wraps first half in `<b class="dc-b">`
- Disable: finds all `b.dc-b`, merges back with next text sibling, calls `normalize()`
- Skips: buttons, nav, `.accessibility-bar`, `.top-bar`, footer, code, pre, inputs
- Settings page: toggle in Reading Aids section alongside high-contrast, text-spacing, reading guide, reduce-motion

**Notion:** `35aa09cf-876a-8185-969d-e60660dcf5ea` â†’ Done

### Note â€” pre-existing deletion
`js/feedback-github.js` was missing from working tree before this sprint (not in git, not committed). Restored it via `git checkout` and excluded from this commit. Aaron should investigate if that file was intentionally removed.

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/digital-confidence/accessibility/settings.html` â€” verify the Bionic Reading toggle appears in Reading Aids and the ð button appears in the header bar
- Toggle it on a module page and confirm text bolding + reversal works
- Next sprint: S-029-EXTENDED (RuFlo vs /loop) or S-IMPECCABLE (design vocabulary)

---

## âš¡ 2026-05-09 â€” S-IMPECCABLE: Impeccable + Taste Skill evaluation

**Trigger:** Aaron typed "next sprint" â†’ Notion locked `35aa09cf-876a-81b9-bc78-c4ac0cd216bb` (P2)

### What Shipped

- Installed 13 skills via `npx skills add`: 1 Impeccable + 12 Taste Skill variants
- Skills live in `.agents/skills/` (symlinked to Claude Code â€” available after session restart)
- `hal-stack/research/design-skills-eval-2026-05-09.md` â€” full evaluation with scan results, applicability matrix, command reference

### Live scan results

**Clarity** (`npx impeccable --json clarity/index.html`):
- 6Ã— WCAG AA contrast failures: `#888888`, `#999999`, `#b0b0a8` on `#ede8df` backgrounds (2.2â€“2.9:1 vs 4.5:1 required)
- Roboto flagged as overused/generic font

**DCC** (`npx impeccable --json --fast digital-confidence/index.html`):
- `border-left: 6px solid #c0392b` at line 744 â€” flagged as "side-tab AI tell"
- Single font (Georgia only â€” no UI/body pairing)
- Flat type hierarchy: 12 sizes between 12pxâ€“22px

### Key verdict
- **Impeccable:** âœ… Use now â€” works on static HTML, found real issues, commands are actionable
- **Taste Skill:** âš ï¸ Design vocabulary only â€” assumes React/Tailwind stack (not our sites)
- **Taste Skill variants `minimalist-ui` + `redesign-existing-projects`:** Worth reading when planning Clarity v2 or DCC redesign

### Next recommended action for Aaron
- **P1:** Fix Clarity contrast: change `#888888`/`#999999`/`#b0b0a8` â†’ `#5a5850` on `#ede8df` sections (WCAG AA passes at 4.6:1) â€” or run `/impeccable colorize` in a new session
- **P2:** Run `/impeccable teach` on Clarity to create `PRODUCT.md` â€” unlocks brand-aware output for all future design commands
- Note: skills load on next Claude Code session restart (they're symlinked, not yet in this session's context)

**Notion:** `35aa09cf-876a-81b9-bc78-c4ac0cd216bb` â†’ Done

---

## âš¡ 2026-05-09 â€” Clarity WCAG AA contrast fix

**Trigger:** Aaron typed "next sprint" Ã— 2 â†’ Notion exit 3 â†’ highest-value available work

### What Shipped

`clarity/dae4994` â€” 3 inline colour fixes in `.cta-card`:

| Element | Before | After | Contrast (on #EDE8DF) |
|---|---|---|---|
| Caption "No obligation..." | `#888` | `#5C584E` | 2.9 â†’ 5.3:1 âœ“ |
| Meta "Aaron Patzalek..." | `#999` | `#5C584E` | 2.3 â†’ 5.3:1 âœ“ |
| Portfolio links | `#999` | `#4A5640` | 2.3 â†’ 5.8:1 âœ“ |

Post-fix scan: 0 real WCAG AA failures. Remaining scanner flags (`#B0B0A8` Ã— 3) are false positives â€” scanner can't resolve `var(--charcoal)` CSS custom properties; actual contrast on `#2C2C2C` header/footer is 6.4:1.

### Next recommended action for Aaron
- Clarity is now prospect-safe on accessibility. Remaining impeccable flags (Roboto font) are design preference â€” address in Clarity v2.
- Next sprint: S-029-EXTENDED (RuFlo vs /loop) or S-OPEN-DESIGN-001

---

## âš¡ 2026-05-09 â€” S-029-EXTENDED: RuFlo vs /loop decision

**Trigger:** Aaron said "you pick: next sprint" â†’ S-029-EXTENDED selected and locked

### What Shipped

`hal-stack/research/ruflo-vs-loop-2026-05-09.md` â€” 1-page decision doc.

**Decision: Defer RuFlo. Stay with /loop.**

RuFlo solves parallel multi-agent coordination, distributed consensus, vector memory, and cost routing at scale. None of those are current bottlenecks. /loop is sovereign, zero-maintenance, and already running overnight.

**Revisit triggers:**
- Monthly CC spend > $200 (3-tier routing saves matter)
- Need 5+ parallel agents simultaneously
- DCC reaches 100+ modules (RuVector earns its place)
- Second developer joins

**Insight surfaced:** The real gap /loop doesn't fill is *persistent context between sessions* â€” not multi-agent orchestration. The `schedule` skill is the sovereign path to that, not RuFlo.

**Notion:** `35aa09cf-876a-81cd-84c0-edb43a991dba` â†’ Done

### Next recommended action for Aaron
- Read `hal-stack/research/ruflo-vs-loop-2026-05-09.md` (2 min) â€” confirm or override the decision
- Next sprint: S-OPEN-DESIGN-001 (Open Design evaluation) or S-PUBLIC-APIS-001

---

## âš¡ 2026-05-09 â€” S-OPEN-DESIGN-001: Open Design evaluation

**Trigger:** Aaron typed "next sprint" â†’ S-OPEN-DESIGN-001 selected

### What Shipped

Installed 70+ skills from `nexu-io/open-design` (Apache-2.0). Three families: Open Design surfaces (~25), zhangzara HTML slide deck variants (~35), specialty outputs (~10). All available after session restart.

`hal-stack/research/open-design-eval-2026-05-09.md` â€” full evaluation.

**Decision: Partial adoption â€” hold for net-new work.**

| Scenario | Decision |
|---|---|
| Existing pages (Clarity, TBI, DCC) | âŒ Wrong workflow for in-place edits |
| Clarity v2 full rebuild | âœ… Use `kami-landing` as starting point |
| Client pitch decks | âœ… Use `open-design-landing-deck` or `html-ppt-pitch-deck` â€” use now |
| TBI blog / email outreach | âœ… Use `blog-post` / `email-marketing` when ready |
| Design critique | âŒ Use Impeccable â€” better tool for that job |

**Key insight:** Open Design is a code-generation framework (inputs.json â†’ HTML), not an in-place editor. Atelier Zero aesthetic (warm paper, coral, Inter Tight + Playfair) doesn't match current brand â€” but could anchor Clarity v2.

**Notion:** `35aa09cf-876a-8168-a4de-fd16356d2439` â†’ Done

### Next recommended action for Aaron
- Lowest-friction use: generate a pitch deck for a prospect meeting using `/open-design-landing-deck` or `/html-ppt-pitch-deck` in a new session (skills load on restart)
- Remaining backlog: S-PUBLIC-APIS-001 (catalogue public-apis for Two Birds products) â€” last P2 item

---

## âš¡ 2026-05-09 â€” S-PUBLIC-APIS-001: Public APIs catalogue

**Trigger:** Aaron typed "next sprint"

### What Shipped

`hal-stack/research/public-apis-catalogue-2026-05-09.md` â€” shortlist of 10 APIs across 4 products with integration notes and static-HTML-safe flag.

**Immediately usable (no key, CORS-safe):**
| API | Product | Feature |
|---|---|---|
| Remotive | Career Coach | Live remote job listings panel |
| Bank of Canada Valet | Clarity | Economic context card (prime rate, CAD/USD) |
| StatCan Labour Force Survey | Career Coach | Canadian unemployment rate badge |
| Currents | DCC | "AI & digital safety in the news" sidebar |

**Deferred (need Cloudflare Worker proxy):**
- Have I Been Pwned â†’ DCC "was my data leaked?" tool â€” highest engagement potential with seniors
- NewsAPI â†’ Clarity industry news sidebar

**Cloudflare Worker pattern documented** â€” free tier (100K req/day) as sovereign backend proxy for key-protected APIs.

**Notion:** `35aa09cf-876a-819c-a4bd-d1a01c4f8639` â†’ Done

### P2 Backlog Status â€” All 6 TikTok-vetting items now Done
- âœ… S-LOOP-001 â€” loop patterns library
- âœ… S-BIONIC-001 â€” Bionic Reading DCC
- âœ… S-IMPECCABLE â€” Impeccable + Taste Skill installed
- âœ… S-029-EXTENDED â€” RuFlo vs /loop decision
- âœ… S-OPEN-DESIGN-001 â€” Open Design 70+ skills installed
- âœ… S-PUBLIC-APIS-001 â€” public-apis catalogue

### Next recommended action for Aaron
- **Quickest product win:** Wire Remotive API into Career Coach â€” live remote job listings, no key needed, CORS-safe, ~45 min sprint
- **Highest impact for prospects:** HIBP "was my data leaked?" in DCC â€” needs a Cloudflare Worker proxy (~60 min to set up, free)
- Notion backlog is now empty â€” time to promote new items or pull from DCC Research DB

---

## âš¡ 2026-05-09 â€” Career Coach: Live Remote Jobs panel

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ highest product value pick

### What Shipped

`career-coach/5baf798` â€” new "Live Remote Jobs" collapsible panel below Job Market Insights.

- Fetches from Remotive API (`https://remotive.com/api/remote-jobs?limit=10`) on first open â€” lazy, no eager load
- Displays 6 live remote listings: title, company, date posted, category badge, "View & Apply â†’" link
- No auth, no backend, CORS-safe â€” pure static HTML JS
- XSS-safe (esc() helper on all API data before rendering)
- Bilingual labels matching existing Career Coach i18n pattern
- Verified API is live and returning data before committing

### Next recommended action for Aaron
- Visit Career Coach in browser â†’ expand "Live Remote Jobs" panel â†’ confirm live listings appear
- The existing "Job Market Insights â€” Canada, March 2026" static panel is now stale â€” update copy to current date when convenient (5 min)
- Next sprint candidates: Bank of Canada Valet â†’ Clarity economic context card, or DCC Research DB rows

---

## âš¡ 2026-05-09 â€” Clarity: Canadian Economic Context card

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ highest prospect-impact pick

### What Shipped

`clarity/32e294b` â€” economic context card in results section (between next-step and CTA).

- Fetches CAD/USD + CORRA overnight rate from Bank of Canada Valet API on page load
- No auth, no backend, CORS-safe, daily updates
- Live values as of 2026-05-08: CAD/USD 0.7307 Â· CORRA 2.27%
- Silent-fail if API unreachable (card simply absent â€” no broken UI)
- Placed between actionable recommendations and the "Book a Call" CTA â€” macro context for AI investment timing

### Next recommended action for Aaron
- Run Clarity diagnostic and verify the economic context card appears in results with live BoC data
- Remaining from public-apis catalogue: StatCan LFS unemployment badge for Career Coach (~30 min), Currents news feed for DCC (~45 min)

Last updated: 2026-05-09

---

## âš¡ 2026-05-09 â€” Kevin's Apartment Search: bug fixes + v2 design preview

**Trigger:** Aaron asked for a UI refresh + QA fixes

### Bugs Fixed (index.html + kevin.js)

| Bug | Fix |
|---|---|
| Hardcoded `new Date('2026-03-28')` in expiry check | â†’ `new Date()` â€” expiry warnings now use today |
| Duplicate `#map-embed` section (Google Maps iframe with exposed API key) | Removed â€” Leaflet map covers it |
| 16 per-card OpenStreetMap iframes loading simultaneously | â†’ `KAS_NO_CARD_MAP` flag â€” removed from v2, preserved in v1 |

### V2 Design Preview (index-v2.html + css/kevin-v2.css)

Open `kevins-apartment-search/index-v2.html` in browser (or via GitHub Pages once it builds).

Key changes:
- **Header**: live stat bar (active listing count, last updated date, commute time) â€” no more hardcoded text
- **Section headings**: emoji removed; accent bar visual treatment instead
- **Section order**: listings â†’ single Leaflet map â†’ criteria panel â†’ second-tier â†’ table â†’ archive
- **Cards**: tighter padding, hover lift effect, grid action bar (primary CTA + compact icon buttons for fav/compare/flag)
- **No per-card iframes** â€” cuts 16 concurrent OSM loads

### What still needs Aaron's call
- **Approve v2 or redirect?** Open index-v2.html, compare with index.html, tell me what to change
- **Google Maps API key** â€” still in the repo (now only in v1's removed section, but may be in git history). Aaron needs to add HTTP referrer restrictions in Google Cloud Console (P1 backlog item).
- **Auto-refresh (listing staleness)** â€” there's no automated mechanism. The AUDIT.md recommended a `listing-availability-probe.yml` GitHub Action (HEAD request to each listing URL). Want me to build that?

---

## âš¡ 2026-05-09 â€” KAS: autonomous run + multi-user transformation

**Trigger:** Aaron asked for autonomous cleanup + multi-user vision

### What Shipped Autonomously (`e37d933`)

| File | What |
|---|---|
| `.github/workflows/listing-availability-probe.yml` | Weekly Monday GitHub Action â€” HEAD-requests all active listing URLs, opens/updates issue for any 404/410/5xx. Replaces broken date_added heuristic with real URL evidence. |
| `js/kas-setup.js` | Multi-user personalisation module. Access code gate + first-visit onboarding modal (name, city, commute anchor, budget) + âš™ï¸ settings button for return visits. Syncs to kevin_criteria localStorage. Non-invasive â€” no kevin.js changes. |
| `config.json` | + tool_name, access_code ("find-my-flat" placeholder), show_demo_listings |
| `index-v2.html` | + kas-setup.js wired in |

### Notion housekeeping
- Closed: "Make kevins-apartment-search private" Ã— 2 (superseded â€” going public/multi-user)
- Created 5 human backlog items (all Owner=Aaron, P1/P2)

### Aaron's 5 decisions (in order)
1. Open `index-v2.html` on GitHub Pages â†’ approve or redirect
2. Choose the access code to publish (or remove for open access)
3. Google Maps API key â†’ 5 min in Google Cloud Console
4. Repo name â€” what to call it publicly
5. Listing data strategy â€” keep Kevin's as demo, replace, or ship empty

Last updated: 2026-05-09

---

## âš¡ 2026-05-09 â€” KAS: Neighbourhood Intelligence + Persona System

**Trigger:** Aaron asked for social/safety/convenience indicators with persona-based flags

### What Shipped (`2397390`)

**`js/kas-neighbourhood.js`** â€” OSM Overpass proximity module, IntersectionObserver lazy-load, 10 flag types (hospital/pharmacy/school/park/transit/train/grocery/low-nightlife/quiet-rail/quiet-road), persona-aware flag filtering, crime context from neighbourhood-data.json, localStorage cache.

**`js/kas-setup.js`** â€” 6 persona toggles added to onboarding: Elder/Senior, Single woman, Family with kids, Young professional, Student, Pet owner. Saved to kas_user_setup.personas.

**`neighbourhood-data.json`** â€” all 13 London ON neighbourhoods extended with: violent_risk / property_risk / break_in_risk / noise_level / noise_notes / railway_nearby / major_road_nearby (community estimates, disclaimer prominent).

**`css/kas-neighbourhood.css`** â€” panel styles, persona grid, spinner.

### Human backlog created (Notion, Owner=Aaron)
- **P2** Walk Score API key + Cloudflare Worker proxy
- **P2** Verify crime annotations against LPS data
- **P2** Decide on Add My Own Listing feature
- **P3** Noise pollution data expansion

### What's deferred (and why)
- Walk Score â€” no CORS, needs proxy + API key
- Automated crime data â€” no free Canadian crime API for static sites
- Flight path noise â€” needs OpenAIP/FlightAware keys

Last updated: 2026-05-09
---

## âš¡ 2026-05-09 â€” KAS: StatCan Crime Data Pipeline

### What Shipped (`623043d`)

**`data/crime-stats.json`** â€” CMA-level StatCan crime data for London ON + 4 Ontario cities.
- Fields: crime_severity_index, violent/property/break-in rates, derived risk (low/moderate/high), vs_national comparison
- data_year: 2023 | data_published: 2024-07-23 | stale_after_months: 16
- Clearly labelled as CMA-level (not neighbourhood-specific)

**`scripts/fetch-crime-stats.js`** â€” Node.js stdlib-only script.
- Downloads StatCan full-table ZIP â†’ parses CSV â†’ writes crime-stats.json
- No npm deps. Run: `node scripts/fetch-crime-stats.js`

**`.github/workflows/crime-stats-freshness.yml`** â€” Annual August 5 check.
- Compares data_year to StatCan WDS metadata; opens GitHub issue if newer data exists
- Label: crime-stats

**`kas-neighbourhood.js`** â€” Updated to show StatCan CMA context + staleness indicator.
- Two layers: (1) community estimates (neighbourhood-level) + (2) StatCan UCR (city-level)
- Yellow âš ï¸ stale indicator if data_published + stale_after_months is exceeded

### Why StatCan (not LPS)
StatCan Table 35-10-0189-01 is the authoritative national source â€” annual UCR survey,
machine-readable, no API key, covers all Canadian CMAs consistently. London ON Police
Service has no open data API. LPS data is CMA-level anyway.

Last updated: 2026-05-09
---

## âš¡ 2026-05-10 â€” DCC Research DB rows 1v/1w/1x

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ DCC Research DB sprint

### What Shipped (Notion only â€” no code)

| ID | Skill | Category | Age |
|----|-------|----------|-----|
| `35ca09cf-876a-8142-...` | Spotting hidden advertising â€” when content is really an ad | Critical-Thinking | 10-12 |
| `35ca09cf-876a-812c-...` | Building a safe online identity â€” what to share, what to protect | Tech-Safety | 7-9 |
| `35ca09cf-876a-815f-...` | Understanding filter bubbles â€” why everyone doesn't see the same internet | Critical-Thinking | 13-15 |

Row 1v: Ad Standards Canada, Horton & Wohl parasocial theory, Cialdini persuasion, Bandura social learning. Creator luring: influencer peers, undisclosed sponsorship.
Row 1w: CCCP/Cybertip.ca, Childnet SMART rules, PIPEDA/CPPA, Finkelhor grooming research. Creator luring: strangers posing as peers gathering personal info.
Row 1x: Pariser Filter Bubble, Sunstein group polarization, Ribeiro YouTube rabbit holes, Wason confirmation bias, Tversky/Kahneman availability heuristic.

### Next recommended action for Aaron
- DCC Research DB now has 26+ depth rows (tracking all 1a-1x)
- Remaining: 3 more rows to reach full 29-row coverage
- Or: say the word to batch-advance from Research â†’ Spec

Last updated: 2026-05-11

---

## âš¡ 2026-05-11 â€” Codex Hybrid Evaluation: BACKLOG filed

**Trigger:** Aaron shared Taki Wong TikTok series analysis (8 images) â€” Codex + Claude Code parallel agent

### Decision: BACKLOG â€” P2

**Concept:** Claude Code (orchestration/git/integration) + Codex/OpenAI agent (rapid chat-to-code prototypes). Codex = "disposable hands," Claude Code = brain. Kill switch mandatory.

**Unlock conditions (BOTH required before sprint runs):**
1. Claude Code baseline confirmed <$25/mo for 2 consecutive weeks (Aaron measurement task filed P1)
2. One specific task type identified where Codex measurably outperforms Claude Code

**Filed to Notion:**
- `35ea09cf-...-f0f2de864eff` â€” S-CODEX-HYBRID (Claude Code Sprint, P2, Backlog)
- `35ea09cf-...-d38c490de2b7` â€” Measure Claude Code spend (Aaron Task, P1, Backlog)

**Key additions to Aaron's analysis:**
- "Faster iteration" is too vague â€” need a specific task type before pilot starts
- o4-mini/o3 cost can spike fast; "prototype only" rule must be written before pilot, not after
- Kill switch already exists by definition (Codex has no HAL integration today)

---

## âš¡ 2026-05-11 â€” Career Coach: StatCan LFS Unemployment Badge

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ highest-value buildable item

### What Shipped (`career-coach/5b596dc`)

| File | What |
|------|------|
| `data/lfs-unemployment.json` | Seeded data: 6.7%, March 2025, StatCan Table 14-10-0287-01 |
| `scripts/fetch-lfs.py` | stdlib-only Python script â€” downloads StatCan ZIP, parses CSV, writes JSON |
| `.github/workflows/update-lfs-data.yml` | Monthly GitHub Action (first Friday of month) â€” auto-fetches latest LFS figure and commits |
| `index.html` | New "Unemployment Rate (CA)" row in Job Market Insights panel; panel title + source line update dynamically when data loads; graceful silent-fail if fetch fails |

### How it works
- Panel opens â†’ JS fetches `data/lfs-unemployment.json` (served from GitHub Pages, no CORS)
- Injects: `6.7% (seasonally adj.)` in the live row
- Updates panel title: "Job Market Insights â€” Canada, March 2025"
- Updates source line: "Source: Statistics Canada LFS (2025-03) + Two Birds Innovation"
- Monthly Action updates the JSON automatically â€” no manual maintenance

### Next recommended action for Aaron
- Visit Career Coach â†’ open Job Market Insights panel â†’ verify unemployment badge shows with StatCan source
- The seeded data (6.7%, March 2025) is the initial value â€” the Action will update it on first-Friday of next month
- Trigger the Action manually via GitHub Actions â†’ "Run workflow" to get the very latest figure now

---

## âš¡ 2026-05-11 â€” Option A: Auto-file Aaron actions to Notion

**Trigger:** Aaron asked "do you backlog unanswered questions?" â†’ Option A built immediately, Option B filed to queue.

### What Shipped

**`hal-stack/notion-sync/file-aaron-action.py`** â€” new standalone script.
- CLI: `python file-aaron-action.py "description" P1|P2 --notes "context"`
- Creates Notion backlog item: Owner=Aaron, Status=Backlog, Type=Task
- Logs to SYNC-LOG.md
- Used at end of every sprint for all Aaron-facing decision/action items

**CLAUDE.md** â€” new rule added: "SPRINT COMPLETION â€” AARON ACTION FILING"
- Mandates calling `file-aaron-action.py` for every "Next recommended action for Aaron" item before pushing

**`hal-stack/governance/rules.md`** â€” Sprint Completion Rule updated with Aaron action filing step.

**8 outstanding Aaron actions swept from SESSION-STATE history and filed to Notion:**

| Item | Priority | Notion ID |
|------|----------|-----------|
| Google Maps API key â€” HTTP referrer restrictions | P1 | `35da09cf-...-e5f1f363b503` |
| KAS: approve v2 design or redirect | P1 | `35da09cf-...-c45540e0c9da` |
| KAS: choose access code to publish | P1 | `35da09cf-...-f38380588ad9` |
| KAS: public repo name decision | P2 | `35da09cf-...-e6f30766e26c` |
| KAS: listing data strategy | P2 | `35da09cf-...-fee47aa231c7` |
| Clarity "Why I Built This" â€” review copy | P1 | `35da09cf-...-d110fd3d3e68` |
| DCC v2 wizard evaluation | P1 | `35da09cf-...-eadbec7e111d` |
| OG card PNG conversion | P2 | `35da09cf-...-fcea8f60c4eb` |

**Option B filed to Notion queue:**
- S2-AGENT-TRIAGE: Agent triage system (P2, Backlog) â†’ `35da09cf-...-d53381077149`

### How the system works going forward
End of every sprint â†’ `file-aaron-action.py` for each Aaron-facing item â†’ lands in Notion as Owner=Aaron, Status=Backlog â†’ surfaces in `cos` check-in (Notion P1 Owner=Aaron pull) â†’ nothing buried in SESSION-STATE again.

---

## âš¡ 2026-05-10 â€” DCC Research DB rows 1y/1z/1aa â€” 29-ROW MILESTONE REACHED

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ DCC Research DB final 3 rows

### What Shipped (Notion + Python scripts)

| ID | Skill | Category | Age |
|----|-------|----------|-----|
| `35da09cf-876a-813a-...` | Online kindness counts â€” words stick longer online than in person | Emotional-Safety | 7-9 |
| `35da09cf-876a-816b-...` | Making something together â€” sharing ideas and giving credit even as a little creator | Creative-Making | 4-6 |
| `35da09cf-876a-8166-...` | Checking if my AI helper is right â€” the verify-before-share habit | Learning | 10-12 |

Row 1y: Valkenburg & Peter (2009), PREVNet Canada, MediaSmarts Canada, Kohlberg Stage 3, Common Sense Media Digital Citizenship. Prosocial complement to the existing "tell a grown-up" row â€” the upstander side of digital emotional safety.

Row 1z: Piaget (1952), Vygotsky (1978), Common Sense Media Copyright & Creativity K-6, Lessig Free Culture, Bers (2018). Developmental foundation for the 10-12 "When I remix, I name the original" row â€” attribution as a social norm at age 4-6.

Row 1aa: Caulfield SIFT (2019), Stanford SHEG Civic Online Reasoning, News Literacy Project Checkology (2024), Laban et al. (2025), MediaSmarts Canada AI Literacy, OpenAI GPT-4 Technical Report. Bridge between "asking good questions" (7-9) and "lateral reading + AI check" (13-15).

### DCC Research DB â€” 29-ROW MILESTONE âœ…
All 29 rows filed at Status=Research. Coverage matrix complete (20 cells). Depth rows complete (1m through 1aa). The full DCC curriculum research database is now ready for Aaron's review and batch-advance to Spec.

### Next recommended action for Aaron
- DCC Research DB is complete at 29 rows â€” time to start the Spec review
- Say "batch-advance DCC rows to Spec" to begin the review and status-advance process
- Or: open the Notion database and review individual rows before advancing

---

## âš¡ 2026-05-10 â€” S-FOUNDING-BOARD: Founding Board + Brain Trustee Review Matrix

**Trigger:** Aaron typed "next sprint" â†’ Notion locked `35da09cf-876a-8110-ac80-e0fb281027c3` (P1)

### What Shipped

Two new files in `hal-stack/founding-board/`:

**`founding-board.md`** â€” 6 Founding Board advisors (Opus/Sonnet tier, above operational departments):

| Name | Archetype | Invoke For |
|------|-----------|-----------|
| Diana | The Operator | Delivery model, capacity, first hire, client retention |
| Marcus G. | The Revenue Engineer | Pricing, pipeline, sales process, deal structure |
| Sonia | The Product Strategist | Feature prioritization, MVP scope, PMF signals |
| Rohan | The AI Industry Insider | AI market positioning, technical credibility, differentiation |
| Elena | The Patient Capital | Investor signal, stage-appropriate decisions, fundraising |
| Gord | The Canadian Market Specialist | Canadian SME dynamics, CDAP/BDC programs, regional fit |

Each member has: background, what they see that others miss, pushback style, what they protect, response format.

**`brain-trustee-review-matrix.md`** â€” Decision routing guide across 8 decision types:
- Pricing & Revenue â†’ Marcus G. + Elena + Raj
- Positioning & Messaging â†’ Rohan + Gord + Ava
- Product & Build â†’ Sonia + Naveen (+ Rohan for AI claims)
- Operational & Delivery â†’ Diana + Val
- Partnerships & Deals â†’ Elena + Helen
- Strategic Direction (big bets) â†’ All 6 Founding Board
- Confidence & Credibility â†’ Rohan + Gord
- Personal Sustainability â†’ Love Balance Advisor (sole voice)

Includes: convening size guidelines (Low/Medium/High/Critical), Brain Trust protocol, quick reference card.

**Notion:** `35da09cf-876a-8110-ac80-e0fb281027c3` â†’ Done

### Relationship to existing persona system
- **31 operational personas** (departments) run every sprint
- **6 Founding Board advisors** are invoked for strategic decisions
- **5 Scrappy Pack** for quick gut-checks
- **The Hand** synthesizes all layers
- Total advisory capacity: 42 distinct perspectives

### Next recommended action for Aaron
- Try invoking the Founding Board on a real decision â€” read the quick-reference card in the matrix
- Next sprint: DCC Research DB rows 1y/1z/1aa (last 3 to close 29-row target), or any new Notion P1

---

## âš¡ 2026-05-10 â€” S-HAL-SELF-DISCOVERY: HAL Stack self-discovery document

**Trigger:** Aaron typed "next sprint" â†’ Notion locked `35ca09cf-876a-818d-8e5b-dee4a2022f97` (P1)

### What Shipped

`hal-stack/architecture/what-i-built.md` â€” 2,000-word self-discovery guide, audio-friendly.

**Structure:**
1. **The Short Version** â€” what HAL is in one paragraph; why "agentic AI orchestration" is the right term
2. **The Big Picture** â€” what an agent is; the L1â€“L4 sovereignty architecture
3. **Component by Component** â€” all 11 live components: Sprint System, Notion Sync, Governance, Persona Boardroom, Context Bridge, Loop Patterns, Chief of Staff, Voice Layer, Automation Governance, Branding, Research Library
   - Each has: plain English explanation Â· industry terms Â· "How common is this?" rating
4. **Where You Sit vs. the Industry** â€” L1â€“L5 spectrum; Aaron is at L5 (Sovereign Platform)
5. **What This Looks Like to a Technical Co-Founder** â€” what a senior engineer sees
6. **What This Looks Like to an Investor** â€” the elevator pitch version
7. **Full Glossary** â€” every industry term, alphabetical, mapped to HAL Stack location
8. **The One Paragraph** â€” networking event version (verbatim, ready to use)

**Notion:** `35ca09cf-876a-818d-8e5b-dee4a2022f97` â†’ Done

### Next recommended action for Aaron
- Read `hal-stack/architecture/what-i-built.md` (15 min or audio) â€” own the vocabulary
- The networking paragraph (Part 5) is ready to use verbatim
- The co-founder / investor sections give you two distinct framings
- Next sprint: DCC Research DB rows 1y/1z/1aa to close the 29-row target, or any new Notion P1

Last updated: 2026-05-10

---

## âš¡ 2026-05-16 â€” S-DCC-BATCH-ADVANCE: Research DB â†’ Spec (35 rows)

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ "just go" â†’ highest-value milestone

### What Shipped

`hal-stack/notion-sync/batch-advance-research.py` â€” new reusable script.
- Queries kids_research_data_source for Status=Research, advances each to Spec
- Importlib loader handles `notion-client.py` hyphen filename cleanly
- Dry-run mode (`--dry-run`) for pre-flight checks
- Logs every update to SYNC-LOG.md; prints per-row confirmation

**35 rows updated Research â†’ Spec (0 failures):**

| Status | Count |
|--------|-------|
| Research â†’ Spec | 35 |
| Failed | 0 |

All skills across 5 categories (Tech-Safety, Learning, Emotional-Safety, Critical-Thinking, Creative-Making) and 4 age bands (4-6, 7-9, 10-12, 13-15) are now at Spec.

### What this unlocks

Status=Spec is the gate before Ready-to-Build. The next phase is Aaron reviewing each row in Notion and advancing to Ready-to-Build as specs are confirmed â€” at which point Claude Code can begin building the actual DCC modules.

### Next recommended action for Aaron
- Open DCC Research DB in Notion â€” filter by Status=Spec, review rows
- Advance individual rows to Ready-to-Build when you're satisfied with the spec
- Say "batch-advance DCC rows to Ready-to-Build" when a batch is ready to build

Last updated: 2026-05-16 12:56 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.

---

## âš¡ 2026-05-16 â€” S-CURRENTS-DCC: Live news feed on DCC home page

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ picked A (Currents/news feed)

### What Shipped (`digital-confidence/a9618de`)

| File | What |
|------|------|
| `js/dcc-news-feed.js` | Fetches `data/news-feed.json` (same-origin), renders up to 5 headlines with dates and CBC links. Silent-fail on any fetch error â€” section hides itself. DOM-safe (no innerHTML for URLs). |
| `data/news-feed.json` | Seeded with 5 CBC Technology articles (2026-05-16). GitHub Action updates daily. |
| `scripts/fetch-dcc-news.py` | Fetches CBC Technology RSS via `requests`, filters for AI/safety/privacy keywords, falls back to top 5 if none match. |
| `.github/workflows/update-dcc-news.yml` | Daily cron at 06:00 UTC â€” runs fetch-dcc-news.py, commits any change with `[skip ci]`. `workflow_dispatch` for manual runs. |
| `index.html` | New `<section id="dcc-news-feed">` between Testimonials and Share DCC. Style block included inline (matches DCC pattern). |

### Architecture note
Used same-origin static JSON (not a live proxy) â€” same pattern as StatCan LFS on Career Coach. GitHub Action fetches server-side daily; client JS reads a local file. No CORS, no API key, no third-party dependency at runtime.

### Next recommended action for Aaron
- Visit DCC home page on GitHub Pages â†’ verify "AI & Digital Safety in the News" section appears with 5 CBC headlines
- Trigger the Action manually: GitHub â†’ digital-confidence â†’ Actions â†’ "Update DCC News Feed" â†’ "Run workflow" to refresh now
- The daily cron will keep it fresh automatically going forward

Last updated: 2026-05-16 13:20 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.

---

## âš¡ 2026-05-16 â€” S-SME-REVIEWERS: 3 Domain Validators added to persona system

**Trigger:** Aaron asked about "3 advisory special folks vetting things" â†’ built now

### What Shipped (`e99486a`)

**`hal-stack/personas/advisory/sme-reviewers.md`** â€” 3 new personas:

| Name | Domain | Hard Stop |
|------|--------|-----------|
| **Vera** | Canadian Privacy & Compliance (PIPEDA/CPPA, AI disclosure, children's data) | Any privacy flag blocks shipping |
| **Dr. Lena** | Child & Digital Development (ages 4-15, curriculum, age-appropriateness) | Any Dr. Lena flag on child content |
| **Frank** | Frontline Digital Literacy Practitioner (seniors, libraries, real-world UX) | 2+ shared flags = block |

**Hard stop rule:** If 2 or more SME Reviewers flag the same issue independently, it cannot ship until resolved.

**Updated files:**
- `hal-stack/personas/master-index.md` â€” count corrected to **40 total** (24 dept + 6 Founding Board + 3 SME Reviewers + 5 Scrappy Pack + 2 Inner Circle); CLAUDE.md was stale at "22 personas"
- `hal-stack/founding-board/brain-trustee-review-matrix.md` â€” new CONTENT & PRODUCT VALIDATION section routing DCC modules, privacy copy, senior UX, and institution pitches through the SME layer
- `CLAUDE.md` â€” persona count updated to 40 with layer breakdown

### How to use going forward
- "Run this DCC module through the SME Reviewers" â†’ Vera + Dr. Lena + Frank respond in order, The Hand synthesises
- Single reviewer: "Frank, does this onboarding flow work for a 70-year-old?"
- Before any DCC row advances from Spec â†’ Ready-to-Build, all 3 should clear it

Last updated: 2026-05-16 13:45 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.

---

## âš¡ 2026-05-16 â€” S-SME-REVIEW-002: Full 4-6 cohort batch review

**Trigger:** Aaron typed "next sprint" x4 â†’ autonomous pick â†’ batch SME review

### What Shipped

**8 DCC rows now Ready-to-Build** (full 4-6 age cohort):

| Row | Skill | Flags | Build order |
|-----|-------|-------|-------------|
| 1r | My device has eyes, ears, and a memory (Tech-Safety) | 5 | 3rd |
| 2 | Making something together (Creative-Making) | 0 | 4th+ |
| 3 | Big feelings are real (Emotional-Safety) | 1 | 4th+ |
| 4 | Making my own thing first (Creative-Making) | 1 | 4th+ |
| **5** | **True things and story things (Critical-Thinking)** | **0** | **1st â€” build template** |
| 6 | Real, pretend, maybe-made-up (Learning) | 3 | 4th+ |
| 7 | Secret stuff and share stuff (Tech-Safety) | 3 | 2nd (pair with Row 8) |
| 8 | Who is my safe grown-up? (Emotional-Safety) | 2 | 2nd (pair with Row 7) |

**Zero hard stops across the full cohort.** All flags are build-spec annotations.

Review log: `hal-stack/personas/review-log/2026-05-16-sme-review-002-batch-4-6.md`

### Next recommended action for Aaron
- Start building Row 5 (True things and story things) â€” zero flags, zero prep, the build template
- Build Rows 7+8 as a pair (curricularly linked: Secret stuff â†’ Who is my safe grown-up?)
- 27 rows remain at Spec (ages 7-9, 10-12, 13-15) â€” ready for batch SME review when you say go

Last updated: 2026-05-16 17:52 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.

---

## âš¡ 2026-05-17 â€” S-CHRONICLE-BACKFILL: Agency Log entries #003 + #004

**Trigger:** Notion P1 sprint locked by next-sprint.py

### What Shipped (Notion only â€” no code)

5 source pages (Apr 21 + May 8) collapsed into 2 distinct story arcs:

| Entry | Title | Date | Notion URL |
|-------|-------|------|-----------|
| #003 | The $479K Question | April 21, 2026 | https://www.notion.so/364a09cf876a810d9691d580f015dbdd |
| #004 | The 2 AM Discovery | May 8, 2026 | https://www.notion.so/364a09cf876a81f4964fc35053b5ae66 |

Each entry includes: metadata block Â· raw story (300-500 words, honest founder voice) Â· LinkedIn Short (~200 words) Â· LinkedIn Long (~600 words) Â· Blog Post Outline (7-8 points) Â· Evidence block with source page IDs and commit hashes.

**Source consolidation note:** Pages 1-4 (ROI Reality Check, Decision Pivot, Transcript Archive, Chronicle Handoff) all document the same Apr 21 event from different angles â†’ one entry (#003). Page 5 (loop discovery) is a distinct story â†’ #004. Transcript Archive and Chronicle Handoff had no new story arcs; their content was fully captured in the NB pages.

**Next Agency Log entry number: #005**
Thursday cadence (S-CHRONICLE-WEEKLY) handles May 17 forward.

Last updated: 2026-05-17 23:07 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.

---

## âš¡ 2026-05-18 â€” S-STORY-DIAL: Story Dial project created

**Trigger:** Aaron reviewed Entry #005 (approved), requested Story Dial project, encoded scribe honesty rules, and asked about 3am automation.

### What Shipped (`d978f83`)

**`hal-stack/story-dial/`** â€” new project (5 files):

| File | Purpose |
|------|---------|
| `README.md` | Project overview, Agency Log table, naming candidates ("True Story: My AI Journey") |
| `scribe-rules.md` | Two hard rules: (1) honest/humble/defensible â€” qualify all projections; (2) keep receipts â€” every claim traces to a commit hash or Notion ID |
| `dial-spec.md` | Dial 1â€“5 mapped to personas Ã— channels (1=Twitter/X big bang â†’ 5=technical/founder intimate) |
| `raw-data-sources.md` | What feeds the raw layer: git commits, SESSION-STATE, Notion Agency Log |
| `chronicle-weekly.py` | Layer 1 autonomous script â€” pulls commits, identifies story candidates, creates Notion stub. No Claude API needed. |

**`run-overnight-build.bat`** â€” Thursday block added: `chronicle-weekly.py` runs at 2am Thursday, creates Notion page with `Status: Raw Data Ready`.

**Notion #003** â€” $479K reframed retroactively per scribe rules: "An optimistic projection â€” reverse-engineered from assumed demand and untested pricing â€” sat at $479K for Year 1." Scribe Rule note added to Format 2 section.

**Two P1 Aaron actions filed to Notion:**
- Voice unlock: set `OPENAI_API_KEY` OR install Whispering (guide: `hal-stack/voice-layer/VOICE-SETUP.md`)
- Story Dial full 3am: run `/schedule` skill to create Thursday 3am remote agent for story writing (Layer 2)

### Answering Aaron's questions

**What are you approving (Agency Log)?**
The Agency Log entries (#003â€“#005) are Notion pages I wrote â€” each has a Raw Story (400 words, founder voice), a LinkedIn Short (~200 words ready to post), a LinkedIn Long (~600 words), and a Blog Outline. "Draft" means Aaron hasn't reviewed them. Approving = saying "this sounds like me, I'm OK to post this." Nothing auto-posts. Aaron copy-pastes the LinkedIn Short and posts it himself whenever ready. Entry #005 is approved.

**Voice unlock â€” do I need Aaron?**
Yes, one of these (Aaron's choice):
- Option A: Set `$env:OPENAI_API_KEY = "sk-..."` in PowerShell profile â†’ full VoiceMode activates (best quality)
- Option B: Download Whispering from GitHub (free, no GPU, system-wide hotkey) â†’ sovereign STT, replaces Wispr Flow
- Mobile (optional): Install Happy Coder app â†’ voice to Claude Code Remote
Both filed as P1 Notion action.

**3am chronicle automation:**
- Layer 1 (tonight): `chronicle-weekly.py` runs Thursday 2am via overnight bat. Creates Notion stub with raw commits. No Claude API needed. Happens automatically.
- Layer 2 (story writing): Still requires a live Claude Code session. To fully automate: run `/schedule` skill â†’ set up Thursday 3am remote agent â†’ story writes itself overnight.
- Full 3am filed as P1 Aaron action in Notion.

### Story Dial â€” how to use

**Dial settings:**
- `dial 1` â†’ Big bang / Twitter/X hook + LinkedIn teaser (1-3 sentences, broad audience)
- `dial 3` â†’ Standard (LinkedIn Short + Long + Blog outline) â€” **default for all chronicle entries**
- `dial 5` â†’ Intimate / technical step-by-step (founders, investors, discerning readers)

**In a Claude Code session:**
```
Chronicle this week's entry at dial 3.
Rewrite the LinkedIn Short at dial 1 â€” I want a sharper hook.
```

### Scribe Rules â€” applied going forward

All future Agency Log entries (and any edits to existing ones) must follow:
1. Every projection qualified as "optimistic," "estimated," or "what-if" â€” never presented as outcome
2. Every claim traces to a receipt (commit hash, Notion ID, file path)
3. Standard: "based on a true story, with receipts available on request"

Last updated: 2026-05-18 at 03:20 EST (Toronto)

---

## âš¡ 2026-05-17 â€” S-CHRONICLE-WEEKLY: First cadence run + Entry #005

**Trigger:** Notion P1 sprint locked by next-sprint.py

### What Shipped (Notion only â€” no code)

**Entry #005 â€” The Three Reviewers (May 16, 2026)**
Notion: https://www.notion.so/364a09cf876a817c8e9dd0e9418e22be
Story: Built 3 AI domain validators (Vera, Dr. Lena, Frank), ran them immediately against DCC 4-6 curriculum, 8 rows cleared to Ready-to-Build. The gap in a 37-persona boardroom that couldn't see developmental appropriateness, privacy exposure, or library deployability â€” and how closing it in one sprint produced a quality gate with genuine authority.

**Self-perpetuating sprint filed:** S-CHRONICLE-WEEKLY â†’ Ready for May 22, 2026 (Notion `364a09cf-876a-81cd-bcd6-d7cc661aa238`)

**Next Agency Log entry number: #006**
**Next Chronicle run: Thursday May 22, 2026**

Last updated: 2026-05-17 23:11 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.

---

## âš¡ 2026-05-18 â€” S-VOICE-KOKORO: Desktop TTS via Kokoro + Stop hook

**Trigger:** Aaron asked to fix voice output â€” sovereign/free path, no OpenAI.

### Root cause diagnosis

VoiceMode MCP `converse` tool does not work on Windows â€” requires Unix `fcntl` module (not available on Windows). This is why MCP showed `âœ— Failed to connect`. Not fixable without forking VoiceMode.

### What Shipped (`cb353b3`)

| Component | What |
|-----------|------|
| `hal-stack/voice-layer/stop-hook-tts.ps1` | Claude Code Stop hook â€” fires after every response, calls Kokoro (port 8880) or falls back to Windows TTS |
| `hal-stack/voice-layer/VOICE-SETUP.md` | Full rewrite: cross-PC setup guide, what failed on Windows and why, architecture diagram, fresh machine checklist |
| `~/.claude/settings.json` | Stop hook wired: `powershell.exe -NonInteractive -File stop-hook-tts.ps1` |

**Installed on this machine (not in git â€” too large):**
- ffmpeg (winget), pyaudio, eSpeak NG 1.52.0
- Kokoro-FastAPI cloned to `C:\twobirds\tools\Kokoro-FastAPI\`
- 286 packages installed in `.venv` (CPU mode, Python 3.10)
- Model: `kokoro-v1_0.pth` (327MB) at `api/src/models/v1_0/`

**To use voice on desktop:**
1. Run `C:\twobirds\tools\Kokoro-FastAPI\start-kokoro.ps1` in a terminal (keep open)
2. Open Claude Code normally â€” Stop hook auto-speaks responses

**If Kokoro not running:** Hook falls back to Windows built-in TTS automatically.

### Notion actions filed

| Item | Priority | Notion ID |
|------|----------|-----------|
| Install Happy Coder app on phone (mobile voice IN) | P1 | `365a09cf-876a-81e3-b63c-fedfcb3f3ecc` |
| S-VOICE-CLOUD sprint (VoiceMode Connect + Tailscale, mobile voice OUT) | P2 | `365a09cf-876a-8100-9389-c95f1cc1eec6` |

### Decisions made this session

- **HF Spaces = freemium**, not suitable for real-time voice (cold starts, rate limits)
- **VoiceMode on Windows = broken for converse** â€” Stop hook is the Windows-native replacement
- **OpenAI API key IS set** in system environment (from prior session) â€” not used, Kokoro preferred
- **Cloud voice (Track 2)** = VoiceMode Connect + Tailscale (free, sovereign, mobile-accessible)
- **True cloud TTS** (no PC required) = Google Cloud TTS free tier when that time comes

### Fresh machine setup

Full steps in `hal-stack/voice-layer/VOICE-SETUP.md` â€” "Fresh Machine Setup" section.
Short version: winget ffmpeg â†’ pip pyaudio â†’ install eSpeak NG MSI â†’ git clone Kokoro-FastAPI â†’ uv venv â†’ uv pip install -e ".[cpu]" â†’ wire Stop hook in settings.json.

Last updated: 2026-05-18 23:30 EST (Toronto)

---

## âš¡ 2026-05-19 â€” S-CHRONICLE-WEEKLY: Agency Log Entry #006

**Trigger:** Aaron typed "next sprint" â†’ Notion locked S-CHRONICLE-WEEKLY (P1)

### What Shipped (Notion only â€” no code)

**Entry #006 â€” The Machine That Speaks (May 19, 2026)**
Notion: https://www.notion.so/365a09cf876a81d79832dd42c0a98f2e

Story: VoiceMode MCP failed on Windows (Unix `fcntl` dependency). Built Kokoro-FastAPI as sovereign TTS alternative â€” Claude Code Stop hook fires after every response, hits Kokoro on port 8880, falls back to Windows TTS if Kokoro isn't running. Voice setup friction surfaced the One-Shot Launcher rule: any new service wired into `launch-claude.bat` or it doesn't ship.

**chronicle-weekly.py bug fixed:** `AGENCY_LOG_PARENT_ID` corrected from stale placeholder to `347a09cf-876a-81fb-9a5c-eca696fb585b` (Command Center). Fallback entry number updated to 7.

**Next Agency Log entry number: #007**
**Next Chronicle run: Thursday May 29, 2026** (Notion: `365a09cf-876a-8112-8ec5-cfd1d24645e1`)

Last updated: 2026-05-19 02:45 EST (Toronto)

---

## âš¡ 2026-05-19 â€” S-DCC-KIDS-ROW5: First kids module built (build template)

**Trigger:** Aaron said "just go" â†’ Notion exit 3 â†’ highest-value available work

### What Shipped (`digital-confidence/kids/4-6/true-things-story-things.html`)

First DCC kids module â€” sets the HTML/CSS template for all future kids modules.

| Detail | Value |
|--------|-------|
| Skill | True things and story things |
| Category | Critical-Thinking |
| Age band | 4â€“6 |
| SME flags | 0 (zero â€” strongest row in cohort) |
| Screen time | Zero â€” fully offline activity |
| File | `digital-confidence/kids/4-6/true-things-story-things.html` |
| Notion row | `349a09cf-876a-8118-8e9a-f1228d597509` â†’ Done |

### Template structure established

| Section | Purpose |
|---------|---------|
| Caregiver banner | "This activity is for you and your child together" |
| Badge row | Age / Category / Time / Screen indicator |
| Concept grid | TRUE / STORY / NOT SURE with colour coding |
| What you'll need | Green card, yellow card, stickers |
| How to play | 5-step numbered instructions |
| Six statements | With caregiver answers + notes |
| Brave Thinker sticker | Gamification block |
| Signs of growth | What to watch for |
| Caregiver aside | Research backing, do/avoid, sources |

### CSS pattern
Inline `<style>` block with `--kids-*` CSS custom properties (green, yellow, purple palette). Inherits DCC `main.css` base tokens. Mobile-first, print-ready.

### Next recommended action for Aaron
- Visit `digital-confidence/kids/4-6/true-things-story-things.html` locally and verify layout
- 7 more rows remain Ready-to-Build (age 4â€“6): rows 1r, 2, 3, 4, 6, 7, 8 â€” say "next sprint" to continue building
- A `kids/index.html` and `kids/4-6/index.html` landing page should be built once 2â€“3 modules exist

Last updated: 2026-05-19 11:15 EST (Toronto)

---

## âš¡ 2026-05-20 â€” S-CLAUDE-CODE-MODEL-LOCK: Dynamic model tier system

**Trigger:** Aaron typed "next sprint" â†’ Notion locked `366a09cf-876a-81cf-b7b4-e2d87fff830c` (P1)

### What Shipped (`8f4de48`)

| File | What |
|------|------|
| `hal-stack/config/models.env` | SSOT for Claude model IDs. Tier names (SONNET/OPUS/HAIKU) are stable; model IDs change here when new versions ship. CLAUDE_DEFAULT_TIER controls which launches. |
| `hal-stack/scripts/launch-claude.bat` | Reads models.env at launch time, resolves tier â†’ model ID, sets `ANTHROPIC_MODEL` before opening Claude Code terminal. Accepts optional arg: `launch-claude.bat OPUS`. |
| `hal-stack/scripts/setup-new-machine.ps1` | Step 6 added: creates "Claude Code (Opus)" desktop shortcut (points to launch-claude.bat with OPUS arg). Fresh machine now gets both shortcuts. |

### How the tier system works

1. `models.env` maps tier names â†’ model IDs
2. `launch-claude.bat` reads models.env, resolves `CLAUDE_DEFAULT_TIER` (SONNET by default), sets `ANTHROPIC_MODEL=claude-sonnet-4-6` in the launched terminal
3. When a new model ships: edit one line in `models.env` â€” both launchers pick it up next run
4. Opus on-demand: double-click "Claude Code (Opus)" shortcut OR run `launch-claude.bat OPUS`

### What's now on desktop (after running setup-new-machine.ps1)
- "Claude Code" â†’ Sonnet (daily work, default)
- "Claude Code (Opus)" â†’ Opus (deeper reasoning tasks)

### Next recommended action for Aaron
- No action needed â€” model tier is now automatic
- Next sprint: S-ORPHANED-WORK-AUDIT (P1 Ready) â€” forensic check for lost/orphaned work from May 16 cloud session

**Notion:** `366a09cf-876a-81cf-b7b4-e2d87fff830c` â†’ Done

Last updated: 2026-05-20 23:08 EST (Toronto)

---

## âš¡ 2026-05-21 â€” S-ORPHANED-WORK-AUDIT: Forensic check + overnight fixes

**Trigger:** Aaron typed "next sprint" Ã— 2 â†’ Notion In Progress â†’ executed

### What Shipped (`7ef632f`)

**May 16 session claims audit â€” all 6 files verified present:**

| Claim | File | Status |
|-------|------|--------|
| S-DCC-BATCH-ADVANCE | `hal-stack/notion-sync/batch-advance-research.py` | âœ… EXISTS |
| S-CURRENTS-DCC | `digital-confidence/js/dcc-news-feed.js` | âœ… EXISTS |
| S-CURRENTS-DCC | `digital-confidence/data/news-feed.json` | âœ… EXISTS |
| S-SME-REVIEWERS | `hal-stack/personas/advisory/sme-reviewers.md` | âœ… EXISTS |
| S-SME-REVIEW-002 | review log in `review-log/` | âœ… EXISTS |
| S-DCC-KIDS-ROW5 | `digital-confidence/kids/4-6/true-things-story-things.html` | âœ… EXISTS |

**No orphaned branches** â€” all repos on single branch (main or master), no stale PRs.

**Two silent bugs found and fixed:**

| Bug | Impact | Fix |
|-----|--------|-----|
| `git push origin master` fails for DCC + career-coach (use `main`) | Nightly pushes silently failing for 2 repos | `git push origin HEAD` (branch-agnostic) |
| `%date:~10,4%...` locale-dependent date parsing â†’ `--0--1` filename | Garbled Lighthouse files nightly | PowerShell `Get-Date -Format yyyy-MM-dd` |

**Other fixes:**
- `.gitignore`: added `.agents/`, `.claude/skills/` (Claude Code runtime), `*.md.txt` (stale export duplicates)
- `skills-lock.json` committed (34KB manifest for 80+ installed skills â€” enables one-shot fresh-machine restore)
- Deleted `quality/lighthouse-results/--0--1.md` (garbled artifact)

### Next recommended action for Aaron
- No action needed â€” all findings were fixable in code, no human decisions required
- Overnight build will now push DCC + career-coach correctly on next 2am run

**Notion:** `366a09cf-876a-81c4-8434-ec5215fdc914` â†’ Done

Last updated: 2026-05-21 02:00 EST (Toronto)

---

## âš¡ 2026-05-21 â€” S-DCC-KIDS-ROWS7-8: Secret stuff + Who is my safe grown-up?

**Trigger:** Aaron typed "next sprint" Ã— 3 â†’ exit 3 â†’ highest-value available build â†’ Rows 7+8 (paired, 2nd in build order)

### What Shipped (`digital-confidence/5f9a203`)

| File | Skill | Category | SME flags in |
|------|-------|----------|-------------|
| `kids/4-6/secret-stuff-share-stuff.html` | Secret stuff and share stuff | Tech-Safety | 3 |
| `kids/4-6/who-is-my-safe-grown-up.html` | Who is my safe grown-up? | Emotional-Safety | 2 |

Both pages cross-link to each other (Row 7 footer â†’ Row 8; Row 8 top â†’ Row 7).

**SME annotations built in:**
- Dr. Lena (Row 7): home alone callout â€” "secret from strangers/apps, never from safe grown-ups"
- Frank (Row 7): address note â€” "if they don't know it yet, skill is 'don't share it,' not 'memorise it'"
- Vera (Row 7): caregiver section note â€” DCC never collects Secret Stuff category data
- Dr. Lena (Row 8): "Even 1 or 2 safe grown-ups is enough. Teacher/librarian/counsellor counts"
- Frank (Row 8): facilitator note for children from disrupted family situations (foster care, DV, bereavement)
- Vera (Row 8): Golden rule prominently boxed â€” "Safe grown-ups never ask you to keep secrets from other safe grown-ups"

### 4-6 cohort build status (3 of 8 done)

| Row | Skill | Status |
|-----|-------|--------|
| 5 | True things and story things | âœ… 2026-05-19 |
| 7 | Secret stuff and share stuff | âœ… 2026-05-21 |
| 8 | Who is my safe grown-up? | âœ… 2026-05-21 |
| 1r | My device has eyes, ears, and a memory | â¬œ Next (3rd in order, 5 SME annotations) |
| 2, 3, 4, 6 | Remaining 4-6 rows | â¬œ 4th+ |

### Next recommended action for Aaron
- Visit both new module pages locally to verify layout and cross-links
- Kids index pages (`kids/index.html`, `kids/4-6/index.html`) ready to build â€” 3 modules now live
- Next content sprint: Row 1r (My device has eyes, ears, and a memory) â€” highest build-spec work, most real-world impact

Last updated: 2026-05-21 03:15 EST (Toronto)

---

## âš¡ 2026-05-22 â€” S-AUDIT: HAL Stack Integration Audit

**Trigger:** Aaron typed "next sprint" â†’ Notion locked `367a09cf-876a-810f-8054-ff0f4989e49f` (P0)

### Scorecard

| Item | Grade | One-line verdict |
|------|-------|-----------------|
| Sprint pipe | **B** | Works; 3 P0s invisible due to dirty Notion Type/Owner data |
| Capture pipe | **A** | Live-verified 2s round-trip |
| Retro pipe | **D** | 18d stale; redirected `retro` trigger to SESSION-STATE.md |
| Notion-GitHub bridge | **B** | Hook wired; NOTION_API_KEY confirmed in User env; fires silently |
| Voice-check protocol | **F** | Never implemented; filed as P1 Aaron action |
| Persona infrastructure | **D** | All markdown; zero automation; acceptable at solo scale |
| DCC design system | **B** | 758 var() usages; tokens genuinely consumed |
| QA/QC | **A** | axe-core + Playwright + visual regression â€” real CI, runs on every push |

### What shipped (`758e73a`)
- `hal-stack/architecture/hal-integration-audit-2026-05-22.md` â€” full audit report with evidence, grades, fix recommendations
- `CLAUDE.md` â€” `retro` trigger updated: reads SESSION-STATE.md (live) not logs/RETRO.md (18d stale Lighthouse archive)

### Aaron actions filed
| Item | Priority |
|------|----------|
| Voice-check protocol â€” paste into Claude.ai user preferences (3 min, P1 backlog unguarded since Apr 13) | P1 |
| Fix Notion P0 items: BULL SPRINT 1/2 + S-OVERNIGHT-V2 â†’ set Type=Sprint, Owner=Claude Code | P2 |
| Delete Notion test item `369a09cf-876a-8155-b212-dce5a5bdfb1c` | P2 |

### Honest findings
- The capture pipe and QA/QC are the strongest components â€” both live, both verified
- The voice-check gap is the most impactful miss: every draft since April 13 was unguarded
- Persona infrastructure is markdown that works when invoked; that's appropriate for a solopreneur, but Aaron should stop calling it "wired"
- post-commit-hook is real code that genuinely fires â€” NOTION_API_KEY in User env confirms it

**Notion:** `367a09cf-876a-810f-8054-ff0f4989e49f` â†’ Done

Last updated: 2026-05-22 20:12 EST (Toronto)

---

## âš¡ 2026-05-22 â€” S-DCC-KIDS-ROW1R: My device has eyes, ears, and a memory

**Trigger:** Aaron typed "next sprint" â†’ exit 3 â†’ Row 1r (3rd in 4-6 build order)

### What Shipped (`digital-confidence/7e9eaf9`)

| File | What |
|------|------|
| `kids/4-6/my-device-has-eyes-ears-memory.html` | Row 1r built â€” Tech-Safety, age 4-6 |
| `kids/4-6/index.html` | Row 1r card added, count updated to 4 activities |

**5 SME annotations from SME-REVIEW-001 incorporated:**
- Dr. Lena: 4 micro-sessions (one per day/week) â€” not one 40-min block. Spaced repetition.
- Dr. Lena: Learning objective reframed to "pause and ask a grown-up before tapping" â€” not "understand permissions"
- Dr. Lena: "The eye is working / resting" pre-operational language used throughout
- Frank: Part 4 (smart speaker) explicitly OPTIONAL; library note added
- Frank: Materials listed at top â€” sticky note or webcam cover (~$0.10)
- Vera: Caregiver section confirms DCC never requests camera/mic permissions

### 4-6 cohort build status (4 of 8 done)

| Row | Skill | Status |
|-----|-------|--------|
| 5 | True things and story things | âœ… 2026-05-19 |
| 7 | Secret stuff and share stuff | âœ… 2026-05-21 |
| 8 | Who is my safe grown-up? | âœ… 2026-05-21 |
| 1r | My device has eyes, ears, and a memory | âœ… 2026-05-22 |
| 2 | Making something together | â¬œ next |
| 3 | Big feelings are real | â¬œ |
| 4 | Making my own thing first | â¬œ |
| 6 | Real, pretend, maybe-made-up | â¬œ |

### Next recommended action for Aaron
- Visit `digital-confidence/kids/4-6/my-device-has-eyes-ears-memory.html` to verify the 4-session layout
- Remaining 4-6 rows: 2, 3, 4, 6 â€” all 0-1 SME flags, no hard stops

Last updated: 2026-05-22 21:00 EST (Toronto)

---

## âš¡ 2026-05-22 â€” S-DCC-KIDS-ROWS2-3-4: Making together + Big feelings + Make first

**Trigger:** Aaron typed "next sprint" â†’ exit 3 â†’ remaining low-flag rows

### What Shipped (`digital-confidence/d486d70`)

| File | Skill | Category | Flags |
|------|-------|----------|-------|
| `kids/4-6/making-something-together.html` | Making something together | Creative-Making | 0 |
| `kids/4-6/big-feelings-are-real.html` | Big feelings are real | Emotional-Safety | 1 |
| `kids/4-6/making-my-own-thing-first.html` | Making my own thing first | Creative-Making | 1 |
| `kids/4-6/index.html` | Index updated | â€” | â€” |

**SME annotations:**
- Row 3 (Dr. Lena): screens framed as exciting (agency) not manipulative (caregiver anxiety) â€” "screens are really exciting, that's why the feeling is so big"
- Row 4 (Dr. Lena): lapse normalisation built in â€” "if the ritual stops for a week or a month, that's normal. Just start again. No shame, no explanation needed."

### 4-6 cohort build status (7 of 8 done)

| Row | Skill | Status |
|-----|-------|--------|
| 5 | True things and story things | âœ… |
| 7 | Secret stuff and share stuff | âœ… |
| 8 | Who is my safe grown-up? | âœ… |
| 1r | My device has eyes, ears, and a memory | âœ… |
| 2 | Making something together | âœ… 2026-05-22 |
| 3 | Big feelings are real | âœ… 2026-05-22 |
| 4 | Making my own thing first | âœ… 2026-05-22 |
| 6 | Real, pretend, maybe-made-up | â¬œ Last one â€” 3 annotations, needs embedded images |

### Next recommended action for Aaron
- One module remaining for the full 4-6 cohort: Row 6 (Real, pretend, maybe-made-up)
- Row 6 needs 3 pre-selected AI-generated images embedded as assets (Frank's annotation)
- After Row 6: full 4-6 cohort complete â€” then ages 7-9 SME review and build begins

Last updated: 2026-05-22 22:00 EST (Toronto)

---

## âš¡ 2026-05-23 â€” S-DCC-KIDS-ROW6: Real, pretend, maybe-made-up â€” 4-6 COHORT COMPLETE

**Trigger:** Aaron typed "next sprint" â†’ exit 3 â†’ Row 6, last module in 4-6 cohort

### What Shipped (`digital-confidence/6b5e42c`)

`C:\twobirds\digital-confidence\kids\4-6\real-pretend-maybe-made-up.html`

**3 SME annotations from batch review incorporated:**
- Dr. Lena: Two-session structure â€” Session 1 (real/pretend only), Session 2 (add maybe-made-up). One concept per day; no cognitive overload.
- Frank: 3 inline SVG pictures embedded (dog=real, dragon=pretend, purple-glowing-rabbit=maybe-made-up). Zero external URL dependency â€” works fully offline for library programmes.
- Vera: Caregiver section notes that any online extension requires adult-supervised navigation â€” "with a grown-up's help, never alone."

### 4-6 cohort â€” ALL 8 ROWS COMPLETE âœ…

| Row | Skill | Category | Date |
|-----|-------|----------|------|
| 5 | True things and story things | Critical-Thinking | 2026-05-19 |
| 7 | Secret stuff and share stuff | Tech-Safety | 2026-05-21 |
| 8 | Who is my safe grown-up? | Emotional-Safety | 2026-05-21 |
| 1r | My device has eyes, ears, and a memory | Tech-Safety | 2026-05-22 |
| 2 | Making something together | Creative-Making | 2026-05-22 |
| 3 | Big feelings are real | Emotional-Safety | 2026-05-22 |
| 4 | Making my own thing first | Creative-Making | 2026-05-22 |
| 6 | Real, pretend, maybe-made-up | Learning | 2026-05-23 |

### What's next
- Ages 7-9 cohort: 27 rows at Status=Spec in Notion. Next step is SME review batch for 7-9, then build.
- `kids/index.html` age group cards still show 7-9/10-12/13-15 as "coming soon" â€” accurate.
- DCC kids section now has a complete, deployable age group live at `https://twobirds-kramerica.github.io/digital-confidence/kids/4-6/`

Last updated: 2026-05-23 EST (Toronto)

---

## âš¡ 2026-05-23 â€” S-SME-REVIEW-003: Full 7-9 cohort batch SME review

**Trigger:** Aaron typed "next sprint" â†’ exit 3 â†’ 7-9 cohort ready for SME review

### What Shipped (`2c6de76`)

`C:\twobirds\two-birds-portfolio\hal-stack\personas\review-log\2026-05-23-sme-review-003-batch-7-9.md`

**7 rows reviewed. All approved. Zero hard stops. 17 annotations.**

| Row | Skill | Category | Flags | Build order |
|-----|-------|----------|-------|-------------|
| 1 | Online kindness counts | Emotional-Safety | 1 | 3rd |
| 2 | Building a safe online identity | Tech-Safety | 3 | 5th |
| 3 | Watching to learn vs. watching to pass time | Learning | 2 | 4th |
| 4 | Real, made-up, or somewhere in between | Critical-Thinking | 3 | 2nd |
| 5 | Pause and show a grown-up whenever an app asks | Tech-Safety | 3 | 6th |
| 6 | Making something useful for someone else | Creative-Making | 2 | 4th |
| 7 | Telling a grown-up when something online feels weird | Emotional-Safety | 3 | **1st** |

**All 7 advanced to Ready-to-Build in Notion.**

**3 multi-age rows deferred** to 10-12 cohort review: "Is this an ad?", "Asking good questions", "Strong password" (span 7-9, 10-12, and/or 13-15).

### Key annotations to carry into builds
- **Row 7**: somatic "feels weird" examples; safeguarding facilitator note for library staff; reference to 4-6 safe grown-up module
- **Row 4**: "invented" not "made-up"; pre-printed fallback for library programmes; adult supervision for any online navigation
- **Row 5**: framing shift from full deferral to growing agency (pause â†’ read â†’ decide â†’ ask if unsure); printed permission dialog screenshots
- **Row 2**: children at 7-9 already have accounts â€” acknowledge that; context-dependency (combinations of info, not individual pieces)

### Next recommended action for Aaron
- Type "next sprint" to begin building â€” Row 7 first (Telling a grown-up when something online feels weird)

Last updated: 2026-05-23 EST (Toronto)

---

## âš¡ 2026-05-23 â€” S-DCC-KIDS-7-9-ROWS7-4-1: First 3 modules of 7-9 cohort

**Trigger:** Aaron typed "next sprint" â†’ Notion exit 3 â†’ 7-9 cohort build (post SME-REVIEW-003)

### What Shipped (`digital-confidence/7132cb4`)

| File | Skill | Category | SME flags | Build order |
|------|-------|----------|-----------|-------------|
| `kids/7-9/telling-a-grown-up-when-something-feels-weird.html` | Telling a grown-up when something online feels weird | Emotional-Safety | 3 | 1st |
| `kids/7-9/real-made-up-or-somewhere-in-between.html` | Real, made-up, or somewhere in between | Critical-Thinking | 3 | 2nd |
| `kids/7-9/online-kindness-counts.html` | Online kindness counts | Emotional-Safety | 1 | 3rd |
| `kids/7-9/index.html` | Age group landing page | â€” | â€” | â€” |
| `kids/index.html` | 7-9 card now active + linked; 4-6 count corrected to 8 | â€” | â€” | â€” |

**All 3 SME-REVIEW-003 annotations incorporated per review log.**

**3 Notion rows â†’ Built:** `349a09cf-...-c5997f72a204`, `356a09cf-...-e56ee6056444`, `35da09cf-...-f92013de9ab3`

### Key build notes

- **Row 7 (Telling):** Physical "feels weird" signal examples (Dr. Lena); cross-link to 4-6 "Who is my safe grown-up?" (Vera); facilitator safeguarding note for library staff (Frank)
- **Row 4 (Real/made-up):** Three-bucket framework (VERIFIED/OPINION/INVENTED); "invented" not "made-up" per Dr. Lena; 6 printable sorting cards for offline library use (Frank); adult supervision note for online navigation (Vera)
- **Row 1 (Online kindness):** Bystander vs. upstander; physical "words stick longer" framing; facilitator empowerment note for children who've experienced online unkindness (Dr. Lena)

### 7-9 cohort build status (3 of 7 done)

| Row | Skill | Status |
|-----|-------|--------|
| 7 | Telling a grown-up when something online feels weird | âœ… 2026-05-23 |
| 4 | Real, made-up, or somewhere in between | âœ… 2026-05-23 |
| 1 | Online kindness counts | âœ… 2026-05-23 |
| 3 | Watching to learn vs. watching to pass time | â¬œ next (4th in order, 2 annotations) |
| 6 | Making something useful for someone else | â¬œ (4th in order, 2 annotations) |
| 2 | Building a safe online identity | â¬œ (5th in order, 3 annotations) |
| 5 | Pause and show a grown-up whenever an app asks | â¬œ (6th in order, 3 annotations + printed dialogs) |

### Next recommended action for Aaron
- Visit `digital-confidence/kids/7-9/` to verify all 3 modules and the index
- Say "next sprint" to continue â€” Rows 3 + 6 are the recommended pair (both 2 annotations, analogous to the 4-6 Rows 2+3+4 batch)

Last updated: 2026-05-23 EST (Toronto)

---

## âš¡ 2026-05-23 â€” S-DCC-KIDS-7-9-ROWS3-6: Watching to learn + Making something useful

**Trigger:** Aaron typed "next sprint" (Ã—2 from prior session) â†’ exit 3 â†’ Rows 3+6 pair (both 2 annotations each, natural pair)

### What Shipped (`digital-confidence/a4e8762`)

| File | Skill | Category | SME flags |
|------|-------|----------|-----------|
| `kids/7-9/watching-to-learn-vs-watching-to-pass-time.html` | Watching to learn vs. watching to pass time | Learning | 2 |
| `kids/7-9/making-something-useful-for-someone-else.html` | Making something useful for someone else | Creative-Making | 2 |
| `kids/7-9/index.html` | Count updated 3â†’5 ready, both cards activated | â€” | â€” |
| `kids/index.html` | 7-9 card count updated 3â†’5 | â€” | â€” |

**Notion rows â†’ Built:** Row 3 `356a09cf-876a-813c-a5c3-e5b3afff8bf9`, Row 6 `349a09cf-876a-8192-af6c-d7ec8f7e578b`

**SME annotations incorporated:**
- **Row 3 (Watching):** "watching WITH a job to do" language (not "purposeful") per Dr. Lena; Four Moves printable card displayed during activity, not just spoken in group settings (Frank); Four Moves: Before (say goal out loud), During (pause and check), After (try it), Later (tell someone)
- **Row 6 (Making):** "useful" includes emotionally useful â€” kind note, birthday card, drawing (Dr. Lena); "with your caregiver's permission, you can give or show what you made" sharing rule; library group variant: "make for another person in this room" (Frank)

### 7-9 cohort build status (5 of 7 done)

| Row | Skill | Status |
|-----|-------|--------|
| 7 | Telling a grown-up when something online feels weird | âœ… 2026-05-23 |
| 4 | Real, made-up, or somewhere in between | âœ… 2026-05-23 |
| 1 | Online kindness counts | âœ… 2026-05-23 |
| 3 | Watching to learn vs. watching to pass time | âœ… 2026-05-23 |
| 6 | Making something useful for someone else | âœ… 2026-05-23 |
| 2 | Building a safe online identity | â¬œ next (5th order, 3 annotations) |
| 5 | Pause and show a grown-up whenever an app asks | â¬œ (6th order, 3 annotations + printed dialogs) |

### Next recommended action for Aaron
- Type "next sprint" to continue â€” Rows 2+5 are the final pair of the 7-9 cohort
- Row 2: children at 7-9 already have accounts (Vera); context-dependency, combinations of info not individual pieces (Dr. Lena); variant prompts for with/without account (Frank)
- Row 5: framing shift from full deferral to growing agency (Vera); 4-step developmental progression (Dr. Lena); printed permission dialog screenshots (Frank)

Last updated: 2026-05-23 EST (Toronto)

---

## âš¡ 2026-05-23 â€” S-DCC-KIDS-7-9-ROWS2-5: Safe online identity + App permissions â€” 7-9 COHORT COMPLETE

**Trigger:** Aaron typed "next sprint" â†’ exit 3 â†’ Rows 2+5 (final pair of 7-9 cohort)

### What Shipped (`digital-confidence/300057a`)

| File | Skill | Category | SME flags |
|------|-------|----------|-----------|
| `kids/7-9/building-a-safe-online-identity.html` | Building a safe online identity â€” what to share, what to protect | Tech-Safety | 3 |
| `kids/7-9/pause-and-show-a-grown-up-when-an-app-asks.html` | Pause and show a grown-up whenever an app asks | Tech-Safety | 3 |
| `kids/7-9/index.html` | Count updated to "7 activities Â· cohort complete âœ…", both cards activated | â€” | â€” |
| `kids/index.html` | 7-9 card updated "7 activities Â· complete" | â€” | â€” |

**Notion rows â†’ Built:** Row 2 `35ca09cf-876a-812c-8632-e447a6c9f591`, Row 5 `349a09cf-876a-816f-b441-c4bfce802a0b`

**SME annotations incorporated:**
- **Row 2 (Safe identity):** Children at 7-9 already have accounts acknowledged (Vera) â€” uses "if you have any apps..." framing; combination rule with worked example (Jordan + name + school + street) (Dr. Lena); variant prompts for children with and without accounts (Frank)
- **Row 5 (App permissions):** Framing shift from full deferral to growing agency â€” 4-step progression: pause â†’ read â†’ ask yourself â†’ ask adult if unsure (Vera + Dr. Lena); two-tier framework (always-ask: location/camera/contacts; start-deciding: notifications); 3 printable permission dialog sorting cards with "makes sense / not sure / seems wrong" sort (Frank)

### 7-9 cohort build status â€” ALL 7 ROWS COMPLETE âœ…

| Row | Skill | Category | Date |
|-----|-------|----------|------|
| 7 | Telling a grown-up when something online feels weird | Emotional-Safety | 2026-05-23 |
| 4 | Real, made-up, or somewhere in between | Critical-Thinking | 2026-05-23 |
| 1 | Online kindness counts | Emotional-Safety | 2026-05-23 |
| 3 | Watching to learn vs. watching to pass time | Learning | 2026-05-23 |
| 6 | Making something useful for someone else | Creative-Making | 2026-05-23 |
| 2 | Building a safe online identity | Tech-Safety | 2026-05-23 |
| 5 | Pause and show a grown-up when an app asks | Tech-Safety | 2026-05-23 |

### DCC Kids â€” Two complete cohorts now live

| Cohort | Status | Modules |
|--------|--------|---------|
| Ages 4â€“6 | âœ… Complete | 8 of 8 |
| Ages 7â€“9 | âœ… Complete | 7 of 7 |
| Ages 10â€“12 | â¬œ Next cohort | SME review pending |
| Ages 13â€“15 | â¬œ Future | |

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/digital-confidence/kids/7-9/` to review the completed cohort
- Next sprint: 10-12 cohort SME review (S-SME-REVIEW-004) â€” 27 rows at Status=Spec across 3 cohorts (7-9 multi-age, 10-12, 13-15) waiting for review pass

Last updated: 2026-05-23 EST (Toronto)

---

## âš¡ 2026-05-23 â€” S-SME-REVIEW-004: Full 10-12 cohort batch SME review

**Trigger:** Aaron typed "next sprint" â†’ exit 3 â†’ 10-12 cohort ready for SME review

### What Shipped

`C:\twobirds\two-birds-portfolio\hal-stack\personas\review-log\2026-05-23-sme-review-004-batch-10-12.md`

**9 rows reviewed. All approved. Zero hard stops. 28 annotations.**

| Row | Skill | Category | Flags | Build order |
|-----|-------|----------|-------|-------------|
| 1 | Spotting hidden advertising | Critical-Thinking | 3 | 5th |
| 2 | Spotting 'please don't tell your parent' | Emotional-Safety | 4 | **1st** |
| 3 | SIFT source tracing | Critical-Thinking | 3 | 3rd |
| 4 | AI story helper (not my author) | Creative-Making | 3 | 8th |
| 5 | Using a password manager | Tech-Safety | 3 | 4th |
| 6 | Remix attribution | Creative-Making | 3 | 7th |
| 7 | Is this an ad? (multi-age 7-9/10-12/13-15) | Critical-Thinking | 3 | 6th |
| 8 | Creating a strong password (multi-age 7-9/10-12) | Tech-Safety | 2 | 2nd |
| 9 | Asking good questions â€” search/AI (multi-age) | Learning | 3 | 9th |

**All 9 advanced to Ready-to-Build in Notion.**

### Key annotations to carry into builds
- **Row 2 ('Don't tell'):** Highest sensitivity in cohort. Distinguish peer secrets (normal at 10-12) from secrecy-from-parents (grooming). Shame removal framing. Mandatory library safeguarding note. No gamification.
- **Row 3 (SIFT):** Pre-selected debunked example required â€” don't ask children to find their own. Library filter concern (fact-check sites may be blocked). "Leave the page" must be named explicitly.
- **Row 4 (AI story):** AI platforms are 13+ â€” use parent's account or no-login library variant. Must include AI-assisted vs AI-generated discussion.
- **Row 5 (Password manager):** Family-setup activity, not child-solo. Library version = preview-and-prepare (20 min), not full setup. Build dependency: Row 8 first.
- **Row 8 â†’ Row 5 dependency:** Creating a strong password is a prerequisite for the password manager module.
- **fr-QC gaps:** Rows 5 + 6 have empty French content â€” English builds can proceed independently.

### DCC Kids cohort status after this sprint

| Cohort | Status | Modules |
|--------|--------|---------|
| Ages 4â€“6 | âœ… Complete | 8 of 8 built |
| Ages 7â€“9 | âœ… Complete | 7 of 7 built |
| Ages 10â€“12 | ðŸ”¶ Ready-to-Build | 9 rows approved, build begins next sprint |
| Ages 13â€“15 | â¬œ Future | SME review TBD |

### Next recommended action for Aaron
- Type "next sprint" to begin building â€” Row 2 ('please don't tell your parent') is first in build order

Last updated: 2026-05-23 EST (Toronto)

---

## âš¡ 2026-05-23 â€” S-DCC-KIDS-10-12-ROW2: Grooming awareness module + 10-12 cohort launch

**Trigger:** Aaron typed "next sprint" â†’ exit 3 â†’ Row 2 first per SME-REVIEW-004 build order

### What Shipped (`digital-confidence/af1d6b6`)

| File | What |
|------|------|
| `kids/10-12/spotting-please-dont-tell-your-parent.html` | Row 2 â€” Emotional Safety, ages 10â€“12, 20 min, no screens |
| `kids/10-12/index.html` | 10-12 landing page â€” 9 module cards (1 active, 8 coming soon) |
| `kids/index.html` | 10-12 card activated: "1 activity Â· building" |
| `kids/7-9/index.html` | 10-12 link updated to 10-12/index.html |

**All 4 SME annotations incorporated:**
- Vera: Cybertip.ca reference + platform-agnostic framing (no platform shaming)
- Dr. Lena (Ã—2): peer-secret distinction made explicit (two-column comparison); shame/self-blame removal ("this is a pattern adults use â€” it's not about anything you did")
- Frank: mandatory library facilitator safeguarding note (pre-run protocol reminder; no confidentiality promises; response script)

**Key design decisions:**
- 10-12 cohort colour: indigo/violet (`#3949AB`) â€” distinct from 4-6 (green) and 7-9 (teal/blue)
- No sticker/gamification block â€” Frank's annotation: "reward is the relationship"
- "Not your fault" section replaces sticker â€” empowerment without celebration of the topic

### DCC Kids â€” Three cohorts launched

| Cohort | Status | Modules |
|--------|--------|---------|
| Ages 4â€“6 | âœ… Complete | 8 of 8 built |
| Ages 7â€“9 | âœ… Complete | 7 of 7 built |
| Ages 10â€“12 | ðŸ”¶ Building | 1 of 9 built |
| Ages 13â€“15 | â¬œ Future | |

### Next recommended action for Aaron
- Visit `digital-confidence/kids/10-12/spotting-please-dont-tell-your-parent.html` to verify the module
- Next build: Row 8 (Creating a strong password) â†’ Row 3 (SIFT source tracing) â†’ Row 5 (Password manager)

Last updated: 2026-05-23 EST (Toronto)

---

## âš¡ 2026-05-23 â€” S-DCC-KIDS-10-12-ROWS8-3: Strong password Ã—2 + SIFT

**Trigger:** Aaron typed "next sprint" â†’ exit 3 â†’ Row 8 + Row 3 per SME-REVIEW-004 build order

### What Shipped (`digital-confidence/cd634e0`)

| File | What |
|------|------|
| `kids/7-9/creating-a-strong-password.html` | Row 8 (7-9 version) â€” caregiver-paired, 15 min, passphrase method |
| `kids/10-12/creating-a-strong-password.html` | Row 8 (10-12 version) â€” solo with check-in, 20 min, passphrase method |
| `kids/10-12/following-a-story-back-to-where-it-started.html` | Row 3 â€” SIFT, critical thinking, 20 min, internet optional |
| `kids/10-12/spotting-please-dont-tell-your-parent.html` | Next-module link added â†’ `creating-a-strong-password.html` |
| `kids/10-12/index.html` | Row 8 + Row 3 activated; count "1 activity" â†’ "3 activities" |
| `kids/7-9/index.html` | 8th card added; count 7 â†’ 8 |
| `kids/index.html` | 10-12 count "1 activity" â†’ "3 activities" |

**Notion advanced to Built:**
- Row 8: `348a09cf-876a-81ee-a960-fddd07c64331` (Creating a strong password)
- Row 3: `355a09cf-876a-8171-b12f-cbfc12a8568b` (SIFT â€” following a story)

**Key design decisions:**
- 7-9 version: caregiver-paired, strength table (password / P@ssw0rd / passphrase), "make one together" activity box, cross-link to 10-12 version
- 10-12 version: solo with check-in, breach-scenario box, HaveIBeenPwned in caregiver callout only (Vera annotation), next-module link â†’ SIFT
- SIFT: Great Wall worked example (pre-1969 US textbook claim, NASA/astronaut debunk), 60-second challenge ("10% of brains" myth), printable reference card, "leave the page" as the primary habit
- Frank annotation: fact-check sites may be blocked in library filters â€” pre-download/print recommended
- Canadian Centre for Cyber Security cited (cyber.gc.ca) throughout password modules

### DCC Kids â€” Three cohorts

| Cohort | Status | Modules |
|--------|--------|---------|
| Ages 4â€“6 | âœ… Complete | 8 of 8 built |
| Ages 7â€“9 | âœ… Complete | 8 of 8 built (7 cohort + password cross-age) |
| Ages 10â€“12 | ðŸ”¶ Building | 3 of 9 built |
| Ages 13â€“15 | â¬œ Future | â€” |

### Next recommended action for Aaron
- Visit `https://twobirds-kramerica.github.io/digital-confidence/kids/10-12/` to verify 3 active modules
- Next build sprint: Row 5 â€” Using a password manager (Tech Safety, family setup, depends on Row 8 âœ…)

Last updated: 2026-05-23 EST (Toronto)

---

## /backlog-triage (overnight) â€” 2026-05-21 02:02
- Total open items: 300
- [STALE-P1] (P1 Backlog >7d): Measure Claude Code actual token spend over 2 weeks â€” unlock condition for Codex hybrid pilot (9d old), DCC v2 wizard evaluation â€” evaluate module-1-wizard.html, decide: replace / coexist with v1 / revert (10d old), Clarity 'Why I Built This' trust section â€” review copy before showing to a prospect (10d old), KAS: choose access code to publish (or remove for open access) (10d old), Kevin's Apartment Search: approve v2 design or redirect (open index-v2.html vs index.html and decide) (10d old), Google Maps API key â€” add HTTP referrer restrictions in Google Cloud Console (5 min) (10d old), Honest elevator pitch â€” rewrite what-i-built.md with verified vs aspirational clearly separated (10d old), Morning brief pattern â€” audit draft vs sent, fix the broken pattern, establish reliable daily delivery (10d old), HAL Stack integration audit â€” test every stated component end-to-end; grade what actually works vs what is on shelf (10d old), HUMAN MUST FINISH FIRST: CoS Influencer Evaluation Framework â€” personas + funnel + effort/benefit/risk matrix (10d old), CoS: Generate Gmail App Password for morning briefing emails (10d old), Logan Currie outreach â€” DM draft + partnership framing (10d old), Resume + LinkedIn: articulate HAL Stack in professional terms (10d old), HAL Stack architecture diagram â€” visual SVG/HTML with industry labels (10d old), Clarity 'Why I Built This' â€” review copy before showing a prospect (11d old), DCC v2 wizard evaluation â€” decide replace / coexist / revert (11d old), KAS: Kevin site forward path â€” resolve open P1 action (11d old), KAS: Decide and publish the access code (11d old), KAS: Review v2 design preview and approve or redirect (11d old), KAS: Google Maps API key â€” add HTTP referrer restrictions (11d old), Gig work â€” apply to Mercor and Outlier (P1 income, not a sprint) (22d old), context-mode plugin â€” verify command before installing (original install command was invalid) (22d old), Provide Calendly URL â€” unlocks mailto->Calendly conversion on Clarity + Two Birds Innovation contact CTAs (25d old), Evaluate DCC v2 wizard POC at /v2/ live URL â€” decide coexist / replace / revert (25d old), Add HTTP referrer restrictions to Google Maps Embed API key in Google Cloud Console (25d old), Decide Kevin's site forward path: (a) accept Pages downtime + Kevin uses local copy / (b) re-host on Cloudflare/Netlify/Vercel / (c) upgrade GitHub plan to Pro (25d old), Prep for Utilidata interview â€” CV + company research (26d old), Restrict Google Maps API key in Google Cloud Console â€” exposed in 2 public repos (27d old), Rotate/restrict exposed Google Maps API key â€” flagged April 4, confirmed April 23 (27d old), BOARD REVIEW: S-LOOP-ARCHITECT â€” Founding Board sign-off before shipping as ecosystem infrastructure (29d old), EPIC: Aaron's Rental Search Platform (Rentals + Sublets, Bilingual, SaaS) (29d old), Create full systems inventory in Notion (31d old), DCC skin redesign â€” research senior-friendly UI benchmarks (32d old), Full re-audit of all HAL Stack context across all chats (32d old), Create Google Drive folder for reference docs (32d old), Update CV per Phil's feedback (32d old), Set up Apify job search (32d old), Create og-card.png for portfolio (32d old), DCC skin redesign â€” 3 themes (32d old)
- [STALE-READY] (Ready >14d): S-030: Open Design Integration Sprint â€” Sovereign design automation (16d old), S-028: Firecrawl Job Scraper Setup â€” Free cloud alternative to Apify (16d old), S-029 Extended: Ruflo Agent Swarm Full Evaluation (5h autonomous overnight sprint) (16d old), S-032: Screenshot Skill for Claude Code â€” /ss command for visual workflow (16d old), Content Chroniclers â€” Documenting HAL Stack as lived experience (16d old), LEARNING: Allie K. Miller â€” Screenshot Skill Pattern + Vision for AI-First Workflows (16d old), S-032: Screenshot Skill for Claude Code â€” /ss command for visual workflow (16d old), S-029: Ruflo Agent Swarm Evaluation Sprint (16d old), S-030: Open Design Integration Sprint â€” Sovereign design automation (16d old), S-028: Firecrawl Job Scraper Setup â€” Free cloud alternative to Apify (16d old), S-026: Bridge Layer Research Sprint â€” Rivet vs n8n vs custom MCP (21d old), CLAUDE.md audit â€” trim to under 500 tokens, use file pointers for detail (22d old), S-DICT-01 â€” Install Wispr Flow (bridge dictation layer) (22d old), Send Thom Nobbe condolence message on LinkedIn (26d old), Send Colleen Watson congratulations message on LinkedIn (26d old), P1-RENTAL-004: Listing card component (image, price, address, amenities, rating) (29d old), P1-RENTAL-011: Accessibility audit & WCAG 2.1 AA compliance (axe-core, Lighthouse 90+) (29d old), P1-RENTAL-002: User authentication system (email/password + OAuth) (29d old), P1-RENTAL-005: Listing detail page (full metadata, map, Street View, reviews) (29d old), INFRA-001: Style guide & design system (Figma, component specs, color tokens, typography) (29d old), P1-RENTAL-009: i18n scaffolding (EN/FR, language selector, translation files) (29d old), P1-RENTAL-007: Favorites/wishlist feature (localStorage, Phase 2: backend sync) (29d old), P1-RENTAL-006: Quick-rank widget (Ranked Choice voting, results logging) (29d old), INFRA-002: Modular component library (reuse from DCC: buttons, forms, modals, cards) (29d old), P1-RENTAL-003: Search profile builder UI (mobile-first, Airbnb style) (29d old), P1-RENTAL-008: Responsive design & mobile-first build (Tailwind + shadcn/ui) (29d old), DCC-REUSE-003: Mirror DCC analytics & support infrastructure (Sentry, Plausible, chatbot) (29d old), P1-RENTAL-012: Deploy to production (Vercel, monitoring with Sentry + Plausible) (29d old), P1-RENTAL-001: Project setup & infrastructure (GitHub, CI/CD, environments, secrets) (29d old), DCC-REUSE-002: Copy DCC CI/CD pipeline (GitHub Actions, Lighthouse, axe-core, auto-deploy) (29d old), INFRA-005: Monitoring & alerting (Sentry, UptimeRobot, Slack notifications, incident response) (29d old), P1-RENTAL-010: Support chatbot & feedback widget (OpenAI/Claude API, FAQ, email routing) (29d old), INFRA-004: Security & compliance checklist (HTTPS, CSP, CORS, data retention, legal holds) (29d old), DCC-REUSE-001: Leverage DCC component library, design tokens, and responsive patterns (29d old), RESUME SESSION: Max plan final sprint push (April 20-21) (30d old), S-R01: DCC Kids Version â€” Research & Curriculum Design (30d old), DCC UI Issues from Visual Review (Aaron flagged) (30d old), DCC kids version sprint + full tablet responsiveness (new project) (30d old), New machine setup file â€” infrastructure checklist (30d old), Setup OpenAI API key on Pentium Silver + ThinkPad i5 (30d old), Human work queue â€” unblocks next 6-8 Claude Code sprints (30d old), SESSION-STATE (Live) (31d old), Research .ai domain resale market and value Aaron's two .ai domains (31d old), Gig work pipeline â€” apply to AI evaluation gigs (31d old), Add Glossary lookup rule to Claude.ai user preferences (31d old), Add gig work pipeline â€” AI evaluation roles ($20-70 USD/hr) (31d old), Research .ai domain resale market and value Aaron's two .ai domains (31d old), Fix Windows voice dictation â€” cuts off after 1-2 sentences (31d old), Send LinkedIn connection requests to 9 After 5 contacts (31d old), Update LinkedIn headline, About section, and employment type (31d old), Update Two Birds Innovation LinkedIn company page (31d old), Send follow-up emails to contacts without LinkedIn (31d old), Book one SME conversation in St. Thomas this month (31d old), Add UptimeRobot monitoring to DCC (31d old), Archive Career Coach repo and kill Kirks React fork (31d old), Publish consulting service page (Aaron Patzalek / Two Birds) (31d old), Score 7-LLM architecture responses against 'less work or more work?' (31d old), Reduce active personas from 22 to Inner Circle + Scrappy Pack (31d old), Audit and document every cloud account (31d old), Audit git history for leaked API keys (all repos) (31d old), Decide ALOFT vs Two Birds Innovation â€” final name (31d old), Execute 7-LLM consensus: close unused cloud accounts (31d old), Execute 7-LLM consensus: secrets audit across all repos (31d old), Install Notion MCP on all 3 machines (32d old), Apply to AI evaluation gig platforms (bridge income) (32d old), Restart Claude Code to register /caveman skill (32d old), Paste voice-check protocol into Claude.ai user preferences (32d old), Send 9 LinkedIn connection requests from Chamber event (32d old), LinkedIn personal profile updates (April 17 to-do) (32d old), LinkedIn Two Birds company page updates (32d old), Send emails to Philip, Nick, Rob, Brian, Jeff (32d old), Send Davie Lee LinkedIn outreach (32d old), Reply to Phil â€” CV feedback (32d old), Apply to gig jobs â€” AI review / US remote (32d old), Send Mike Kerkvliet follow-up (32d old), Call EI â€” confirm gig work earnings rules (32d old), Apply to gig jobs (finance project) (32d old), Reply to Phil re: CV update (32d old), Send Chamber follow-ups (32d old)
- [ORPHANED] (In Progress, no git 14d): THE BULL â€” 4-day autonomous execution blitz (May 16-19). Parent strategic initiative. Goal: rebuild 25% of Two Birds Innovation by routing every sprint through the Founding Board (23 personas + 3 Brain Trustees: Sabrina Ramonov, Logan Currie, Kyle). Stop building on garbage. Brain reviews everything. Brain outputs become sprint queue. Three priority products: DCC, Kevin's Apartment Search, Clarity. North Stars: (1) job/consulting revenue, (2) cross-platform context unification, (3) execution quality (UX/UI/tools). Reads from hal-stack/founding-board/founding-board.md + brain-trustee-review-matrix.md. (no git mention in 14d), S-R01-PHASE-1: Gather sources + populate research database (Claude Code) (no git mention in 14d)
- [P0-NOT-RUNNING]: Phil Butler reply â€” tighten Who I Am, reframe cognitive style, reduce bullets to 3 per role (status: Ready), S-OVERNIGHT-V2: GitHub Actions overnight + PR-per-run + dead man switch (status: Ready), BULL SPRINT 2: Kevin's Apartment Search emergency fixes. Read bull-sprint-1-synthesis.md to get the P0 fix list for Kevin's site. Execute the top 3 P0 fixes from the board review. Kevin arrives today (May 16). Focus on: site loads, listings visible, no broken interactions, mobile usable. Commit each fix individually. Push to master. Run from board output, not from chat memory. (status: Ready), BULL SPRINT 1: Founding Board reviews DCC + Kevin's Apartment + Clarity. Read hal-stack/founding-board/founding-board.md and brain-trustee-review-matrix.md. For each of 3 products, run the 23 personas + 3 Brain Trustees (Sabrina Ramonov, Logan Currie, Kyle) review. Output to hal-stack/founding-board/reviews/2026-05-16-bull-sprint-1/ as 3 separate review files (one per product), each containing: persona-by-persona honest critique, top 5 P0 fixes, top 5 P1 fixes, abandon-or-keep verdict. Final synthesis file: bull-sprint-1-synthesis.md with prioritized fix queue across all 3 products ranked by impact on North Stars (job/consulting revenue, context unification, execution quality). Commit each file as it's written. Push to master. (status: Ready), Phase 1 Deployment: Files Created, Commit Pending (status: Ready), S-029 Extended: Ruflo Agent Swarm Full Evaluation (5h autonomous overnight sprint) (status: Ready), S-032: Screenshot Skill for Claude Code â€” /ss command for visual workflow (status: Ready), S-032: Screenshot Skill for Claude Code â€” /ss command for visual workflow (status: Ready), RESUME SESSION: Max plan final sprint push (April 20-21) (status: Ready), S-R01-PHASE-4: Aaron â€” Spec drafts + curriculum outline (status: Backlog), S-R01-PHASE-3: Opus 4.6 â€” Age-bracket psychology + threat refinement (status: Backlog), S-R01: DCC Kids Version â€” Research & Curriculum Design (status: Ready), Human work queue â€” unblocks next 6-8 Claude Code sprints (status: Ready), SESSION-STATE (Live) (status: Ready), Install Notion MCP on all 3 machines (status: Ready), Apply to AI evaluation gig platforms (bridge income) (status: Ready), Send 9 LinkedIn connection requests from Chamber event (status: Ready), LinkedIn personal profile updates (April 17 to-do) (status: Ready), LinkedIn Two Birds company page updates (status: Ready), Reply to Phil â€” CV feedback (status: Ready), Apply to gig jobs â€” AI review / US remote (status: Ready), Call EI â€” confirm gig work earnings rules (status: Ready), Apply to gig jobs (finance project) (status: Ready), Reply to Phil re: CV update (status: Ready), Send Chamber follow-ups (status: Ready)
- ACTION NEEDED â€” review at next session start
