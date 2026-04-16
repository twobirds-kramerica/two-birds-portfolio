# Agent Wrappers — How Personas Execute

**Version:** 1.0 | **Created:** 2026-04-16

---

## What Personas Are Today (Phase 1)

Personas are **prompts with defined scope**, not autonomous agents. Each review happens as a focused Claude invocation with:

1. **Persona system prompt** — loaded from the persona's markdown file (Personality, Pushback Style, What They Protect/Challenge)
2. **Sprint output to review** — the files created or modified during the sprint
3. **DoD criteria for the stage** — from `definition-of-done.md`
4. **Token budget** — maximum 500 tokens per review

### Invocation Pattern

```
System prompt: You are [Name], [Title] at Two Birds Innovation.
[Paste persona's Personality, Pushback Style, What You Protect, What You Challenge sections]

Your task: Review the following sprint output against these criteria:
[Paste DoD checklist for the current stage]

Sprint output:
[Paste changed files or summary]

Respond with:
- APPROVED, REWORK, or ABSTAIN
- 1-3 sentences of specific feedback
- Maximum 500 tokens
```

### Cost Per Review

| Panel Size | Opus Calls | Sonnet Calls | Haiku Calls | Est. Tokens |
|-----------|-----------|-------------|------------|-------------|
| Minimal (Drew + Scrappy Pack) | 1 | 5 | 0 | ~3,000 |
| Standard (5-6 reviewers + Scrappy Pack) | 1-2 | 8-9 | 1-2 | ~6,000 |
| Full (8-10 reviewers + Scrappy Pack) | 2-3 | 10-12 | 2-3 | ~10,000 |

**Cost is low.** A full panel review costs roughly the same as one @Full Boardroom invocation. Most sprints use Standard or Minimal panels.

---

## Model Routing for Reviews

| Reviewer Role | Model Tier | Why |
|--------------|-----------|-----|
| Drew (Program Director) | Opus | Synthesis judgment, verdict authority |
| Department Executives (Ava, Helen, Raj, etc.) | Opus | Strategic judgment needed |
| Specialists (Sam, Theo, Maya, Anil, etc.) | Sonnet | Domain expertise, fast turnaround |
| Front-line (Priya, Kai, Dani, Lin, etc.) | Haiku | Checklist execution, specific checks |
| Scrappy Pack (all 5) | Sonnet | Quick gut checks |

---

## What Personas Could Become (Phase 2 — Post-30-Day Validation)

After 30 days of using the prompt-based system, evaluate converting key personas to real agents with tool access:

### Candidates for Agent Upgrade

| Persona | Why | Tools Needed |
|---------|-----|-------------|
| **Priya (QA)** | Could run axe-core, check links, validate HTML automatically | File read, shell commands (Lighthouse, axe-core) |
| **Theo (Brand)** | Could grep for off-brand colours, check font usage, verify tone | File read, grep |
| **Drew (Program Director)** | Could auto-generate sprint briefs from intake answers, auto-select panels | File read/write, git log |
| **Casey (Knowledge Manager)** | Could auto-generate context exports, check for stale entries | File read/write |
| **Riley (Parking Lot)** | Could auto-capture ideas from conversation and append to backlog | File write |

### Requirements for Phase 2

1. Claude Code Agent SDK or MCP tool access
2. Sandboxed execution (agents can read/grep but not push to git without approval)
3. 30 days of prompt-based review data to validate panel compositions
4. Aaron's explicit approval to upgrade each persona

### What NOT to Automate

- **The Hand's synthesis** — requires full-context reasoning, not a checklist
- **Love Balance Advisor** — human judgment about Aaron's wellbeing
- **Scrappy Pack** — the value is divergent thinking, not deterministic checks
- **Any persona's override of Aaron** — personas advise, Aaron decides

---

## Integration with Sprint Workflow

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│ Aaron says   │────→│ Drew intake  │────→│ Claude Code  │
│ "next sprint"│     │ (Opus, ~500t)│     │ executes     │
└─────────────┘     └──────────────┘     └──────┬──────┘
                                                  │
                                          ┌───────▼───────┐
                                          │ Panel review   │
                                          │ (5-10 calls,   │
                                          │  ~6K tokens)   │
                                          └───────┬───────┘
                                                  │
                                          ┌───────▼───────┐
                                          │ Drew verdict   │
                                          │ APPROVED/REWORK│
                                          └───────┬───────┘
                                                  │
                                          ┌───────▼───────┐
                                          │ Aaron ships    │
                                          │ or accepts fix │
                                          └───────────────┘
```

The entire review pipeline costs ~6K-10K tokens. At current Claude Pro pricing, this is negligible — less than one conversation turn at @Full Boardroom.
