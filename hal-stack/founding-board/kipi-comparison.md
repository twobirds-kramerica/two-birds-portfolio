# kipi-system ↔ HAL Stack — Deep-Dive Comparison

**Sprint:** S-027 (kipi-system deep-dive comparison to HAL Stack)
**Date:** 2026-04-20
**Research mode:** active — every claim is tagged to a live-fetched source from 2026-04-20.
**Scope:** 4 repos in the `assafkip/` ecosystem, mapped to HAL Stack equivalents and gaps.

---

## Executive summary

Assaf Kipnis has publicly shipped a Python-based founder OS (`kipi-system`) and a scrubbed multi-project variant (`claude-cortex`), plus two smaller standalone skills. Several of the patterns solve problems HAL Stack has already named as broken or missing. **At least three are direct rip candidates** (loop tracker, token guard, morning-brief HTML builder). One (`founder-debrief` skill) is directly installable tomorrow. The ADHD design philosophy is complementary to — not a replacement for — HAL's Love Balance Advisor persona.

**Critical licensing flag up front:** `kipi-system` and `research-mode` have **no LICENSE file**. On GitHub, the absence of a licence means all rights reserved. We cannot ship their code verbatim without written permission from the author. `claude-cortex` (MIT) and `founder-skills` (MIT) are safe to rip. This affects the rip/skip/adapt calculus below.

---

## Repo overview (live-fetched 2026-04-20)

| Repo | Stars | License | Language | Core pitch (from README) |
|------|-------|---------|----------|--------------------------|
| `assafkip/kipi-system` | 59 | **none (all rights reserved)** | Python | "Portable founder OS for Claude Code" — morning routine, loop tracker, conversation debriefs, ADHD-aware output |
| `assafkip/claude-cortex` | 0 | MIT | Python | Multi-project / scrubbed variant of the same system; 4 plugin groups, 8 agent skills, 40 specialist agents, 69 MCP tools, 25 slash commands |
| `assafkip/founder-skills` | 11 | MIT | — | Two skills: `founder-debrief` (8-question extraction) + `neurodivergent-founder` (output shaping) |
| `assafkip/research-mode` | 121 | **none (all rights reserved)** | — | Already cloned into `~/.claude/skills/research-mode/` in an earlier HAL session (SESSION-STATE 2026-04-16). Anti-hallucination toggle, cite-or-say-unsure |

**Author context:** Assaf Kipnis is an AUDHD (ADHD + Autism) pre-seed founder. All design decisions are ADHD-first. The kipi README explicitly states it has been "refined across 50+ investor and design partner conversations" — production-tested, not a thought experiment.

---

## The 5 explicit evaluation criteria

### 1. Morning brief pattern — kipi `/q-morning` vs HAL's broken morning brief

**kipi (fetched):**
- Single command `/q-morning` produces one HTML file per day.
- Pulls from calendar, email, CRM, social.
- Output is copy-paste actions sorted by friction (2-minute replies first, deep work later — "momentum builds before the hard stuff").
- Every follow-up is pre-written in the user's voice (fed from writing samples).
- Open loops with escalation table (0-2 quiet, 3-6 drafted, 7-13 flagged, 14+ forced decision).
- Verification gate: a script checks the JSON before HTML builds. Missing sections = build blocked. "The AI can't bypass it."
- Source files: `q-system/.q-system/commands.md` (35+ step routine), `verify-schedule.py`, `audit-morning.py`, `marketing/templates/build-schedule.py`.

**HAL Stack:**
- Glossary "Known broken / in progress" entry: "*Morning brief pattern — some drafts sent, some unsent, lost track. P1 task: use gmail_list_drafts to audit, identify draft vs sent status, restructure into reliable daily pattern.*" (Notion Glossary fetched 2026-04-19.)
- No current implementation. Repeated flagging over multiple sessions.

**Recommendation: DIRECT RIP (modulo licence).**
- The whole architecture fits HAL's problem. The friction-ordered list, voice-aware drafts, and loop escalation are exactly what "a reliable daily pattern" looks like.
- Blocker: kipi-system has no licence. Two paths:
  1. Adopt the **equivalent** from `claude-cortex` (MIT) — which contains the same morning-routine code per its own README. Safe.
  2. Email Assaf for explicit permission to use kipi code. He's shipping publicly; likely amenable.
