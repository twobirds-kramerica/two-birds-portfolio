# Skills Inventory with Evidence

Each skill assessed honestly against what the repo history proves.

---

## 1. AI Product Evaluation and Critical Testing

**Level:** Strong
**Evidence:**
- Evaluated and rejected WisprFlow against sovereignty principles (S21 capture, confirmed in Claude.ai export conversation #111, Apr 8). Decision documented with reasoning: fails closed-source, paid, and non-modular criteria.
- Evaluated 6 tools in `hal-stack/backlog/evaluation-candidates.md` (notebooklm-py, Aider, Ollama, Remotion, Banana Claude, Marketing Skills). Each assessed for sovereignty compatibility, cost, and fit.
- Built `tools/job-fit-assessment.html` using Anthropic API with deliberate model selection (Haiku 4.5 for cost, not Opus for quality-signalling).
- Identified that "faceless brand plan" didn't exist as a document through systematic search of 115 Claude.ai conversations (Session 16). This is investigative product evaluation work.
- Cross-platform evaluation: used Claude, GPT, and Gemini across the same projects, comparing capabilities and importing personas between platforms (confirmed in Claude.ai export, project "Aaron Persona import ChatGPT and Gemini April 2026").

**Can claim on CV:** "Evaluated 6+ AI tools against a structured sovereignty framework. Built evaluation criteria, documented trade-offs, made go/no-go recommendations with reasoning."
**Cannot yet claim:** Paid evaluation work for a client. Published evaluation methodology.

---

## 2. Non-Developer Infrastructure Building

**Level:** Strong
**Evidence:**
- Built the HAL Stack from scratch: sovereignty framework, persona system (22 personas across 6 departments), sprint automation, context bridge, pending-capture system. All in markdown and vanilla JS. Zero npm dependencies for infrastructure.
- `command-matcher.js` -- pure JavaScript fuzzy matcher, no dependencies, 10/10 tests pass (Session S-001).
- `check-freshness.js` -- content staleness scanner, scanned 252 DCC files, no dependencies (Session S-003).
- Sprint queue system with 8 ready-to-paste prompts, human backlog, retro system, capture system. All markdown-based, L4-compatible.
- 180+ commits in the portfolio repo since March 25, 2026.

**Can claim on CV:** "Designed and built a complete project management and automation infrastructure using markdown, JSON, and vanilla JavaScript. No frameworks, no build tools, no dependencies."
**Cannot yet claim:** Infrastructure used by anyone other than Aaron. Production-scale system.

---

## 3. Product Management and Delivery (Prior Experience)

**Level:** Rare (20+ years)
**Evidence:**
- Career history documented in Claude.ai export: TELUS, Start.ca, Staples Canada, Goodwill Canada. Confirmed in conversation #5 (Jan 13, Professional DNA analysis).
- Product scoring methodology applied in conversation #83 (Mar 26): structured evaluation of 5+ products using defined criteria.
- Shipped 7 digital products in 90 days (DCC, Career Coach, Clarity, Aaron Patzalek, Two Birds Innovation, Kevin's Apartment, Quality Dashboard). All live on GitHub Pages.

**Can claim on CV:** "20+ years leading digital product delivery across telecom, retail, ecommerce, and non-profit. Shipped 7 products as solo founder in 90 days."
**Cannot yet claim:** Nothing. This is Aaron's strongest documented skill.

---

## 4. Multi-Industry Experience

**Level:** Rare
**Evidence:**
- TELUS (telecom), Start.ca (ISP), Staples Canada (retail/ecommerce), Goodwill Canada (non-profit). Confirmed in professional DNA analysis (conversation #5).
- Now: digital literacy for seniors (DCC), consulting for SMEs (Clarity), civic tool (Kevin's Apartment).

**Can claim on CV:** "Led product and operations teams across telecom, retail, ecommerce, non-profit, and now AI consulting."
**Cannot yet claim:** Nothing. The breadth is the asset.

---

## 5. Sovereignty Thinking and Vendor Risk Assessment

**Level:** Strong
**Evidence:**
- Four-layer sovereignty model (L1-L4) designed and documented in Session 12.
- Full decapitation audit of 12 components (Session 15): Claude Code, Claude.ai, GitHub, Pages, Formspree, Cloudflare, Whisper, context bridge, personas, Node, PowerShell, Windows.
- "Headless Claude" concept coined and documented.
- Brand-level sovereignty definition imported from Gemini research (Session 20): "Sovereignty = building tools that empower the user to act for themselves."
- WisprFlow rejection is a practical example of the framework in action.

**Can claim on CV:** "Designed a four-layer vendor sovereignty framework and applied it to audit all business-critical components. Documented fallback paths for every dependency."
**Cannot yet claim:** Framework adopted by external organisations.

---

## 6. Cross-LLM Persona Design and Prompt Engineering

**Level:** Strong
**Evidence:**
- 22 personas across 6 departments with defined pushback styles, model routing, and weighting system (Session 15).
- Culture spec with non-negotiable rules: protect work > customer > Aaron.
- Context loader prompt designed to work with any LLM (Claude, GPT, Gemini, local Llama). Tested in Claude Code; designed for L4.
- Sprint prompts written for 8+ autonomous sprints, each producing working output.
- Persona import across Claude, ChatGPT, and Gemini (confirmed in export project).

**Can claim on CV:** "Designed multi-agent persona systems with structured prompts, model routing, and weighting. Prompts are vendor-agnostic by design."
**Cannot yet claim:** Published prompt engineering methodology. Client-facing persona work.

---

## 7. Solo Founder Execution

**Level:** Working (early stage)
**Evidence:**
- Founded Two Birds Innovation early 2026.
- DCC: 29 modules, bilingual EN/FR, WCAG AA, 252+ HTML pages. Live site.
- Career Coach: AI job application tool with LLM portability layer. Live site. Score improved 31 to 41/60.
- Clarity: AI business diagnostic. Live site.
- Revenue target CA$10,000/month by August 2026. Current MRR: $0.
- Branding: logo designed (V05 selected), DCC logo (V07), brand guidelines, sovereignty philosophy documented.

**Can claim on CV:** "Founded an AI consultancy and shipped 7 products in 90 days as a solo founder with no external funding."
**Cannot yet claim:** Revenue. Paying clients. Product-market fit validated beyond beta testers.

---

## 8. Technical Communication for Non-Technical Audiences

**Level:** Strong
**Evidence:**
- DCC is literally a digital literacy programme for seniors who are afraid of technology.
- "Brenda" persona: 74-year-old, alone, terrified of her iPad. Used as the design test for every module.
- Trust-first design: Module 1 teaches the escape hatch before anything else.
- Brand guidelines use plain language. Culture spec mandates: "No corporate jargon."
- Journey archive chapters 1-3 written in accessible, magazine-feature style.

**Can claim on CV:** "Built a 29-module digital literacy programme for seniors with anxiety-first design. Every interface decision tested against a real user persona."
**Cannot yet claim:** Formal technical writing publications.

---

## 9. System Debugging and Root Cause Analysis

**Level:** Working
**Evidence:**
- Identified Brenda's empty Formspree submission root cause (Session 11): traced to setup-wizard.js calling Formspree from onboarding flow. Fixed by removing the call entirely.
- Found `novalidate` bug on beta-survey.html that disabled HTML5 validation with no JS compensation (Session 11).
- Recovered "faceless brand plan" mystery: determined through 115-conversation scan that it was never a document, just a values thread (Session 16).
- Journey archive rediscovery (Session 21 chat): noticed the journey/ directory existed but hadn't been updated in 10 days.
- Web3Forms key investigation: correctly identified it as a public identifier, not a secret (Session 11).

**Can claim on CV:** "Debugged production form submissions, traced data flow across frontend JavaScript, and conducted systematic root cause analysis across 115 archived conversations."
**Cannot yet claim:** Formal incident response experience. On-call or SRE-type debugging.
