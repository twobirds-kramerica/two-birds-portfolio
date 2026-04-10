<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:10 EST (Toronto)
Confidence: HIGH — this is a documentation system, not a technical build
Known gaps: Claude.ai data export process not verified (L1-dependent)
-->

# Context Bridge System

Persistent context across sessions, tools, and LLMs. Pure markdown — no code, no database, no vendor lock-in.

## Problem

Every new Claude Code session starts cold. Every Claude Web chat is isolated. Aaron's decisions, context, and institutional knowledge scatter across dozens of chats that he can't search, link, or reuse.

## Solution

A markdown-based context system that works at all four sovereignty layers:

| Layer | How It Works |
|-------|-------------|
| **L1** | Claude Code reads `context-index.md` at session start via CLAUDE.md. Instant context injection. |
| **L2** | Any other AI tool (Cursor, Aider, GPT) reads the same index file. Paste `context-loader-prompt.md` into the chat. |
| **L3** | LLM on a VPS reads the index via API. Same markdown format. |
| **L4** | Aaron reads the index himself with a text editor. Pastes relevant context into whatever tool he's using. No AI required. |

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file — how the system works |
| `context-index.md` | Master index of all exported contexts |
| `context-export-template.md` | Template for exporting a session's context |
| `context-loader-prompt.md` | Prompt block to paste into any new LLM chat |
| `retroactive-catchup-plan.md` | Plan for recovering context from past Claude.ai chats |

## How to Use

### After a Claude Code session:
1. Copy `context-export-template.md`
2. Fill in the fields (5 minutes)
3. Save as `exports/YYYY-MM-DD-session-title.md`
4. Add one-line entry to `context-index.md`

### Starting a new session (any LLM):
1. Paste `context-loader-prompt.md` into the chat
2. The LLM reads the index and orients itself
3. Or: Aaron reads the index himself (L4)

### Quarterly maintenance:
1. Archive old exports (older than 3 months) to `exports/archive/`
2. Review index for stale entries
3. Update confidence levels on decisions that have been validated or invalidated