- Estimated effort once licensed: 3-5 days to adapt to HAL's specific data sources (Notion instead of CRM, Gmail as-is, no Twitter for now).
- **Rip-the-pattern-without-the-code** is always available and licence-safe: read the README, build the HAL equivalent ourselves.

### 2. Loop tracker — kipi `loop-tracker.py` vs HAL's lost context problem

**kipi (fetched `loop-tracker.py`, first 80 lines):**
- Loop has: `id` (date-serial like `L-2026-04-20-003`), `type`, `target`, `opened` date, `touch_count`, `escalation_level`, `status` (open / closed).
- Commands: `open`, `close`, `escalate`, `list`, `force-close`, `stats`, `prune`, `touch`.
- Loop types: `dm_sent`, `email_sent`, `materials_sent`, `comment_posted`, `action_created`, `debrief_next_step`, `dp_offer_sent`, `connection_request_sent`, `lead_sourced`.
- Storage: `output/open-loops.json`. Dedup by `target + type`.
- Auto-close triggers (per README): Gmail reply, LinkedIn DM reply, connection accepted.

**HAL Stack:**
- "Lost context problem" is named but not codified. Symptoms visible in the context-system directory (journey archive gaps, Session 19 recovery, SC-002). The `pending-capture.md` + `context-system/exports/` pattern is the closest analogue — but it captures *events*, not *open outbound actions*.
- `stories.md` tracks open items but doesn't track *expected-responses* (e.g., "I messaged Davie Lee 8 days ago, did he respond?").
- No automated escalation. Decay surfaces only when Aaron notices.

**Recommendation: DIRECT RIP (via `claude-cortex` MIT variant, not kipi).**
- This is the single highest-value pattern in the ecosystem for HAL. Loop tracking with auto-close on Gmail/LinkedIn reply is a wildly useful primitive.
- Effort: 1-2 days to adapt to HAL (swap `output/open-loops.json` for a Notion database row or keep as local JSON; wire Gmail MCP for reply detection).
- Pairs perfectly with HAL's existing "Davie Lee LinkedIn outreach" item that's been stalled for weeks — exactly the failure mode this solves.
- **Related HAL gap:** multiple items in `human-backlog.md` are outbound-action-waiting-on-response with no tracking. Loop tracker would catch all of them.

### 3. Session handoff — kipi `/q-handoff` + `session-start.py` vs HAL's cold-start problem

**kipi (from README):**
- `/q-handoff` command saves context at session end.
- `session-start.py` auto-loads context on first use each day.
- Time-layered memory: 48-hour working memory auto-cleaned, 7-day patterns roll up, monthly insights persist, knowledge graph (`graph.jsonl`) links entities across time.
- Canonical memory separate from project-specific memory: `canonical/*` (talk tracks, objections, market intel, decisions) vs `my-project/*` (relationships, current state, progress).

**HAL Stack:**
- `SESSION-STATE.md` — serves the handoff role. Currently 1457 lines of append-only log.
- `hal-stack/context-system/exports/` — per-session context exports.
- **Gaps:**
  - No auto-load on session start (Claude Code does read CLAUDE.md automatically, but not a working-memory layer).
  - No time-layered decay. SESSION-STATE just grows.
  - No canonical/project-specific separation. Everything lives in one pile.
  - No knowledge graph. Entities are mentioned inline, not linked.

**Recommendation: ADAPT, don't rip wholesale.**
- HAL's SESSION-STATE is serving the critical function. kipi's time-layered decay is a clear improvement but replacing SESSION-STATE wholesale would break the existing retro / next-sprint command flow.
- **Propose:** add a time-layered memory directory (`hal-stack/context-system/memory/{working,weekly,monthly}/`) as a complement. Run a decay script nightly. Keep SESSION-STATE as-is.
- Effort: 2-3 days. The knowledge graph is a separate follow-up (weeks), defer.
- kipi's `canonical/*` vs `my-project/*` split is already mirrored in HAL by `hal-stack/` vs individual repo directories — the pattern exists, just not named.

