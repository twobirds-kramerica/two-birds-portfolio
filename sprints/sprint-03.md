# Sprint 03 — Commit Density Timeline
Date created: April 1, 2026
Status: READY TO RUN

## Instructions for Claude Code
Switch to: C:\twobirds\two-birds-portfolio

Run git log across all repos to get commit timestamps:
For each repo in C:\twobirds\: git log --format="%ai %s" --no-walk --all

Aggregate commits by date. Build a timeline showing build intensity.
Create journey/raw/commit-density-timeline.md with:
- Date | Commits that day | Repos touched | Notable work
- Cover March 1 through April 1, 2026

Also create a visual HTML version at:
C:\twobirds\two-birds-command-centre\journey-timeline.html
A single-page visual timeline. Dark theme. Each day is a bar.
Sprint days (March 25-28) should show dramatically taller bars.
Hover to see commit messages for that day.

Commit to command-centre: "feat: journey timeline visualisation"
Commit to portfolio: "feat: commit density timeline raw data"
Push both.
Update LAST-RUN-SUMMARY.md. Push.
