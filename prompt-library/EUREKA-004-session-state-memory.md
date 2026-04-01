# 🔴 EUREKA-004 — Session State as Memory
Date captured: April 1, 2026
Theme: Workflow
Shareability: 5
Personal flag: 🟢 Universal

## The Problem It Solves
Claude Code has no memory between sessions. Every new conversation starts from zero. If you built something complex yesterday, today's Claude has no idea it happened. You lose context, repeat work, and make contradictory decisions. Session state as memory solves this by writing a structured summary at the end of every session and reading it at the start of the next one. The file becomes Claude's long-term memory.

## Why It's A Eureka Moment
The insight is that a markdown file committed to git IS a memory system. It's version-controlled, portable, human-readable, and machine-readable. You don't need a database, a vector store, or a memory API. You need a file with a consistent structure that gets read at the start and written at the end. The git history gives you time travel for free — you can see what Claude knew at any point in the past.

## The Hook (for social media)
"Claude Code has no memory between sessions. So I gave it one — a markdown file it reads at the start and writes at the end. Git history gives it time travel for free."

## The Verbatim Prompt
```
Read C:\twobirds\two-birds-portfolio\SESSION-STATE.md before starting.

[... do work ...]

FINAL STEP — Create or update C:\twobirds\two-birds-portfolio\SESSION-STATE.md with:
- Date and time of this session
- Phases that ran and their completion status
- Commits made (repo, commit message, push status)
- Anything skipped and why
- Next recommended action
```

## The Result
A living document that carries context across sessions. Every session reads the previous state and writes the new state. After 5 sessions in a single day, the file contains a complete record of what happened, what was committed, and what to do next. The "Next recommended action" line is particularly powerful — it means tomorrow's session starts with a clear instruction, not a blank page.

## How To Adapt It
- Create a SESSION-STATE.md in your project root
- Add "Read SESSION-STATE.md before starting" to the top of every prompt
- Add the "FINAL STEP — update SESSION-STATE.md" template to the bottom
- Keep the structure consistent: date, phases, commits, skipped, next action
- The file should be committed to git so it's never lost and always versioned
- For multi-repo projects, keep state in one central repo (the portfolio pattern)
