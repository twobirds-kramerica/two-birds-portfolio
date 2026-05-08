# HAL Stack — Loop Patterns
**Created:** 2026-05-08 | **Source:** Boris Cherny /loop (TikTok S-LOOP-001)

Boris Cherny (Claude Code creator) runs **dozens of /loop instances simultaneously** as his primary automation pattern. Key quote: *"The thing I've been finding myself using more and more is loop. So this is slash loop and it's just like the coolest thing."*

His use cases (from the talk):
- Babysitting PRs — fixing CI, auto-rebasing
- Flaky test detection and repair
- Clustering Twitter/X feedback every 30 minutes
- Server-side monitoring

This directory contains ready-to-run loop prompts adapted for Two Birds. Each file is a self-contained prompt you paste at a Claude Code session start.

---

## How to run a loop

### Option A — Manual one-shot (normal mode)
Open a Claude Code terminal session, paste the prompt from any loop file, press Enter.
Claude executes the loop body once, then stops. Re-run manually as needed.

### Option B — `/loop` with self-pacing (current session)
Paste the prompt, prepend it with `/loop` in the Claude Code terminal.
Claude executes, then calls `ScheduleWakeup` to re-fire itself on interval.
Session must stay open. Good for: watching a long build, monitoring a deploy.

### Option C — Windows Task Scheduler (overnight / recurring)
Add a new task in Task Scheduler pointing at `run-overnight-build.bat`, modified to
pass the loop prompt as the session input. Already-proven path (used for DCC overnight runs).
Good for: daily/nightly jobs that should run whether or not Aaron is at the machine.

### Option D — `schedule` skill (Anthropic-side cron)
Use the `/schedule` skill to create a remote scheduled agent.
Good for: jobs that need to run even when the machine is off.
Note: burns tokens on Anthropic's side — use only for high-value recurring jobs.

---

## Loop inventory

| File | Job | Recommended Interval | Mode |
|------|-----|---------------------|------|
| `loop-pr-babysitter.md` | Watch open PRs across Two Birds repos; fix CI failures; flag stale branches | On-demand or daily | A or C |
| `loop-backlog-health.md` | Check Notion Product Backlog; surface P0/P1 items that have been Backlog >7 days without movement; report to SESSION-STATE | Weekly | A or C |
| `loop-content-freshness.md` | Run DCC content freshness check; flag modules stale >90 days; append report to SESSION-STATE | Weekly | A or C |
| `loop-notion-sync-verify.md` | Verify last Notion sync succeeded; re-run next-sprint.py if SYNC-LOG shows >48h stale | Daily | C |

---

## Boris Cherny pattern principles (extracted from screenshots)

1. **Cron + repeat** — every loop has an interval. Even babysitting loops fire on a schedule, not reactively.
2. **Dozens in parallel** — each loop is narrow and focused. Don't build one loop that does everything.
3. **Server-side** — the most valuable loops run without Aaron present.
4. **100 agents simultaneously** — loops are lightweight; they spawn agents only when needed, not continuously.
5. **Sovereign** — /loop is built into Claude Code. Zero external dependencies, zero cost.
