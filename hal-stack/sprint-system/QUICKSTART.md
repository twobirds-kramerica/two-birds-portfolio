# Sprint System — Quick Start

Phone-friendly. Read in 2 minutes.

---

## How to Run a Sprint

1. Open Claude Code on any machine
2. Type or paste:
   ```
   Read C:\twobirds\two-birds-portfolio\hal-stack\sprint-system\sprint-queue.md — find the first sprint with status READY. Execute its prompt exactly as written. When done, change its status to DONE, add today's date, update SESSION-STATE.md with the results, auto-generate context export, commit, and push to master.
   ```
3. Walk away. It runs autonomously.

## How to Check What Happened

1. Open Claude.ai on your phone
2. Paste:
   ```
   Read https://raw.githubusercontent.com/twobirds-kramerica/two-birds-portfolio/master/SESSION-STATE.md — then report: what shipped, any human actions needed (sorted NOW/SOON/LATER), any blockers, and what I should do next. Keep it short — I'm on my phone.
   ```
3. Read the report. Do any NOW items.

## How to Check Your To-Do List

Open: `hal-stack/sprint-system/human-backlog.md`

- **NOW** items first (2-5 min each)
- **SOON** items when you have 15 min
- **LATER** items when you feel like it

## How to Add a New Sprint

1. Open `sprint-queue.md`
2. Copy template from `sprint-template.md`
3. Fill it in (or ask Claude.ai to write the prompt)
4. Save, commit, push
5. Next time you type "next sprint," it picks it up

## Files Cheat Sheet

| File | What |
|------|------|
| `sprint-queue.md` | The queue — all sprints with prompts |
| `human-backlog.md` | Your personal to-do list |
| `next-sprint-mobile.txt` | Short command for phone |
| `retro-mobile.txt` | Short retro command for phone |
| `QUICKSTART.md` | This file |
