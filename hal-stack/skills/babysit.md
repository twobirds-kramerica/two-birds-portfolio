# Skill: /babysit
**Domain:** Engineering / CI
**Layer Compatibility:** L1-L4
**Loop command:** `/loop 5m /babysit`
**Source:** Boris Cherny pattern — `/loop 5m /babysit`

## What It Does
Scans all Two Birds repos for CI failures and mechanical issues, applies safe fixes,
and reports anything requiring human judgement to SESSION-STATE.md.

## Instructions

1. **Fetch all repos**
   ```
   for each repo in [two-birds-portfolio, digital-confidence, clarity, career-coach, aaron-patzalek, two-birds-innovation]:
     git fetch origin
     git status --short
   ```

2. **CI health check**
   ```
   gh run list --limit 3 --repo twobirds-kramerica/two-birds-portfolio
   gh run list --limit 3 --repo twobirds-kramerica/digital-confidence
   ```
   For any FAILED run:
   - `gh run view [id] --log-failed`
   - If fix is ≤5 min and mechanical (YAML syntax, printf flag, missing file ref, Canadian English typo): apply it, commit, push
   - If fix requires product judgement: log to SESSION-STATE.md under "CI Blockers — needs Aaron"

3. **Stale branch scan**
   ```
   git branch -a --sort=-committerdate | grep -v "HEAD\|master\|main"
   ```
   Flag any unmerged branch >14 days old → SESSION-STATE.md "Stale Branches"

4. **Uncommitted work scan**
   Check `git status` for each repo. Flag anything uncommitted >24 hours old.

5. **Report** (append to SESSION-STATE.md, one block per run)
   ```
   ## /babysit — [DATE TIME]
   - CI: [PASS / N failures fixed / N blockers flagged]
   - Stale branches: [none / list]
   - Uncommitted: [none / list]
   ```

6. **Commit if any fixes applied**
   ```
   git commit -m "fix(babysit): [description of fix]"
   git push origin master
   ```

## Quality Checklist
- [ ] Every FAILED CI run has been read (not just listed)
- [ ] Fixes applied are mechanical only — no product changes
- [ ] Anything needing Aaron is in SESSION-STATE.md with "needs Aaron" tag
- [ ] No force pushes

## Referenced By
- `loop-pr-babysitter.md` — schedule wrapper
- `.claude/loop.md` — runs as section 1 of the default maintenance loop
