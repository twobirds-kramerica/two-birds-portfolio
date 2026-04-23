<!--
  DCC Product Wiki — produced by S-ARCHAEOLOGY-001 (2026-04-22 ~23:40 EST)
  Status: PARTIAL. Full spec called for 3-4h with a fresh session; was
  executed under ~30min time pressure at end of 6h+ max-mode window.
  Phase 3 (Notion scan of 10 pages) and Phase 5 (Notion page creation)
  were deferred — flagged in §Open Questions + Phase notes below.

  Evidence sources used:
    - 82MB Claude chat export at C:\Users\getkr\Downloads\...\conversations.json
      (150 total conversations; 24 identified as DCC-specific via narrowed
      keyword filter: "digital confidence" / "DCC" / "warm hearth" /
      "brenda" / "two birds" / "hal stack" / "sovereignty" / "module 1-3"
      in title OR "digital confidence" / "warm hearth" / "brenda" in summary)
    - Direct repo read of digital-confidence on master @ ef7e140 (live 2026-04-22)
    - Portfolio-side CLAUDE.md, SESSION-STATE.md, retro files, RELIABILITY-ISSUES.md

  Every claim below is either [CONFIRMED: source] or [UNKNOWN: why not confirmed].
  Aaron reviews UNKNOWN flags in §11; answers feed into the next wiki revision.
-->

# DCC Product Wiki — Complete Specification (Partial, Archaeology v0.1)

**Last updated:** 2026-04-22 ~23:40 EST (Toronto)
**Source:** Chat export archaeology (24/150 conversations) + repo read + portfolio CLAUDE.md + RETRO.md
**Status:** Living document — Aaron reviews and corrects UNKNOWN flags. Produced under time constraints; deeper chat-export read needed in a proper fresh-session run of S-ARCHAEOLOGY-001.

## 1. Product Vision

