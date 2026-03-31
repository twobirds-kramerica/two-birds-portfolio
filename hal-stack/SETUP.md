# HAL Stack Setup Guide
Step-by-step to get HAL operational on any Windows machine.
(Incorporates lessons from i5 Lenovo setup, March 2026)

## Prerequisites
- Windows 10 or 11
- Admin access
- Internet connection
- Anthropic account with Claude Max or Pro

## Step 1 — Install Windows Terminal FIRST
```
winget install Microsoft.WindowsTerminal --accept-source-agreements
```
Pin to taskbar. Use Windows Terminal for everything. Never use old PowerShell.

## Step 2 — Fix Execution Policy
In Windows Terminal as Administrator:
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
```

## Step 3 — Install Node.js
Download LTS from nodejs.org. Accept all defaults.
Confirm: `node --version` (should show v20+)

## Step 4 — Install Git
Download from git-scm.com/download/win. Accept all defaults.
Confirm: `git --version`

## Step 5 — Install Claude Code
```
npm install -g @anthropic-ai/claude-code
```
Confirm: `claude --version`

## Step 6 — Create Twobirds Folder and Clone Repos
CRITICAL: cd to C:\ FIRST before mkdir.
```
cd C:\
mkdir twobirds
cd C:\twobirds
git clone https://github.com/twobirds-kramerica/digital-confidence
git clone https://github.com/twobirds-kramerica/career-coach
git clone https://github.com/twobirds-kramerica/kevins-apartment-search
git clone https://github.com/twobirds-kramerica/two-birds-portfolio
git clone https://github.com/twobirds-kramerica/quality-dashboard
git clone https://github.com/twobirds-kramerica/clarity
git clone https://github.com/twobirds-kramerica/aaron-patzalek
git clone https://github.com/twobirds-kramerica/two-birds-innovation
```

## Step 7 — Set Git Identity
```
git config --global user.name "Aaron Patzalek"
git config --global user.email "aaron.patzalek@gmail.com"
```

## Step 8 — Launch Claude Code and Login
```
cd C:\twobirds\digital-confidence
claude
```
When asked about API key — say NO (use claude.ai subscription, not API billing)
Login via browser with Anthropic account
Confirm: shows Opus 4.6 · Claude Max at top

## Step 9 — Create Desktop Launcher
Open Notepad. Type:
```
wt -d C:\twobirds\digital-confidence cmd /k "claude"
```
Save As → All Files → claude-code.bat → Desktop
Right-click → Properties → Advanced → Run as administrator

## Step 10 — Install Enhancement Tools
```
cd ~
git clone https://github.com/thedotmack/claude-mem ~/.claude/claude-mem
git clone https://github.com/obra/superpowers ~/.claude/superpowers
git clone https://github.com/affaan-m/everything-claude-code ~/.claude/everything-claude-code
git clone https://github.com/gsd-build/get-shit-done ~/.claude/gsd
git clone https://github.com/hesreallyhim/awesome-claude-code ~/.claude/awesome-claude-code
cd ~/.claude/claude-mem && npm install
```

## Step 11 — Install n8n (HAL Automation Engine)
```
npm install -g n8n
n8n start
```
Access at: http://localhost:5678
Create admin account. This is your automation engine.

## Step 12 — Keep-Alive Configuration
Open Task Scheduler → Create Basic Task
- Name: HAL Keep Alive
- Trigger: At startup
- Action: Start program → `wt -d C:\twobirds\digital-confidence cmd /k "claude"`

This ensures Claude Code starts automatically when the machine boots.

## Troubleshooting

### Git push rejected
```
git pull --rebase origin main
git push origin main
```

### npm not found after Node install
Restart Windows Terminal. Node adds npm to PATH on install.

### Claude Code won't start
Check Node version: `node --version` (needs v18+)
Re-install: `npm install -g @anthropic-ai/claude-code`

### Paste doesn't work in terminal
Use Windows Terminal (not PowerShell or CMD directly).
Ctrl+V works in Windows Terminal. Right-click → Paste also works.
