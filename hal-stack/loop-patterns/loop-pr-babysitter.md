# Loop: PR Babysitter
**Pattern:** Boris Cherny — `/loop 5m /babysit` (exact command, cited Threads post)
**Tier:** 1 — Active session only (requires open terminal)
**Skill:** `hal-stack/skills/babysit.md`

---

## How to run

```
/loop 5m /babysit
```

That's it. Boris's exact pattern. The skill (`/babysit`) contains the logic.
The loop fires it every 5 minutes while your session is open.

To run once manually (no loop):

```
/babysit
```

---

## What `/babysit` does each iteration

See full logic in `hal-stack/skills/babysit.md`. Summary:

1. Fetch all Two Birds repos — check for CI failures
2. For any FAILED run: read log, apply fix if mechanical (≤5 min), commit
3. Scan for stale branches (>14 days unmerged)
4. Report to SESSION-STATE.md

---

## loop.md integration

Bare `/loop` in the `two-birds-portfolio` project automatically runs babysit
as part of the `.claude/loop.md` maintenance default. You don't need to type
`/loop 5m /babysit` explicitly unless you want the faster 5-minute cadence.

---

## Notes
- Never force-push. Never reset --hard. Flag conflicts to Aaron.
- Only auto-fix CI failures that are clearly mechanical (YAML syntax, printf flag, missing file reference).
- Leave anything requiring product judgement for Aaron.
- This loop stops when you close the terminal. For overnight CI monitoring, use GitHub Actions (already live).
