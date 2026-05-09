# Sprint-system helpers (2026-04-22)

Three pure-Python helpers any sprint's FINAL STEP can call. No npm, no Node, no
external services beyond the existing Notion sync. All three shipped as part
of S-LOOP-ARCHITECT (3/4 components; watcher daemon rejected on design grounds —
a local daemon cannot spawn authenticated Claude Code sessions; use the
`schedule` skill or `/loop` + `ScheduleWakeup` for overnight chaining).

## failure-router.py

Route a sprint failure to Notion + aaron-todos without halting the loop.

```python
# Python import form (preferred inside Python sprints)
import sys
sys.path.insert(0, "hal-stack/sprint-system")
from failure_router import route_failure

try:
    do_sprint_step()
except Exception as e:
    route_failure(
        sprint_id="S-FOO-BAR",
        step="Step 3: deploy to Vercel",
        error=str(e),
        recommended_fix="Complete Vercel OAuth at the login URL above",
        product="DCC",
    )
    # Loop continues; next sprint can still run.
```

```bash
# CLI form (for shell-script sprints)
python hal-stack/sprint-system/failure-router.py \
    --sprint-id S-FOO-BAR \
    --step "Step 3: deploy to Vercel" \
    --error "No credentials found" \
    --fix "Complete Vercel OAuth" \
    --product DCC
```

**Routes to:**
1. Notion Product Backlog row (P1 Blocked, Owner=Aaron, Type=Human Action)
2. `aaron-todos-YYYY-MM-DD.md` appended under "P1 — Autonomous failures routed here"

Exit 0 if either surface succeeds. Exit 1 only if both fail (rare; you still
shouldn't halt the loop — log locally and continue).

## human-task-capture.py

Regex-scan arbitrary text (commit messages, SESSION-STATE entries, sprint
output) for human-action markers and auto-file each to Notion.

Recognised markers (colon required to prevent prose false positives):
`TODO:`, `BLOCKED:`, `HUMAN NEEDED:`, `MANUAL STEP:`, `NEEDS AARON:`, `AARON TO DO:`

```bash
# Pipe any sprint output through it
some-script.py | python hal-stack/sprint-system/human-task-capture.py --source S-FOO-BAR --product DCC

# Or scan a file directly
python hal-stack/sprint-system/human-task-capture.py --file SESSION-STATE.md --source session-22
```

```python
# Python form
from human_task_capture import scan_and_file
n_filed = scan_and_file(text, source="S-FOO-BAR", product="DCC")
```

Dedupe-aware within a single run. Matches `BLOCKED` / `HUMAN NEEDED` / `MANUAL STEP`
file as `Status=Blocked`; other markers file as `Status=Backlog`.

## trigger-writer.py

Writes `NEXT-SPRINT-TRIGGER.md` (authoritative next-sprint marker) or
`QUEUE-EMPTY.md` (loop stops here). Does NOT itself spawn a new session —
see below for the "who actually picks up the baton" question.

```bash
# Explicit next sprint
python hal-stack/sprint-system/trigger-writer.py --next S-FOO-BAR

# Pull next Ready sprint from Notion
python hal-stack/sprint-system/trigger-writer.py --next-from-notion

# Queue empty (loop exits)
python hal-stack/sprint-system/trigger-writer.py --empty
```

Keeps an append-only log at `hal-stack/sprint-system/trigger-writer-log.md`.

## Who picks up the baton after the trigger is written?

`trigger-writer.py` writes a marker file. A separate mechanism must actually
start the next Claude Code session:

- **`schedule` skill** (recommended for overnight) — creates an Anthropic-side
  scheduled agent that runs cron-scheduled. Requires Aaron's explicit setup
  (paid-token concern; will burn tokens at intervals until canceled).
- **`/loop` + `ScheduleWakeup`** — keeps an already-open session alive by
  self-pacing. Max 1 hour between wake-ups. What tonight's ~27-hour run
  effectively was.
- **Manual** — Aaron opens a fresh session and types `next sprint`. The
  `next-sprint.py` script reads Notion and locks the next item.

A local Python watcher daemon CANNOT spawn authenticated CC sessions; that
approach was rejected in S-LOOP-ARCHITECT.

## Recommended FINAL STEP template

```python
# At end of any sprint:
import subprocess, sys, traceback
from pathlib import Path

sys.path.insert(0, "hal-stack/sprint-system")
from failure_router import route_failure
from human_task_capture import scan_and_file

SPRINT_ID = "S-YOUR-SPRINT"

try:
    # 1. Write SESSION-STATE.md entry (per CLAUDE.md)
    # 2. Commit + push
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", f"feat: {SPRINT_ID}"], check=True)
    subprocess.run(["git", "push"], check=True)

    # 3. Scan the SESSION-STATE entry + commit message for human-action markers
    text = Path("SESSION-STATE.md").read_text(encoding="utf-8").split("---")[-1]
    scan_and_file(text, source=SPRINT_ID)

    # 4. Write the trigger marker
    subprocess.run([sys.executable, "hal-stack/sprint-system/trigger-writer.py",
                   "--next-from-notion"], check=False)
except Exception as e:
    route_failure(
        sprint_id=SPRINT_ID,
        step="FINAL STEP",
        error=f"{type(e).__name__}: {e}\n\n{traceback.format_exc()}",
        recommended_fix="Review the error; manually complete git push + SESSION-STATE update.",
    )
    # Do NOT re-raise; let the loop continue.
```

Last updated: 2026-04-22 at 03:15 EST (Toronto)
