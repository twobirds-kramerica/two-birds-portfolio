# Loop: PR Babysitter
**Pattern:** Boris Cherny — "I have one that's babysitting my PRs like fixing CI auto rebasing"
**Interval:** On-demand or daily via Task Scheduler
**Repos:** two-birds-portfolio, digital-confidence, clarity, career-coach, aaron-patzalek, two-birds-innovation

---

## Prompt (paste at session start)

```
PR BABYSITTER LOOP — Two Birds Innovation
Read SESSION-STATE.md before starting.

PHASE 1 — SCAN OPEN PRs (5 min)

For each repo in C:\twobirds\:
  git fetch origin
  git log --oneline origin/master..HEAD (check if local is ahead)
  git status (check for uncommitted changes)

Report:
- Any branches ahead of master with no open PR
- Any uncommitted changes sitting in working tree
- Any merge conflicts

PHASE 2 — CI HEALTH CHECK (5 min)

Check the most recent GitHub Actions run status for:
  - two-birds-portfolio (axe-core + link checker + gitleaks)
  - digital-confidence (content-count, build-health)

Use: gh run list --limit 3 --repo twobirds-kramerica/[repo]

For any FAILED run:
  - Read the failure log: gh run view [id] --log-failed
  - If the fix is a 1-line change (printf, YAML syntax, etc.) apply it and commit
  - If the fix requires more than 5 minutes, log to SESSION-STATE.md under "CI Blockers"

PHASE 3 — STALE BRANCH ALERT (2 min)

For each repo:
  git branch -a --sort=-committerdate | head -10
  Flag any branch not merged to master that is >14 days old.
  List them in SESSION-STATE.md under "Stale Branches".

PHASE 4 — REPORT

Append to SESSION-STATE.md:
---
## PR Babysitter Run — [DATE]
- Repos scanned: N
- CI failures found: N (list)
- Fixes applied: N (list commits)
- Stale branches: N (list)
- Uncommitted work: N (list)
---

Commit: chore(loop): pr-babysitter run [DATE]
Push to master.
```

---

## Notes
- Never force-push. Never reset --hard. Flag conflicts to Aaron.
- Only auto-fix CI failures that are clearly mechanical (YAML syntax, printf flag, missing file reference).
- Leave anything requiring product judgement for Aaron.