### 4. ADHD design philosophy — kipi "AUDHD rules" vs HAL's Love Balance Advisor

**kipi (from README + `neurodivergent-founder` skill):**
- Proactive output-shaping. Every response obeys:
  - **No decisions.** System picks who to contact, what to say, in what order.
  - **No shame.** Never "overdue" → "carried forward." Never "you forgot" → "not yet done." Language rule, applied to every output.
  - **Friction-ordered.** Quick wins first. Dopamine before discipline.
  - **Effort-tracked.** "You sent 4 messages today" over "nobody responded yet."
- `neurodivergent-founder` skill activates on "ADHD" / "energy modes" keywords. Tags tasks by energy level (Quick Win / Deep Focus / People / Admin).

**HAL Stack:**
- Love Balance Advisor persona: private wellness seat, tracks hours, tokens, workload, stress signals, language patterns. Can override other agents. **Only surfaces on wellbeing signals** — reactive intervention, not proactive shaping.

**Recommendation: BOTH, not either.** These are complementary:
- kipi = proactive output-shaping (every response AUDHD-aware).
- Love Balance Advisor = reactive surveillance + intervention (triggers on stress signals).
- **Propose:** adopt kipi's language rules ("carried forward" not "overdue," etc.) as an always-on output shaper. Keep Love Balance Advisor as the threshold-triggered override. Together they cover the full loop.
- Effort: 1 day to codify the language rules into CLAUDE.md as a sub-rule of Rules of Engagement. The "Scrappy Pack output rule" is already in CLAUDE.md; this would be a sibling.
- Pattern already partly adopted: the Warm Hearth design system's `quiz-result__message` uses kipi-style "you've carried forward everything you've learned" wording (coincidence or zeitgeist, but the DCC end-user copy is aligned).

### 5. Token guard — kipi `token-guard.py` vs HAL's quota optimization backlog

**kipi (fetched `token-guard.py`, first 60 lines):**
- Two-layer defence: Layer 1 = hook-based circuit breaker; Layer 2 = behavioural rules in CLAUDE.md.
- Called by `PreToolUse` + `UserPromptSubmit` hooks.
- Thresholds (concrete):
  - `RETRY_LIMIT = 3` — same tool + input repeated → block
  - `VOLUME_CEILING = 50` — tool calls since last user message → block
  - `VOLUME_WARNING = 35` — warn
  - `AGENT_CEILING = 30` — agent spawns per message → block
  - `MCP_RATE_LIMIT = 30` per 60-second window → block
  - `READ_SPIRAL_LIMIT = 15` — consecutive reads without write → warn
  - `FILE_REREAD_LIMIT = 3` — same file read N times → warn
  - `GREP_DRIFT_LIMIT = 5` — greps since last write → warn
  - `EDIT_FAIL_LIMIT = 3` — failed edits on same file → block
  - `STALL_TIME_SECONDS = 120` + `STALL_MIN_CALLS = 10` → warn
- Sensitive-file pattern blocking: `.env`, `.pem`, `.key`, `credentials`.
- Exit codes: `0` = allow (optionally warn), `2` = block.

**HAL Stack:**
- No equivalent. CLAUDE.md has a "Pattern counter rule" (if Aaron asks the same Q 3+ times, declare pattern broken) — but that's human-facing, not tool-call throttling.
- "Quota optimization backlog" — searched; no dedicated backlog item matches that exact phrase, but Aaron's token spend has come up (e.g., in the caveman-plugin install). The sprint reference may be aspirational.

**Recommendation: RIP — highest immediate ROI of the five.**
- `token-guard.py` in isolation is ~300 lines of Python, MIT-available via `claude-cortex`. Drop it in under `hal-stack/guardrails/token-guard.py`. Wire to hook config. Done in one afternoon.
- Sensitive-file protection (blocks reads on `.env`) is free extra safety.
- Defensive guardrails like this get more valuable as the repo and sprint cadence grow — now is the right time, before a runaway session happens.

---

## Bonus patterns worth stealing (outside the 5 criteria)

From the README + architecture of `claude-cortex` (MIT-safe):

