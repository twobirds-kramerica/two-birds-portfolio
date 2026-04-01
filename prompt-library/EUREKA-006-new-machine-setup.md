# 🔴 EUREKA-006 — One-Prompt Machine Setup
Date captured: April 1, 2026
Theme: Setup
Shareability: 5
Personal flag: 🟢 Universal

## The Problem It Solves
Setting up a new development machine takes hours of Googling, installing, configuring, and troubleshooting. When you're working across multiple machines — a primary laptop, a secondary, a desktop — the setup needs to be repeatable and fast. This prompt generates a complete step-by-step setup guide for Claude Code on Windows, including every gotcha discovered through real multi-machine experience.

## Why It's A Eureka Moment
The guide isn't generated from documentation — it's generated from pain. Every step includes the workaround for the thing that actually breaks: Ctrl+V not pasting in terminal (right-click instead), `%USERNAME%` failing in PowerShell (use `${env:USERNAME}`), `gh` not found after install (close and reopen PowerShell). These gotchas aren't in any official docs. They come from setting up two real machines and hitting every wall.

## The Hook (for social media)
"I set up Claude Code on a brand new Windows laptop in 15 minutes using one prompt. Every step includes the workaround for the thing that actually breaks."

## The Verbatim Prompt
```
Create a complete step-by-step guide for setting up Claude Code on a new
Windows machine. Based on hard-won learnings from i5 Lenovo and silver
Pentium setups. Include every section below exactly:

- BEFORE YOU START: right-click paste, admin PowerShell, credentials needed
- STEP 1: Install prerequisites (Git, GitHub CLI, Node.js via winget)
- STEP 2: Install Claude Code (npm install -g @anthropic-ai/claude-code)
- STEP 3: Authenticate GitHub (gh auth login) and Claude
- STEP 4: Create workspace and set permissions (icacls)
- STEP 5: Clone all repos (gh repo clone for each)
- STEP 6: Set git identity
- STEP 7: Create desktop launcher (.bat file with shortcut)
- STEP 8: Disable sleep on AC power (powercfg)
- STEP 9: Register overnight scheduler
- STEP 10: Verify everything works (git pull, git log)
- KNOWN GOTCHAS: every real error encountered and its fix
```

## The Result
A 10-step setup guide that takes 15 minutes on good internet. Tested across two machines (i5-6200U with Windows 10 Pro and Pentium N6000 with Windows 11 Home). Includes 6 documented gotchas that prevent the most common failures. The guide is stored at `new-machine-setup/SETUP-NEW-WINDOWS-MACHINE.md` and can be handed to anyone setting up a Two Birds development environment.

## How To Adapt It
- Replace the repo list with your own repositories
- Replace the git identity with your own name and email
- Adjust the workspace path (C:\twobirds) to your preference
- Add or remove steps based on your stack (database, Docker, etc.)
- The gotchas section is the most valuable part — add your own as you discover them
- Keep the guide in version control so it improves over time
- The key insight: a setup guide written from memory of what broke is worth ten times one written from docs
