# Backlog Item Format — Two Birds Innovation
Use this template when filing items to the Notion Product Backlog.
Last synced from CLAUDE.md: 2026-04-28.

## ITEM TEMPLATE

```
ITEM: [one-line title, imperative verb]
PRIORITY: P1 | P2 | P3 | P4
TYPE: Sprint | Feature | Bug | Task | Research | Decision | Human Action
OWNER: Aaron | Claude Code | Drew (PM) | Pending
PRODUCT: HAL Stack | DCC | Two Birds Innovation | Career Coach | Clarity | (etc.)
NOTES: [2-3 sentence context — why this matters, any deadline, any blocker]
```

If any field is ambiguous, mark it `Pending` rather than guessing.

## NOTION-SYNC HELPERS
All proven end-to-end via the 2026-04-21 run. See `hal-stack/notion-sync/notion-client.py`:
- `build_backlog_properties(item, status, priority, type_, owner, product, notes)` + `create_backlog_item(client, ...)` — Product Backlog one-call row creation
- `build_research_row_properties(...)` + `create_research_row(client, ...)` — DCC Kids Research DB one-call creation with enum validation
- `NotionClient.create_page`, `.update_page_properties`, `.set_select`, `.append_to_rich_text` (auto-chunks >2000-char appends)
- CLI: `--test`, `--dry-run-create`

## BACKLOG IDS
- Product Backlog data source: `dee08637-7122-46cd-bc29-7775ce3ab8f6`
- Command Center page: `347a09cf-876a-81fb-9a5c-eca696fb585b`