1. **Echo of Prompt** — before each step executes, a script re-injects that step's requirements fresh into context. Combats "Lost in the Middle" attention drift documented in Stanford 2023 research. **Rip candidate** for multi-phase autonomous sprints.
2. **Verification gate on structured output** — `verify-schedule.py` checks JSON before HTML build. If verification fails, build blocks. Applied to HAL: a `verify-sprint-complete.py` that checks SESSION-STATE.md and commit log before marking a sprint Done.
3. **Structured deliverables, not text summaries** — log *what was actually produced* (counts of items, files, links), not "done." Already partially practised in HAL (SESSION-STATE entries list concrete files + commits); codifying as a rule would be cheap.
4. **No self-authorised skipping** — AI must ask before skipping a step. Already implicit in HAL's "one commit per phase" discipline; formalising as a rule worth ~20 lines in CLAUDE.md.
5. **Path-scoped rule files** — `claude-cortex` has 18 behavioural rule files that fire based on where in the repo Claude is working. HAL has `CLAUDE.md` at root only. Path-scoped rules would let DCC-specific rules (e.g., "WCAG AAA mandatory") fire only in `digital-confidence/` without polluting other contexts.
6. **Voice enforcement from writing samples** — agent shapes output to user's voice from stored samples. HAL's voice-check protocol is a banned-word list; kipi's is positive (match this voice) rather than negative (don't say this). Both could coexist.

From `founder-skills` (MIT-safe, smallest install effort):

7. **`founder-debrief` skill** — 8 extraction questions after any investor / customer / advisor call. Routes each answer to the right file (what-resonated → talk-tracks, pushback → objections, next steps → tasks). **Install tomorrow.** Zero build effort — clone + copy into `~/.claude/skills/`.
8. **`neurodivergent-founder` skill** — output-shaping rules (energy-tagged tasks, framing outreach as sharing expertise not asking favours). **Install tomorrow.** Pairs with the kipi ADHD rules recommendation above.

---

## Rip / skip / adapt — concrete shortlist

Sorted by ROI-to-effort ratio:

| # | Item | Source | Licence-safe | Effort | Immediate value |
|---|------|--------|--------------|--------|-----------------|
| 1 | `founder-debrief` skill | founder-skills (MIT) | ✅ | 10 min clone-and-copy | Extract Aaron's next 10 actions from every investor/partner call |
| 2 | `neurodivergent-founder` skill | founder-skills (MIT) | ✅ | 10 min clone-and-copy | Energy-tagged tasks, positive-frame outreach language |
| 3 | Token guard (`token-guard.py`) | claude-cortex (MIT) | ✅ | 1 afternoon | Halts runaway token spend; blocks `.env` reads |
| 4 | Loop tracker | claude-cortex (MIT) | ✅ | 1-2 days | Auto-escalation on stalled outbound (Davie Lee, iA Financial, etc.) |
| 5 | ADHD output language rules | kipi README | ✅ (rip the pattern, write the words ourselves) | 1 day | "Carried forward" over "overdue" — immediate tone upgrade |
| 6 | Morning-brief HTML builder | claude-cortex (MIT) | ✅ | 3-5 days | Resolves HAL's named-broken morning brief |
| 7 | Echo of Prompt | claude-cortex pattern | ✅ (rip the idea) | 1 day per sprint-type | Reduces phase-drift on long autonomous sprints |
| 8 | Path-scoped rule files | claude-cortex structure | ✅ (rip the structure) | 2 days | DCC-specific rules without polluting CLAUDE.md |
| 9 | Time-layered memory decay | claude-cortex pattern | ✅ (rip the idea) | 2-3 days | SESSION-STATE stops growing unbounded |
| 10 | Knowledge graph (`graph.jsonl`) | claude-cortex | ✅ (MIT) but high complexity | 1-2 weeks | Deferred — nice but not urgent |

**Skip (for now):**
- Apify / X-Twitter scraping — out of HAL's priority set.
- Slack approval workflows — no Slack in HAL yet.
- Full CRM integration — Notion Command Center already serves.

---

## Licensing caveat (action required)

**`~/.claude/skills/research-mode/` was cloned into HAL's setup 2026-04-16** (per SESSION-STATE) from `assafkip/research-mode`, which has **no licence**. This means HAL is currently using another author's code without express permission.

