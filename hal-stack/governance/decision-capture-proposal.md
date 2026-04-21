# Decision Capture — Governance Fix Proposal

**Date:** 2026-04-20
**Sprint:** S-FORENSICS — Decision archaeology + governance gap analysis
**Context:** Three decisions (Warm Hearth palette vote, font legal discussion, Legal/CTO veto power) were reconstructed into the Notion Decision Log. Two of three had PARTIAL capture: the *outcomes* were well-documented, the *origin discussions* were lost.

---

## The loss pattern (observed across all 3 decisions)

| Loss mode | Warm Hearth vote | Font legal | Legal/CTO veto |
|-----------|------------------|------------|----------------|
| Outcome documented in repo / Notion? | ✅ multiple places | ✅ licence file, commit | ✅ 3 places |
| Origin discussion (who, when, alternatives) documented? | ❌ Claude.ai chat only | ❌ Claude.ai chat only | ⚠ partial |
| Recoverable without Claude.ai export? | ❌ | ❌ | ✅ |
| Recoverable WITH Claude.ai export? | likely yes | likely yes | yes |

**The single pattern:** decisions made in a Claude.ai *chat* never get archived as structured records. The Claude instance cannot proactively write to Notion mid-chat (no Notion MCP write tool in the chat), so the decision lives in chat-history only. Until the user copies it out or remembers to capture it, it's effectively ephemeral.

**The downstream effect:** the OUTCOME propagates (it gets coded into a Claude Code sprint or a doc edit), but the RATIONALE — "why did we pick Merriweather specifically?" — disappears. Future-Aaron asking that question has to reconstruct from memory.

---

## Proposed fix (three layers)

### Layer 1: Claude.ai user-preference rule (highest leverage, lowest effort)

Add the following rule to Aaron's Claude.ai user preferences, near the existing voice-check + N.B. rules:

> **Decision-capture rule.** When a chat contains a DECISION — a choice between options, a policy change, a scope change, a rule adoption, a naming call — Claude MUST, before closing the topic, offer to capture the decision to the Notion Decision Log (data source `03198a8f-849e-41ee-ba85-b22019841ce7`). The offer is one line:
>
> `[decision capture] → Notion Decision Log? (Decision, Context, Outcome, Participants, Veto-Power)`
>
> Aaron says yes/no/modify. On yes, Claude uses the Notion MCP write tool to create the row directly. If the tool isn't loaded, Claude calls `tool_search` for "notion" before asking Aaron to paste anything. On no, Claude offers to log it to `hal-stack/sprint-system/pending-capture.md` via a Claude Code prompt.
>
> The trigger signal is strong — Claude surfaces the offer even if the chat's primary purpose is something else. Missing a decision capture is the failure mode this rule exists to prevent.

### Layer 2: Claude Code `capture:` command enhancement

Today, `capture: <item>` in a Claude.ai chat generates a Claude Code prompt that appends to `pending-capture.md`. Extend that prompt template (at `hal-stack/sprint-system/capture-prompt.md`) so when the captured item has `TYPE: decision`, it routes to the Decision Log DB in Notion instead of `pending-capture.md`.

Specifically, the capture template's routing table gains a row:

| TYPE | Destination |
|------|-------------|
| human-backlog | `hal-stack/sprint-system/human-backlog.md` |
| story | `hal-stack/backlog/stories.md` |
| epic | `hal-stack/backlog/epics.md` |
| blocker | `hal-stack/sprint-system/sprint-queue.md` status=BLOCKED |
| issue | `RELIABILITY-ISSUES.md` |
| **decision** | **Notion Decision Log data source `03198a8f-849e-41ee-ba85-b22019841ce7`** |

With a specific field-mapping: the capture template prompts Claude.ai to fill Decision / Context / Outcome / Participants / Where-Logged / Veto-Power — and only then emits the Claude Code prompt.

### Layer 3: Post-commit decision flag (uses the hook just shipped)

The post-commit → Notion hook shipped this session (commit `8748048`) logs every commit to the SESSION-STATE (Live) page. Extend it with one rule: if the commit message subject line starts with `decide(` (conventional-commit-like type), ALSO append a stub row to the Decision Log DB with Status=Logged. The stub prompts Aaron to fill in Where-Logged / Veto-Power / Participants later via Notion UI.

Example: `decide(palette): adopt Warm Hearth (Option A, 65.5% weighted vote)` → auto-creates a Decision Log row with Decision = subject line, Date = commit date, Evidence-Link = commit URL.

This makes the commit itself the capture surface for decisions made during Claude Code sessions.

---

## Recommended adoption order

1. **Layer 3 first** (smallest change): extend the post-commit hook to detect `decide(...)` conventional-commit prefix. ~30 min of work — edit `hal-stack/notion-sync/post-commit-hook.py`, test with one test-commit, ship. Benefits: zero user-side behaviour change, captures any future Claude Code decision automatically.

2. **Layer 1 next** (highest leverage but requires behaviour change): Aaron pastes the decision-capture rule into Claude.ai user preferences. ~5 min. Benefits: every future chat that surfaces a decision offers capture. Failure mode: if Claude.ai side doesn't have Notion MCP write tool loaded, the fallback is the `capture:` command (Layer 2).

3. **Layer 2 last** (glue): update `hal-stack/sprint-system/capture-prompt.md` to include the decision → Notion routing. ~15 min. Benefits: closes the fallback path when Layer 1 can't write directly.

Total effort: ~50 min across all three. Highest payoff: Layer 1.

---

## Out of scope for this proposal (but related)

- **Back-populating the Decision Log from Claude.ai export.** Blocked on the export being available (S-026 Full Context Re-Audit is the umbrella sprint for this). Once the export lands, a Claude Code sprint can scan conversations, extract decisions, and populate Decision Log rows with full origin discussion. This would recover the font-legal discussion and the original Warm Hearth vote artefact.
- **Decision-review cadence.** Decision Log is append-only today. A separate proposal could introduce a "review open decisions monthly" cadence where Aaron (or the inner-circle persona layer) revisits logged decisions to flag any that need revisiting.
- **Veto-exercise audit trail.** Currently there's no record of Helen or Naveen actually exercising a veto. A P3 follow-up: add a `Veto-Exercised-Date` + `Veto-Rationale` pair of fields to the Decision Log schema so when a veto IS used, it's captured.

---

## Deliverables for this sprint

- ✅ 3 rows in the Decision Log DB (data source `03198a8f-849e-41ee-ba85-b22019841ce7`) — one per reconstructed decision.
- ✅ Three Status values assigned per evidence quality: Missing-From-Backlog (Warm Hearth vote), Actioned (Font licensing — outcome landed; origin discussion missing), Logged (Legal/CTO veto — rule documented across 3 durable locations).
- ✅ This proposal doc (3-layer governance fix).

Confidence: 85%. High on the loss-pattern analysis (evidence gathered from git log, repo grep, Notion search — the pattern is consistent across all three). Medium on the fix effort estimates (Layer 1 depends on whether Notion MCP write tools are available in Aaron's Claude.ai today — hasn't been verified). 15% reserved for: the Claude.ai-side rule implementation may need tuning once it's tried in practice — false positives (Claude offering capture on non-decisions) is the likely first failure mode.

## Next action

Aaron reviews the 3 Decision Log rows in Notion. If the reconstruction is roughly accurate, Layer 3 (hook extension) is the smallest next sprint to ship.
