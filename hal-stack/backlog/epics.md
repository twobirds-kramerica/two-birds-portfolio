<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:30 EST (Toronto)
Confidence: HIGH for shipped items, MEDIUM for planned items
Known gaps: Faceless brand/influencer plan location unknown — needs recovery from Claude.ai history
-->

# HAL Stack — Epics

All epics layer-tagged per sovereignty model.

## E1: Sovereignty Framework
**Layer:** L1-L4
**Priority:** P1
**Status:** v0.1 SHIPPED (Session 12, April 10 2026)
**Deliverables:** Four-layer model, decapitation checklist, layer tags, ADRs
**Next:** Fill decapitation checklists for remaining components (GitHub, Formspree, Cloudflare, Gmail)
**Blockers:** None

## E2: Cross-Context System
**Layer:** L1-L4
**Priority:** P1
**Status:** v0.1 SHIPPED (Session 12, April 10 2026)
**Deliverables:** Context index, export template, loader prompt, retroactive catchup plan
**Next:** Aaron to do retroactive recovery sprint (2 hours, manual). Add context export to CLAUDE.md workflow.
**Blockers:** Aaron — manual context recovery from Claude.ai history

## E3: Voice-to-Machine
**Layer:** L1-L4 target
**Priority:** P2
**Status:** RESEARCH COMPLETE (Session 12, April 10 2026)
**Deliverables:** Component breakdown, four-layer options, signup checklist, build plan, sovereignty notes
**Next:** Aaron creates OpenAI Platform account (10 min, CA$5). Then first build sprint (~2.5 hours).
**Blockers:** Aaron — OpenAI account creation

## E4: Machine Profile
**Layer:** L4-native
**Priority:** P2
**Status:** v0.1 SHIPPED (Session 12, April 10 2026)
**Deliverables:** machines.json (EZbook registered), register-machine.ps1, claude-code-identifier
**Next:** Run register-machine.ps1 on i5 Lenovo. Detect remaining specs for Pentium Silver.
**Blockers:** Physical access to other machines

## E5: Branding Foundation
**Layer:** L1
**Priority:** P2
**Status:** NEEDS REWORK
**Deliverables:** Logo v1.0 (April 9), Logo v1.1 (April 9)
**Issue:** Aaron flagged v1.1 is not quite what was specced. Needs review against original chat spec before LinkedIn upload.
**Next:** Aaron reviews v1.1 render, provides specific feedback. Logo v1.2 rework sprint.
**Blockers:** Aaron — design review

## E6: Content Freshness Layer
**Layer:** L1 initial, L3 target
**Priority:** P3
**Status:** NOT STARTED
**Origin:** March 8, 2026 session — concept documented, not built
**What:** Automated check of DCC module lastmod dates. Alert when content is stale.
**Next:** Design freshness rules (how old is "stale"?). Build as n8n workflow or simple script.
**Blockers:** n8n not installed yet

## E7: Claude Code Quota Optimisation
**Layer:** L1-only
**Priority:** P3
**Status:** RESEARCH ONLY
**What:** Understand Opus vs Sonnet usage patterns, optimise for cost within Pro plan limits
**Next:** Monitor usage over next 2 weeks, document patterns
**Blockers:** None — observation only

## E8: Faceless Brand / Influencer Plan
**Layer:** L1
**Priority:** P3
**Status:** NEEDS RECOVERY
**What:** Content strategy for faceless brand approach — documented somewhere in Claude.ai history
**Next:** Recover context during retroactive catchup sprint (E2 dependency)
**Blockers:** Claude.ai data export / manual recovery

## E9: Claude.ai Data Export + Retroactive Ingestion
**Layer:** L1 dependency
**Priority:** P2
**Status:** PLAN DOCUMENTED (retroactive-catchup-plan.md)
**What:** Export past Claude.ai sessions, ingest into context bridge
**Next:** Aaron checks claude.ai settings for data export option
**Blockers:** Aaron — requires manual action, L1-dependent feature