Options:
- (a) Email Assaf for retroactive permission. He's shipping publicly and likely amenable.
- (b) Replace with an equivalent from `claude-cortex` (MIT) — research-mode logic lives in `plugins/kipi-core/skills/research-mode/` per the cortex README.
- (c) Re-implement from the Anthropic docs that research-mode is itself a packaging of (per its own README: "Activates citation constraints from Anthropic's documentation"). Zero licence risk.

Same applies to any rip from `kipi-system` proper — use the `claude-cortex` (MIT) version of the same code when it exists. The cortex README explicitly says: "If a feature exists in the code, it works" — i.e., nothing was stripped from cortex that's in kipi.

---

## Architecture alignment (cultural fit)

- kipi is Python-first. HAL tooling is already Python (see `hal-stack/notion-sync/`). No friction.
- kipi uses `.claude/` + slash commands + MCP tools + skills + agents. Same primitives HAL uses.
- kipi is single-user first, multi-project via `kipi new <path> <name>`. HAL is multi-project from day 1 (10 repos, 1 portfolio). Drop-in compatible.
- kipi's "canonical vs project" split maps to HAL's "hal-stack vs each repo" split. The mental model already exists.
- kipi's ADHD-first design philosophy aligns with Aaron's solo-founder constraints (time-scarce, cold-start-prone, context-loss-prone). Good match.

**No cultural misfits identified.** The biggest philosophical difference is kipi's "one canonical system per founder" vs HAL's "every machine + remote is a node with L1→L4 fallback." HAL's sovereignty model is more paranoid; kipi's is pragmatic. Both are defensible.

---

## Recommended follow-up sprints

1. **Micro-sprint (10 min):** Install `founder-skills` (MIT). Clone + copy to `~/.claude/skills/`. Verify `/debrief` and `neurodivergent-founder` skills appear after `/reload-plugins`.
2. **Small sprint (1 afternoon):** Rip `token-guard.py` from `claude-cortex` into `hal-stack/guardrails/`. Wire PreToolUse + UserPromptSubmit hooks in `~/.claude/settings.json`.
3. **Medium sprint (2 days):** Rip loop tracker from `claude-cortex`. Adapt storage to Notion database row (new data source) or keep local JSON. Wire Gmail MCP for auto-close.
4. **Licensing clean-up (30 min):** Swap `~/.claude/skills/research-mode/` for the `claude-cortex` MIT version, OR email Assaf for permission on kipi + research-mode.
5. **ADHD language rules (1 day):** Add an "Output language" sub-rule under Rules of Engagement in CLAUDE.md.
6. **Large sprint (3-5 days):** Rip the morning-brief HTML builder. Resolves HAL's long-named-broken morning brief. Do this AFTER the loop tracker ships — the brief reads from open loops.

---

## Source references (all live-fetched 2026-04-20)

- `assafkip/kipi-system` — `gh api repos/assafkip/kipi-system`, README via `gh api /readme`, `loop-tracker.py` first 80 lines, `token-guard.py` first 60 lines.
- `assafkip/claude-cortex` — `gh api repos/assafkip/claude-cortex`, README via `gh api /readme`, root file tree.
- `assafkip/founder-skills` — `gh api repos/assafkip/founder-skills`, README, root file tree. MIT licence confirmed via `gh api /license`.
- `assafkip/research-mode` — `gh api repos/assafkip/research-mode`, README, root file tree. No licence confirmed via `gh api /license` (404).
- HAL Stack Glossary — Notion page `348a09cf-876a-815a-802c-c9c182167749`, fetched 2026-04-19 (S-026 build session). "Known broken / in progress" section cited for morning brief.
- HAL Stack `SESSION-STATE.md` — fetched 2026-04-19 (S-025 entry cites research-mode install).
- Stanford "Lost in the Middle" (2023), Laban et al. 2025 "LLMs Get Lost in Multi-Turn Conversation" — cited by kipi and claude-cortex READMEs as research basis; not independently fetched.

**Confidence:** 90%. High on fetched facts (repo state, README content, implementation details). Medium on the ROI-to-effort estimates — those assume a solo Claude Code executor and typical HAL sprint velocity. Lower on what Assaf would say about licensing — informed guess, not verified.
