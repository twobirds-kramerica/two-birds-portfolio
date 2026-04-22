# Aaron — To-Do Backlog from 2026-04-21 autonomous session

Compiled from 12+ max-mode sprints shipped 2026-04-21 (S-030 through
S-R01-PHASE-1f). Everything in this file is a **human-required action**
that was NOT auto-executable during autonomous development. Grouped by
priority; each item has a time estimate.

**Rule going forward** (per Aaron 2026-04-21): items in this file
accumulate during autonomous cycles; Aaron reviews them in batches
when he switches to review mode. No inline pauses during dev.

---

## P0 — High-stakes content review (do before any S-R01 Spec status advance)

- [ ] **Review sextortion row tone** (15 min)
  Row: `349a09cf-876a-816a-a0b2-d5b4bc4aa532`.
  Specifically check for any accidental victim-blaming phrasing; confirm the non-shaming + "boys 14-17 primary target" framing reads right for a parent audience. This is the single highest-stakes row in the DB. Flag any wording you want changed.

---

## P1 — Content review for S-R01 rows (advance Status Research → Spec)

- [ ] **Review 8 rows shipped today in DCC Kids Research DB** (70 min total)
  Grid now complete (20/20 age×category cells) plus 3 second-row entries:
  - `349a09cf-876a-8118...` 4-6 Critical-Thinking: "True things and story things" (1c)
  - `349a09cf-876a-81c0...` 7-9 Emotional-Safety: "Telling a grown-up..." (1c)
  - `349a09cf-876a-8136...` 4-6 Creative-Making: "Making my own thing first..." (1d)
  - `349a09cf-876a-8153...` 13-15 Tech-Safety: "Turning on two-factor auth..." (1d)
  - `349a09cf-876a-8192...` 7-9 Creative-Making: "Making something useful..." (1e)
  - `349a09cf-876a-816a...` 13-15 Emotional-Safety: "Sextortion resistance" ← already P0 above (1f)
  - `349a09cf-876a-811d...` 10-12 Tech-Safety: "Using a password manager..." (1g, prerequisite for 1d 2FA row)
  - `349a09cf-876a-8163...` 13-15 Critical-Thinking: "Lateral reading + AI check" (1h, builds on 4-6 Learning + 13-15 CT-1)
  - `349a09cf-876a-8124...` 10-12 Creative-Making: "When I remix, I name who made the original" (1i, positive creator-citizenship)
  - `349a09cf-876a-8122...` 10-12 Emotional-Safety: "Stepping out of a pile-on" (1j, 3 rehearsed moves, Kids Help Phone escalation)
  - `349a09cf-876a-816f...` 7-9 Tech-Safety: "Pause and show on app permissions" (1k, completes Tech-Safety ladder 4-6→7-9→10-12→13-15)
  - `349a09cf-876a-819e...` 13-15 Learning: "AI tutor vs shortcut" (1l, **hits Phase-1 target at 20 rows**, 4-move protocol grounded in Dartmouth 2025 + Nature 2025 RCT + Khan Academy)
  If depth/voice meets your bar, batch-advance them to Status=Spec.

- [x] **Add Cybertip.ca reference to sextortion row** ✅ done 2026-04-21 via S-R01-PHASE-1f-CYBERTIP-PATCH. Appended Canadian parallel to en-CA-Content (669 chars) + Research-Source (858 chars) via `append_to_rich_text`. Row verified: en-CA-Content now 3 blocks / 3828 chars; Research-Source 2 blocks / 2240 chars. Cybertip.ca + Canadian Centre for Child Protection + Government of Canada March 2025 investment announcement all cited.

---

## P1 — Consulting funnel monetisation (biggest revenue-adjacent leverage)

- [ ] **Mailto → Calendly on Clarity + Two Birds Innovation CTAs** (15 min each)
  Requires: your Calendly event URL (or Cal.com / TidyCal).
  (a) Clarity's "Book a Free 30-Minute Call" button (AUDIT §7).
  (b) Two Birds Innovation contact section (AUDIT §8 item 1).
  One URL, two sites, 30 min total. Biggest single revenue-adjacent change — mailto loses qualified leads at this demographic.

