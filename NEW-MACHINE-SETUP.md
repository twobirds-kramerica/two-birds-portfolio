# NEW LAPTOP SETUP — Claude Code Fast Track v2.0

**Last Updated:** 2026-03-31
**Author:** Aaron Kramer | Two Birds Innovation
**Time to complete:** ~45 minutes on a clean Windows machine

> This is the exact setup sequence used to get HAL operational on the i5 Lenovo in March 2026.
> Follow every step in order. Do not skip steps. Every step has been battle-tested.

---

## Step 1 — Install Windows Terminal FIRST (before anything else)

Open PowerShell and run:
```
winget install Microsoft.WindowsTerminal --accept-source-agreements
```

Pin Windows Terminal to your taskbar. **Use Windows Terminal for every command in this guide.** Never use the old Command Prompt or legacy PowerShell window.

---

## Step 2 — Fix PowerShell Execution Policy

Open Windows Terminal **as Administrator** (right-click → Run as administrator), then run:
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
```

This allows scripts to run. Required for npm global installs.

---

## Step 3 — Install Node.js

1. Go to **nodejs.org** and download the LTS version
2. Run the installer — accept all defaults
3. Open a **new** Windows Terminal window after install

Confirm it worked:
```
node --version
npm --version
```

You should see v20 or higher. If not, restart Windows Terminal and try again.

---

## Step 4 — Install Git

1. Go to **git-scm.com/download/win** and download Git for Windows
2. Run the installer — accept all defaults (important: keep "Git from the command line" selected)

Confirm it worked:
```
git --version
```

---

## Step 4.5 — Install Python 3.10+ (for HAL sync scripts)

Needed for `hal-stack/notion-sync/` (Notion ↔ GitHub sync) and any future Python tooling. Not optional on new machines.

```
winget install Python.Python.3.12 --accept-source-agreements --accept-package-agreements
```

**Close Windows Terminal and open a new one** after install — Windows PATH updates do not propagate to already-open shells.

Confirm:
```
python --version
```
Must print 3.10 or higher. If you see a Microsoft Store message instead, close the terminal and open a new one.

Install the one pip dependency used by the sync scripts:
```
pip install requests
```

---

## Step 5 — Install Claude Code

```
npm install -g @anthropic-ai/claude-code
```

Confirm it worked:
```
claude --version
```

You should see a version number. If you see "command not found," restart Windows Terminal.

---

## Step 6 — Create the Twobirds Folder and Clone All Repos

> CRITICAL: You must `cd C:\` first. Running `mkdir` from another directory creates the folder in the wrong place.

```
cd C:\
mkdir twobirds
cd C:\twobirds
```

Now clone every active repo:
```
git clone https://github.com/twobirds-kramerica/digital-confidence
git clone https://github.com/twobirds-kramerica/career-coach
git clone https://github.com/twobirds-kramerica/kevins-apartment-search
git clone https://github.com/twobirds-kramerica/two-birds-portfolio
git clone https://github.com/twobirds-kramerica/quality-dashboard
git clone https://github.com/twobirds-kramerica/two-birds-innovation
git clone https://github.com/twobirds-kramerica/aaron-patzalek
```

---

## Step 7 — Set Your Git Identity

```
git config --global user.name "Aaron Patzalek"
git config --global user.email "aaron.patzalek@gmail.com"
```

This ensures your commits are attributed correctly on GitHub.

---

## Step 8 — Launch Claude Code and Log In

```
cd C:\twobirds\digital-confidence
claude
```

**When asked about API key — say NO.** You are using your claude.ai Max subscription, not API billing. Log in via browser when prompted.

After login, confirm the header shows: `Opus 4.6 · Claude Max`

---

## Step 9 — Create a Desktop Launcher

1. Open Notepad
2. Type exactly: `wt -d C:\twobirds\digital-confidence cmd /k "claude"`
3. Save as → change "Save as type" to **All Files** → name it `claude-code.bat` → save to Desktop
4. Right-click the file → Properties → Advanced → tick **Run as administrator** → OK

Double-clicking this file now launches Claude Code in the right directory.

---

## Step 10 — Install the Enhancement Tools (Claude Mem, Superpowers, GSD, etc.)

```
cd ~
git clone https://github.com/thedotmack/claude-mem ~/.claude/claude-mem
git clone https://github.com/obra/superpowers ~/.claude/superpowers
git clone https://github.com/affaan-m/everything-claude-code ~/.claude/everything-claude-code
git clone https://github.com/gsd-build/get-shit-done ~/.claude/gsd
git clone https://github.com/hesreallyhim/awesome-claude-code ~/.claude/awesome-claude-code
cd ~/.claude/claude-mem && npm install
```

These tools add persistent memory, micro-planning, TDD, and autonomous task execution to Claude Code sessions.

---

## Step 11 — Install n8n (HAL Automation Engine) — Optional Until April 2026

```
npm install -g n8n
n8n start
```

Access at: **http://localhost:5678** — create your admin account on first visit.

This is the automation engine for the HAL Stack. Skip this step until you are ready to set up prompt tracking and GitHub webhooks.

---

## Step 12 — Set Up Keep-Alive (Auto-Start Claude Code on Boot)

1. Open **Task Scheduler** (search in Start menu)
2. Click **Create Basic Task** in the right panel
3. Fill in:
   - Name: `HAL Keep Alive`
   - Trigger: **When the computer starts**
   - Action: **Start a program**
   - Program: `wt`
   - Arguments: `-d C:\twobirds\digital-confidence cmd /k "claude"`
4. Finish

Claude Code will now start automatically every time this machine boots.

---

## Troubleshooting

### Git push rejected
```
git pull --rebase origin main && git push origin main
```
GitHub Actions often auto-commits to the repo. This syncs those changes before pushing.

### npm not found after installing Node
Restart Windows Terminal. Node adds npm to PATH on install, but the change only takes effect in a new terminal window.

### Claude Code won't start
```
node --version
```
Needs v18 or higher. If your version is older, re-download Node from nodejs.org (LTS) and reinstall. Then:
```
npm install -g @anthropic-ai/claude-code
```

### Paste doesn't work in the terminal
Only Windows Terminal supports Ctrl+V paste. If you are in an old PowerShell or CMD window, switch to Windows Terminal.

### git clone asks for username/password
GitHub now uses personal access tokens, not passwords. Go to github.com → Settings → Developer settings → Personal access tokens → Generate new token (classic). Use the token as your password.

---

## Quick Reference — What Goes Where

| Folder | What's in it |
|--------|-------------|
| `C:\twobirds\digital-confidence` | DCC — primary repo, launch Claude Code here |
| `C:\twobirds\two-birds-portfolio` | HAL Stack docs, sprint archives, WIP dashboard |
| `C:\twobirds\career-coach` | Career Coach app |
| `C:\twobirds\kevins-apartment-search` | Kevin's Apartment tool |
| `C:\twobirds\quality-dashboard` | Quality Dashboard |
| `~/.claude/` | Claude Code config, CLAUDE.md, enhancement tools |
| `~/.claude/claude-mem/` | Persistent memory injection tool |
| `~/.claude/superpowers/` | TDD, micro-planning, brainstorming skills |
| `~/.claude/gsd/` | Autonomous multi-task execution |

---

*Fast Track v2.0 — tested on i5 Lenovo, Windows 10 Pro, March 2026*
