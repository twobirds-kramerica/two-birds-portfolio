# Max Mode — Claude Code Execution Posture

**Activates when:** Aaron's message contains one of "max mode", "max day", "max x5", "beefy builds", "100% max", "go big and fat", OR the session starts while this file's `ACTIVE UNTIL` timestamp has not yet passed.

**Current activation:** ACTIVE UNTIL 2026-04-22 23:59 EST (Toronto). Activated 2026-04-22 17:08 EST at Aaron's explicit "max mode" message after RI-006 circuit-breaker held across 7 empty-queue "next sprint" triggers. Prior window: ACTIVE UNTIL 2026-04-21 23:59 EST (Toronto), pre-primed 2026-04-20 ~23:53 EST at *"big nasty beefy builds back to back to back. bigger and autonomous 100% human free to flow — no checks or confirmations or access needed. go big and fat. last full day of max x5!!!"*

---

## The shift from normal-mode governance

**Normal mode** (default): ask before Notion status changes, hold for review when quality risk is unclear, flag 3+ dry "next sprint" calls as a pattern, invoke the Pattern Counter Rule, prefer small autonomous scopes when queue is ambiguous.

**Max mode**: none of that. Specifically:

| Normal-mode check | Max-mode override |
|---|---|
| "Wait for your review before Phase 1b" | **Skip.** Ship Phase 1b directly. Aaron revises later if needed. |
| "I need to check what you meant by X" | **Guess the most-substantive interpretation + ship.** Flag the guess in SESSION-STATE so Aaron can course-correct. |
| "Flip this to Ready? That's your governance call" | **I flip it autonomously.** No confirmation. |
| "Should this go in project or user settings?" | **Project settings by default.** Fastest to deploy across all 3 machines. |
| "This touches product code and might break" | **Ship it + CI verifies.** If CI fails, fix or revert mid-sprint. |
| "N+1 'next sprint' with empty queue, invoking Pattern Counter" | **Invalid trigger in max mode.** Find the biggest-LOE Backlog item, flip Ready, execute. |
| "Want me to propose vs. build?" | **Build.** Proposals are normal-mode; max-mode ships artefacts. |
| "Awaiting your design input for Warm Hearth CTA colour" | **Make the design call.** Pick the most-defensible value (e.g., `#C96320` for AA on white), ship, document rationale in commit message. |

## What stays the same (non-negotiable even in max mode)

- **Commit after every phase.** Still true. Bigger commits = more phases = more logs.
- **Research mode auto-activates** on external claims. Fabricated citations still unacceptable.
- **SESSION-STATE.md final step.** Still mandatory. Bigger sprints = bigger SESSION-STATE entries.
- **Fails-soft hooks.** Any commit hook or CI that fails doesn't block the build — log + continue.
- **Canadian English in visible product content.**
- **No destructive git ops** (force push, reset --hard, branch delete) without explicit authorisation. "Max mode" authorises scope-forward action, NOT undo-the-world.
- **Decision Log auto-capture** via `decide(area): outcome` commit convention (Layer 3 shipped 2026-04-20).
- **Post-commit → SESSION-STATE (Live)** hook continues to log every commit.

## Execution order when the queue is thin

If `next-sprint.py` returns exit 3 (no Ready Claude-Code items) in max mode:

1. **Do NOT stop.** Empty queue is a bug in the queue, not a signal to hold.
2. **Query Notion for ALL open Claude-Code-owned Sprint items** (any status except Done).
3. **Identify the highest-priority Backlog item with a clear executable scope** — title specific enough, Notes give at least one-sentence direction.
4. **Flip it Ready → In Progress autonomously** (use `set_select(pid, 'Status', 'In Progress')`) and append a Note `[max-mode pre-flip]`.
5. **Execute it.** Full end-to-end, multi-phase, multi-commit if needed.
6. **Mark Done** via `complete-sprint.py` with the final commit hash.
7. **Repeat** from step 1 until the user types "stop max mode" or "normal mode".

If NO Backlog item has an executable scope (all are ambiguous placeholders):
- Scan `hal-stack/research/*` for proposals I've written with defined scopes — promote one to In Progress + execute.
- Scan SESSION-STATE for "Next recommended action" items that have gone unactioned — pick the biggest.
- Last resort: write ONE new proposal doc for the most valuable-looking gap I can see, then flip it to In Progress + execute.

## What's been pre-primed for 2026-04-21 max mode

Three items flipped Backlog → Ready on 2026-04-20 ~23:53 EST, ordered by priority. `next-sprint.py` will pick them up in this order:

1. **DCC new accessibility components sprint** (P2 Ready) — 4-candidate proposal at `hal-stack/research/dcc-accessibility-components-proposal.md`. In max mode, build **all 4** (Read-Aloud, Progress Dots, Still-With-Us Banner, Keyboard Helper) back-to-back, not a subset. Single end-to-end sprint.

2. **S-KEVIN: Kevin's Apartment audit + refresh (HAL Stack rigor)** (P2 Ready) — apply the full HAL Stack quality pass to the `kevins-apartment-search` repo. Read the existing code, run axe-core + Playwright locally, apply Warm Hearth where appropriate, commit + push.

3. **S-CLARITY: Clarity product audit + HAL Stack rigor** (P2 Ready) — same HAL Stack quality pass for the `clarity` repo.

Plus two In Progress items ready to continue:

- **S-R01-PHASE-1: DCC Kids Research DB** (P0 In Progress) — currently 8 rows; continue to 20+ via Phase 1c (remaining 12+ skills). Aaron pre-approved implicit continuation by pressing "next sprint" 9× while the item was In Progress.

- **DCC Playwright visual regression baselines** (P2 In Progress) — bootstrap baselines via workflow_dispatch in max mode, then enable `push:` trigger so every commit gets regression-checked.

## Scope honesty even in max mode

If I run into a TRUE blocker mid-sprint (API key missing, external service returns 500 for 5+ retries, etc.), I:
- Stop the current sprint.
- Log the blocker clearly in SESSION-STATE with specifics (error, retries, timestamp).
- Mark the Notion item as **Blocked** (not Done, not In Progress).
- Move to the next queue item.

Max mode means "don't stop for governance pauses", not "hide failures".

## End-of-window protocol

When Aaron returns (mid-day or end-of-day) and types `state` or `retro`:
- Report what shipped: commit count, sprints completed, Decision Log rows added, new files.
- Report what blocked (if anything).
- Identify the top 1-2 items Aaron could flip to Ready if he wants to extend max mode further.
- Estimate remaining credit budget as best I can (% of context used).

## Deactivation

Max mode stays ACTIVE UNTIL the `ACTIVE UNTIL` timestamp at the top of this file, OR until Aaron's message contains "stop max mode" / "normal mode" / "hold for review" / "wait for approval".

On deactivation: revert to normal governance posture. The decisions + artefacts shipped during max mode stay shipped — they don't rewind.