- [ ] **Add LinkedIn link to Two Birds Innovation contact section** (3 min)
  Currently missing from the consulting brand site — prospects WILL check LinkedIn before emailing; absence loses warm touches. TBI AUDIT §7.

- [ ] **Add OG card images across brand sites** (design work, 1-2 h each)
  Missing on aaron-patzalek AND two-birds-innovation. Every LinkedIn / Slack / email link preview currently renders blank. Covered in both AUDITs. Single image can serve both with minor variant.

- [ ] **First case study / pilot walkthrough for Two Birds Innovation** (1-2 h, blocked on a pilot)
  TBI AUDIT §7. Biggest conversion lift for the CA$2,500 audit offer.

- [x] **Apply S-CLARITY-PORTABILITY pattern to Career Coach** ✅ done 2026-04-21 as S-CC-PORTABILITY (commit `9d7e44e` on career-coach main). Provider `<select>` wired in settings with conditional key field; 4 llmChat call sites updated; redundant model override dropped from salary-negotiation call. Career Coach L1 → L3/L4.

- [x] **Self-host DM Sans + DM Serif Display for Career Coach** ✅ done 2026-04-21 as S-CC-FONTS (commit `45d3ddd` on career-coach main). ~145 KB vendored across 5 woff2 files + 2 OFL licences + 2 @font-face shims. Career Coach L1 → L3 on fonts; combined with S-CC-PORTABILITY, fully L3/L4-capable.

- [ ] **Complete Career Coach `pricing.html`** (1-2 h, blocked on deciding what Pro is)
  Currently a 23-line "Coming Soon" stub. Pre-req for any Pro conversion. CC AUDIT §7.

- [ ] **Cross-promote Clarity + Career Coach** (5 min per site)
  Each free AI-workflow product should link to the other. Top-of-funnel overlap is maximum; current setup leaves conversion on the floor. CC AUDIT §7.

- [ ] **Live-site smoke test Clarity provider picker** (5 min)
  Run `https://twobirds-kramerica.github.io/clarity/` with each provider option (Anthropic / OpenAI / Gemini / Ollama) in sequence. Confirm each key flow works end-to-end. Gemini + OpenAI + Ollama paths weren't exercised live in the autonomous session.

- [ ] **Smoke test Clarity with current Sonnet 4.6 model** (5 min)
  Run one diagnostic with the new model and eyeball the output quality vs. the old Sonnet 4.0.

---

## P1 — Notion backlog hygiene ✅ CLOSED

- [x] **File `S-DCC-VIS-STYLEGUIDE-STABLE` in Notion** — done 2026-04-21 via S-R01-PHASE-RETRO, Notion `349a09cf-876a-817a-8cbf-d292b8544e28`
- [x] **File `S-KEVIN-CSP-READY` in Notion** — done 2026-04-21 via S-R01-PHASE-RETRO, Notion `349a09cf-876a-8183-ac2f-e4fcc9931db4`

---

## P2 — Content generation (needs you to draft/provide)

- [ ] **Pricing page for Clarity** (2-3 h)
  Content needed: what the CA$2,500 AI Workflow Audit includes (duration, deliverables, timeline, guarantee). Pre-qualifies leads, raises close rate. From Clarity AUDIT §7 item 2.

- [ ] **Testimonial/portfolio-evidence block for Clarity** (30 min)
  Even one pseudonymous quote ("— Manufacturing owner, Kitchener") adds disproportionate trust. Alternative: "Who I've worked with" paragraph pointing at DCC / Kevin / Career Coach repos.

- [ ] **"Why I built this" section for Clarity** (30 min)
  Solo parent / St. Thomas origin is trust-building for the target demographic. Lean in.

---

## P2 — Clarity email-capture + list infrastructure

- [ ] **Email capture before Save Report on Clarity** (2 h)
  Requires setup: pick Formspree / Buttondown / ConvertKit. After the LLM returns, show a 2-field capture ("Email to send yourself this report" + optional "Best time to chat") before the CTA card; gate Save Report on it with a clear "Skip" link. From Clarity AUDIT §7 item 1.

