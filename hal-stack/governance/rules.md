# Governance Rules — Two Birds Innovation
Sourced from CLAUDE.md. Read this file when any of these rules are relevant.
Last synced from CLAUDE.md: 2026-04-28.

## TIMESTAMP RULE
Every RETRO.md, SESSION-STATE.md, and automated-run-log.md must end with these exact two lines as the final lines — nothing after them:
```
Last updated: [YYYY-MM-DD] at [HH:MM] EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.
```
Get time via PowerShell: `$ts = (Get-Date).ToString("yyyy-MM-dd HH:mm") + " EST (Toronto)"`

## PATTERN COUNTER RULE
If Aaron asks the same question 3+ times in a session, stop troubleshooting instances. Declare the pattern broken. Propose a systemic fix. Log to RELIABILITY-ISSUES.md. Never say "yes it works" unless confirmed 3 times in a row.

## SPRINT COMPLETION RULE
Every sprint MUST end with SESSION-STATE.md update and git push. No exceptions. If the FINAL STEP cannot complete, log the blocker in sprint-queue.md with status BLOCKED.

## SESSION LENGTH RULE (S-MCP-RELIABILITY-001, 2026-04-22)
A single Claude Code session should not exceed ~3 hours of continuous active work or ~40 sequential tool calls against the same Notion data source. Longer sessions compound cache-warmth failures and decision fatigue. When approaching the limit: finalise current sprint, commit + push + update SESSION-STATE, then stop.

## MCP WRITE SAFETY RULE (S-MCP-RELIABILITY-001, 2026-04-22)
Every Notion write from Claude Code should go through `hal-stack/mcp-reliability/notion-write-safe.py`'s `safe_notion_write()` wrapper. Adds retry-with-backoff + response verification. Logs to `logs/mcp-write-log.txt`; exhausted writes fall back to `logs/mcp-write-fallback.json`. Prevents the S-041 class of bug (POST succeeded, client crashed, work looked failed).

## REPO VISIBILITY RULE (Security Cleanup Sprint, 2026-04-23/24)
Any repo containing real user data (names, addresses, financials, personal notes) must be private by default. Public is opt-in only and requires explicit confirmation. When flipping a public repo to private on the current org plan, GitHub Pages goes 404 (Pages-on-private requires Pro tier). Decide data classification BEFORE first commit, not retro-fitted after a security audit.

## RESEARCH MODE AUTO-ACTIVATION
Activate automatically (no manual toggle) when: evaluating external tools/platforms/services, competitive analysis, making factual claims about companies/people/products/pricing, or any task where citations are expected. Do NOT activate when building, writing code, or executing sprints — speed matters more than citations in execution mode. To activate: follow `~/.claude/skills/research-mode/SKILL.md`.

## RELIABLE WORKFLOW (as of April 2, 2026)
- Retro PRIMARY: PowerShell `cat logs/RETRO.md` — always accurate
- Retro SECONDARY: Claude Web — use when CDN cooperates only
- Next sprint: Claude Code terminal — reliable
- Remote Control builds: unreliable — use cloud scheduler "Run now" instead
- Overnight: Windows Task Scheduler on i5 — reliable

## OVERNIGHT SCHEDULER
Script: `C:\twobirds\run-overnight-build.bat`
Runs: Daily at 2:00 AM via Windows Task Scheduler
Logs: `C:\twobirds\two-birds-portfolio\logs\automated-run-log.md`

## MAX MODE
See `hal-stack/governance/max-mode.md` for full rules. Summary: activates on "max mode" / "max day" / "beefy builds" / "100% max" / "go big and fat" in Aaron's message, or when max-mode.md ACTIVE UNTIL is in the future. In max mode: skip governance pauses, flip Backlog→Ready autonomously, build-don't-propose.

## NOTION SYNC RULES (S-024)
- On "next sprint": `python hal-stack/notion-sync/next-sprint.py`. Exit 1/3 → fall back to sprint-queue.md.
- On sprint completion: `python hal-stack/notion-sync/complete-sprint.py <id> <commit>`.
- On backlog capture: write via `notion-client.py` helpers AND append to `pending-capture.md`.
- NOTION_API_KEY is an environment variable only. Never commit.
- See `hal-stack/notion-sync/README.md` for full architecture.

## BACKLOG ROUTING
**Writes** (new items, status changes) always go to Notion: Product Backlog `dee08637-7122-46cd-bc29-7775ce3ab8f6`, Command Center `347a09cf-876a-81fb-9a5c-eca696fb585b`.
**Reads** use GitHub raw first; fall back to Notion MCP; paste is last resort.

## SOVEREIGNTY — L1 TO L4 FLOAT MODEL
Every component must be designed so dropping between layers is a configuration change, not a rebuild.
- L1 — Commercial, fast and cheap (current default)
- L2 — Alternative commercial, swap-ready
- L3 — Open-source hosted
- L4 — Open-source local only, air-gapped, ungovernable

Claude is explicitly a swappable headless LLM backend, not a permanent dependency.
Deeper detail: `hal-stack/architecture/decapitation-checklist.md`.

## MACHINES
Three machines, all running Claude Code. Confirm by processor name, not brand.
- Lenovo Pentium Silver — newer chassis, slower. Source machine, still in use.
- Lenovo ThinkPad i5 — older chassis, more powerful. Fully set up.
- EZbook — from Phil / Employment Services. Fully set up.
