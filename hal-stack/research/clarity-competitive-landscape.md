# Clarity — Competitive Landscape Research
**Date:** 2026-05-29 | **Prepared for:** Aaron Patzalek / Two Birds Innovation

---

## 1. Competitor Table

| Tool | Target | Inputs Collected | Outputs Produced | Free? | API Model |
|---|---|---|---|---|---|
| **Impact Maker** (impactmaker.co) | SMEs | Website URL only — tool reads the business from the web | Board-ready AI automation report, ROI model, industry benchmarks, EU AI Act compliance flag — delivered in ~8 min | Free, no account | Hosted backend (their API, their cost) |
| **Hello Alice AI Readiness Assessment** (helloalice.com) | US small business owners | Structured questionnaire on operations, tech stack, team | Personalised recommendations + automation opportunities, impact projections | Free, account required | Hosted backend |
| **PxlPeak AI Readiness Assessment** (pxlpeak.com/tools/ai-readiness-assessment) | Small business | 10 questions across 4 dimensions (data, process, culture, infrastructure) | Scored report + personalised implementation roadmap | Free | Hosted backend |
| **FounderPal SWOT Generator** (founderpal.ai/swot-analysis-generator) | Founders / solopreneurs | Business type / product description (text prompt) | SWOT matrix in ~10 seconds | Free, no email required | Hosted backend; paid plans ($69–$199 one-time) unlock full strategy suite |
| **Microsoft AI Readiness Assessment** (learn.microsoft.com) | Enterprise / SME | 10 multiple-choice questions across 7 pillars (strategy, governance, data, culture, infra, etc.) | Scored readiness report + curated recommendations by stage | Free | Hosted (Microsoft Azure) |
| **DS+CO AI Readiness Check** (aireadycheck.dixonschwabl.com) | Financial institutions, then broader | 29 questions across strategy, risk, data, talent, governance | Readiness score (0–30+), top 3 prioritised steps, board conversation starters | Free | Hosted backend |
| **BizHealth.ai** (bizhealth.ai) | SMEs | 200+ indicators across 12 areas (finance, ops, HR, sales, marketing, tech, leadership) | Comprehensive health score across all 12 areas, gap analysis — 30–40 min | Paid (no free tier) | Hosted backend |
| **BDC LIFT** (bdc.ca/en/solutions/lift) | Canadian SMEs ($1M+ revenue) | Advisor-led consultation (not self-serve) | Digital maturity roadmap + eligibility for $25K–$5M AI adoption loans | Free advisory, loan product | Human advisors, not self-serve AI |
| **Board of Innovation AI Adoption Assessment** (ai-adoption.boardofinnovation.com) | Mid-market / enterprise | Structured assessment (exact questions not disclosed) | AI adoption maturity level + roadmap recommendations | Free (lead-gen for consulting) | Hosted backend |
| **ISED Canada SME AI Toolkit** (ised-isde.canada.ca) | Canadian SMEs | Self-guided checklist / questionnaire | Scan → pilot → scale framework, responsible AI guidance | Free, government | No AI call — static guidance |

---

## 2. How Competitors Handle the API Key Question

**Clarity is the only tool in this space that uses a bring-your-own-key (BYOK) model.** Every other competitor — Impact Maker, Hello Alice, PxlPeak, FounderPal, Microsoft, DS+CO — runs a hosted backend that absorbs API costs. The BYOK approach is almost exclusively found in developer tools (e.g., some MCP/Apify integrations), not consumer-facing SME diagnostics.

