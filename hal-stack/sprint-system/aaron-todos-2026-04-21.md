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
  If depth/voice meets your bar, batch-advance them to Status=Spec.

- [ ] **Add Cybertip.ca reference to sextortion row** (5 min)
  Canadian-specific follow-up: Take It Down works cross-border but US reporting paths (tips.fbi.gov, etc.) should be paired with Cybertip.ca for Canadian teens. Small edit to the existing row.

---

## P1 — Clarity monetisation (biggest revenue-adjacent leverage)

- [ ] **Mailto → Calendly on Clarity CTA** (15 min)
  Requires: your Calendly event URL (or Cal.com / TidyCal).
  Replace `mailto:aaron.patzalek@gmail.com` on Clarity's "Book a Free 30-Minute Call" button with the Calendly link. Biggest UX/conversion win-per-minute identified in Clarity AUDIT §7.

- [ ] **Live-site smoke test Clarity provider picker** (5 min)
  Run `https://twobirds-kramerica.github.io/clarity/` with each provider option (Anthropic / OpenAI / Gemini / Ollama) in sequence. Confirm each key flow works end-to-end. Gemini + OpenAI + Ollama paths weren't exercised live in the autonomous session.

- [ ] **Smoke test Clarity with current Sonnet 4.6 model** (5 min)
  Run one diagnostic with the new model and eyeball the output quality vs. the old Sonnet 4.0.

---

## P1 — Notion backlog hygiene

- [ ] **File `S-DCC-VIS-STYLEGUIDE-STABLE` in Notion** (5 min)
  Currently only named in commit history. Build styleguide-specific visual regression with viewport clip + region masking. LOE: 1-2 h.

- [ ] **File `S-KEVIN-CSP-READY` in Notion** (5 min)
  Extract inline `<script>` / `<style>` from `kevins-apartment-search/index.html` into external files; replace 11 remaining inline onclick handlers. LOE: 1-2 h. Low value today; valuable the moment Kevin's repo migrates to any header-capable host.

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

- [ ] **Notion: file `S-R01-INFRA`, `S-NOTION-CREATE-PAGE`, `S-R01-PHASE-1c/1d/1e/1f` as retro-backlog entries** (20 min)
  None of the meta-tooling or content-batch sprints shipped today have formal Notion rows. They were promoted under max-mode's "last resort" clause. Worth creating Done rows for the paper trail if you want clean Notion history.

- [ ] **S-R01-PHASE-1 remaining: 6 more rows to hit 20+ target** (6 × 45 min)
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
