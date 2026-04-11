<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 02:15 EST (Toronto)
Confidence: MEDIUM — weight levels are defined, token cost estimates are rough
Known gaps: Actual token costs per profile depend on prompt length, context size, and model
-->

# Weighting System

How Aaron controls how much he hears from each department.

## Weight Scale

| Weight | Name | What Aaron Sees | Token Cost |
|--------|------|----------------|------------|
| **0** | Silent | Nothing. Department not consulted. | 0 |
| **1** | Executive Brief | One paragraph from the executive. Top concerns only. No specialist detail. | ~500 tokens |
| **2** | Key Team | Executive + relevant specialists. Detailed feedback. Dissenting views flagged. | ~2,000 tokens |
| **3** | Full Swarm | Entire department debates. All perspectives visible. Internal disagreements surfaced. | ~5,000 tokens |

## How Weights Work in Practice

**Weight 0 — Silent:**
The department doesn't exist for this decision. No prompt tokens spent, no output generated. Use for decisions where a department has zero relevance (e.g., Marketing weight 0 for an infrastructure decision).

**Weight 1 — Executive Brief:**
Only the department executive is consulted. They give a one-paragraph opinion with their top concern and recommendation. Think "VP drops by your office for 30 seconds."

**Weight 2 — Key Team:**
The executive consults with key specialists before responding. You see the executive's summary plus flagged concerns from specialists who disagree or see risks. Think "the VP had a meeting with their team and is reporting back."

**Weight 3 — Full Swarm:**
The entire department is visible. You see the executive, specialists, AND front-line workers. Internal debates are surfaced — "the QA lead disagrees with the Senior Dev on this approach." Think "you're sitting in on the department's team meeting."

## How Weights Affect Credits

Rough estimates for a single decision with each profile:

| Profile | Total Tokens (est.) | Opus Calls | Sonnet Calls | Haiku Calls |
|---------|--------------------|-----------:|-------------:|------------:|
| Quick Decision | ~3,000 | 2 | 1 | 0 |
| Brand & Launch | ~15,000 | 3 | 5 | 2 |
| Architecture Decision | ~12,000 | 2 | 5 | 1 |
| Full Boardroom | ~30,000 | 6 | 10 | 6 |
| Solo Founder | ~500 | 0 | 0 | 1 |
| Sovereignty Review | ~18,000 | 4 | 5 | 1 |

**Warning:** Full Boardroom on every decision will burn through credits fast. Reserve it for major strategic decisions. Most daily work should use Quick Decision or Solo Founder.

## How Weights Interact with Model Routing

Weights determine WHICH personas speak. Model routing determines HOW SMART they are.

At weight 1, only the executive speaks — and they use Opus-tier by default.
At weight 3, front-line workers speak too — they use Haiku-tier by default.

Override: Aaron can bump any persona to a higher model tier for a specific decision. "I want Priya (QA) to use Opus for this accessibility review" is a valid override.
