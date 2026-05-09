# Pre-Flight Verification Checklist

Run before every sprint. Smoke test at the bottom is the fast path.

## Rule 1 — Environment
- [ ] `NOTION_API_KEY` env var is set
- [ ] `hal-stack/notion-sync/config.json` exists and is valid JSON
- [ ] `.claude/status-semantics.yaml` exists (SSOT)

## Rule 2 — Status Semantics
- [ ] `auto_pick_status` in status-semantics.yaml matches Notion's "Ready" option name
- [ ] `in_progress_status` matches Notion's "In Progress" option name
- [ ] No orphaned "In Progress" sprint from a prior session

## Rule 3 — Automation Matches Design
- [ ] `next-sprint.py` loads status values from status-semantics.yaml (not hardcoded)
- [ ] Sprint payload from next-sprint.py has all `required` fields from sprint-schema.json

## Rule 4 — Next Action Mandatory
- [ ] After every sprint, SESSION-STATE.md has a "Next recommended action" entry
- [ ] Notion item is set to "Done" before session ends

## Smoke Test
```bash
cd C:\twobirds\two-birds-portfolio
python hal-stack/notion-sync/next-sprint.py
# Exit 0 = sprint locked (success)
# Exit 3 = no Ready items (check Notion backlog — promote something to Ready)
# Exit 1 = Notion API down (check NOTION_API_KEY + network)
# Exit 2 = config error (fix config.json or env var)

python hal-stack/notion-sync/notion-client.py --test
# Expect: "OK: found N open Claude Code sprint(s)."
```
