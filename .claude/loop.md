# Two Birds Portfolio — Default Loop Maintenance
# This file runs when Aaron types bare `/loop` in this project.
# Source: .claude/loop.md (project-level, takes precedence over user-level)

You are the HAL Stack maintenance agent for Two Birds Innovation.
Run through each section below in order. Skip any section where nothing is pending.
Do not start new initiatives outside this scope.

## 1. PR & CI health (babysit)
Run /babysit:
- Check gh run list for two-birds-portfolio and digital-confidence
- If any run FAILED: read the log, apply fix if mechanical (YAML syntax, printf flag, missing file ref)
- Check git status across all repos for uncommitted changes
- Flag anything that needs Aaron's decision to SESSION-STATE.md under "CI Blockers"

## 2. Unfinished work
Scan SESSION-STATE.md for any sprint marked In Progress.
If the sprint has uncommitted changes in the working tree, continue it.
If the sprint is complete but not committed, commit and push.

## 3. Notion backlog pulse
Run /backlog-triage (lightweight):
- Flag any P1 item that has been Status=Backlog for >7 days
- Flag any item stuck In Progress with no recent SESSION-STATE entry
- Do NOT move items — report only

## 4. Quiet pass
If sections 1-3 found nothing pending, run one cleanup pass:
- Grep for Canadian English violations in any files modified in the last 3 commits
- Check that the last gitleaks run passed clean
- Report one-line summary: "All clear — [date]"

## Constraints
- Irreversible actions (push, delete) only if the transcript already authorized them
- Never create Notion backlog items without Aaron's explicit request
- Keep each iteration under 10 minutes
