<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:30 EST (Toronto)
Confidence: MEDIUM — stories derived from epics, sizing is approximate
Known gaps: Some stories may be missing from unrecovered Claude.ai sessions
-->

# HAL Stack — Stories

Tactical work items derived from epics. Each layer-tagged.

## Sovereignty Framework (E1)

| ID | Story | Layer | Priority | Status | Blocked By |
|----|-------|-------|----------|--------|------------|
| S1.1 | Fill decapitation checklist for GitHub (repos + Pages) | L1-L4 | P2 | Pending | — |
| S1.2 | Fill decapitation checklist for Formspree | L1-L4 | P2 | Pending | — |
| S1.3 | Fill decapitation checklist for Cloudflare | L1-L4 | P2 | Pending | — |
| S1.4 | Fill decapitation checklist for Gmail pipeline | L1-L4 | P2 | Pending | — |
| S1.5 | Schedule first quarterly decapitation drill | L1-L4 | P3 | Pending | S1.1-S1.4 |

## Cross-Context System (E2)

| ID | Story | Layer | Priority | Status | Blocked By |
|----|-------|-------|----------|--------|------------|
| S2.1 | Add context export step to CLAUDE.md workflow | L1-L4 | P2 | Pending | Aaron review |
| S2.2 | Retroactive recovery: 10 most important Claude.ai sessions | L1 | P2 | Pending | Aaron |
| S2.3 | Create exports/ directory with first real export | L1-L4 | P2 | Pending | S2.2 |
| S2.4 | Test context-loader-prompt with GPT (L2 validation) | L2 | P3 | Pending | — |

## Voice-to-Machine (E3)

| ID | Story | Layer | Priority | Status | Blocked By |
|----|-------|-------|----------|--------|------------|
| S3.1 | Create OpenAI Platform account + API key | L1 | P1 | Pending | Aaron |
| S3.2 | Build Sub-Sprint 1: Working STT loop | L1 | P1 | Pending | S3.1 |
| S3.3 | Build Sub-Sprint 2: Keyword command map | L4 | P1 | Pending | — |
| S3.4 | Build Sub-Sprint 3: Command router + TTS response | L4 | P1 | Pending | S3.2, S3.3 |
| S3.5 | Build Sub-Sprint 4: Continuous listen loop | L1-L4 | P2 | Pending | S3.4 |
| S3.6 | Test Whisper.cpp on i5 Lenovo (L4 STT benchmark) | L4 | P3 | Pending | — |

## Machine Profile (E4)

| ID | Story | Layer | Priority | Status | Blocked By |
|----|-------|-------|----------|--------|------------|
| S4.1 | Run register-machine.ps1 on i5 Lenovo | L4 | P3 | Pending | Physical access |
| S4.2 | Detect Pentium Silver specs | L4 | P3 | Pending | Physical access |
| S4.3 | Add machine-ID check to CLAUDE.md startup | L4 | P3 | Pending | Aaron review |

## Branding (E5)

| ID | Story | Layer | Priority | Status | Blocked By |
|----|-------|-------|----------|--------|------------|
| S5.1 | Aaron reviews logo v1.1 against original spec | L1 | P2 | Pending | Aaron |
| S5.2 | Logo v1.2 rework based on Aaron's feedback | L1 | P2 | Pending | S5.1 |
| S5.3 | Upload final logo to LinkedIn company page | L1 | P2 | Pending | S5.2 |

## Content Freshness (E6)

| ID | Story | Layer | Priority | Status | Blocked By |
|----|-------|-------|----------|--------|------------|
| S6.1 | Define "stale" rules per content type | L4 | P3 | Pending | — |
| S6.2 | Build freshness check script (PowerShell or Node) | L4 | P3 | Pending | S6.1 |
| S6.3 | Wire to n8n cron (when n8n installed) | L3 | P3 | Pending | n8n |
