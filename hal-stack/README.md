<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:05 EST (Toronto)
Confidence: HIGH
Known gaps: None
-->

# HAL Stack — Two Birds Innovation

Always-on AI development and automation infrastructure. Local-first, sovereign by design.

## What HAL Is

HAL is the persistent infrastructure layer that makes Two Birds Innovation autonomous. It manages context across sessions, profiles machines, tracks work, and will eventually accept voice commands. Every component is designed to work at all four sovereignty layers (L1-L4).

## Sovereignty Model

| Layer | What | Example |
|-------|------|---------|
| **L1** | Commercial cloud | Claude Code, GitHub |
| **L2** | Alternative commercial | Aider, Codeberg |
| **L3** | Open-source hosted | Whisper on VPS |
| **L4** | Open-source local | Ollama on desktop, plain markdown |

**Rule:** Dropping from L1 to L4 must be a configuration change, not a rebuild.
See `architecture/sovereignty-principles.md` for the full model.

## Current State (April 2026)

| Subsystem | Status | Layer |
|-----------|--------|-------|
| Sovereignty Framework | v0.1 shipped | L1-L4 |
| Context Bridge | v0.1 shipped | L1-L4 |
| Voice Layer | Research complete | L1-L4 target |
| Machine Profile | v0.1 shipped | L4-native |
| Backlog | Consolidated | L4-native |
| n8n Automation | Not started | L3 |
| Prompt Tracking | Schema only | L1-L4 target |

## Directory Structure

```
hal-stack/
├── README.md              ← you are here
├── architecture/          — design docs, ADRs, sovereignty framework
├── context-system/        — cross-session context bridge (markdown-only)
├── voice-layer/           — voice-to-machine research and planning
├── machine-profile/       — hardware registry and self-ID
├── backlog/               — epics, stories, evaluation candidates
├── sessions/              — sprint logs and results
├── n8n/                   — automation workflows
├── prompt-tracking/       — prompt lifecycle tracking
├── scripts/               — utility scripts
└── docs/                  — reference docs (machine specs, ports, services)
```

## Core Principles

1. **Sovereignty** — no vendor lock-in, four-layer escape paths
2. **Low-cost** — stay under CA$50/month total infrastructure
3. **Automation** — if you do it twice, automate it
4. **Voice-ready** — keyboard today, voice tomorrow
5. **Canadian** — data residency, privacy-first
6. **Modular** — every subsystem is separable
7. **Plain language** — no jargon walls
8. **Static output** — HTML/CSS/JS, no frameworks

## Machines

| Machine | Role | Status |
|---------|------|--------|
| EZbook (Win 11) | Active daily driver | Operational |
| i5 Lenovo (Win 10) | Build machine / overnight scheduler | Operational |
| Pentium Silver | Legacy fallback | Operational |
| Home Desktop | Future HAL server | Planned |

## Quick Links

- [Sovereignty Principles](architecture/sovereignty-principles.md)
- [Decapitation Checklist](architecture/decapitation-checklist.md)
- [Architecture Overview](architecture/overview.md)
- [Context Bridge](context-system/README.md)
- [Voice Layer Research](voice-layer/README.md)
- [Machine Registry](machine-profile/README.md)
- [Backlog](backlog/epics.md)
