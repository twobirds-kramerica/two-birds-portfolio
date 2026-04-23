<!--
  HAL Stack Wiki — produced by S-ARCHAEOLOGY-002 (2026-04-23 ~00:20 EST)
  Status: MVP — anchored on the authoritative HAL Stack project_memory
  (019cc3d2, 13,765 chars) from the 2026-04-22 export. Every claim cites
  that source, the Two Birds Command memory (019d87ad, 4503 chars), or
  direct repo inspection.
-->

# HAL Stack Wiki — Complete Specification (v0.1, MVP)

**Last updated:** 2026-04-23 00:20 EST (Toronto)
**Source:** `memories.json` project_memories[019cc3d2] + [019d87ad] + `two-birds-portfolio/hal-stack/` repo state
**Status:** Living document — Aaron reviews and corrects.

## 1. What HAL Is

> "Aaron Patzalek is the solo founder of Two Birds Innovation, a Canadian tech company based in St. Thomas, Ontario. He has ~20 years of background in services development, retail operations, ecommerce, and telco. His primary build is the **HAL Stack** — a voice-first, sovereignty-aware AI development architecture managed through markdown files in a public GitHub repo (`twobirds-kramerica/two-birds-portfolio`). Aaron has no coding background and works primarily through voice dictation (Windows Win+H) and Claude Code autonomous sprints." — HAL Stack project_memory

**Core purpose from projects.json description:** *"Build an efficient, intelligent and cohesive product development flow."*

## 2. Sovereignty Float Model (L1→L4)

Every component designed so moving between layers is a configuration change, not a rebuild:
- **L1** — commercial fast/cheap (current default)
- **L2** — alternative commercial (swap-ready)
- **L3** — open-source hosted
- **L4** — open-source local only (ungovernable)

> "Claude is explicitly a swappable headless LLM backend, not a permanent dependency." — HAL Stack project_memory

Float Free Index currently **48/100** with documented path to 80/100 per DCC project_memory (same index applies across portfolio).

## 3. Governance + Source of Truth

> "**Single source of truth: Notion Command Center** is live and authoritative. Every session: read Command Center on startup before responding; write all new backlog items/decisions/actions to Notion immediately; update status when sprints complete; answer 'what am I working on' from Notion, not chat memory. **GitHub = code repo. Notion = brain.**"

Canonical IDs:
- Command Center page: `347a09cf-876a-81fb-9a5c-eca696fb585b`
- Product Backlog data source: `dee08637-7122-46cd-bc29-7775ce3ab8f6`
- Job Pipeline data source: `92415698-9009-4d74-b86b-ad23f5afe475`
- Glossary/Command Reference page: `348a09cf-876a-815a-802c-c9c182167749`
- **Sprint Queue Manager data source: `a297b04c-7887-42d1-b73b-21af94d57cd8`** (per Two Birds Command memory — the queue that auto-promotion runs against; distinct from Product Backlog)

## 4. HAL Boardroom — Persona Structure

**Inner Circle:**
- **The Sheriff** — Chief of Staff, default synthesiser, casual name spoken / formal name written
- **Love Balance Advisor** — equal weight to The Sheriff; private wellness seat; data walled off from all others

**Scrappy Pack** (aka "The Why Guys") — standing advisory filter below Inner Circle. Five personas:
1. The Researcher
2. Why Not
3. The Fifth Why
4. The Ripper
5. The Sovereignty Check

**Default output:** 1 bullet `Scrappy Pack says: [one sentence]` + mandatory LOE. No individual personas shown by default.
**Expand** when Aaron says "what does the whole team/pack think" or "expand the pack".
**LOE is mandatory every time the Pack speaks.**

**Founding Board governance:**
- 22 named personas across 6 departments (being rationalised to ~3 active agents per multi-LLM audit consensus)
- **Helen (GC)** and **Naveen (CTO/Engineering VP)** hold veto cards that override all voting weights on legal/compliance and technical risk decisions respectively
- Runs only when sprint queue is empty (P4 priority)

## 5. Machines (3 total; all have Claude Code)

Per HAL Stack project_memory:
1. **Lenovo Pentium Silver** — newer chassis, slower processor; original dev machine
2. **Lenovo ThinkPad i5** — older chassis, more powerful; migration complete
3. **EZbook** — most recent, from Phil Butler via Employment Services; fully configured; Claude.ai raw export lives at `hal-stack/context-system/ingestion/raw/` (gitignored, local-only)

> "Always confirm which machine by processor name (Pentium Silver vs. i5), not brand — both are Lenovo. Do not confuse them."

**UNKNOWN — machine primacy mismatch**: Two Birds Command memory lists "i5 Lenovo (primary), EZbook Pentium Silver Lenovo (secondary)". HAL Stack memory labels Pentium Silver as "original dev machine". Different machine is "primary" across the two memories. Aaron to resolve.

## 6. Key People

- **Mike Kerkvliet** — Manager, Business Development & Entrepreneurship, St. Thomas Economic Development. Two opportunity streams: (a) Paperwork Labs (digital municipal forms SaaS, CAD $10-20K/year; Mike co-founded but can't operate due to conflict of interest — Aaron's framing: "audition with potential, not free strategy delivery"). (b) Economic development team consolidation — potential role.
- **Phil Butler** — Employment specialist at Employment Services Elgin. Provided the EZbook laptop.
- **Davie Lee** — Director of AI & Innovation at interVal, EIR at TechAlliance St. Thomas. LinkedIn outreach draft ready in Gmail.
- **Helen (GC)** and **Naveen (CTO/Engineering VP)** — Founding Board veto-card holders (see §4).
- **Assaf Kipnis (kipi-system)** — external founder OS inspiration; Aaron follows on LinkedIn + GitHub.

