<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 02:15 EST (Toronto)
Confidence: MEDIUM — model equivalences across vendors are approximate
Known gaps: Local model quality at L4 not benchmarked on Aaron's hardware
-->

# Model Routing

Which personas get which model tier, and why.

## Default Routing

| Role Level | Default Tier | Reasoning |
|-----------|-------------|-----------|
| **Executive** | Opus | Deep reasoning, strategic judgment, nuance. These personas make the highest-stakes calls. |
| **Specialist** | Sonnet | Competent, fast, cost-effective. Good enough for focused domain work. |
| **Front-line** | Haiku or local | Execution, checklists, formatting. Speed over depth. |

## Model Equivalences Across Layers

| Tier | L1 (Anthropic) | L1 alt (OpenAI) | L2 (Google) | L3 (Hosted) | L4 (Local) |
|------|----------------|-----------------|-------------|-------------|------------|
| **Opus** | Claude Opus 4 | GPT-4o | Gemini Pro | Llama 3 70B on VPS | Llama 3 70B local (needs 48GB+ RAM) |
| **Sonnet** | Claude Sonnet 4 | GPT-4o-mini | Gemini Flash | Llama 3 8B on VPS | Llama 3 8B or Phi-3 local (needs 8GB+ RAM) |
| **Haiku** | Claude Haiku | GPT-3.5 | Gemini Nano | Phi-3 mini on VPS | Phi-3 mini local (needs 4GB RAM) |

**L4 reality check:** At L4, all personas run at Sonnet-equivalent max on Aaron's current hardware (12GB EZbook, 8GB i5). Opus-equivalent local models need 48GB+ RAM — the future desktop might handle it, but current machines cannot. This means executives lose nuance at L4 but remain functional.

## Override Rules

### Bump UP (specialist → Opus)
When to override a specialist to Opus-tier:
- The specialist is making a judgment call, not just executing a checklist
- The decision has financial or strategic consequences
- Example: Fatima (Cost Analyst) evaluating whether to switch from Claude Pro to a pay-per-token plan — bump to Opus for this specific analysis

### Bump DOWN (executive → Sonnet)
When to override an executive to Sonnet-tier:
- Speed matters more than depth
- The question is straightforward, not nuanced
- Credit conservation is a concern
- Example: Quick Decision profile — all executives can run at Sonnet for routine approvals

### Force LOCAL (any tier → L4)
When to force any persona to local model:
- Sovereignty drill (testing L4 readiness)
- Sensitive content (personal Aaron context on the L4 machine)
- Credit exhaustion (Claude Pro limit reached)
- Internet outage

## Credit Impact

| Profile | Opus Calls | Sonnet Calls | Haiku Calls | Est. Total Cost |
|---------|-----------|-------------|------------|-----------------|
| Quick Decision | 2 | 1 | 0 | Minimal |
| Full Boardroom | 6 | 10 | 6 | Significant |
| Solo Founder | 0 | 0 | 1 | Negligible |

**Honest note:** These are rough estimates. Actual credit usage depends on prompt length, context window size, and response length. The Claude Pro plan includes substantial usage, but Full Boardroom on every decision would likely hit limits.

## Layer Impact on Quality

| Layer | Executive Quality | Specialist Quality | Front-line Quality |
|-------|------------------|-------------------|-------------------|
| **L1** | Excellent | Good | Adequate |
| **L2** | Very Good | Good | Adequate |
| **L3** | Good | Good | Adequate |
| **L4** | Adequate (limited by hardware) | Adequate | Basic |

At L4, the boardroom still functions but loses the nuance that makes executive-level personas valuable. The framework survives — the quality degrades gracefully.
