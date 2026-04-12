<!--
STATUS: v0.2 — TEMPLATE
Created: 2026-04-11 16:10 EST (Toronto)
Updated: 2026-04-11 22:58 EST (Toronto)
-->

# Sprint Template

Copy this template to add a new sprint to `sprint-queue.md`.

---

```
## S-[NNN]: [Title]

**Priority:** P[1/2/3]
**Duration:** [estimate]
**Status:** READY / BLOCKED / DONE
**Blocked by:** [what must happen first, or "—"]
**Layer:** [L1-L4]
**Story refs:** [S1.1, S5.6, etc.]

### Prompt

AUTONOMOUS SPRINT — [TITLE]
Repo: C:\twobirds\two-birds-portfolio\
Read SESSION-STATE.md before starting. Commit after each phase.

PHASE 0 — PROCESS PENDING CAPTURES (mandatory)

Read hal-stack/sprint-system/pending-capture.md.
If the "Current Queue" section contains any items:
1. For each item, route to destination based on TYPE:
   - human-backlog → append to sprint-system/human-backlog.md
   - story → append to backlog/stories.md
   - epic → append to backlog/epics.md
   - blocker → flag at top of session results as highest priority
   - issue → append to backlog/stories.md as P1 bug
2. Preserve priority, category, context, and action
3. Clear merged items from pending-capture.md (keep header, empty queue)
4. Commit: "chore(hal): merged [N] captured items from pending queue"
If pending-capture is empty, skip to Phase 1.

[PHASE 1+ — Sprint-specific work here]

FINAL STEP: Update SESSION-STATE.md, auto-generate context export,
commit, push to master.

### Expected Outputs
- [file or commit expected]
- [file or commit expected]
```

---

## Rules Every Sprint Prompt Must Include

1. **PHASE 0 — Process pending captures.** NON-NEGOTIABLE. Every sprint checks `pending-capture.md` first so nothing Aaron logged gets lost.
2. `Read SESSION-STATE.md before starting`
3. `Commit after each phase`
4. `Update SESSION-STATE.md` at the end
5. `Auto-generate context export` at the end
6. `Push to master` at the end
7. Quality over completeness
8. No scope creep — improvements go to backlog
9. Plain language, timestamps on all files
