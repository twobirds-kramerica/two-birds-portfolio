<!--
STATUS: v1.0 — LIVING DOCUMENT
Created: 2026-04-15 01:25 EST (Toronto)
Confidence: HIGH
-->

# Persona System — Usage Guide

How to use the Two Birds Innovation boardroom personas in practice.

---

## Quick Start

### Invoke a profile by name

Say one of these to activate a pre-built configuration:

| Command | What It Does | Token Cost |
|---------|-------------|------------|
| `@Quick Decision` | Naveen + Claire + Raj + Val/Drew. Fast call. | ~3,000 |
| `@Brand & Launch` | Full Marketing, heavy Strategy + Legal. For public-facing work. | ~15,000 |
| `@Architecture Decision` | Full Engineering, heavy Strategy + Finance. For tech decisions. | ~12,000 |
| `@Full Boardroom` | All departments at full swarm. Maximum perspectives. | ~30,000 |
| `@Solo Founder` | Just Val (Chief of Staff). Minimal, for creative thinking. | ~500 |
| `@Sovereignty Review` | Full Engineering + Legal, heavy Finance. For vendor/tool evaluation. | ~18,000 |
| `@Scrappy Pack` | Advisory layer only — 5 founder-archetype personas. | ~5,000 |

### Response format

Each persona speaks briefly. The Hand synthesizes. Love Balance flags if relevant.

**Department response (Weight 1-3):**
```
**[Name] ([Title]):** [1-3 sentences — their take]
```

**The Hand (always last):**
```
**THE HAND — SYNTHESIS**
**Decision needed:** [one sentence]
**Departments agree on:** [bullets]
**Departments disagree on:** [bullets with attribution]
**Trade-offs:** [what you gain/lose]
**Recommendation:** [one clear action]
**Confidence:** [HIGH / MEDIUM / LOW] — [why]
```

**Love Balance Advisor (only when flagged):**
```
**LOVE BALANCE CHECK**
**Flag:** [what triggered this]
**Current load estimate:** [light / moderate / heavy / red zone]
**Impact if unchanged:** [what suffers]
**Suggestion:** [what to defer, cut, or delegate]
```

---

## How to Expand a Specific Department

To see all 4 personas in a department, set its weight to 3. Example for Engineering:

**Step 1:** Set weights — `Engineering: 3, Marketing: 0, Strategy: 1, Legal: 0, Finance: 1, Ops: 1`

**Step 2:** Engineering responds with all 4 personas:

```
**Naveen (VP Engineering, Opus):**
[Strategic view — architecture, feasibility, risk]

**Sam (Senior Developer, Sonnet):**
[Implementation view — how to build it, what's hard, what's simple]

**Jordan (DevOps / Infrastructure, Sonnet):**
[Ops view — deployment, monitoring, sovereignty, hosting]

**Priya (QA / Testing, Haiku):**
[Quality view — what could break, how to test, accessibility]
```

**Step 3:** The Hand synthesizes across all responding departments.

This pattern works identically for any department. Set weight to 3, get all 4 voices.

---

## How to Invoke Scrappy Pack Alone

The Scrappy Pack operates outside the department structure. Invoke it for founder gut checks.

**Command:** `@Scrappy Pack` followed by your question.

**Response format:**
```
**SCRAPPY PACK CHECK**

**Mack (Cash):** [1-2 sentences — does this make money?]
**Tess (Visibility):** [1-2 sentences — does anyone see this?]
**Grit (Time):** [1-2 sentences — do you have time for this?]
**Patch (Simplicity):** [1-2 sentences — is this overbuilt?]
**Sage (Long game):** [1-2 sentences — will this matter in 6 months?]

**THE HAND — SYNTHESIS:** [recommendation]
**LOVE BALANCE:** [flag or "No flag."]
```

**When to use instead of departments:**
- "Should I even be doing this?" questions
- Prioritisation decisions between competing projects
- Reality checks on ambitious plans
- When the boardroom feels too formal for the problem

---

## How to Run a Solo Founder Decision

For quick decisions where you want minimal overhead — just Inner Circle.

**Command:** `@Solo Founder` followed by your question.

**What happens:**
- Only Val (Chief of Staff) responds from the departments
- The Hand still synthesizes (but with minimal input)
- Love Balance Advisor still monitors

