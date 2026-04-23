<!--
  Career Coach Product Wiki — produced by S-ARCHAEOLOGY-004 (2026-04-23 ~00:30 EST)
  Status: MVP. Sources: career-coach/AUDIT.md, README.md, commit log, DCC
  project_memory (Career Coach listed as portfolio product), Job Application
  Suite prompt_template (019c784a — provides the "voice" origin for banned-
  words list + "no AI tells" rule that propagated portfolio-wide).
-->

# Career Coach Product Wiki — v0.1 MVP

**Last updated:** 2026-04-23 00:30 EST (Toronto)
**Source:** `career-coach/` repo + AUDIT.md + commit log + DCC project_memory + Job Apps prompt_template (019c784a) as voice-origin
**Status:** Living document — Aaron reviews and corrects.

## 1. What Career Coach Is

Per DCC project_memory (portfolio inventory):
> "**Career Coach** — AI job application tool with red flags detector, cover letter templates, salary negotiation coach, privacy-first beta."

**Origin:** derived from Aaron's own job-application work (project `019c784a` "Aaron Patzalek Job Application Suite 2026", active Feb 2026). The Job Apps prompt_template is "The Editor" — a senior resume strategist persona with explicit anti-fabrication rules; Career Coach productises that into a tool anyone can use.

**Live URL:** `https://twobirds-kramerica.github.io/career-coach/`

## 2. Product Vision

- **Audience:** Canadian job-seekers, especially in career transitions (services / operations / telco backgrounds, adjacent to Aaron's own)
- **Value prop:** honest CV/cover-letter writing help that won't embellish, stuff keywords, or produce "AI tells"
- **Privacy:** bring-your-own-key LLM + client-side only — no server-side storage of anyone's job hunt
- **Monetisation:** free core + eventual Pro tier (blocked on "deciding what Pro is" per AUDIT §8 item #3)

## 3. Voice Rules (from Job Apps prompt_template, inherited)

The Editor persona — direct quotes from `projects.json[019c784a].prompt_template`:

> "Language matching only: mirror the job posting's own words where Aaron's experience legitimately supports it. Never invent a skill or metric."

> "No keyword stuffing: if something doesn't fit naturally, flag it rather than forcing it."

> "**No AI tells: banned words include spearheaded, leveraged, fostered, passionate, dynamic, results-driven, delve, and tapestry.** Write like a sharp human wrote it."

> "No fluff: every bullet must carry a result, a scope, or a decision. Cut anything decorative."

> "When uncertain whether something is accurate, ask before writing it. Confidence level required on every substantive output."

**This banned-words list is the authoritative origin** of the portfolio-wide voice-check protocol — ported from Career Coach's productised heritage into `CLAUDE.md` STANDING RULES + `hal-stack/sprint-system/backlog/P2-voice-check-protocol.md`.

## 4. Technical State (verified via commit log)

Shipped components:
- `09890c3` — LLM portability layer (all 3 API calls migrated to `js/llm-provider.js`)
- `9d7e44e` — **S-CC-PORTABILITY**: provider picker wired end-to-end (same pattern as Clarity's `a5a0d4d`)
- `45d3ddd` — **S-CC-FONTS**: self-hosted DM Sans + DM Serif Display (dropped Google Fonts; ~145 KB across 5 woff2 + 2 OFL licences + 2 @font-face shims)
- `0b53a6e` — **S-CC-CSP-READY**: 1560-line inline script extracted to `js/app.js` (S-KEVIN-CSP-READY pattern — paves the way for stricter CSP)
- `4f37d4f` — **S-CC-HYGIENE**: skip-link, main landmark, en-CA lang, OG meta, axe-core CI, AUDIT.md
- `da62d75` — **S-CROSS-PROMO**: footer links to Clarity + DCC (cross-promotion sibling pattern)
- `80ee1e1` — **S-037**: stale Google Fonts preconnect cleanup (beta/index.html)
- `e76a581` — **S-042**: AUDIT.md PROGRESS UPDATE header (3 of 5 Top-5 items shipped)

## 5. AUDIT Status (from career-coach/AUDIT.md PROGRESS UPDATE header)

Top-5 next actions from the 2026-04-21 audit:
- 1. Apply S-CLARITY-PORTABILITY pattern — **SHIPPED** (`9d7e44e`)
- 2. Self-host DM fonts — **SHIPPED** (`45d3ddd`)
- 3. Complete `pricing.html` — **OPEN** (blocked on deciding what Pro is; current file is a 23-line "Coming Soon" stub)
- 4. Clarity + Career Coach cross-promotion — **SHIPPED** (`da62d75`)
- 5. Pro-launch email capture — **OPEN** (not shipped; builds the list that converts when Pro ships)

## 6. Monetisation Model

- **Free core tier** — CV analysis, red-flags detector, cover-letter templates, salary negotiation coach (privacy-first, client-side only)
- **Pro tier** — **UNKNOWN scope** (blocked decision)
- **Pro-launch email capture** — **OPEN** backlog item (Aaron-todo 2026-04-21): asking users "tell me when Pro ships" during CSV export or after first successful CV analysis is high-ROI (30 min + Formspree integration)

## 7. Open Questions

1. **What IS Pro?** — blocks both pricing.html + email capture. Identified in AUDIT but no decision yet.
2. **Target job-seeker persona** — Aaron's own profile (services/ops/telco senior leader) or broader? AUDIT's voice rules mirror Aaron's own job-app work verbatim — productising or generalising?
3. **AI output quality** — has Haiku 4.5 actually produced good cover letters + CV analyses in real use? AUDIT §9 flags this as "not covered" — never validated with sample runs.
4. **Competitor landscape** — Teal, Jobscan, Rezi mentioned in AUDIT; positioning vs paid competitors (privacy-first is a real differentiator, but has the positioning been tested?)
5. **Real job-seeker walkthrough** — AUDIT §9 flags no actual Canadian job-seeker has been watched completing the onboarding; likely reveals UX friction invisible to static inspection.

## 8. Decision Log

| Date | Decision | Source |
|---|---|---|
| 2026-02-19 | Job Apps Suite project created (precursor to productised Career Coach) | projects.json[019c784a] |
| 2026-02-19 | "The Editor" voice + banned-words list locked | Job Apps prompt_template |
| 2026-04-21 | Career Coach HAL Stack rigor audit (S-CC-HYGIENE) | commit `4f37d4f` |
| 2026-04-21 | LLM portability shipped | commit `9d7e44e` |
| 2026-04-21 | DM Sans + DM Serif Display self-hosted | commit `45d3ddd` |
| 2026-04-21 | Inline 1560-line script extracted (CSP-ready) | commit `0b53a6e` |
| 2026-04-21 | Cross-promotion to Clarity + DCC | commit `da62d75` |
| 2026-04-22 | Stale preconnect cleanup (S-037) | commit `80ee1e1` |
| 2026-04-22 | AUDIT PROGRESS UPDATE header (S-042) | commit `e76a581` |

## 9. Pointers

- Repo: `C:\twobirds\career-coach` (main branch)
- Audit + progress: `career-coach/AUDIT.md`
- Live URL: `https://twobirds-kramerica.github.io/career-coach/`
- Origin project: `019c784a` "Aaron Patzalek Job Application Suite 2026" (projects.json)
- Sibling tools: Clarity (same portability pattern), DCC (portfolio hero)
- Voice origin: Job Apps prompt_template (not versioned in repo; lives in Claude.ai project workspace)
