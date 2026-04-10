<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:05 EST (Toronto)
Confidence: HIGH — synthesised from existing ARCHITECTURE.md and session history
Known gaps: Port assignments for future services not confirmed
-->

# HAL Stack — Architecture Overview

## What HAL Is

HAL (Home Automation & Learning) is the persistent infrastructure layer that makes Two Birds Innovation autonomous. It runs across Aaron's machines — currently the EZbook laptop and i5 Lenovo — as a distributed local-first system.

**Layer:** L1-L4 target. Individual components vary.

## Architecture Principles

1. **Sovereignty first** — every component swappable (see `sovereignty-principles.md`)
2. **Markdown is the database** — human-readable, git-versioned, works at L4
3. **Static output only** — no runtime servers required for products
4. **Modular** — each subsystem works independently
5. **Voice-ready** — designed for eventual voice-to-machine interface

## Current System Map

```
INPUTS
  Aaron (EZbook / i5 / phone) → Claude Code CLI (L1)
  Claude Web (claude.ai) → research + prompt drafting (L1)
  Windows Task Scheduler → overnight builds (L4-native)

PROCESSING
  Claude Code CLI → edits repos → git push (L1)
  SESSION-STATE.md → cross-session handoff (L4-native)
  CLAUDE.md → per-repo context injection (L4-native)

OUTPUTS
  GitHub Pages → live products (L1, L2=Cloudflare Pages)
  Formspree → form submissions (L1, L2=Web3Forms)
  Git repos → all work product (L4-native, portable)
```

## Subsystems

| Subsystem | Status | Layer | Directory |
|-----------|--------|-------|-----------|
| Sovereignty Framework | v0.1 shipped | L1-L4 | `architecture/` |
| Context Bridge | v0.1 shipped | L1-L4 | `context-system/` |
| Voice Layer | Research only | L1-L4 target | `voice-layer/` |
| Machine Profile | v0.1 shipped | L4-native | `machine-profile/` |
| Backlog | Consolidated | L4-native | `backlog/` |
| n8n Automation | Not started | L3 | `n8n/` |
| Prompt Tracking | Schema only | L1-L4 target | `prompt-tracking/` |

## Data Flow

All critical data flows through git-versioned markdown files:

```
SESSION-STATE.md ← session results
     ↓
NEXT-SPRINT-QUEUE.md ← prioritised work
     ↓
Claude Code (or any tool) ← executes work
     ↓
Git repos ← work product
     ↓
GitHub Pages (or any host) ← published output
```

This pipeline works identically at L4 (Aaron editing files manually) and L1 (Claude Code doing it).