**North star:** Digital literacy for "silver tech" seniors who live with anxiety around technology (identity theft, banking scams, accidental charges). Move them from fear to an internal "Security Shield" mindset where they use devices confidently without dependence on family members. [CONFIRMED: founding chat 2026-02-16 "Digital literacy training manual for seniors", 511 messages, Aaron's opening framing]

**Original founding intent** (direct quote, chat 2026-02-16 Human msg 1):
> "You are a World-Class Instructional Designer specializing in 'Silver Tech' (Digital Literacy for Seniors). You are creating a 50-80 page Master Self-Driven Training Manual for a user named Brenda. The User Profile (Brenda): 70+ years old, lives in St. Thomas, Ontario. Psychology: High anxiety regarding technology ('The sky is falling' mindset). She is deeply afraid of identity theft, banking scams, and being 'tricked' into accidental charges. Hardware: iPad and iPhone. Goal: Move from fear to 'The Security Shield' mindset, eventually using her devices..."

**Evolution:** founding brief was a 50-80 page PDF manual. Aaron pivoted to a website same conversation: *"for the output — what do you think about creating a website in claude code? I would just need the data and prompt to do it, and maybe that would be better vs a document."* Deployed on GitHub Pages (same ecosystem as the prior Elite Karate site) rather than a separate domain. [CONFIRMED: 2026-02-16 chat Human msg 2]

## 2. Core Principles (Non-Negotiable)

| Principle | Source | Status |
|---|---|---|
| **Static HTML/CSS/JS only — no npm, no Node frameworks** | Portfolio CLAUDE.md STANDING RULES (line 14) | CONFIRMED |
| **Self-hosted fonts — no Google Fonts CDN** | `digital-confidence/css/fonts.css` header: *"sovereignty requirement, no Google CDN"* | CONFIRMED |
| **Canadian English throughout visible content** | CLAUDE.md STANDING RULES | CONFIRMED |
| **WCAG AAA contrast via tokens** | `digital-confidence/css/tokens.css` shadow + focus tokens meet 7:1 pair ratios | CONFIRMED via token math |
| **No external CDNs — sovereignty** | S-037 cross-repo preconnect sweep (2026-04-22); `hal-stack/architecture/decapitation-checklist.md` | CONFIRMED |
| **Commit after every phase** | CLAUDE.md STANDING RULES | CONFIRMED |
| **Bilingual EN/FR** | 12 FR modules under `digital-confidence/lang/fr/modules/` | CONFIRMED — partial (17/29 modules lack FR) |
| **Trust-first design** | 2026-02-16 chat ("move from fear to security shield mindset") | CONFIRMED intent; specific patterns UNKNOWN without deeper chat read |

## 3. Personas

### Brenda (primary, confirmed)
- **Age / location:** 70+, St. Thomas, Ontario
- **Psychology:** High anxiety re: technology. "Sky is falling" mindset.
- **Fears:** Identity theft. Banking scams. Being "tricked" into accidental charges.
- **Devices:** iPad + iPhone. **Not Samsung** — Aaron corrected this in Human msg 2: *"Im not sure where the samsung got mixed into the conversation. I (aaron) have the samsung phone, but brenda is only apple for phone and tablet."*
- **Goal:** Move from fear to "Security Shield" mindset; eventual independent device use.
- **Appearance in content:** Module 1 "The Escape Hatch" opens with "Margaret's Story" — a similar 74-year-old iPad user panicking at a fake virus warning. UNKNOWN whether Margaret = Brenda-renamed or a separate persona. [Source: `digital-confidence/module-1.html` lines 370-377]

### Additional personas
UNKNOWN: Kids version (referenced in `digital-confidence/components/warm-hearth/` + S-R01 Kids Research DB in HAL Stack) implies a separate "kids" persona set. Not extracted from chat export in this pass.

## 4. Device and Platform Support

| Device | Source | State |
|---|---|---|
| iPad (older + newer home-gesture models) | module-1.html steps 1-3 | CONFIRMED shipped |
| iPhone | module-1.html | CONFIRMED shipped |
| Android (older + newer gesture models) | module-1.html steps for Android | CONFIRMED shipped |
| Windows Desktop | module-1.html Windows key steps | CONFIRMED shipped |
| Mac | UNKNOWN (module-1 Windows-only in confirmed set; Mac may be in other modules) |
| Touch-first | WCAG AAA 44px floor / 56px DCC default per tokens.css | CONFIRMED |
| Screen-reader (NVDA / VoiceOver / TalkBack) | module-1 has `role="note"`, `aria-label`, alt text on images | CONFIRMED partial; comprehensive a11y verified via axe-core.yml CI |
| Keyboard-only | Explicit `:focus-visible` styling S-QD-FOCUS pattern; module-1 has `data-action`+ delegated listeners (S-KEVIN-CSP-READY pattern) | CONFIRMED |

## 5. Module Inventory (29 total)

**27 numbered main modules + 1 half-step (module-2-5) + 1 bonus (module-visual-ai).** Fixed in S-038 (2026-04-22, commit `37ba935`) — prior CLAUDE.md claim of "21 modules" was stale.

Full list captured authoritatively in `digital-confidence/v2/data/index.json` (shipped S-DCC-V2 Phase 3, commit on digital-confidence main):
- module-1: The Escape Hatch
- module-2: The Security Shield
- module-2-5: Everyday Digital Tasks (half-step)
- module-3: Passwords & Biometrics
- module-4: App Store Safety
- module-5: Email & Messages
- module-6: Banking & Transactions
- module-7: Photos & Memories
- module-8: Stay Connected
- module-9: Understanding AI
- module-10: Grocery & Food Delivery
- module-11: Ride-Sharing Apps
- module-12: Getting the Help You Deserve
- module-13: Understanding Social Media
- module-14: Smart Home Basics
- module-15: Telehealth & Medical Portals
- module-16: Staying Safe When You Travel
- module-17: Using AI for Research
- module-18: Staying Connected When It Matters Most
- module-19: Your Digital Life — Keeping It Safe and Organised
- module-20: Understanding Your Internet Plan
- module-21: Understanding Your Mobile Plan
- module-22: TV and Home Phone
- module-23: Buying and Selling Online Safely
- module-24: Staying in Touch — Communication Apps
- module-25: When Things Stop Working
- module-26: Managing Your Notifications
- module-27: Your Inbox — Managing Email and Spam
- module-visual-ai: Show Me! Using Your Camera to Learn Anything (bonus)

**FR parity:** 12/29 modules have `lang/fr/modules/` translations (1-12); 17 are EN-only. [CONFIRMED via `ls lang/fr/modules/`]

## 6. Feature Inventory

| Feature | State | Source |
|---|---|---|
| Long-scroll module pages | **Shipped** | All 29 module-*.html files |
| Wizard-UX variant (coexist with long-scroll) | **Shipped** 2026-04-22 via S-032 (single-URL POC) + S-DCC-V2 Phase 1-6 (full `/v2/` tree) | `module-1-wizard.html`, `v2/` directory |
| Read-aloud page button | **Shipped** 2026-04-21 S-030 | `digital-confidence/js/read-aloud.js`, commit `dd3c220` |
| Module progress dots | **Shipped** 2026-04-21 S-030 | `js/module-progress.js` |
| Check-in banner ("Still with us?") | **Shipped** 2026-04-21 S-030 | `js/check-in.js` |
| Keyboard shortcut helper (`?` dialog) | **Shipped** 2026-04-21 S-030 | `js/keyboard-helper.js` |
| Warm Hearth theme (default) | **Shipped** | `css/tokens.css` header: *"Voted winner (Option A, 65.5%). Kitchen-table warmth, trusted-neighbour tone, zero intimidation."* |
| Dark-theme + high-contrast toggles | **Shipped** (per tokens-dark.css + tokens-high-contrast.css) | CONFIRMED file existence; behaviour not fully traced |
| Font-size A-/A/A+ toggle | **Shipped** | `css/tokens.css` lines 165-167: `html.text-size-s/m/l` classes |
| Accessibility bar top-right | **Shipped** | module-1 lines 286-292 |
| Sidebar nav (all 29 modules) | **Shipped** | module-1 lines 302-361 |
| Print-centre / print-optimised output | **Shipped** | `print-centre.html` + `css/print.css` |
| Scam simulator | **Shipped** | `scam-simulator.html` |
| GA4 + Microsoft Clarity analytics (consent-gated) | **Shipped** | module-1 lines 120-140 + 161-169 |
| Consent UI + localStorage gating | **Shipped** | `js/analytics-consent.js` |
| Favicon + apple-touch-icon | **Shipped** 2026-04-11 (V07 heart-bulb logo) | `assets/logos/dcc/` |
| Certificate-of-completion (wizard v2) | **Shipped** 2026-04-22 S-DCC-V2 Phase 5 | `v2/js/certificate.js` |
| Kids version | **Planned — not shipped** | S-R01 Kids Research DB in HAL Stack; placeholder at `components/warm-hearth/dcc/` |
| Playwright visual regression CI | **Shipped partial** (styleguide excluded per 4 failed attempts) | `.github/workflows/` + RETRO 2026-04-21 S-DCC-VIS-STYLEGUIDE-STABLE |
| Axe-core a11y CI | **Shipped** every-push | `.github/workflows/axe-core.yml` |
| Weekly external-link-check | **Shipped** | `.github/workflows/broken-external-link-check.yml` |
| Content freshness badges + workflow | **Shipped** | `hal-stack/content-freshness/` + DCC badges |
| Offline fallback + PWA manifest | **Shipped** | `offline.html` + `manifest.json` |
| Newsletter + sharing | **Shipped** | per git log `c983fb9` |
| Feedback widget + GitHub-issue capture | **Shipped** | `js/feedback-github.js` + `js/feedback-widget.js` |

## 7. Design Decisions

### Colour palette — Warm Hearth (confirmed live default)
Primary Warm Hearth tokens in `digital-confidence/css/tokens.css`:
- `--color-bg: #FFF8F0` (warm cream)
- `--color-surface: #FFFFFF`
- `--color-primary: #2A7B6F` (warm teal)
- `--color-accent: #E8842C` (burnt orange)
- `--color-text: #3D3229` (warm charcoal)
- `--color-border: #E8DDD0`

**Vote result:** 65.5% for Option A (Warm Hearth) over alternatives. [CONFIRMED: `tokens.css` header comment]. **Decision date:** 2026-04-18 or 2026-04-19 per chat "Exploring DCC UI style options" (2026-04-18, 10 msgs). [CONFIRMED partial: date range; specific voting-body details UNKNOWN without deeper chat extraction.]

### Typography
- Body: **Merriweather** (SIL-OFL, serif, self-hosted at `fonts/merriweather/`)
- Heading: **Source Sans 3** (SIL-OFL, self-hosted at `fonts/source-sans-3/`)
- Base size: 18px (senior-friendly floor per tokens.css:70)
- Min allowed: 16px
- H1: clamp(28px, 2.4vw + 20px, 36px)

**Why Merriweather + Source Sans 3 vs Inter?** UNKNOWN from chat export in this pass — decision is referenced in `css/fonts.css` header but rationale would require reading the relevant chat conversation. Flag for deeper archaeology.

### Accessibility commitments
- WCAG AAA contrast (7:1) via token pairs — enforced by design, verified by axe-core CI
- 44px minimum tap target (`--tap-target-min`); 56px DCC senior default (`--tap-target`)
- `:focus-visible` styling applied via S-QD-FOCUS pattern across products
- Native `<dialog>` for modals (Escape + focus-trap free)
- Reduced motion honoured via `@media (prefers-reduced-motion: reduce)`

### UX pattern state (current)
- **Default:** long-scroll rich module pages (27 numbered + 2 supplementary)
- **Evaluation-in-flight 2026-04-22:** two coexisting wizard variants
  - S-032 parallel URL: `module-1-wizard.html` at root
  - S-DCC-V2 full tree: `/v2/` subdirectory with own menu + shell + 5 screens for module-1
- **Decision pending:** Aaron evaluates POC; then coexist-permanently / replace-with-wizard / revert.

## 8. Content and Messaging Principles

- **Zero jargon, no acronyms in user-facing content** — CONFIRMED via module-1 voice (plain language in step-by-step instructions; jargon explained inline when unavoidable)
- **Voice-check protocol** — banned words + em dashes scanned; external content tagged with compliance marker. [CONFIRMED: `hal-stack/sprint-system/backlog/P2-voice-check-protocol.md`; portfolio README.md fixed 18 em dashes in S-039]
- **Reassurance patterns** — "You are in a safe place. Nothing on this page can harm your device. You cannot break anything by reading." [CONFIRMED: module-1.html line 243-245; mirrored in wizard orientation screen as "You are safe here / You cannot break anything / You can stop and come back any time."]
- **Canadian English** — "organised", "centre", "colour" (visible throughout module copy)
- **Québécois French** — UNKNOWN whether explicitly Québécois or Canadian-French-generic. [Spec §8 says "fr-QC" but the `lang` attributes in existing FR files use `fr-CA` per my observation in S-032 wizard work.]

## 9. Technical Architecture

- **Stack:** vanilla HTML + CSS + JS. No npm. No React. No framework. [CONFIRMED: STANDING RULES]
- **Hosting:** GitHub Pages from `digital-confidence` repo. [CONFIRMED: RETRO 2026-04-22 confirmed live at `https://twobirds-kramerica.github.io/digital-confidence/`]
- **CI/CD:** 10 GitHub Actions workflows at `digital-confidence/.github/workflows/`:
  - `accessibility-reminder.yml`
  - `axe-core.yml` (every push)
  - `broken-external-link-check.yml` (weekly)
  - `build-health-report.yml`
  - `content-count-report.yml`
  - `content-freshness.yml`
  - `deploy-check.yml`
  - `human-sprint-reminder.yml`
  - `link-checker.yml`
  - `monthly-business-report.yml`
- **Sovereignty:** self-hosted fonts (SIL-OFL Merriweather + Source Sans 3); no Google Fonts CDN; no external CDN for anything runtime-critical; all preconnects for non-runtime services (GA4 / Clarity) are consent-gated and user-cancelable.
- **Explicitly rejected:**
  - React / Vue / Svelte — violates static-only rule
  - npm / yarn / pnpm — violates no-node-frameworks rule
  - Google Fonts CDN — violates sovereignty (self-host instead)
  - Vercel-based hosting — DCC is live on GH Pages; Vercel deploy was a phantom investigation (RI logged as false premise in 2026-04-22 retro)
- **Portable sovereignty (L1→L4 float):** per decapitation checklist, every component can drop between layers by config change. [CONFIRMED partial: not all components individually verified, but tokens + fonts + vanilla stack all pass.]

## 10. Revenue Model

- **B2B white-label licensing** — CONFIRMED partial via `digital-confidence/_b2b/` directory (outreach dashboard, pitch deck) + `digital-confidence/b2b/` (public index, pricing, ROI calculator, case-study template)
- **Target buyers:** UNKNOWN from chat export in this pass. Inferred candidates from portfolio docs: libraries, municipalities, healthcare, credit unions.
- **Pricing:** UNKNOWN specific numbers. Spec §10 mentioned "CA$15k-$30k/year" range as a target; unable to confirm without deeper chat or Notion scan.
- **Revenue target:** $10,000/month by August/September 2026. [CONFIRMED: portfolio CLAUDE.md "WHO AARON IS" section]
- **What a buyer needs to see:** UNKNOWN — inferred from the existence of completion certificates (S-DCC-V2 Phase 5) + white-label CSS-var hook (`--client-logo-url`) + the B2B pitch deck.
- **Kids version:** planned as separate product. S-R01 Kids Research DB Phase 1 shipped 20 rows (age × category coverage grid complete). [CONFIRMED: RETRO 2026-04-21]

## 11. Open Questions (UNKNOWN flags — Aaron review required)

**Status update 2026-04-23 via S-ARCHAEOLOGY-001 continuation:** projects.json + memories.json (10008-char DCC project_memory) read; many UNKNOWNs closed. Remaining genuine unknowns below.

### ANSWERED via project_memory (no longer UNKNOWN)

- ~~Margaret vs Brenda~~ **ANSWERED**: Brenda is REAL — Aaron's step-mother (full name Brenda Bender, per DCC project_memory). Trish Patzalek is the second DCC beta tester. Margaret in module-1 is a narrative composite/privacy-renamed persona derived from Brenda's psychology. [Source: `memories.json` project_memories[019c67c5]]
- ~~Brenda iPad+iPhone-only vs Android/Windows modules~~ **ANSWERED**: "Primary testing device: Samsung S24 Android Chrome" per DCC project_memory. Brenda's profile was the founding inspiration, but the actual audience broadened and the product is tested on Aaron's Android. Android + Windows escape-hatches included for parity.
- ~~Warm Hearth vote mechanics~~ **ANSWERED**: "Warm Hearth won org vote (65.5%). Font licensing audit completed (Georgia and Segoe UI rejected)." [Source: HAL Stack project_memory 019cc3d2] — it was an **org vote** (Founding Board personas, not beta users).
- ~~Merriweather + Source Sans 3 rationale~~ **PARTIAL ANSWER**: Georgia + Segoe UI were rejected during font audit; Merriweather + Source Sans 3 chosen. Specific trade-off criteria still not cited verbatim. [Source: HAL Stack project_memory]

### Still UNKNOWN (Aaron review required)

1. **FR locale precision** — code uses `fr-CA`; spec §8 said "fr-QC". Which is authoritative? (Matters for locale-specific fallbacks + content references.)
2. **Target B2B buyer industries** — inferred (libraries, municipalities, healthcare, credit unions); not confirmed.
3. **CA$15k-$30k/year pricing confirmation** — not in DCC project_memory. Likely in `_b2b/pitch-deck.html` or chat Apr 2 "$1M in a year?".
4. **Kids version device strategy** — S-R01 Kids Research DB exists; actual product shape still undefined.
5. **Long-scroll vs wizard decision** — pending Aaron's evaluation of POC URLs (both S-032 at root + S-DCC-V2 at /v2/).
6. **Completion-data sharing with B2B buyers** — certificate.js is learner-local PDF; whether there's a back-channel N-learners-completed flow for buyers is unverified. Would live in `admin/` or `_analytics/` if it exists.
7. **DCC v2 status per HAL Stack memory** — "DCC v2 is parked until a clearer brief is defined" (HAL Stack project_memory 019cc3d2, updated 2026-03-06). Yet today (2026-04-22) Aaron scoped + approved S-DCC-V2 with "Run immediately. Budget is live. Aaron approved April 22, 2026" note. Interpretation: the "parked" status was superseded by Aaron's April 22 direction. Confirm explicitly.
8. **Machine primacy mismatch** — HAL Stack memory says "Lenovo Pentium Silver: original dev machine". Two Birds Command memory says "i5 Lenovo (primary), EZbook Pentium Silver Lenovo (secondary)". Different machine labelled primary across the two memories. Confirm current primary.

## 11a. NEW CONFIRMED — authoritative voice spec (from DCC prompt_template)

The DCC project has a prompt_template (Aaron's canonical voice spec for any Claude instance working in DCC). Direct quotes:

**Persona & Tone:**
> "You are a Senior Instructional Designer for older adults. Your 'voice' is calm, patient, and non-judgmental."

**Prohibited Phrasing:**
> "Never use words like 'simply,' 'obviously,' 'just,' or technical acronyms (API, UI, UX, MFA) without defining them as a 'Security Tool' first."

**Encouragement Loops:**
> "Every 500 words, include a 'Confidence Check' that reminds Brenda: 'You are doing great, and your device is safe.'"

**Visual-First Descriptions:**
> "Since this is a text-based guide that will be printed, you must use spatial descriptions. Instead of saying 'Open Settings,' say 'Look for the grey icon that looks like mechanical gears on your home screen.'"

**The "3-Second Rule":**
> "Integrate the '3-Second Rule' (Stop, Breathe, Verify) into every security-related chapter."

**Canadian Localisation:**
> "Always default to Canadian spelling (e.g., 'Centre,' 'Labour') and reference Ontario-specific resources provided in the Brenda_Interview_Context file."

**Exercise Design:**
> "Every practical exercise must be 'Low Stakes.' Never ask her to do something that could lead to a charge or a data change until Week 5 (Safe Transactions). Include a 'Success State' for every exercise so she knows exactly what the screen should look like when she finishes."

**No Summaries rule:**
> "If asked to generate a module, provide the full, printable text. Do not outline what would be in it."

These eight rules are the authoritative voice spec. Anywhere `tokens.css` / `CLAUDE.md` references "voice-check protocol" it should resolve to these.

## 12. Decision Log (chronological, partial)

| Date | Decision | Source |
|---|---|---|
| 2025-11-25 | Claude chat export window begins — Aaron's earliest conversation in this export | `conversations.json` date sort |
| 2026-02-16 | DCC founded as "50-80 page Master Self-Driven Training Manual" → pivoted same conversation to "website in claude code" | Chat "Digital literacy training manual for seniors", human msgs 1-2 |
| 2026-02-16 | Brenda persona defined (70+, St. Thomas, iPad+iPhone only, anxiety, Security Shield goal) | Same chat, human msg 1 |
| 2026-02-16 | Light/dark mode + font-size toggle approved day-1 | Same chat, human msg 3: *"please allow a brightness (dark or light) background ... allow her the option to change font sizing for the entire site"* |
| 2026-03-06 | Early feedback-form refinement (133-msg chat) | Chat "Digital Confidence Center feedback form refinement" |
| 2026-03-14 | Module buildout accelerating | Chat "Senior engineer workflow integration setup" (220 msgs, mis-titled) |
| 2026-03-22 | DCC AEO / cross-linking sprint | Chat "DCC cross-linking sprint prompt" |
| 2026-03-25 | DCC Mega Build Night (464 msgs) — large content expansion | Chat name |
| 2026-04-01 | DCC MegaBuild relocation project (720 msgs — largest single conversation) | Chat name |
| 2026-04-11 | DCC V07 heart-bulb logo selected (S-002) | Portfolio RETRO + git log |
| 2026-04-15 | Engineering standards + style guide foundation (S-016) | Portfolio RETRO |
| 2026-04-18 | DCC UI style options explored | Chat name |
| 2026-04-19 | Warm Hearth palette voted winner (Option A, 65.5%) | `tokens.css` header |
| 2026-04-21 | Max-mode 44-sprint session; 8/9 repos have axe-core CI + AUDIT.md; S-030 accessibility components shipped (Read-Aloud + Progress-Dots + Check-In + Keyboard-Helper); DCC Kids Research DB 8→20 rows (Phase 1 target) | Portfolio RETRO |
| 2026-04-22 | Max-mode 18-sprint session; S-DCC-V2 wizard-first /v2/ shipped; S-MCP-RELIABILITY-001 shipped; RI-006 "just go" trigger added; module count corrected 21→27; 200-page theme-color Warm Hearth alignment | Portfolio SESSION-STATE |
| 2026-04-22 | DCC reskin unlock conversation | Chat "Unlocking DCC reskin for seniors site" (16 msgs) |

---

## Phase progress notes

- **Phase 1 (chat export read):** PARTIAL — 150 conversations inventoried, 24 confirmed DCC-specific, 3 sampled for specific decisions (founding + style-options + reskin-unlock). Not done: full chronological read of the 720-msg Apr 1 MegaBuild or the 464-msg Mar 25 Mega Build Night, which almost certainly contain the specific decisions currently marked UNKNOWN.
- **Phase 2 (repo read):** PARTIAL — tokens.css, fonts.css, module-1.html fully; other modules only via previous session's H1/title grep (S-038 work). Workflow list confirmed via `ls .github/workflows/`. Not done: `DESIGN-SYSTEM.md` or `ACCESSIBILITY-REPORT.md` deep reads (prior session read module-1 structurally; these exist and are referenced but not cited here).
- **Phase 3 (Notion scan of 10 pages):** **DEFERRED** — not executed. 10 specific page IDs listed in spec; each is a fetch + extract operation. Next session with fresh budget.
- **Phase 4 (wiki):** THIS DOCUMENT. Written under time pressure; flagged PARTIAL in header.
- **Phase 5 (write to Notion):** **DEFERRED** — 2 new Notion pages under Command Center. Next session.
- **Phase 6 (SESSION-STATE):** Completed separately in the S-ARCHAEOLOGY-001 SESSION-STATE block.

Next archaeology session should (a) read the Apr 1 MegaBuild 720-msg chat in full, (b) read the Mar 25 Mega Build Night 464-msg chat, (c) scan the 10 Notion pages, (d) reconcile + close UNKNOWN flags, (e) publish to Notion as Phase 5.
