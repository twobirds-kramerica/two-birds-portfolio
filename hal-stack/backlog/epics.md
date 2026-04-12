<!--
STATUS: v0.2 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:30 EST (Toronto)
Updated: 2026-04-11 01:45 EST (Toronto)
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
**Priority:** P1
**Status:** TWO BIRDS FINALIZED, DCC IN REVIEW (Session 17, April 11 2026)
**Deliverables:** Two Birds V05 finalised (all formats). Brand guidelines v1.0. DCC 8 variations + guidelines created.
**Next:** Aaron uploads two-birds-1024.png to LinkedIn. Aaron selects DCC logo. CIPO research (future).
**Blockers:** Aaron — DCC logo selection, LinkedIn upload

## E6: Content Freshness Layer
**Layer:** L1 initial, L3 target
**Priority:** P3
**Status:** NOT STARTED
**Origin:** March 6, 2026 — HAL Stack Day 1 requirement (confirmed via Claude.ai export ingestion, Session 16). Originally backlogged as March 8.
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

## E8: Faceless Brand Principle
**Layer:** L1-L4
**Priority:** P3
**Status:** RESOLVED — NOT A STANDALONE PLAN (Session 16 discovery)
**What:** "Faceless brand" is a VALUES CHOICE, not a strategy document. Build recognition through product quality and content, not personal image. Thread across conversations Jan–Apr 2026. Now captured in `personas/culture-spec.md`.
**Next:** No further action needed unless Aaron wants to formalise it as a full strategy doc.
**Blockers:** None

## E9: Claude.ai Data Export + Retroactive Ingestion
**Layer:** L1 dependency
**Priority:** P2
**Status:** INFRASTRUCTURE READY (Session 14, April 11 2026)
**What:** Export past Claude.ai sessions, ingest into context bridge
**Deliverables:** Ingestion sprint prompt, expected discoveries list, raw/ folder ready
**Next:** Aaron requests data export from claude.ai tomorrow. When it arrives, paste ingestion-sprint-prompt.md into Claude Code.
**Blockers:** Aaron — request export, then drop file in raw/

## E10: HAL Boardroom — Multi-Agent Workspace
**Layer:** L1-L4
**Priority:** P2
**Status:** VISION DOCUMENTED (Session 14, April 11 2026)
**What:** Multiple machines with dedicated AI personas, shared context, voice-orchestrated. Aaron as founder/friction-generator.
**Deliverables:** boardroom-vision.md (architecture, culture spec, persona roles, hardware reqs)
**Next:** Aaron decides timeline (2026 or 2027). Minimum viable = 2 machines (already owned).
**Blockers:** Aaron — timeline decision, persona names

## E11: GitHub L4 Fallback — Local Git Backup
**Layer:** L4
**Priority:** P3
**Status:** ARCHITECTURE DESIGNED (Session 15, April 11 2026)
**What:** Pentium Silver as dumb local git mirror. Auto-syncs from GitHub every 4 hours. Never pushes.
**Deliverables:** `architecture/local-backup.md` — setup script, sync strategy, failover procedure
**Next:** Aaron sets up Pentium Silver with script. One-time 30-minute setup.
**Blockers:** Physical access to Pentium Silver

## E12: Persona & Swarm Framework
**Layer:** L1-L4
**Priority:** P1
**Status:** v0.1 DOCUMENTED (Session 15, April 11 2026)
**What:** 6 departments, 22 personas, weighting system, profiles, model routing, culture spec
**Deliverables:** Full persona system in `hal-stack/personas/`
**Next:** Aaron reviews department compositions. Test one profile in a real sprint.
**Blockers:** Aaron — persona review and first test run

## E13: Skill Library
**Layer:** L1-L4
**Priority:** P2
**Status:** FOUNDATION (Session 15, April 11 2026)
**What:** Reusable instruction sets any persona can reference
**Deliverables:** Schema + 3 starter skills (brand review, sovereignty audit, sprint prompt writing)
**Next:** Create skills as needs emerge. Don't pre-build — let practice drive the library.
**Blockers:** None

## E15: Employability Project
**Layer:** L1-L4
**Priority:** P2
**Status:** CAPTURED (pending-capture merge, April 12 2026)
**What:** Formalise employability as a tracked workstream. Connects to 56 career conversations in Claude.ai export and employment-recovery.md.
**Next:** Aaron to clarify intent — active job search, career positioning, or employability insurance? [VERIFY]
**Blockers:** Aaron — scope clarification

## E14: Full Decapitation Audit
**Layer:** L1-L4
**Priority:** P2
**Status:** COMPLETE (Session 15, April 11 2026)
**What:** Every component assessed for sovereignty across all four layers
**Deliverables:** 12-component audit in `architecture/decapitation-checklist.md`, sovereignty dashboard in `sovereignty-principles.md`
**Next:** Action items: test Aider as L2, confirm Cloudflare Pages as live L2, document DNS records, build local backup script
**Blockers:** None
