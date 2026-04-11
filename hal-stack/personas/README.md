<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 01:57 EST (Toronto)
Confidence: HIGH — architecture is clear, implementation details TBD
Known gaps: Token cost estimates are approximate, multi-LLM coordination untested
-->

# Persona System — HAL Boardroom Operating Model

## What This Is

The persona system turns the HAL Boardroom from "Aaron talks to one AI" into "Aaron leads a senior team that debates, challenges, and produces better decisions." Each department is a full swarm — not one persona but an entire team with executives, specialists, and front-line workers.

## How Personas Differ from Skills

| | Personas | Skills |
|---|---------|--------|
| **What** | Characters with judgment, opinions, and pushback style | Reusable instruction sets — how-to procedures |
| **Why** | Provide perspective, challenge assumptions, protect quality | Ensure consistent execution of known processes |
| **Example** | "VP Engineering says this creates tech debt" | "Run the sovereignty audit checklist on this tool" |
| **Has opinions?** | Yes — and will argue for them | No — follows instructions |
| **Pushes back?** | Yes — that's the point | No — executes what it's told |

Personas USE skills. The VP Engineering persona uses the "sovereignty-audit" skill when evaluating a new tool. But the persona decides WHEN to invoke the skill and HOW to interpret the results.

## The Swarm Model

Each department is a team that debates internally before presenting to Aaron:

```
Department (e.g., Engineering)
├── Executive (VP Engineering) — sets direction, presents to Aaron
├── Specialist (Senior Dev) — deep expertise, informs the executive
├── Specialist (DevOps) — operational perspective
└── Front-line (QA) — catches what everyone else misses
```

At **weight 3** (full swarm), the internal debate is visible — Aaron sees specialists disagreeing with the executive, QA flagging concerns, etc.

At **weight 1** (executive only), Aaron gets one paragraph from the VP summarising the department's position.

At **weight 0** (silent), the department isn't consulted at all.

## Weighting: A Dial, Not a Switch

Every department has a weight from 0 to 3:

| Weight | What Aaron Sees |
|--------|----------------|
| **0** | Nothing. Department not consulted. |
| **1** | Executive summary. One paragraph, top concerns only. |
| **2** | Executive + key specialists. Detailed feedback, dissenting views flagged. |
| **3** | Full team debate. All perspectives visible. Internal disagreements surfaced. |

Aaron sets weights per decision using pre-built profiles (see `profiles.md`) or custom values. The default is profile-dependent.

## Model Routing

Not all personas need the same AI horsepower:

| Role Level | Default Model Tier | Why |
|-----------|-------------------|-----|
| Executive | Opus-tier | Deep reasoning, strategic judgment, nuance |
| Specialist | Sonnet-tier | Competent, fast, cost-effective for focused tasks |
| Front-line | Haiku-tier or local | Execution, formatting, checklists — speed over depth |

See `model-routing.md` for full details and override rules.

## Layer Tags

| Layer | What It Means for Personas |
|-------|--------------------------|
| **L1** | Cloud LLMs (Claude, GPT, Gemini) — full capability |
| **L2** | Alternative commercial LLMs — slightly different perspectives |
| **L3** | Hosted open-source (Llama on VPS) — good but not Opus-quality |
| **L4** | Local LLMs (Ollama) — all personas run at Sonnet-equivalent max. Executives lose nuance but remain functional. |

The persona system is **L1-L4 compatible** by design. Prompts are plain text. No vendor-specific features. At L4, the quality drops but the structure survives.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `persona-schema.md` | Template for defining any persona |
| `culture-spec.md` | Non-negotiable culture every persona inherits |
| `weighting-system.md` | Weight scale and what each level means |
| `profiles.md` | Pre-built configuration profiles |
| `model-routing.md` | Which personas get which model tier |
| `departments/` | One file per department with full team |
