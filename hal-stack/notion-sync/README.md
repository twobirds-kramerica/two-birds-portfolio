# Notion ↔ GitHub Sync (HAL Stack)

Bidirectional sync between Aaron's Notion Command Center and the GitHub sprint queue. Notion is the source of truth for backlog item state; GitHub markdown is a read-only mirror.

## Architecture

```
 Notion Command Center (source of truth for backlog state)
   └─ Product Backlog database
        └─ items filtered by Type=Sprint AND Owner=Claude Code
             │
             │  notion-client.py  (read/update via Notion API v1)
             │
             ├──► sync-queue.py          → sprint-queue-from-notion.md
             ├──► next-sprint.py         → locks next READY item, returns details
             └──► complete-sprint.py     → marks Done, records commit hash in Notes
                      │
                      ▼
                 SYNC-LOG.md (append-only event log)

 Local fallback path:
   If the Notion API is unreachable, all scripts fall back to the hand-
   maintained sprint-queue.md. No items are ever deleted from local.
```

## Files

| File | Purpose |
|------|---------|
| `config.json` | Data source IDs, status mapping, Notion API version, property names |
| `notion-client.py` | API wrapper + reusable helpers. `python notion-client.py --test` verifies connectivity. |
| `sync-queue.py` | Pulls sprints from Notion, writes `hal-stack/sprint-system/sprint-queue-from-notion.md` |
| `next-sprint.py` | Finds highest-priority READY Claude Code sprint, marks it In Progress, prints details |
| `complete-sprint.py` | Takes a sprint name or Notion page ID + commit hash, marks Done, logs completion |
| `SYNC-LOG.md` | Append-only sync event log (created on first run) |
| `SETUP.md` | One-time setup: create Notion integration, share Command Center, set `NOTION_API_KEY` |

## Invariants

- `NOTION_API_KEY` is read from env var only. Never committed.
- All Notion API calls are wrapped in try/except. On failure, callers fall back to local files and the error is recorded in `SYNC-LOG.md`.
- `sync-queue.py` never deletes from `sprint-queue.md`. It only generates a parallel `sprint-queue-from-notion.md`. Migration to a single source is a later, deliberate cutover.
- Valid status transitions: `Ready` → `In Progress` → (`Done` or `Blocked` or `Review`).

## Python environment

- Python 3.10+ (confirmed available on all three Aaron machines).
- Single external dependency: `requests`. Install once per machine: `pip install requests`.
- Everything else is stdlib.

## Commands

```
python notion-client.py --test                  # verify connection + list open Claude Code sprints
python sync-queue.py                            # pull Notion → sprint-queue-from-notion.md
python next-sprint.py                           # lock next sprint (Ready → In Progress), print details
python complete-sprint.py <name-or-page-id> <commit-hash>
```

## Source-of-truth rules

- **Backlog item state (Status, Priority, Owner):** Notion wins. `sprint-queue.md` is read-only.
- **Sprint content (prompts, phase instructions, expected outputs):** local markdown wins. Notion tracks item-level state only.
- **Conflicts:** logged to `SYNC-LOG.md` with timestamp. Notion status is applied. Local metadata is preserved.

## First-time setup

See `SETUP.md`.
