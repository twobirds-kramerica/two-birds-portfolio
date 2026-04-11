<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 01:35 EST (Toronto)
Confidence: MEDIUM — workflow is sound, Claude.ai export format unknown
Known gaps: Don't know what format Claude.ai data export uses (JSON? ZIP? HTML?)
-->

# Cross-Context Ingestion

Infrastructure to receive, process, and index Aaron's Claude.ai data export.

## What This Is

Aaron has 3+ months of Claude.ai (web) sessions containing decisions, research, and context that exist only in Anthropic's servers. When Aaron requests his data export, this folder contains everything needed to process it.

## Status

- **Blocker:** Aaron requests data export from claude.ai (he said he'll do this tomorrow)
- **Ready:** Ingestion sprint prompt is written and waiting
- **Not built:** Automated processing — the sprint prompt handles it via Claude Code

## Workflow

```
1. Aaron requests data export from claude.ai
   (Settings → Account → Export Data)

2. Export arrives (email link or direct download)

3. Aaron saves it to:
   C:\twobirds\two-birds-portfolio\hal-stack\context-system\ingestion\raw\

4. Aaron opens Claude Code and pastes:
   ingestion-sprint-prompt.md

5. Claude Code processes the export:
   - Detects format (JSON, ZIP, HTML, etc.)
   - Scans for HAL-relevant content
   - Generates summaries per session
   - Updates context-index.md
   - Flags decisions needing ratification
   - Flags contradictions with current docs

6. Aaron reviews flagged items (15-30 min)
```

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `ingestion-sprint-prompt.md` | Complete Claude Code prompt for processing |
| `expected-discoveries.md` | What we expect to find in the export |
| `raw/` | Where Aaron drops the export file (gitignored) |

## Important

- The `raw/` directory should be gitignored — export may contain personal data
- Processing output goes to `context-system/exports/` like any other context export
- This is a one-time operation (per export). Not an ongoing pipeline.
