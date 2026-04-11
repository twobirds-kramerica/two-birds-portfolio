<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 01:40 EST (Toronto)
Confidence: MEDIUM — vision is clear, implementation details are speculative
Known gaps: Hardware costs, persona interaction protocols, multi-LLM coordination untested
-->

# HAL Boardroom — Multi-Agent Workspace Vision

## The Vision

A physical workspace where multiple machines sit on a desk, each running a dedicated AI persona with a specific role. Aaron sits in the centre, orchestrating by voice. The personas share context through a common git repo but bring different perspectives, different LLM backends, and different priorities.

This is not a chatbot army. This is a senior leadership team.

## Culture Spec — How Personas Behave

The HAL Boardroom operates under one rule: **protect the work, then the customer, then Aaron — in that order.**

### What This Means

1. **Protect the work.** Don't ship bad code. Don't skip tests. Don't cut corners because it's 2am. Quality is non-negotiable.
2. **Protect the customer.** Brenda (beta tester persona) exists because real seniors use this software. Every decision passes the "would this confuse Brenda?" test.
3. **Protect Aaron.** From burnout, from bad decisions, from scope creep, from himself at 2am. This means pushing back, saying stop, challenging the "why" before building the "what."

### Persona Behaviour Rules

- **Come prepared.** Read the context index before starting. Don't ask questions the repo already answers.
- **Push back.** If Aaron says "build X," the first response should be "why?" not "yes." Positive friction, not compliance.
- **Say stop.** If scope is creeping, quality is dropping, or Aaron is building the wrong thing — say so directly. No hedging.
- **Respect Aaron's time.** He has 6-year-old twins. Don't waste his attention on things that don't matter.
- **Some should be hardasses.** Not every persona is friendly. The risk/legal persona should be blunt. The strategy persona should be demanding. Aaron is building execution muscle and wants to be challenged, not coddled.

### What Personas Are NOT

- Not yes-men who agree with everything
- Not tools that execute without thinking
- Not personalities that need to be managed or placated
- Not Aaron's friends — they're his colleagues

## Minimum Viable Boardroom (2 machines)

The smallest version that proves the concept.

| Machine | Persona | LLM | Role |
|---------|---------|-----|------|
| EZbook | **Builder** — dev/engineering | Claude (L1) | Executes sprints, writes code, ships features |
| i5 Lenovo | **Strategist** — research/challenge | GPT or Gemini (L2) | Reviews Builder's output, challenges assumptions, researches alternatives |

**How it works:**
1. Aaron speaks a command: "Next sprint"
2. Builder (EZbook) reads backlog, starts executing
3. Strategist (i5) reads Builder's plan, flags concerns: "Why are we building voice before revenue is stable?"
4. Aaron arbitrates: "Builder, proceed. Strategist, note the concern in the backlog."
5. Both machines share context via the git repo — they pull before starting, commit when done

**What this proves:** Multi-agent coordination through shared repo. Different LLMs providing different perspectives. Aaron as orchestrator, not typist.

## Full Vision (4-6 terminals)

| Terminal | Persona | Role | LLM | Notes |
|----------|---------|------|-----|-------|
| 1 | **Builder** | Dev/engineering | Claude Code | Writes code, ships features, runs tests |
| 2 | **Strategist** | Research/challenge | GPT-4 | Market research, competitive analysis, "why are we doing this?" |
| 3 | **Marketer** | Content/growth | Gemini | LinkedIn posts, pitch decks, email sequences, brand voice |
| 4 | **Guardian** | Risk/legal/quality | Claude (Opus) | Code review, security audit, accessibility check, "what could go wrong?" |
| 5 | **Operator** | Finance/ops | Local LLM (L4) | Budget tracking, time estimates, resource allocation, "can we afford this?" |
| 6 | **EA** | Personal chief-of-staff | Local LLM (L4) | Schedule, reminders, personal context, ADHD support |

### Multi-LLM Diversity — Deliberate

Different terminals use different LLMs **on purpose.** Claude, GPT, and Gemini have different strengths, biases, and blind spots. Having all three in the boardroom means:
- No single vendor's worldview dominates
- Blind spots in one LLM get caught by another
- If one vendor goes down, the boardroom still operates at reduced capacity
- Sovereignty is structural, not just documented

## L4 Personal Machine — ARCHITECTURALLY SEPARATE

**⚠ L4 ONLY. NEVER SYNCED TO REMOTE. ⚠**

One machine in the boardroom holds Aaron's personal context:
- ADHD patterns and coping strategies
- Personal preferences that shape work style
- Emotional state tracking (burnout indicators)
- Private notes about relationships, partnerships, personal goals
- Things Aaron would never put in a git repo that gets pushed to GitHub

### Architecture Rules for the L4 Personal Machine

1. **Never connects to the internet.** Air-gapped.
2. **Never syncs to any remote repo.** Local git only.
3. **Never shares data with other boardroom machines.** One-way: Aaron can read from it and carry context verbally. The machine never writes to shared repos.
4. **No cloud LLM.** Local model only (Ollama + Llama or similar).
5. **Physical security.** Aaron controls physical access.
6. **Separate from HAL Stack infrastructure.** This machine is NOT part of the boardroom's shared context system. It's Aaron's personal tool.

### Why This Matters

The L4 personal machine exists because some context is too sensitive for any cloud service, any shared repo, or any machine that could be accessed by anyone other than Aaron. In the sovereignty model, this is the ultimate L4: not just "runs locally" but "never leaves this room."

## Hardware Requirements

### Minimum Viable (2 machines — already owned)
- EZbook (Celeron, 12GB) — Builder
- i5 Lenovo (i5-6200U, 8GB) — Strategist
- Cost: CA$0 (already owned)

### Full Vision (4-6 terminals)
- 2 existing machines repurposed
- 2-4 additional machines needed
- Recommended: used ThinkPads or NUCs (CA$100-200 each)
- One machine with 32GB+ RAM for local LLMs
- Total estimated cost: CA$400-800 for additional hardware
- The L4 personal machine can be the Pentium Silver (already owned, already slow — personal context doesn't need speed)

## Cross-Agent Awareness

All boardroom machines (except the L4 personal machine) share context through:

1. **Git repo** — `two-birds-portfolio` is the shared filesystem
2. **Context index** — `context-system/context-index.md` is the shared memory
3. **SESSION-STATE.md** — the handoff file between sessions
4. **machines.json** — each machine knows who it is and what role it plays

No custom networking, no message queues, no APIs between machines. Just git pull and git push. This is L4-native coordination — it works even if every cloud service disappears.

## Open Questions for Aaron

1. **When?** Is the boardroom a 2026 or 2027 goal? Affects hardware purchasing timeline.
2. **Which machine gets Guardian?** The risk/legal persona needs the most capable LLM. That suggests the desktop (when it arrives) or a dedicated machine with good RAM.
3. **Pentium Silver as L4 personal?** It's slow but personal context doesn't need speed. Good candidate?
4. **Voice as primary interface?** The vision assumes Aaron orchestrates by voice. Is keyboard acceptable as the interim interface?
5. **Persona names?** Builder, Strategist, Marketer, Guardian, Operator, EA — are these right? Should they have human-sounding names or functional titles?