- [ ] **Post-diagnostic follow-up email list** (setup-dependent)
  "Not ready for a call? Get the weekly Two Birds briefing" → capture intent even without immediate call booking.

---

## P2 — DCC / Kevin hygiene follow-ups

- [ ] **Cross-browser device test for Kevin's Apartment** (10 min)
  Open on Safari iOS and Firefox desktop before next Kevin-shown update. Visual check only.

- [ ] **Cross-browser device test for Clarity** (10 min)
  Same pattern. Five minutes max.

- [ ] **Monitor Monday 2026-04-27 10:00 EDT** (≤ 2 min check)
  The new `listing-availability.yml` cron fires for the first time that day. Check for any auto-opened GitHub issue on Kevin's repo. If any of the 14 active listings have expired URLs, the workflow will flag them with archive instructions.

- [ ] **Tune check-in-banner timing if needed** (5 min)
  DCC module pages now show a "Still with us?" banner at 8-min idle or 50% scroll. If early feedback says too aggressive, swap `IDLE_MS` in `js/check-in.js` from `8 * 60 * 1000` → `12 * 60 * 1000`. Single-line change.

---

## P2 — Research DB primary-source upgrades (optional polish)

- [ ] **Upgrade Piaget/Erikson paraphrase citations to primary sources** (45 min total)
  Five of the new DCC Kids Research rows use textbook-paraphrased Piaget / Erikson references. If you want primary-source anchoring, add direct publication cites (e.g., Piaget 1952, Erikson 1963) as a follow-up pass.

---

## P3 — Long-horizon items that came up

- [x] **Notion: retro-file today's sprints as Done/Backlog entries** ✅ done 2026-04-21 via S-R01-PHASE-RETRO (commit deabcae). 14 Done entries + 2 Backlog follow-ups filed via create_backlog_item helper. Zero failures on 16 consecutive API calls. Entries include: S-KEVIN-HYGIENE, S-CLARITY-PORTABILITY, S-NOTION-CREATE-PAGE, S-R01-INFRA, S-R01-PHASE-1c through 1l, plus S-DCC-VIS-STYLEGUIDE-STABLE and S-KEVIN-CSP-READY as Backlog.

- [x] **S-R01-PHASE-1 remaining: 6 more rows to hit 20+ target** ✅ done 2026-04-21 — DB hit 20 rows at S-R01-PHASE-1l (commit 7dca6d2). Coverage grid 20/20; 8 cells have 2nd-row depth; three ladders complete (Tech-Safety, Emotional-Safety, AI-literacy) spanning all 4 age brackets.

- [ ] **S-R01-PHASE-1 remaining: 6 more rows beyond 20+ target (stretch — optional)** (6 × 45 min)
  Grid is complete; next rows deepen cells. High-value candidates: 2nd 10-12 Tech-Safety (password manager), 2nd 13-15 Critical-Thinking (AI/deepfake literacy), 2nd 10-12 Creative-Making (fair-use / credit when remixing). Can be done autonomously in future sessions.

- [ ] **Opus 4.6-specific sprints waiting on model**: S-R01-PHASE-3 — age-bracket psychology refinement. Tagged for Opus 4.6 per original sprint notes.

- [ ] **S-026 data re-audit** — BLOCKED on your fresh Claude.ai data export.

---

## What was NOT the bottleneck today (keep doing)

- Small autonomous sprints with clear scope
- Meta-tooling before content when tooling is missing
- Scope-honesty when a sprint is obviously too big for one session
- Verified citations via WebSearch before writing any factual content
- Committing after every phase
- Push + SESSION-STATE after every sprint

---

**Generated:** 2026-04-21 during autonomous session (sprints 1-12+)
**Format:** P0 = review-before-anything-else; P1 = revenue/safety adjacent; P2 = useful polish; P3 = long-horizon. Time estimates are "focused work" minutes, not calendar time.
