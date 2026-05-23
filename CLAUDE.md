# Two Birds Innovation — Master Context
Auto-loaded at every session. Last updated: 2026-04-28.

## WHO AARON IS
Aaron Patzalek. St. Thomas, Ontario. Married, parent of twins. 20+ year Senior PM (most recently Telus). Founded Two Birds Innovation early 2026. Revenue target $10k/month by Aug/Sep 2026. Sole income earner.

## FIVE NON-NEGOTIABLE RULES
1. Static HTML/CSS/JS only. No npm, no Node frameworks.
2. Canadian English throughout all content.
3. Commit after every phase. Update SESSION-STATE.md + push after every sprint.
4. Read SESSION-STATE.md before starting any work session.
5. `git log --oneline -30` first. Never re-propose a sprint without grepping git log for it first.

## ONE-SHOT LAUNCHER RULE (2026-05-19)
Any new tool or background service that needs to run alongside Claude Code MUST be wired into:
- `hal-stack/scripts/launch-claude.bat` — add a `start /min` line for the new service
- `hal-stack/scripts/setup-new-machine.ps1` — add the install step
Never give Aaron manual "run this separately" instructions. One double-click starts everything.
Fresh machine = clone two-birds-portfolio → run setup-new-machine.ps1 → desktop shortcut appears.

## SPRINT COMPLETION — AARON ACTION FILING (2026-05-11)
At the end of every sprint, before pushing: for each item in "Next recommended action for Aaron" that requires a decision or explicit human action, call:
`python hal-stack/notion-sync/file-aaron-action.py "description" P1|P2 --notes "context"`
This ensures no Aaron-facing item gets buried in SESSION-STATE. Items land in Notion as Owner=Aaron, Status=Backlog, Type=Task. Do NOT file items Aaron can't act on (build tasks, future sprints, code-only work — those go to the sprint queue).

## TRIGGERS
- `next sprint` → `python hal-stack/notion-sync/next-sprint.py`; exit 3 → `hal-stack/sprint-system/sprint-queue.md`; check `hal-stack/sprint-system/pending-capture.md` first (Phase 0); max-mode rules: `hal-stack/governance/max-mode.md`
- `just go` → execute ONE sprint autonomously, normal mode, no chaining; stop + return control after
- `retro` → read `SESSION-STATE.md`, summarise last 5 sprints shipped, patterns, and what's stalled; `logs/RETRO.md` is Lighthouse-only archive (18d+ stale, not the live source)
- `state` → read `SESSION-STATE.md`, report top 3 next actions
- `dashboard` → read `WIP-DASHBOARD.md`
- `hal` → read `hal-stack/HAL-BACKLOG.md`
- `journey` → read latest `journey/` entry
- `cos` → Chief of Staff daily check-in (see `hal-stack/cos/README.md`); read `hal-stack/cos/morning-briefing.md` first (overnight context); then pull Google Calendar today+tomorrow (MCP), Gmail urgent scan (MCP), Notion P1 Owner=Aaron; apply Logan Currie CoS protocol + Head/Heart/Hand diagnostic on any stalled items; ADHD-aware energy matching
- `cos-week` → Monday weekly review; Priority Dashboard for the week; flag overcommitment; set mid-week parking lot reminder; read SESSION-STATE + Notion P1+P2; output: this week's top 3 + what's parked + one thing to protect
- `cos-retro` → Friday pattern review; what shipped vs. planned; execution/avoidance/energy patterns observed; setup framing for Monday; write summary to `hal-stack/cos/weekly-retro-[date].md`

## KEY FILES
- Session state: `SESSION-STATE.md`
- Retro: `SESSION-STATE.md` (live, per sprint) · `logs/RETRO.md` (Lighthouse archive only)
- Notion backlog: data source `dee08637-7122-46cd-bc29-7775ce3ab8f6`
- Human todos: `hal-stack/sprint-system/aaron-todos-2026-04-21.md`

## REPOS (`C:\twobirds\`)
digital-confidence (DCC, 29 modules, GH Pages) · career-coach · clarity · aaron-patzalek · two-birds-innovation · kevins-apartment-search (private) · quality-dashboard · two-birds-command-centre · elite-karate-site · two-birds-portfolio

## GIT IDENTITY
Name: Aaron Patzalek · Email: aaron.patzalek@gmail.com · Org: twobirds-kramerica

## DEEPER RULES (read when relevant)
- Governance (Pattern Counter, Session Length, MCP Write Safety, Repo Visibility, Timestamp, Sprint Completion, Notion sync, Sovereignty): `hal-stack/governance/rules.md`
- Engagement (Sparring Partner, Confidence %, N.B., Voice Check, SESSION-STATE final step, Scrappy Pack): `hal-stack/governance/engagement-rules.md`
- Backlog item format + Notion helper signatures: `hal-stack/governance/backlog-format.md`
- Max mode full rules: `hal-stack/governance/max-mode.md`
- Sovereignty/L1-L4 architecture: `hal-stack/architecture/decapitation-checklist.md`
- Personas (40 total — 24 dept + 6 Founding Board + 3 SME Reviewers + 5 Scrappy Pack + 2 Inner Circle): `hal-stack/personas/` · `hal-stack/founding-board/`
- Voice-check banned words: `hal-stack/sprint-system/backlog/P2-voice-check-protocol.md`
- Notion sync scripts + README: `hal-stack/notion-sync/`
- Notion Glossary (canonical source): page `348a09cf-876a-815a-802c-c9c182167749`
