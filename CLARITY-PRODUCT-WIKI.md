<!--
  Clarity Product Wiki — produced by S-ARCHAEOLOGY-003 (2026-04-23 ~00:25 EST)
  Status: MVP. Primary sources: clarity/AUDIT.md, clarity/README.md (just
  created this session), DCC project_memory (Clarity is listed as a
  portfolio product there), commit log in clarity repo.
-->

# Clarity Product Wiki — v0.1 MVP

**Last updated:** 2026-04-23 00:25 EST (Toronto)
**Source:** `clarity/` repo commit log + AUDIT.md + README.md + DCC project_memory (Clarity described as a sibling product)
**Status:** Living document — Aaron reviews and corrects.

## 1. What Clarity Is

**Free AI-readiness diagnostic tool for Canadian small and medium-sized businesses.** Short self-assessment; user receives a SWOT-style output with quick wins + recommended next steps. Paired with an optional CA$2,500 consulting upgrade for deeper work.

Per DCC project_memory (portfolio inventory):
> "**Clarity** — Free AI business diagnostic for SMEs with SWOT output and consulting lead capture."

**Live URL:** `https://twobirds-kramerica.github.io/clarity/`

## 2. Product Vision

- **Audience:** Canadian SME owners who suspect AI matters but don't know where to start
- **Value prop:** 5-10 minute self-diagnostic that produces something they can actually use, not a lead-magnet quiz
- **Monetisation:** Free tool → consulting lead capture → CA$2,500 audit-and-recommendations engagement
- **Hosting:** Static HTML/CSS/JS on GitHub Pages (same as rest of portfolio)

## 3. Core Principles (inherited from Two Birds standing rules)

- Static HTML/CSS/JS only — no npm, no Node frameworks
- Self-hosted fonts (no Google Fonts CDN) — **UNKNOWN which fonts Clarity ships; AUDIT.md §2 mentions self-host recommendation pattern; requires direct `ls clarity/fonts/`**
- Canadian English
- Sovereignty L1-L4 float model per HAL Stack architecture
- WCAG AAA contrast via tokens
- 44px minimum tap targets

## 4. Technical State (verified via commit log)

Shipped components (from commit log):
- `a5a0d4d` — **S-CLARITY-PORTABILITY**: LLM provider picker wired end-to-end (Anthropic / OpenAI / Gemini / Ollama; bring-your-own-key; runs client-side). This is the sovereignty win — users can swap providers without leaving the tool.
- `acfa927` — LLM portability layer + API call migrated to `js/llm-provider.js`
- `e4e79b7` — **S-CLARITY-PORTFOLIO-EVIDENCE**: factual portfolio-evidence line under CTA card (DCC + Kevin + Career Coach references; sidesteps "no testimonials" audit flag without fabricating social proof)
- `e14da50` — inline script extracted to `js/clarity.js` (S-KEVIN-CSP-READY pattern — paves the way for stricter CSP)
- `c5b7fe0` — **S-CROSS-PROMO**: results page links to Career Coach + DCC (each product becomes the other's top-of-funnel)
- `1f594fe` — weekly external-link check CI (mirrors DCC pattern)
- `58fc6dd` — "Clarity CTA optimised — references audit, better copy, urgency, no-obligation framing"
- `2d28926` — S-CLARITY HAL Stack rigor audit report (the AUDIT.md that lives in repo)

## 5. AUDIT Status (from clarity/AUDIT.md PROGRESS UPDATE header, S-042)

Top-5 next actions from the 2026-04-21 audit:
- 1. Mailto → Calendly — **OPEN** (blocked on Aaron providing Calendly URL, P1 in `aaron-todos-2026-04-21.md`)
- 2. Pricing page or section — **OPEN** (no pricing.html file exists; blocked on product decision)
- 3. Email capture before Save Report — **OPEN** (not shipped; would plug the leakiest part of the funnel)
- 4. LLM portability Route B — **SHIPPED** (`a5a0d4d`)
- 5. Testimonial or portfolio-evidence block — **SHIPPED factual variant** (`e4e79b7`)

## 6. Monetisation Model

- **Free tool** → lead capture (email before Save Report is still open per §5)
- **CA$2,500 consulting audit** upgrade
- **Cross-promotion to sibling tools** (Career Coach + DCC) shipped 2026-04-21

## 7. Open Questions

1. **Pricing validation** — CA$2,500 is a number, not a tested number per the original AUDIT. Has it been tested with 5 prospects?
2. **Pricing-page content** — blocked on "deciding what Pro is" (same theme as Career Coach)
3. **Email capture timing** — before Save Report, after Save Report, or both? Decision pending
4. **Font stack** — not verified in this wiki pass; `ls clarity/fonts/` would confirm
5. **Dark/light palette** — not verified; Clarity AUDIT mentions contrast checks but theme variants not documented here

## 8. Decision Log

| Date | Decision | Source |
|---|---|---|
| 2026-04-21 | Clarity HAL Stack rigor audit (S-CLARITY) | commit `2d28926` |
| 2026-04-21 | LLM portability shipped end-to-end (4 providers) | commit `a5a0d4d` |
| 2026-04-21 | Cross-promotion to Career Coach + DCC | commit `c5b7fe0` |
| 2026-04-21 | Factual portfolio-evidence block (testimonial substitute) | commit `e4e79b7` |
| 2026-04-22 | AUDIT.md PROGRESS UPDATE header added (S-042) | commit `fe7af3d` |
| 2026-04-23 | Root README.md created (S-NEXT-SESSION) | commit `9b193d3` |

## 9. Pointers

- Repo: `C:\twobirds\clarity` (master branch)
- Audit + progress: `clarity/AUDIT.md`
- Live URL: `https://twobirds-kramerica.github.io/clarity/`
- Sibling tools: Career Coach (same portability pattern), DCC (hero portfolio product)
