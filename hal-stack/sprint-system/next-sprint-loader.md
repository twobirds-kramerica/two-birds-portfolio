<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 16:20 EST (Toronto)
Confidence: HIGH
Known gaps: Claude Code CLI invocation from batch file needs testing
-->

# "Next Sprint" Trigger

## How It Works

1. Aaron opens Claude Code on any machine
2. Types the short command below
3. Claude Code reads the sprint queue, finds the top READY sprint
4. Executes the prompt from that sprint entry
5. When done: marks it DONE, updates SESSION-STATE.md, pushes

## The Command (copy-paste or memorise)

```
Read C:\twobirds\two-birds-portfolio\hal-stack\sprint-system\sprint-queue.md — find the first sprint with status READY. Execute its prompt exactly as written. When done, change its status to DONE, add today's date, update SESSION-STATE.md with the results, auto-generate context export, commit, and push to master.
```

## Short Version (phone-friendly)

```
next sprint
```

This works because CLAUDE.md already has a trigger for "next sprint." The difference: CLAUDE.md's current trigger says "read backlog, execute top 3 items." We should update CLAUDE.md to point to the sprint queue instead. Until then, use the full command above.

## What Happens If There Are No READY Sprints

Claude Code will report: "No READY sprints in the queue. All items are either DONE or BLOCKED. Check human-backlog.md for actions that unblock them."

## What Happens If a Sprint Fails Mid-Way

Claude Code should:
1. Commit whatever completed successfully
2. Mark the sprint as BLOCKED with a note explaining what failed
3. Add the failure to SESSION-STATE.md
4. Push what was committed
5. Aaron reviews the failure in the next retro