**Implications for Clarity:**
- BYOK is a genuine friction point for non-technical SME owners (they don't have an OpenAI API key)
- It is also Clarity's single largest competitive differentiator: zero backend infrastructure cost, zero data storage risk, complete user privacy — which maps well to Canadian privacy expectations (PIPEDA)
- The BYOK model is a feature for privacy-forward messaging but a barrier for mass adoption

---

## 3. Standard Output Format — What the Best Tools Produce

Across the competitive set, the emerging standard output bundle is:

1. **Maturity/readiness score** — a single number or stage (e.g., 1–5 or 0–30) that benchmarks the business
2. **SWOT or gap analysis** — FounderPal and static SWOT generators focus here; enterprise tools include it as one layer
3. **Top 3–5 prioritised recommendations** — almost universal; the best tools rate by effort and ROI
4. **Quick wins** — Impact Maker and Hello Alice both highlight "fastest return" opportunities
5. **Industry benchmarks** — Impact Maker includes these; most others do not for SMEs
6. **Compliance flag** — Impact Maker includes an EU AI Act flag; no Canadian equivalent exists in any tool
7. **A next-step CTA** — board conversation starters (DS+CO), loan eligibility (BDC), or consulting upgrade (BizHealth.ai, Board of Innovation)

Clarity currently produces items 2, 3, 4, and 7 — it is missing the score, benchmarks, and compliance dimension.

---

## 4. Monetisation Models in the Free Tool Space

| Model | Examples | How It Works |
|---|---|---|
| **Free tool → consulting upsell** | Board of Innovation, BizHealth.ai, Clarity | Free diagnostic acts as a lead magnet; paid engagement is advisory/consulting |
| **Free tool → subscription upsell** | FounderPal ($69–$199 one-time), Hello Alice (premium resources) | Freemium; deeper strategy tools or saved history behind paywall |
| **Free tool → loan / financing product** | BDC LIFT | Government-backed; tool qualifies SMEs for a $500M loan pool |
| **Free tool → partner referrals** | Microsoft (Azure, Copilot), PxlPeak (agency services) | Tool drives adoption of the vendor's own paid platform |

Clarity's model — free diagnostic + CA$2,500 consulting upgrade — is the correct archetype for a solo practitioner. Board of Innovation uses the same pattern at enterprise scale.

---

## 5. Canadian-Specific Competitors and Context

- **BDC LIFT** is the most significant Canadian-specific entry: a $500M program pairing advisory with low-cost loans, launched April 2026. It targets $1M+ revenue businesses and is advisor-led, not self-serve.
- **ISED Canada SME AI Toolkit** is a static government resource (no AI generation), focused on responsible deployment.
- **CAIAI (aiadoption.ca)** is a policy body, not a diagnostic tool.
- **Signal49 Research / Future Skills Centre** is building a sector-specific AI use-case decision tool (as of April 2026, still in development).

**No free, self-serve, AI-generated diagnostic tool specifically targeting Canadian SMEs exists.** Clarity occupies this gap cleanly.

---

## 6. What Clarity Should Add — 5 Specific Feature Recommendations

### R1 — AI Readiness Score (single number, 0–100)
**What:** Add a computed score before the SWOT output — a weighted sum across the inputs already collected (current AI usage, team size, industry maturity, revenue goal ambition).
**Why:** Every top competitor surfaces a score. It gives the user something to share, remember, and return to improve. It also makes the consulting upsell more concrete: "Your score is 38/100 — a 60-minute session can get you to 65."
**Effort:** Low — calculate in `clarity.js` from existing inputs; pass as context to the LLM prompt.

### R2 — Industry Benchmark Line ("Average for [Industry] in SW Ontario: X")
**What:** After the score, show a static benchmark sentence drawn from a small JSON lookup table built from ISED / BDC published data on Canadian SME AI adoption rates by sector.
**Why:** Impact Maker is the only free tool that does this, and it is a standout feature. Benchmarks convert abstract scores into motivation. A plumbing company owner seeing "your industry average is 22/100" immediately understands their opportunity.
**Effort:** Medium — requires one-time research to populate a 15–20 industry lookup table; no backend needed (static JSON).

### R3 — Shareable / Printable PDF Report
**What:** A "Download Report" button that generates a one-page PDF (or print-formatted HTML) of the SWOT + recommendations + score + next step, with Two Birds Innovation branding.
**Why:** DS+CO and BizHealth.ai both produce board-ready documents. SME owners want to share results with their business partner, accountant, or bank. A branded PDF is a distribution channel — every shared report is a referral.
**Effort:** Medium — use `window.print()` with a print-specific CSS stylesheet; no library needed.

### R4 — Email Capture + Follow-Up Sequence Hook
**What:** After the report renders, offer "Email me this report + a 3-part AI quick-start guide" — captures name and email, sends report via a lightweight form backend (Formspree or Netlify Forms, free tier).
**Why:** Clarity currently has no list-building mechanism. Every competitor converts free tool users into an email audience. A 3-email sequence (day 0: report, day 3: case study, day 7: consulting offer) is the standard lead-nurture pattern and requires zero ongoing effort once written.
**Effort:** Low-medium — Formspree free tier, one HTML form, three pre-written emails.

### R5 — Canadian Privacy / PIPEDA Compliance Flag
**What:** Add a one-line assessment output item: "Privacy posture: [Low / Medium / High risk] — [one-sentence rationale based on data handling inputs]." Include a tooltip explaining PIPEDA relevance.
**Why:** No competitor offers a Canadian regulatory lens. ISED's toolkit covers responsible AI but not privacy risk. Given Clarity's audience (Canadian SMEs) and Clarity's own BYOK/no-storage architecture, leading with privacy is a genuine differentiator that resonates in post-Bill C-27 discourse.
**Effort:** Low — add 2–3 privacy-related questions to the input form (e.g., "Does your business collect customer personal data?") and include a PIPEDA-aware instruction in the LLM prompt.

---

## Sources

- [Impact Maker Free AI Readiness Assessment](https://www.impactmaker.co/free-ai-readiness-assessment-tool)
- [Hello Alice AI Readiness Assessment for Small Business](https://helloalice.com/is-your-small-business-ready-for-ai-this-free-assessment-has-the-answer/)
- [PxlPeak AI Readiness Assessment for Small Business](https://pxlpeak.com/tools/ai-readiness-assessment)
- [FounderPal SWOT Analysis Generator](https://founderpal.ai/swot-analysis-generator)
- [Microsoft AI Readiness Assessment](https://learn.microsoft.com/en-us/assessments/94f1c697-9ba7-4d47-ad83-7c6bd94b1505/)
- [DS+CO AI Readiness Check (RBJ article)](https://rbj.net/2025/11/19/dsco-free-ai-readiness-check/)
- [DS+CO AI Readiness Check launch (PR Newswire)](http://www.prnewswire.com/news-releases/dixon-schwabl--company-unveils-ai-readiness-check-for-financial-leaders-at-nyba-forum-302608756.html)
- [BDC Launches LIFT — Canadian SMEs](https://www.bdc.ca/en/about/mediaroom/news-releases/bdc-launches-lift-getting-canadian-smes-off-the-ai-sidelines)
- [BDC LIFT Program Page](https://www.bdc.ca/en/solutions/lift)
- [Board of Innovation AI Adoption Assessment](https://ai-adoption.boardofinnovation.com/)
- [BizHealth.ai Best Business Diagnostic Tools 2026](https://bizhealth.ai/resources/best-business-health-assessment-tools-small-business-owners-2026/)
- [FounderPal pricing / features (AITECHFY)](https://aitechfy.com/aitool/founderpal/)
- [ISED Canada SME AI Adoption Blueprint](https://ised-isde.canada.ca/site/ised/en/sme-ai-adoption-blueprint)
- [ISED Canada Toolkit for SMEs Deploying AI](https://ised-isde.canada.ca/site/ised/en/toolkit-small-and-medium-sized-enterprises-smes-deploying-artificial-intelligence-ai)
- [Canadian AI Adoption Initiative (CAIAI)](https://www.aiadoption.ca/)
- [Signal49 / Future Skills Centre AI Adoption Guide April 2026](https://fsc-ccf.ca/research/ai-adoption-among-small-businesses/)
- [OECD Digital Business Diagnostic Tools for SMEs](https://www.oecd.org/en/publications/digital-business-diagnostic-tools-for-smes-and-entrepreneurship_516bdf9c-en.html)
