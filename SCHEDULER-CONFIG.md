# Scheduler Configuration
Last updated: April 1, 2026

## Active Scheduler: Windows Task Scheduler (local i5)
- Script: C:\twobirds\run-overnight-build.bat
- Schedule: Daily at 2:00 AM
- Auth: Full git push access via local credentials
- Run log: logs/automated-run-log.md

## Cloud Scheduler (claude.ai/code/scheduled)
- Status: KEEP ACTIVE as manual trigger only
- Use: Hit "Run now" when stepping away during the day
- Do not rely on for overnight builds — push is blocked in cloud environment
- Repo connected: two-birds-portfolio

## i5 Sleep Prevention
- Command run: powercfg /change standby-timeout-ac 0
- Status: Sleep disabled on AC power ✅
