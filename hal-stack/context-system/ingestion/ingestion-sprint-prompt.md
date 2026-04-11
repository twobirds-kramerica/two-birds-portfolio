<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 01:35 EST (Toronto)
Confidence: MEDIUM — prompt is comprehensive but export format is unknown
Known gaps: Claude.ai export format not verified
-->

# Ingestion Sprint Prompt

Aaron: paste this entire block into Claude Code when your data export arrives.

---

```
CLAUDE.AI DATA EXPORT INGESTION SPRINT
Repo: C:\twobirds\two-birds-portfolio\
Target: 2 hours max

STEP 0 — FORMAT DETECTION

Look in: hal-stack/context-system/ingestion/raw/

Detect the export format:
- If ZIP: unzip in place, then examine contents
- If JSON: read and parse structure
- If HTML: read as text, extract conversation content
- If multiple files: list them, identify the structure
- If format is unknown: describe what you see and STOP

Report: file count, total size, format, date range of conversations.

STEP 1 — SCAN AND CATEGORISE

Read through all conversations. For each one, categorise:

a. HAL-RELEVANT — contains architecture decisions, tool evaluations, 
   infrastructure planning, voice layer discussions, sovereignty model, 
   or HAL Stack design work

b. PRODUCT-RELEVANT — contains DCC, Career Coach, Clarity, or other 
   product decisions, design choices, or research

c. BUSINESS-RELEVANT — contains revenue strategy, pricing, B2B, 
   partnerships, Mike K / Paperwork Labs, government grants, LinkedIn 
   strategy, branding, or culture/values discussions

d. PERSONAL/SKIP — casual conversation, debugging help, one-off 
   questions that don't carry forward

Create a summary table: conversation date, title (generated), category, 
one-line summary, importance (HIGH/MED/LOW).

STEP 2 — GENERATE CONTEXT EXPORTS

For every HIGH or MEDIUM importance conversation:
1. Generate a context export using the template in context-export-template.md
2. Save to hal-stack/context-system/exports/YYYY-MM-DD-[title].md
3. Focus on DECISIONS and CONTEXT, not implementation details

For LOW importance: skip entirely. Don't waste tokens.

STEP 3 — UPDATE INDEX

Add all new exports to context-index.md (newest first). One line each.

STEP 4 — FLAG FOR AARON

Create: hal-stack/context-system/ingestion/ingestion-results.md

Include:
a. Total conversations processed
b. Category breakdown (how many HAL, product, business, skipped)
c. DECISIONS NEEDING RATIFICATION — any decision from past sessions 
   that contradicts current architecture or hasn't been formally accepted
d. CONTRADICTIONS — anything in past sessions that conflicts with 
   current hal-stack/ docs
e. EXPECTED BUT MISSING — check against expected-discoveries.md. 
   What did we expect to find but didn't?
f. SURPRISES — things found that weren't expected

STEP 5 — COMMIT

Commit: "feat(hal): Claude.ai data export ingested — [N] sessions processed"
Do NOT commit the raw export files (they may contain personal data).
Push to master.

IMPORTANT:
- Do NOT modify any existing hal-stack/ files based on what you find. 
  Only CREATE new exports and UPDATE the index.
- Flag contradictions but do not resolve them. Aaron decides.
- If the export is too large to process in one session, process the 
  most recent 3 months first and create a story for the rest.
```