**Response format:**
```
**Val (Chief of Staff):** [brief operational view]

**THE HAND — SYNTHESIS:**
**Recommendation:** [one sentence]
**Confidence:** [level]

**LOVE BALANCE:** [flag or "No flag."]
```

**When to use:**
- Creative brainstorming you don't want scrutinised yet
- Personal reflection on business direction
- Quick "yes or no" calls that don't need 31 opinions
- When you're tired and need one clear voice, not a boardroom

---

## How Model Routing Works

Each persona has a default model tier based on their role level:

| Role Level | Default Model | Why |
|------------|--------------|-----|
| **Executive** (6 dept + 2 Inner Circle) | **Opus** | Deep reasoning, strategic judgment, nuance. Highest-stakes decisions. |
| **Specialist** (12 dept + 5 Scrappy Pack) | **Sonnet** | Competent, fast, cost-effective. Focused domain expertise. |
| **Front-line** (6 dept) | **Haiku or local** | Execution, checklists, formatting. Speed over depth. |

### Override rules

**Bump UP** (specialist to Opus):
- The specialist is making a judgment call, not executing a checklist
- The decision has financial or strategic consequences
- Example: "I want Fatima (Cost Analyst) to use Opus for this pricing analysis"

**Bump DOWN** (executive to Sonnet):
- Speed matters more than depth
- The question is straightforward
- Credit conservation is a concern
- Example: Quick Decision profile — executives can run at Sonnet for routine calls

**Force LOCAL** (any tier to L4):
- Sovereignty drill
- Sensitive personal content
- Credit exhaustion
- Internet outage

### At L4 (local models)

All personas function at L4 but with reduced quality:
- Executives lose nuance (Opus-equivalent needs 48GB+ RAM, Aaron has 12GB max)
- Specialists work adequately (Sonnet-equivalent fits in 8GB)
- Front-line works fine (Haiku-equivalent fits in 4GB)

The framework survives at L4. Quality degrades gracefully.

### Credit impact by profile

| Profile | Opus Calls | Sonnet Calls | Haiku Calls |
|---------|-----------|-------------|------------|
| Quick Decision | 2 | 1 | 0 |
| Brand & Launch | 3 | 5 | 2 |
| Architecture Decision | 2 | 5 | 1 |
| Full Boardroom | 6 | 10 | 6 |
| Solo Founder | 0 | 0 | 1 |
| Sovereignty Review | 4 | 5 | 1 |
| Scrappy Pack | 0 | 5 | 0 |

**Rule of thumb:** Quick Decision and Solo Founder for daily use. Full Boardroom for major decisions only. Scrappy Pack when you need a founder gut check.

---

## Custom Profiles

Create your own by setting six numbers:

```
Engineering: [0-3], Marketing: [0-3], Strategy: [0-3], Legal: [0-3], Finance: [0-3], Ops: [0-3]
```

Example: `Engineering: 2, Marketing: 0, Strategy: 3, Legal: 1, Finance: 2, Ops: 0`

Name it and reuse it. The system is just six numbers plus an optional Scrappy Pack toggle.

---

## File Map

| File | What It Contains |
|------|-----------------|
| `master-index.md` | Complete roster — all 31 personas with roles and model tiers |
| `inner-circle.md` | The Hand + Love Balance Advisor |
| `advisory/scrappy-pack.md` | 5 Scrappy Pack sub-personas |
| `departments/engineering.md` | Naveen, Sam, Jordan, Priya |
| `departments/marketing.md` | Ava, Theo, Maya, Kai |
| `departments/strategy.md` | Claire, Ethan, Rosa, Leo |
| `departments/legal-risk.md` | Helen, Anil, Nora, Dani |
| `departments/finance.md` | Raj, Fatima, Marcus, Lin |
| `departments/operations-ea.md` | Val, Drew, Casey, Riley |
| `profiles.md` | 6 pre-built weighting profiles |
| `weighting-system.md` | How weights 0-3 work |
| `model-routing.md` | Opus/Sonnet/Haiku routing rules |
| `culture-spec.md` | Non-negotiable behaviour rules all personas inherit |
| `persona-schema.md` | Template for creating new personas |
