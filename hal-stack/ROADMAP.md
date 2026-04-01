# HAL Stack — Roadmap
**Owner:** Aaron Kramer | Two Birds Innovation
**Last Updated:** March 31, 2026

> HAL = Home Automation & Learning stack. Local-first AI infrastructure for Two Birds Innovation.

---

## Phase 1: Foundation ✅ COMPLETE (100%)

| Component | Status | Notes |
|-----------|--------|-------|
| Hardware: i5 Lenovo desktop, 16GB RAM | ✅ Complete | Primary dev/build machine |
| OS: Windows 10 Pro | ✅ Complete | Stable, no plans to upgrade |
| Claude Code v2.1.88 | ✅ Complete | Pro plan, primary dev tool |
| Windows Terminal | ✅ Complete | Ctrl+V works |
| Git identity configured (Aaron Patzalek) | ✅ Complete | All repos under C:\twobirds\ |
| All repos cloned locally | ✅ Complete | 8+ repos |
| Enhancement tools installed | ✅ Complete | Claude Mem, Superpowers, GSD, Everything CC, Awesome CC |
| Desktop launcher | ✅ Complete | claude-code.bat |
| GitHub Pages deployment | ✅ Complete | DCC, Career Coach, Kevin's, Portfolio all live |
| Quality Dashboard | ✅ Complete | Local build status across all repos |
| Portfolio command centre | ✅ Complete | WIP-DASHBOARD.md — single source of truth |
| Static site architecture | ✅ Complete | HTML/CSS/JS only, no build tools, no backend |
| hal-stack/ directory structure | ✅ Complete | README, ARCHITECTURE, SETUP, docs/, scripts/ |

**Phase 1 completion date:** March 31, 2026

---

## Phase 2: Intelligence 🔵 ACTIVE

Local AI tooling for prompt tracking, content generation assistance, and knowledge management.

| Step | Component | Status | Command / Notes |
|------|-----------|--------|-----------------|
| 1 | **n8n install** | 🔵 NEXT | `npm install -g n8n && n8n start` — port 5678 |
| 2 | n8n basic workflow: prompt tracking | ⬜ Queued | Log every Claude Code session prompt + output summary |
| 3 | n8n workflow: content freshness alerts | ⬜ Queued | Weekly check of DCC module dateModified values |
| 4 | OpenCode installed for remote mobile access | ⬜ Queued | Remote build monitoring |
| 5 | keep-alive script configured | ⬜ Queued | Prevent machine sleep during builds |
| 6 | LightRAG install | ⬜ Queued | `pip install lightrag` — local RAG on port 9621 |
| 7 | LightRAG: DCC content ingest | ⬜ Queued | Feed all 241 pages into RAG index |
| 8 | LightRAG: query interface | ⬜ Queued | Ask questions about DCC content, get sourced answers |
| 9 | Mobile dashboard showing build status | ⬜ Queued | Quick status from phone |
| 10 | Failure email alerts via n8n | ⬜ Queued | Proactive error notification |
| 11 | **HAL-007: Portfolio as Live PMO** | ⬜ Queued | Cross-session backlog access — n8n webhooks expose portfolio files, Claude Web MCP connects |

**Target:** April–May 2026

---

## Phase 3: Automation ⬜ PLANNED

Scheduled tasks, monitoring, and self-healing infrastructure.

| Step | Component | Status | Notes |
|------|-----------|--------|-------|
| 1 | Scheduled sitemap validation | ⬜ Planned | n8n cron → run sitemap-validator workflow |
| 2 | Automated broken link monitoring | ⬜ Planned | n8n cron → GitHub Actions trigger |
| 3 | Formspree backup automation | ⬜ Planned | Monthly CSV export reminder or automated pull |
| 4 | Content publishing pipeline | ⬜ Planned | Draft → review → publish workflow in n8n |
| 5 | Home desktop as permanent HAL server | ⬜ Planned | Always-on local infrastructure |

**Target:** May–June 2026

---

## Phase 4: Scale ⬜ DEFERRED

| Step | Component | Status | Notes |
|------|-----------|--------|-------|
| 1 | Voice-activated builds (Whisper) | ⬜ Deferred | Social Stack Diary #1 concept |
| 2 | Multi-agent routing (Claude / Gemini / GPT) | ⬜ Deferred | Task-specific model selection |
| 3 | API gateway for client tools | ⬜ Deferred | B2B service delivery |
| 4 | LinkedIn content scheduler | ⬜ Deferred | Automated posting from pre-written content |
| 5 | Email newsletter automation | ⬜ Deferred | Requires email platform selection first |
| 6 | HAL prompt tracking → spin out as DevLoop product | ⬜ Deferred | Potential SaaS product |

**Target:** TBD — after Phase 2 and 3 are stable

---

*HAL Stack is a Two Birds Innovation internal project. Not a product for sale (yet).*
