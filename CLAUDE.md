# Two Birds Innovation — Master Context
Last updated: 2026-05-28.

## FIVE NON-NEGOTIABLE RULES
1. Static HTML/CSS/JS only. No npm, no Node frameworks.
2. Canadian English throughout all content.
3. Commit after every phase. Update SESSION-STATE.md + push after every sprint.
4. Read SESSION-STATE.md before starting any work session.
5. `git log --oneline -30` first. Never re-propose a sprint without grepping git log for it first.

## VOICE-CHECK RULE (2026-05-22)
Any written content Aaron will send externally: apply voice-check protocol, append compliance tag.
Protocol + banned words: `hal-stack/protocols/voice-check.md`.
Tag format: `✓ voice check: [scanned items] | [count caught] | [count fixed]`

## ONE-SHOT LAUNCHER RULE (2026-05-19)
New tools/services → wire into `hal-stack/scripts/launch-claude.bat` + `hal-stack/scripts/setup-new-machine.ps1`. Never give manual startup instructions.

## SPRINT COMPLETION — AARON ACTION FILING (2026-05-11)
Before push: file Aaron-facing actions via `python hal-stack/notion-sync/file-aaron-action.py "description" P1|P2 --notes "context"`. Build tasks go to sprint queue, not Notion.

## TRIGGERS
- `next sprint` → `python hal-stack/notion-sync/next-sprint.py`; exit 3 → `hal-stack/sprint-system/sprint-queue.md`; check `hal-stack/sprint-system/pending-capture.md` first; max-mode rules: `hal-stack/governance/max-mode.md`
- `just go` → one sprint, autonomous, normal mode, stop after
- `retro` → read SESSION-STATE.md, summarise last 5 sprints, patterns, stalls; `logs/RETRO.md` is archive only
- `state` → read SESSION-STATE.md, top 3 next actions
- `dashboard` → read `WIP-DASHBOARD.md`
- `hal` → read `hal-stack/HAL-BACKLOG.md`
- `journey` → read latest `journey/` entry
- `cos` / `cos-week` / `cos-retro` → `hal-stack/cos/README.md`; read `hal-stack/cos/morning-briefing.md` first

## KEY FILES
- Session state: `SESSION-STATE.md`
- Notion backlog: `dee08637-7122-46cd-bc29-7775ce3ab8f6`
- Human todos: `hal-stack/sprint-system/aaron-todos-2026-04-21.md`

## REPOS (`C:\twobirds\`)
digital-confidence (DCC, 29 modules, GH Pages) · career-coach · clarity · aaron-patzalek · two-birds-innovation · kevins-apartment-search (private) · quality-dashboard · two-birds-command-centre · elite-karate-site · two-birds-portfolio

## GIT IDENTITY
Name: Aaron Patzalek · Email: aaron.patzalek@gmail.com · Org: twobirds-kramerica

## DEEPER RULES (read when relevant)
- Governance: `hal-stack/governance/rules.md`
- Engagement + Scrappy Pack: `hal-stack/governance/engagement-rules.md`
- Backlog format: `hal-stack/governance/backlog-format.md`
- Max mode: `hal-stack/governance/max-mode.md`
- Sovereignty/L1-L4: `hal-stack/architecture/decapitation-checklist.md`
- Personas (40): `hal-stack/personas/` · `hal-stack/founding-board/`
- Notion sync: `hal-stack/notion-sync/`
- Notion Glossary: `348a09cf-876a-815a-802c-c9c182167749`
