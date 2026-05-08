# HAL Stack — Automation Map
**Created:** 2026-05-08 | **Source:** Boris Cherny /loop research + official CC docs

Every recurring HAL Stack job mapped to the right automation tier.

---

## Tier definitions

| Tier | Tool | Session needed | Machine needed | Cost |
|------|------|---------------|----------------|------|
| **1 — Active session** | `/loop` + named skills | Yes | Yes | Free |
| **2 — Machine unattended** | Task Scheduler + `run-overnight-build.bat` extension | No | Yes (2 AM) | Free |
| **3 — GitHub Actions** | `.github/workflows/*.yml` | No | No | Free (public repos) |
| **4 — Anthropic cloud** | `/schedule` Routines | No | No | Token cost, 1hr min |

---

## Full job map

### Engineering / CI

| Job | Current state | Tier | Command | Frequency |
|-----|--------------|------|---------|-----------|
| CI failure detection + fix | Manual (babysitter loop new today) | **1** | `/loop 5m /babysit` | During active work |
| Stale branch scan | Manual | **1** | included in `/babysit` | During active work |
| gitleaks secret scan | ✅ GitHub Actions live | **3** | `.github/workflows/ci.yml` | Every push |
| axe-core accessibility | ✅ GitHub Actions live | **3** | `.github/workflows/ci.yml` | Every push |
| External link checker | ✅ GitHub Actions live | **3** | `.github/workflows/ci.yml` | Every push |
| DCC build health report | ✅ GitHub Actions live (fixed today) | **3** | `build-health-report.yml` | Daily 7 AM |
| Lighthouse audits | ✅ `run-overnight-build.bat` | **2** | Batch script | Daily 2 AM |

### Backlog / Sprint management

| Job | Current state | Tier | Command | Frequency |
|-----|--------------|------|---------|-----------|
| Next sprint pull | Manual (`next sprint` trigger) | Human | `python next-sprint.py` | Session start |
| Backlog health check | Manual (new today) | **1** | `/loop 60m /backlog-triage` | During long sessions |
| P1 items going cold | ❌ Not automated | **2** | Add to `run-overnight-build.bat` | Weekly (Sun 8 PM) |
| Notion sync verify | Manual (new today) | **2** | Add to `run-overnight-build.bat` | Daily 6 AM |

### Content

| Job | Current state | Tier | Command | Frequency |
|-----|--------------|------|---------|-----------|
| DCC module freshness | ❌ Script exists, not scheduled | **2** | Add to `run-overnight-build.bat` | Weekly (Mon 6 AM) |
| Brand site lastmod check | ❌ Not automated | **2** | Add to `run-overnight-build.bat` | Weekly (Mon 6 AM) |
| Canadian English scan | Manual (part of /babysit quiet pass) | **1** | included in `.claude/loop.md` | Every loop iteration |
| DCC Research DB stretch | Manual sprints | Human | `next sprint` | As needed |

### Git / Repo health

| Job | Current state | Tier | Command | Frequency |
|-----|--------------|------|---------|-----------|
| All-repo git pull + push | ✅ `run-overnight-build.bat` | **2** | Batch script | Daily 2 AM |
| Codeberg mirror push | ✅ `run-overnight-build.bat` | **2** | Batch script | Daily 2 AM |
| SESSION-STATE commit log | ✅ PostToolUse hook | **1** | `settings.json` hook | Every git commit |

---

## What to build next (priority order)

### 1. Extend `run-overnight-build.bat` — Tier 2 gaps
Add these three blocks to the existing overnight .bat file:

```batch
REM --- Notion sync verify (daily 2 AM) ---
cd C:\twobirds\two-birds-portfolio
python hal-stack/notion-sync/next-sprint.py >> logs\automated-run-log.md 2>&1

REM --- Content freshness (weekly, Mondays only) ---
if "%WEEKDAY%"=="Mon" (
  node hal-stack/content-freshness/check-freshness.js >> logs\automated-run-log.md 2>&1
)

REM --- Backlog health (weekly, Sundays only) ---
if "%WEEKDAY%"=="Sun" (
  claude -p "/backlog-triage" >> logs\automated-run-log.md 2>&1
)
```

### 2. Add a `daily-report` GitHub Actions workflow to two-birds-portfolio
Mirror what DCC already has. Fires at 7 AM, opens an issue with:
- Last 5 commits
- Any open CI failures
- Backlog P1 count

### 3. When to add Tier 4 (Routines)
Only if Aaron needs a job to run while the machine is **off** (travel, etc.).
Minimum 1-hour interval. No local file access. Token cost.
Not needed now — machine is on nightly.

---

## `.claude/loop.md` coverage

Bare `/loop` now covers these automatically during active sessions:

| Section | Skill | What it does |
|---------|-------|-------------|
| 1 | `/babysit` | CI health + stale branches |
| 2 | _(inline)_ | Unfinished work from SESSION-STATE |
| 3 | `/backlog-triage` (lightweight) | P1 cold / orphaned In Progress |
| 4 | _(inline)_ | Canadian English + gitleaks quiet pass |
