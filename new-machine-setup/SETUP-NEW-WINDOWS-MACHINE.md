# Claude Code New Machine Setup — Windows
Estimated time: 15 minutes. Works on Windows 10 and 11.

## BEFORE YOU START
- Right-click paste works when Ctrl+V does not — use it everywhere in terminal
- Always open PowerShell as Administrator (right-click → Run as Administrator)
- Have ready: GitHub credentials (twobirdsinnovation@gmail.com), Anthropic API key

## STEP 1 — Install prerequisites
Open PowerShell as Administrator. Right-click paste each line one at a time:
```
winget install --id Git.Git
winget install --id GitHub.cli
winget install --id OpenJS.NodeJS
```
Close and reopen PowerShell as Administrator after all three installs.

## STEP 2 — Install Claude Code
```
npm install -g @anthropic-ai/claude-code
claude --version
```
Should show version number. If command not found, close and reopen PowerShell.

## STEP 3 — Authenticate GitHub and Claude
```
gh auth login
```
Choose: GitHub.com → HTTPS → Login with web browser → paste the one-time code
```
claude
```
Follow prompts to log in with your Anthropic account.

## STEP 4 — Create workspace and set permissions
```
mkdir C:\twobirds
icacls "C:\twobirds" /grant "${env:USERNAME}:(OI)(CI)F" /T
```
Note: Use `${env:USERNAME}` not `%USERNAME%` — the `%` syntax fails in PowerShell.

## STEP 5 — Clone all Two Birds repos
```
cd C:\twobirds
gh repo clone twobirds-kramerica/digital-confidence
gh repo clone twobirds-kramerica/two-birds-portfolio
gh repo clone twobirds-kramerica/career-coach
gh repo clone twobirds-kramerica/kevins-apartment-search
gh repo clone twobirds-kramerica/quality-dashboard
gh repo clone twobirds-kramerica/aaron-patzalek
gh repo clone twobirds-kramerica/two-birds-innovation
gh repo clone twobirds-kramerica/clarity
gh repo clone twobirds-kramerica/elite-karate-site
```

## STEP 6 — Set git identity
```
git config --global user.name "Aaron Patzalek"
git config --global user.email "aaron.patzalek@gmail.com"
```

## STEP 7 — Create desktop launcher
Create a file at `C:\twobirds\launch-claude-code.bat` containing:
```
@echo off
cd /d C:\twobirds
claude --dangerously-skip-permissions
```
Right-click the file → Send to → Desktop (create shortcut)
Right-click the desktop shortcut → Properties → Advanced → Run as Administrator → OK

## STEP 8 — Disable sleep on AC power
```
powercfg /change standby-timeout-ac 0
```

## STEP 9 — Register overnight scheduler
```
powershell -ExecutionPolicy Bypass -File "C:\twobirds\setup-task-scheduler.ps1"
schtasks /query /tn "TwoBirds-Overnight-Build" /fo LIST
```
Should show the task listed with Next Run Time of 2:00 AM.

## STEP 10 — Verify everything works
```
cd C:\twobirds\two-birds-portfolio
git pull origin master
git log --oneline -5
```
Should show recent commits — if yes, setup is complete.

## KNOWN GOTCHAS
- **Ctrl+V may not paste in terminal** — right-click instead
- **If git push rejected:** run `git pull --rebase` first then push again
- **If icacls fails with %USERNAME%:** use `${env:USERNAME}` in PowerShell
- **If gh not found after install:** close and reopen PowerShell as Administrator
- **If claude command not found:** close and reopen PowerShell, try again
- **If Node version error with n8n:** run `node --version` first, needs v18+

## TOTAL ESTIMATED TIME: 15 minutes on good internet

---

## KNOWN ISSUES AND FIXES
Learned from i5 and silver laptop setups. Apply to all new machines.

### ISSUE 1 — LAST-RUN-SUMMARY.md shows stale after push
**Cause:** GitHub CDN caches the raw file for a few minutes after push.
**Fix:** Wait 5 minutes and type Retro again. Not a system failure.
**Prevention:** None needed — self-resolving.

### ISSUE 2 — Cloud scheduler push blocked (403)
**Cause:** claude.ai/code/scheduled runs in Anthropic cloud with read-only git proxy.
**Fix:** Windows Task Scheduler on local machine has full push access.
**Prevention:** Always use Windows Task Scheduler for overnight builds. Cloud scheduler = manual trigger only, not overnight automation.

### ISSUE 3 — git push rejected on new machine
**Cause:** Remote has changes not in local.
**Fix:** `git pull --rebase` first, then `git push`.
**Prevention:** Always pull before pushing on a new machine.

### ISSUE 4 — icacls fails with %USERNAME%
**Cause:** `%` syntax is cmd.exe, not PowerShell.
**Fix:** Use `${env:USERNAME}` in PowerShell always.
**Prevention:** Copy commands from this setup guide exactly.
