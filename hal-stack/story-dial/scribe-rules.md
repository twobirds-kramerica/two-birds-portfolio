# Scribe Rules — Story Dial
**Version:** 1.0 | **Established:** 2026-05-18 | **Applies to:** All Agency Log entries, past and future

---

## Rule 1 — Honest, Humble, Defensible

Every numerical claim, revenue figure, timeline, or outcome must be:

**Qualified if it's a projection:**
> "an optimistic projection of $479K" (not "$479K Year 1 projections" presented as fact)
> "if the plan had hit targets, Year 1 could have reached $479K — we hadn't tested a single assumption"
> "a what-if: what if this had worked and we hit $479K in Year 1?"

**Attributed to a source if it's a result:**
> "DCC has X modules, verified in the Notion Research DB" (receipt exists)
> "The CI fix shipped same night — commit 5650be6" (commit hash is the receipt)

**Language to qualify projections:**
- "optimistic projection"
- "projected outcome"
- "if targets were met"
- "the forecast at the time"
- "what if we'd hit..."
- "early estimate" / "pre-validation number"

**Language that is banned (no receipts):**
- Presenting a projection as an outcome
- Revenue or growth numbers without "projected" / "estimated" / "forecast"
- "This led to X" where X is inferred, not evidenced
- Corporate superlatives: "groundbreaking," "revolutionary," "industry-leading"

---

## Rule 2 — Keep Receipts

Every claim in a story must trace to observable, verifiable evidence:

| Claim type | Required receipt |
|-----------|-----------------|
| Something shipped | Git commit hash or Notion item ID |
| A decision was made | SESSION-STATE entry or Notion backlog item |
| A number was used | Source document, tool output, or "estimated at the time" qualifier |
| Something was discovered | The specific commit, log entry, or sprint it surfaced in |
| A persona or tool was built | File path in the repo |

**Receipt format in the Raw Story section:**
> "Built the three SME Reviewers (commit e99486a, 2026-05-16) — Vera for privacy, Dr. Lena for child development, Frank for senior accessibility."

**Applying to existing entries:**

| Entry | Issue | Fix applied |
|-------|-------|------------|
| #003 The $479K Question | $479K presented as projection-fact | Reframed as "optimistic, untested Year 1 projection" |
| #004 The 2 AM Discovery | CI fix and /loop automation — receipts exist (commits) | Confirmed clean |
| #005 The Three Reviewers | Content verified against commit e99486a | Confirmed clean |

---

## Tone Guardrails

These rules apply to ALL dial settings, including Dial 1 (big bang):

- A big attention-grabbing headline is fine. A misleading one is not.
- "I built an AI boardroom" ← accurate, defensible, hooky
- "I automated $479K in revenue" ← banned (no receipt, not an outcome)
- "What if your AI builder projected $479K before asking a single customer?" ← allowed (framed as question/what-if)

The goal is storytelling that stands up to "wait, is that true?" from a discerning reader.
The standard: **based on a true story, with receipts available on request.**
