# Two Birds Innovation — Master Context
Auto-loaded by Claude Code at every session.
Last updated: April 1, 2026

## WHO AARON IS
Aaron Patzalek. St. Thomas, Ontario. Solo parent of 6-year-old twin daughters.
20+ year Senior Product Manager. Most recently Telus. Founded Two Birds Innovation early 2026.
Revenue target: $10,000/month by August/September 2026.
Sole income earner. Time is the most constrained asset.

## STANDING RULES — NON-NEGOTIABLE
- Static HTML/CSS/JS only. No npm. No Node frameworks.
- Canadian English throughout all content.
- Commit after every phase.
- Run git log --oneline -30 before touching any repo.
- Run as Administrator to avoid permission blocks.
- Read SESSION-STATE.md before starting any work session.
- After every session: overwrite logs/RETRO.md and push.
- Never rebuild something already built — check git log first.
- TIMESTAMP RULE: Every RETRO.md, SESSION-STATE.md, and automated-run-log.md must end with these exact two lines as the final lines of the file — nothing after them:
  Last updated: [YYYY-MM-DD] at [HH:MM] EST (Toronto)
  CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.
  Use PowerShell to get time: $ts = (Get-Date).ToString("yyyy-MM-dd HH:mm") + " EST (Toronto)"
- PATTERN COUNTER RULE: If Aaron asks the same question 3+ times in a session, stop troubleshooting instances. Declare the pattern broken. Propose systemic fix. Log to RELIABILITY-ISSUES.md. Never say "yes it works" unless confirmed 3 times in a row.

## RELIABLE WORKFLOW (as of April 2, 2026)
- Retro PRIMARY: PowerShell `cat logs/RETRO.md` — always accurate
- Retro SECONDARY: Claude Web — use when CDN cooperates only
- Next sprint: Claude Code terminal — reliable
- Remote Control builds: unreliable — use cloud scheduler "Run now" instead
- Overnight: Windows Task Scheduler on i5 — reliable

## ALL REPOS (located at C:\twobirds\)
- digital-confidence: DCC, 241 pages, 21 modules, bilingual EN/FR
- career-coach: AI job application tool
- clarity: AI business diagnostic for SMEs
- aaron-patzalek: personal brand site
- two-birds-innovation: company brand site
- kevins-apartment-search: civic rental tool
- quality-dashboard: portfolio health monitor
- two-birds-command-centre: operations dashboard
- elite-karate-site: client site, pending feedback
- two-birds-portfolio: master portfolio, backlog, session state

## KEY FILES
Backlog: C:\twobirds\two-birds-portfolio\NEXT-SPRINT-QUEUE.md
Session state: C:\twobirds\two-birds-portfolio\SESSION-STATE.md
Last run: C:\twobirds\two-birds-portfolio\logs\RETRO.md
HAL backlog: C:\twobirds\two-birds-portfolio\hal-stack\HAL-BACKLOG.md
Journey archive: C:\twobirds\two-birds-portfolio\journey\

## TRIGGER COMMANDS
When the user types any of these, execute the corresponding action:
"next sprint" — read backlog, execute top 3 Claude Code executable items
"retro" — read and report logs/RETRO.md contents
"state" — read SESSION-STATE.md, orient fully, report top 3 next actions
"dashboard" — read WIP-DASHBOARD.md, report full portfolio status
"hal" — read HAL-BACKLOG.md, report next infrastructure item
"journey" — read latest journey archive entry, summarise progress
"sprint-01" — execute sprint file at sprints/sprint-01.md
"sprint-02" — execute sprint file at sprints/sprint-02.md
"sprint-03" — execute sprint file at sprints/sprint-03.md

## GIT IDENTITY
Name: Aaron Patzalek
Email: aaron.patzalek@gmail.com
Org: twobirds-kramerica

## OVERNIGHT SCHEDULER
Script: C:\twobirds\run-overnight-build.bat
Runs: Daily at 2:00 AM via Windows Task Scheduler
Logs: C:\twobirds\two-birds-portfolio\logs\automated-run-log.md
