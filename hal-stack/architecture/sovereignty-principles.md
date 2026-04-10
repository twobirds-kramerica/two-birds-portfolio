<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:03 EST (Toronto)
Confidence: HIGH — derived from Aaron's stated principles across multiple sessions
Known gaps: L4 local LLM performance benchmarks not tested on Aaron's hardware
-->

# Sovereignty Principles — Four-Layer Model

## Why This Exists

Aaron runs a solo consultancy with twin six-year-olds. He is the sole income earner. If any vendor — including Anthropic — changes pricing, kills a free tier, or goes hostile tomorrow morning, Aaron's business cannot stop. Every tool, every workflow, every automation must be designed so that swapping vendors is a configuration change, not a rebuild.

This is not paranoia. This is architecture.

## The Four Layers

| Layer | Name | Description | Cost Profile | Example |
|-------|------|-------------|-------------|---------|
| **L1** | Commercial Fast | Cloud APIs, SaaS tools, proprietary platforms | Paid or free-tier | Claude Code, GitHub, Formspree |
| **L2** | Alternative Commercial | Different vendor, same category, swap-ready | Paid or free-tier | GPT-4, Codeberg, Web3Forms |
| **L3** | Open-Source Hosted | Open-source software on rented infrastructure | VPS cost only | Whisper on DigitalOcean, Gitea on VPS |
| **L4** | Open-Source Local | Runs on Aaron's own hardware, zero external dependencies | Hardware + electricity | Whisper.cpp on i5, Ollama + Llama local |

## Rules

### Non-Negotiable

1. **Every component must have at least an L2 and an L4 identified.** You don't have to build L4 today. You must know what L4 would be.
2. **Data formats must be vendor-neutral.** Markdown, JSON, CSV, SQLite. Never a proprietary format that requires a specific tool to read.
3. **Interfaces must be generic.** "Takes text, returns text" — not "requires Claude's tool_use format."
4. **Decapitation cost must be documented.** For every L1 component, the answer to "how long to drop to L2/L3/L4?" must be written down.

### Allowed

- Using L1 as the daily driver. L1 is fast, cheap, and good. Use it.
- Using proprietary features (Claude's tool_use, GitHub Actions) — as long as the swap path is documented.
- Accepting that L4 will be slower, dumber, or uglier than L1. That's the trade-off.

### Forbidden

- Storing critical data in a format only one vendor can read.
- Building workflows that assume a specific LLM's personality, quirks, or undocumented behaviours.
- Using "it's too hard to switch" as a reason not to document the switch path.
- Treating any vendor relationship as permanent.

## "Headless Claude" — What It Means

Claude is currently the L1 LLM for Two Birds Innovation. "Headless Claude" means:

- Claude is a **swappable backend**. HAL Stack assumes "some LLM that takes text and returns text," never "Claude specifically."
- Prompts are stored as plain markdown. They don't use Claude-specific XML tags or features that wouldn't work with GPT, Gemini, or a local Llama model.
- Context files (SESSION-STATE.md, CLAUDE.md) are human-readable. A human at L4 could read them and do the work manually.
- No workflow depends on Claude's specific output format, personality, or response structure.

This does NOT mean Claude is bad. It means Claude is good **and replaceable** — which is the highest compliment in sovereign architecture.

## Layer Decision Framework

When choosing a component:

1. **Start at L1.** Get it working fast with the best commercial tool.
2. **Document L2 immediately.** What's the 15-minute swap?
3. **Research L3/L4 lazily.** Write it down, don't build it yet.
4. **Test decapitation annually.** Pick one L1 component per quarter, drop it to L2 for a day. See what breaks.

## Relationship to Float-Free Architecture

The Float-Free framework (documented in `sovereignty/`) is the predecessor to this model. Float-Free focused on vendor-specific escape plans. The four-layer model generalises that into a design principle applied to every new component from day one.
