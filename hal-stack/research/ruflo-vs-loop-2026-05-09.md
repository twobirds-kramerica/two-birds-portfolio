# RuFlo vs /loop — Trade-off Decision
**Date:** 2026-05-09 | **Sprint:** S-029-EXTENDED | **Owner:** Aaron to decide

---

## What RuFlo Claims

RuFlo (claude-flow v3, GitHub #1 at time of vetting) is a multi-agent orchestration framework:

| Claim | What it means |
|---|---|
| 60+ specialized agents | Pre-built agents: Researcher, Coder, Analyst, Tester, Architect, Reviewer, Optimizer, Documenter |
| Queen hierarchy | One orchestrator agent coordinates sub-agents and manages task routing |
| 5 consensus protocols (Raft/BFT/Gossip/CRDT) | Agents vote/sync on shared state — designed for distributed reliability |
| WASM Agent Booster 352x faster | JS/WASM runtime for agent loops vs pure Python |
| 170+ orchestration tools | Tool library for agents to call |
| RuVector (PostgreSQL vector) | Long-term memory and semantic search across prior agent outputs |
| 3-tier routing, 75% cost reduction | Routes simple tasks to cheaper models, complex to flagship |
| Install: `npm install -g ruflow` | Single npm global — external dependency |

---

## What /loop + HAL Stack Already Does

Shipped in S-LOOP-001. Currently running overnight via `run-overnight-build.bat`:

| Loop | Job | Frequency |
|---|---|---|
| `loop-pr-babysitter` | CI failures, uncommitted work, stale branches — auto-fix mechanical errors | On-demand / nightly |
| `loop-backlog-health` | Flag cold P1s, stale Ready items, orphaned In Progress | Weekly (Sundays) |
| `loop-content-freshness` | DCC module staleness, brand site lastmod | Weekly (Mondays) |
| `loop-notion-sync-verify` | NOTION_API_KEY canary, SYNC-LOG freshness | Nightly (2 AM) |

Zero external dependencies. Sovereign. Working today.

---

## The Core Question: Do You Have the Problems RuFlo Solves?

**RuFlo is built for:**
- Parallel execution of 5–20 independent agents simultaneously
- Long-running distributed tasks where agents need to agree on shared state (consensus)
- Teams where multiple people need to observe agent coordination in real time
- Organisations that need semantic search across hundreds of prior agent runs (RuVector)
- Cost optimisation at scale — routing 1,000+ monthly tasks across model tiers

**Your current workload:**
- Sequential sprints (one sprint at a time, human in the loop between them)
- 10 repos, mostly static HTML — no backend agents, no concurrent builds
- ~20–30 Notion backlog items — no semantic search pressure
- Monthly Claude Code spend is single-person scale, not $200+/month

**Verdict: You don't have these problems yet.** The 352x speed claim is for agent loop overhead — irrelevant when your bottlenecks are Notion API latency and git pushes. The 75% cost reduction matters at volume you're not at.

---

## Sovereignty Risk

| Factor | RuFlo | /loop |
|---|---|---|
| External dependency | Yes — `npm install -g ruflow`, maintained by third party | No — built into Claude Code |
| Abandonment risk | Real — GitHub #1 today, unknown in 6 months | Zero — Anthropic-maintained |
| Breaking changes | npm major versions can break workflows silently | Claude Code updates are controlled |
| Data leaving machine | Unclear — orchestration layer may phone home | No — all local |
| Setup friction | Meaningful — install, configure, learn Queen hierarchy | Zero — already working |

RuFlo is open-source and free, which reduces some risk. But a solo founder on a revenue deadline cannot afford to debug a broken orchestration layer mid-sprint.

---

## Decision

**Defer RuFlo. Stay with /loop.**

The HAL Stack loop layer is working, sovereign, and zero-maintenance. RuFlo adds complexity that solves problems you don't have at your current scale.

Revisit when **any of these triggers fire:**

| Trigger | Why it changes the calculus |
|---|---|
| Monthly CC spend > $200 | 3-tier routing's 75% savings becomes meaningful |
| Need 5+ genuinely parallel agents | /loop's sequential model becomes the bottleneck |
| DCC reaches 100+ modules needing semantic retrieval | RuVector earns its place |
| Second developer joins | Queen hierarchy makes coordination visible |

---

## What to Do Instead

The gap /loop doesn't fill isn't RuFlo — it's **persistence between sessions**. RuFlo's Queen layer maintains state across runs; our loops currently don't.

The simpler sovereign fix: the `schedule` skill (already installed) creates Anthropic-side scheduled agents that maintain their own context. That closes the persistence gap without the RuFlo dependency.

**Recommended next action:** Schedule one of the backlog-health or freshness loops via `/schedule` instead of the bat file — test persistent context across sessions. Cost: ~$0.10/run. No external deps.

---
*Written: 2026-05-09 | Re-evaluate: when triggers above fire*