## 7. Standing Rules (Aaron's collaboration patterns)

- **N.B. Rule:** Before saying "I can't" OR asserting any fact about Aaron's calendar, inbox, files, repo state, or external-system contents, call the relevant tool first. Guessing is the same bug class as refusing without checking.
- **Sparring-partner tone** preferred; pushback appreciated; no flattery.
- **Voice dictation** (Win+H) as primary input; typos expected and don't affect comprehension.
- **Aaron prefers backlogging items silently** mid-focus rather than discussing them; prefers one combined prompt over multiple sequential; sessions should end when token use is excessive.
- **LOE (effort vs return) mandatory** every time the Scrappy Pack speaks.

## 8. Workflow Patterns

- **Sprint system** with backlog (NOW / SOON / LATER / DONE) in Notion; GitHub for code
- **Claude Code autonomous overnight sprints**
- **Voice-first** — Win+H dictation, known to stop after 1-2 sentences (P3 backlog to fix)
- **Autonomous Queue Promotion:** before every "next sprint" — (1) query Sprint Queue Manager, (2) if Ready empty AND Backlog has P0: auto-promote P0 to Ready, (3) if still empty AND P1 exists: promote P1, (4) lock + execute. **Data source: `a297b04c-...`.**

## 9. Key Learnings & Principles

Directly from HAL Stack project_memory:

> "**Stop building custom when existing solutions exist.** A core failure pattern: writing custom tooling (e.g., 150-line Python sync script) only to discover an official solution exists. CTO-level thinking means finding existing solutions first."

> "**Stop orchestrating the orchestrator.** Aaron has been building scaffolding (personas, sovereignty frameworks, multi-machine architecture) instead of converting his ikigai into revenue. The framing: 'stop orchestrating the orchestrator and go sell the orchestration.'"

> "**Evaluate tools by effort vs return.** Score each recommendation by whether it makes Aaron do less work or more work. Tool count is inversely correlated with usefulness."

## 10. Tools & Resources (current inventory)

- **Notion** (official MCP server active) — brain
- **GitHub** (`twobirds-kramerica/two-birds-portfolio`) — code
- **Claude Code** — autonomous sprint engine
- **Cloudflare Pages** — hosting
- **Formspree** — forms
- **Apify** — `apify-mcp-server`; `actors.docs.apify/rag-web-browser` Actor active
- **Amplitude** — EZbook configured (workspace `damp-snowflake-837553`, EU region)
- **UptimeRobot** — recommended for uptime monitoring
- **Plausible or Fathom** — recommended for analytics
- **research-mode (assafkip)** — installed via manual clone

**Accounts to close per audit:** Supabase, Vercel, Resend (unused).
**Rejected / L1-only sovereignty flag:** Google CodeWiki (use freely, build no dependencies).

## 11. Active Strategic Items (from HAL Stack memory, as of 2026-04-04)

- **Job search** — active priority ABOVE architecture work (13 scored roles in Notion Job Pipeline)
- **DCC v2** — "parked until a clearer brief is defined" in the memory, but superseded on 2026-04-22 by explicit approval + S-DCC-V2 sprint execution this session
- **Persona rationalisation** — 22 → ~3 active agents per multi-LLM audit
- **Company rename** — "ALOFT" vs "Two Birds Innovation"; domain purchase blocked on decision
- **Logo** — not finalised; Session 15 produced 10 variations (designer recommended V04); LinkedIn upload deferred

## 12. Open Questions / UNKNOWN

1. **Current company name decision** — Two Birds Innovation vs ALOFT — still pending per memory (dated 2026-04-04). Has this been resolved?
2. **Active persona count** — memory says 22 → ~3 target; current state uncertain.
3. **"Command" vs "Two Birds Innovation"** — memory dated 2026-04-13 treats Two Birds Command as a separate project workspace for ops; HAL Stack memory dated 2026-04-04 folds it under HAL Stack. Which is the current mental model?
4. **Employment insurance runway** — "Aaron is on employment insurance with limited runway." Still the case? (Matters for sprint prioritisation.)
5. **kipi-system adoption** — Aaron was following but hadn't adopted as of the memory snapshot. Status?

## 13. Decision Log (from memories; chronological)

| Date | Decision | Source |
|---|---|---|
| 2026-03-06 | HAL Stack project created | projects.json[019cc3d2] `created_at` |
| 2026-04-13 | Two Birds Command project created (ops/command layer) | projects.json[019d87ad] |
| 2026-04-04 | HAL Stack memory last updated; DCC v2 parked | memory `updated_at` |
| 2026-04-04 | "Stop orchestrating the orchestrator" audit finding | memory key learnings |
| 2026-04-22 | DCC v2 un-parked; S-DCC-V2 approved + shipped Phase 1-6 | portfolio SESSION-STATE |
| 2026-04-22 | Notion MCP schema fetch pattern documented (collection:// syntax + Two Birds Claude Code Sync integration) | memory |

## 14. Pointers (deeper detail elsewhere)

- Portfolio-side operational rules: `CLAUDE.md` root (this repo)
- Sovereignty architecture: `hal-stack/architecture/decapitation-checklist.md` + `hal-stack/architecture/decapitation-details/`
- Founding Board personas: `hal-stack/personas/`
- Voice-check banned words: `hal-stack/sprint-system/backlog/P2-voice-check-protocol.md`
- Pattern library: `hal-stack/research/autonomous-dev-patterns-v1.md` (13 distilled patterns)
- Reliability issues log: `RELIABILITY-ISSUES.md` (RI-001 through RI-007 as of 2026-04-22)
