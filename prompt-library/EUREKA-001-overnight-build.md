# 🔴 EUREKA-001 — The Overnight Build Agent
Date captured: April 1, 2026
Theme: Automation
Shareability: 5
Personal flag: 🟢 Universal

## The Problem It Solves
You have a backlog of build tasks but only so many waking hours. Every morning you start a Claude Code session by re-reading what needs to happen, then manually executing items one at a time. The overnight build agent runs your backlog while you sleep — reading your prioritised queue, executing the top items, committing and pushing after each, then writing a log of what it did.

## Why It's A Eureka Moment
Most people think of AI assistants as interactive — you talk, it responds. This prompt turns Claude Code into an autonomous build agent that reads your own planning documents as its instructions. Your backlog file becomes the control plane. The log file becomes the accountability layer. You wake up to completed work and a clear record of what changed.

## The Hook (for social media)
"I built an overnight build agent that reads my backlog, executes the top 3 items, commits and pushes each one, then writes a log of what it did — all while I sleep."

## The Verbatim Prompt
```
You are an autonomous build agent for Two Birds Innovation.
Read C:\twobirds\two-birds-portfolio\NEXT-SPRINT-QUEUE.md and
C:\twobirds\two-birds-portfolio\SESSION-STATE.md.
Execute the top 3 items that are fully Claude Code executable —
skip anything marked as Aaron manual, pending approval, or
requiring human input. Commit and push after each completed item.
After completing all tasks, append a run entry to
C:\twobirds\two-birds-portfolio\logs\automated-run-log.md with:
date/time, tasks completed, commits made, anything skipped and why,
next recommended action. Then commit and push the log file.
Finally, overwrite C:\twobirds\two-birds-portfolio\logs\LAST-RUN-SUMMARY.md
with a plain-text summary of what ran, then commit and push it.
Canadian English. Static HTML/CSS/JS only. No npm. No Node frameworks.
```

## The Result
A Windows Task Scheduler task that runs daily at 2:00 AM. Claude Code reads the backlog, picks the top 3 executable items, builds them autonomously, commits after each phase, pushes to GitHub, and writes a timestamped log. Aaron checks the log file each morning to see what was completed overnight.

## How To Adapt It
- Replace the file paths with your own backlog and state files
- Change "top 3 items" to however many you want per run
- Replace "Aaron manual" with whatever your skip criteria are
- Add your own stack constraints (the "Static HTML/CSS/JS only" line)
- The key insight: your planning document IS the prompt input — keep it machine-readable
