# Codeberg Mirror Status

**Date:** April 4, 2026
**Audit result:** No Codeberg mirrors configured on any repository.

---

## Current Status

| Repo | Codeberg Remote | Status |
|------|----------------|--------|
| digital-confidence | ❌ Not configured | Needs setup |
| career-coach | ❌ Not configured | Needs setup |
| clarity | ❌ Not configured | Needs setup |
| two-birds-portfolio | ❌ Not configured | Needs setup |
| two-birds-innovation | ❌ Not configured | Needs setup |
| aaron-patzalek | ❌ Not configured | Needs setup |
| kevins-apartment-search | ❌ Not configured | Can wait |
| two-birds-command-centre | ❌ Not configured | Can wait |
| quality-dashboard | ❌ Not configured | Can wait |
| elite-karate-site | ❌ Not configured | Can wait |

---

## Setup Instructions (Aaron — 30 Minutes Total)

### Step 1: Create Codeberg Account
1. Go to [codeberg.org](https://codeberg.org)
2. Click "Register"
3. Username: `twobirds` or `aaronpatzalek`
4. Email: aaron.patzalek@gmail.com

### Step 2: Create Organisation
1. Click your avatar → "New Organisation"
2. Name: `twobirds-innovation`

### Step 3: Create Empty Repos on Codeberg
For each repo, create a new empty repository on Codeberg with the same name.

### Step 4: Add Remotes (Run in Windows Terminal)
```powershell
cd C:\twobirds\digital-confidence
git remote add codeberg https://codeberg.org/twobirds-innovation/digital-confidence.git
git push codeberg main --all

cd C:\twobirds\career-coach
git remote add codeberg https://codeberg.org/twobirds-innovation/career-coach.git
git push codeberg main --all

cd C:\twobirds\clarity
git remote add codeberg https://codeberg.org/twobirds-innovation/clarity.git
git push codeberg master --all

cd C:\twobirds\two-birds-portfolio
git remote add codeberg https://codeberg.org/twobirds-innovation/two-birds-portfolio.git
git push codeberg master --all

cd C:\twobirds\two-birds-innovation
git remote add codeberg https://codeberg.org/twobirds-innovation/two-birds-innovation.git
git push codeberg master --all

cd C:\twobirds\aaron-patzalek
git remote add codeberg https://codeberg.org/twobirds-innovation/aaron-patzalek.git
git push codeberg master --all
```

### Step 5: Add to Overnight Build Script
Add these lines to `C:\twobirds\run-overnight-build.bat` after the main Claude Code section:

```batch
REM Mirror to Codeberg
cd /d C:\twobirds\digital-confidence
git push codeberg main 2>>C:\twobirds\two-birds-portfolio\logs\codeberg-sync.log
cd /d C:\twobirds\career-coach
git push codeberg main 2>>C:\twobirds\two-birds-portfolio\logs\codeberg-sync.log
cd /d C:\twobirds\clarity
git push codeberg master 2>>C:\twobirds\two-birds-portfolio\logs\codeberg-sync.log
```

---

## Priority Order
1. digital-confidence (revenue product, 241+ pages)
2. career-coach (revenue product)
3. clarity (revenue product)
4. two-birds-portfolio (business intelligence)
5. two-birds-innovation (company site)
6. aaron-patzalek (personal brand)
7–10. Remaining repos (when time allows)

---

## Verification
After setup, run `git remote -v` in each repo. You should see both `origin` (GitHub) and `codeberg` remotes listed.
