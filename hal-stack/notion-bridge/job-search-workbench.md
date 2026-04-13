# Job Search Workbench (Notion)

**Status:** Active
**Owner:** Aaron
**Created:** April 13, 2026
**Lives in:** Notion (under Two Birds Innovation hub)
**Brain:** Claude (any chat session in the Job Search Project on Claude.ai)

## What this is

Live system for vetting and tracking job postings. Aaron pastes a posting into Claude chat. Claude scores it against the locked framework (Capability 35 / Title 15 / Values 20 / Survivability 15 / Comp 15). Tier 3 skips auto-write to the database. Tier 1 and 2 wait for Aaron's go/no-go before writing.

## Direct links

- **Two Birds Innovation hub (Notion):** https://www.notion.so/341e616fed0981ada084cba16edda7bb
- **Job Search Workbench (Notion):** https://www.notion.so/341e616fed0981ce9e69e7f6c9b248ad

## Source of truth for the framework

The canonical scoring framework lives in the Claude project as `Aaron_JobSearch_Framework_v1.md`. The version in the Notion Workbench page is a working copy. **If they ever drift, the Claude project file wins.**

## Backup plan

1. Monthly: Notion Settings > Export > Markdown & CSV > save the zip
2. End of any working session: ask Claude for a markdown backup of the Jobs database
3. Framework canonical version stays in the Claude project, not Notion

## Open infrastructure issue

**GitHub MCP not connected to Claude.ai.** Discovered April 13, 2026. Until resolved, all GitHub commits from chat sessions have to route through Claude Code as a two-step. Logged as P1 in the Two Birds Innovation hub backlog (Notion).

## Schema (Jobs database)

Fields: Company, Role Title, Status, Tier, Total Score, Capability /35, Title Alignment /15, Values Lifestyle /20, Interview Survivability /15, Comp Alignment /15, Location, Comp Range, Recommended Resume (Ops/Innovation), Baseline ATS, Projected ATS, Source, Posting URL, Date Added, Rationale, Notes.

Status options: Lead / Drafting / Applied / Interview / Offer / Closed-Lost / Skipped
Tier options: Tier 1 - Customize / Tier 2 - Base resume / Tier 3 - Skip
