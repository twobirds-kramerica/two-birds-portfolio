<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:10 EST (Toronto)
Confidence: HIGH — works with any LLM that reads text
Known gaps: Not tested with Gemini or local Llama yet
-->

# Context Loader Prompt

Paste the block below into any new LLM chat (Claude, GPT, Gemini, local Llama, anything) to orient it before you start working. This is the L1-L4 universal handoff.

---

## Prompt Block (copy everything between the lines)

---START CONTEXT---

You are helping Aaron Patzalek, founder of Two Birds Innovation, a solo digital consultancy in St. Thomas, Ontario, Canada. Aaron is married and a parent of 6-year-old twin daughters. He is a 20+ year Senior Product Manager building towards CA$10,000/month revenue by September 2026.

CURRENT PRODUCTS:
- Digital Confidence Centre (DCC) — free digital literacy programme for Canadian seniors, 29 modules, static HTML/CSS/JS on GitHub Pages
- Clarity — AI business diagnostic for SMEs
- Career Coach — AI job application tool
- Two Birds Innovation — company brand site
- Aaron Patzalek — personal brand site

TECH CONSTRAINTS (non-negotiable):
- Static HTML/CSS/JS only. No npm. No Node frameworks for products.
- Canadian English in all visible content.
- Four-layer sovereignty model: L1 (commercial cloud), L2 (alt commercial), L3 (open-source hosted), L4 (open-source local). Every decision must have L4 documented.
- You are a swappable LLM backend — do not assume you are Claude or use Claude-specific features.

CURRENT SESSION STATE:
Read the file at: hal-stack/context-system/context-index.md for recent session history.
Read SESSION-STATE.md for the most recent session details.
Read NEXT-SPRINT-QUEUE.md for the current backlog.

If these files are not available (you're in a web chat without file access), ask Aaron to paste the relevant sections.

KEY REPOS (all at C:\twobirds\ on local machines):
digital-confidence, career-coach, clarity, aaron-patzalek, two-birds-innovation, two-birds-portfolio, quality-dashboard, two-birds-command-centre

GIT IDENTITY: Aaron Patzalek / aaron.patzalek@gmail.com / twobirds-kramerica

---END CONTEXT---

## Usage Notes

- This prompt works with any LLM. It doesn't use Claude-specific features.
- Update the "CURRENT SESSION STATE" section if file paths change.
- The prompt is intentionally brief — it orients the LLM, then the LLM reads files for details.
- At L4 (no LLM), Aaron reads the context-index.md himself.
