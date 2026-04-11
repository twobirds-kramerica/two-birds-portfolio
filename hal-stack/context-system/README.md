<!--
STATUS: v0.2 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:10 EST (Toronto)
Updated: 2026-04-11 01:30 EST (Toronto)
Confidence: HIGH
Known gaps: Claude.ai data export format unknown
-->

# Context Bridge System

Persistent context across sessions, tools, and LLMs. Pure markdown. Zero human overhead.

## Problem

Every new session starts cold. Aaron's decisions, context, and knowledge scatter across dozens of chats that can't be searched, linked, or reused.

## Solution

Automated context export at the end of every sprint. Aaron's only job: glance, correct, confirm. 30 seconds max.

## How It Works at Each Layer

| Layer | Export Workflow | Load Workflow |
|-------|---------------|---------------|
| **L1 (Claude Code)** | Auto-generated as part of SESSION-STATE.md update. Claude Code writes the export. Aaron glances and confirms. | Claude Code reads `context-index.md` at session start via CLAUDE.md. |
| **L1 (Claude Web)** | Aaron pastes "Archive this session" prompt. LLM generates export. Aaron copies result to repo. | Paste `context-loader-prompt.md` into chat. |
| **L2 (GPT/Gemini/other)** | Same "Archive this session" prompt works with any LLM. | Paste `context-loader-prompt.md` into chat. |
| **L4 (Manual)** | Aaron fills out template by hand (5 min). Fallback only. | Aaron reads `context-index.md` himself. |

## Key Principle

**Aaron does NOT fill out templates.** The AI generates the export. Aaron reviews it. If the AI is unavailable (L4), Aaron fills the template manually — but this is the exception, not the workflow.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `context-index.md` | Master index of all exported contexts |
| `context-export-template.md` | Template + auto-generation prompt |
| `claude-code-auto-export.md` | Copy-paste block for sprint prompts |
| `context-loader-prompt.md` | Universal LLM handoff prompt |
| `retroactive-catchup-plan.md` | Claude.ai history recovery plan |
| `ingestion/` | Infrastructure for Claude.ai data export processing |

## Workflow: After a Claude Code Sprint

1. Sprint prompt includes auto-export instruction (from `claude-code-auto-export.md`)
2. Claude Code generates context export as part of SESSION-STATE.md update
3. Export saved as `exports/YYYY-MM-DD-session-title.md`
4. One-line entry added to `context-index.md`
5. Aaron's effort: **zero** (unless correction needed — 30 seconds)

## Workflow: After a Claude Web Chat

1. Aaron pastes the "Archive this session" prompt from `context-export-template.md`
2. LLM generates the export in markdown
3. Aaron copies to repo (or emails to himself for later commit)
4. Aaron's effort: **~60 seconds** (paste prompt, copy output)

## Quarterly Maintenance

1. Archive old exports (older than 3 months) to `exports/archive/`
2. Review index for stale entries
3. Update confidence levels on decisions validated or invalidated
