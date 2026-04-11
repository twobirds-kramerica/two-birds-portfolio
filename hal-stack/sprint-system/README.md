<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 16:10 EST (Toronto)
Confidence: HIGH
Known gaps: None
-->

# Sprint System

Two commands. That's all Aaron needs.

## "next sprint"

Open Claude Code on any machine. Type two words. Claude Code reads the sprint queue, picks the highest-priority non-blocked sprint, and executes it autonomously. No copy-pasting. No context-switching. Walk away.

**How it works:**
1. Claude Code reads `sprint-queue.md`
2. Finds the first sprint marked `READY` (not blocked, not done)
3. Executes the complete prompt stored in that sprint entry
4. When done: marks it `DONE` in the queue, updates SESSION-STATE.md, auto-generates context export, commits, pushes
5. Aaron comes back to finished work

## "retro"

Open Claude.ai on phone or laptop. Paste the retro prompt. Claude.ai reads what just happened and reports: what shipped, what broke, what Aaron needs to do next.

**Known limitation:** Claude.ai can't read Aaron's local files directly. Aaron either pastes the latest SESSION-STATE entry, or reads the GitHub raw URL. See `retro-prompt.md` for full details.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `sprint-queue.md` | The actual queue — ready-to-run sprint prompts |
| `sprint-template.md` | Template for adding new sprints |
| `next-sprint-loader.md` | How the "next sprint" trigger works |
| `next-sprint.bat` | Windows batch file — double-click to run |
| `next-sprint-mobile.txt` | Short command for phone copy-paste |
| `retro-prompt.md` | Retro prompt for Claude.ai |
| `retro-mobile.txt` | Short retro trigger for phone |
| `human-backlog.md` | Everything Aaron personally needs to do |
| `QUICKSTART.md` | Phone-friendly quick reference |

## Layer Compatibility

**L4-native.** The entire sprint system is markdown files in a git repo. Any tool that can read text files can use it. Any human with a text editor can read the queue and execute sprints manually.
