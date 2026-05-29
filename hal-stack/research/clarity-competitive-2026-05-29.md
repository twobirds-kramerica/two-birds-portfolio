# Clarity — Competitive Analysis
**Date:** 2026-05-29

---

## Competitor Landscape

| Tool | Free? | BYOK? | Canadian? | Standout Feature |
|---|---|---|---|---|
| **Impact Maker** | Yes | No | No | Reads your website URL — no form. Produces ROI model + benchmarks in 8 min |
| **Hello Alice** | Yes (account required) | No | No | US-focused; automation opportunities + impact projections |
| **PxlPeak** | Yes | No | No | 10 questions, 4-dimension score, implementation roadmap |
| **FounderPal** | Free (SWOT only); $69–$199 full suite | No | No | 10-second SWOT, no email gate, upsells to full strategy toolkit |
| **Microsoft AI Readiness** | Yes | No | No | 7-pillar framework; most authoritative brand halo |
| **DS+CO AI Readiness Check** | Yes | No | No | 29 questions, scored 0–30+, board conversation starters |
| **BizHealth.ai** | Paid | No | No | 200+ indicators, 12 business areas — most comprehensive |
| **BDC LIFT** | Free advisory | No | **Yes** | $500M Canadian loan program (launched April 2026), advisor-led, requires $1M+ revenue |

---

## Critical Findings

**On BYOK (Bring Your Own Key):**
Clarity is the only tool in the space using a BYOK model. No other SME-facing diagnostic does this. It is simultaneously Clarity's biggest privacy/cost advantage and its biggest conversion barrier with non-technical owners.

**The Canadian self-serve gap:**
No free, AI-generated, self-serve diagnostic tool targeting Canadian SMEs exists. BDC LIFT is the only Canadian-specific offering and it requires $1M+ revenue and a human advisor. This is Clarity's uncontested lane.

---

## 5 Actionable Feature Recommendations

1. **AI Readiness Score (0–10 or 0–100)** — calculated from existing inputs; every top competitor has one; makes the consulting upsell concrete. *(Implemented overnight: readiness_score added to prompt and displayed in results header)*

2. **Industry Benchmark Line** — a static JSON lookup of Canadian SME AI adoption averages by sector (ISED/BDC data); Impact Maker is the only free tool that does this and it's a standout feature. Brief: show "Your industry average: 3/10" alongside the score.

3. **Shareable/Printable PDF Report** — print-CSS-only, branded Two Birds report. DS+CO and BizHealth.ai both produce board-ready docs. Every shared report is a referral. *(Print CSS already exists — needs a "Download as PDF" button that triggers window.print())*

4. **Email Capture + 3-Email Follow-Up Sequence** — Formspree free tier: day 0 report, day 3 case study, day 7 consulting offer. Clarity currently has zero list-building mechanism. This is the highest-value lead-gen addition.

5. **Canadian Privacy / PIPEDA Compliance Flag** — no competitor offers a Canadian regulatory lens. 2–3 added input questions + PIPEDA-aware LLM prompt instruction. Strong differentiator post-Bill C-27 (Online Harms Act).

---

## What Was Implemented Overnight (2026-05-29)

- Readiness score (1–10) added to prompt and displayed as badge in results header
- 7 industries → 15 industries (added Automotive, Construction, Agriculture, Food & Hospitality, Legal & Accounting, Personal Services, Real Estate, Transportation & Logistics)
- Demo mode: "See a sample report" link on setup screen, pre-baked Riverside Plumbing & Heating example
- CTA button text in results changed from "Book a Free 30-Minute Call" to "Email Aaron about my results →" (href was already becoming a mailto: but label was wrong)

## Next Sprint Candidates (in priority order)
1. Email capture + Formspree follow-up sequence (P1 — zero list-building currently)
2. Industry benchmark line — static JSON, Canadian ISED/BDC data (P2)
3. Cloudflare Worker proxy — removes API key barrier entirely (P1 — biggest conversion blocker)
4. PIPEDA compliance flag — 2–3 added form questions + prompt update (P2)

---

## Sources
- [Impact Maker](https://impactmaker.ai/)
- [FounderPal SWOT](https://founderpal.ai/swot-analysis-generator)
- [Microsoft AI Readiness](https://adoption.microsoft.com/en-us/ai-readiness/)
- [DS+CO AI Readiness Check](https://dsco.io/ai-readiness-check/)
- [BDC LIFT](https://www.bdc.ca/en/articles-tools/blog/bdc-lift-new-program)
