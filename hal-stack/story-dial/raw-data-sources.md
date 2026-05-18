# Raw Data Sources — Story Dial
**Version:** 1.0 | **Created:** 2026-05-18

---

## What Feeds the Raw Layer

The raw story material is pulled automatically from three sources:

### 1. Git Commits (primary)
```bash
git log --oneline --after="7 days ago" --all --no-merges
```
Runs across all Two Birds repos. Commits are the most reliable receipt — timestamped, immutable, specific.

**Repos scanned:**
- `two-birds-portfolio` (HAL Stack, governance, context)
- `digital-confidence` (DCC product)
- `career-coach` (Career Coach product)
- `clarity` (Clarity product)
- `two-birds-innovation` (company site)
- `aaron-patzalek` (personal brand site)
- `kevins-apartment-search` (KAS project)

**What to look for in commits:**
- `feat:` → something new shipped
- `fix:` → a real problem was solved
- `log(SESSION-STATE):` → a sprint completed
- Commit messages that contain a story arc (discovery, pivot, problem → solution)

---

### 2. SESSION-STATE.md (secondary)
The "What Shipped" and "Next recommended action" sections of each sprint entry.
These are written in the moment — they contain the intent and the context behind the commits.

Extracted section format:
```
## ⚡ [date] — [sprint ID]: [sprint title]
### What Shipped
[content]
```

---

### 3. Notion Agency Log (context)
Previous entries are read to avoid repeating the same story or the same framing.
Also used to identify the correct next entry number.

**Notion DB:** Command Center / Agency Log
**Query:** All entries ordered by entry number desc, limit 3

---

## Story Candidate Criteria

Not every commit becomes a story. The following qualify as story-worthy:

| Signal | Example |
|--------|---------|
| Problem discovered + solved same session | CI silently failing, fixed overnight |
| A pivot or course correction | $479K projection → zero validation discovered |
| A capability unlocked | SME Reviewers created → 8 rows cleared to Ready-to-Build |
| A pattern or learning | /loop pattern from Boris Cherny → overnight automation |
| A first (first of its kind in the build) | First live SME review catching real issues |

**Not story-worthy (stay as log):**
- Routine batch work with no unexpected discovery (e.g., "advanced 35 rows in Notion")
- Config changes, typo fixes, dependency bumps
- Work where the "what" is mechanical and the "so what" is absent

---

## Raw Story Format

When `chronicle-weekly.py` creates the Notion stub, it writes the Raw Story section:

```
## Raw Data — Week of [date]

### Commits (last 7 days)
[list of feat/fix commits with hashes]

### Story candidates
[1-2 candidates identified from commits + SESSION-STATE]

### Receipts
[list of commit hashes, Notion IDs, file paths that evidence the story]

### Suggested story arc
[one paragraph — what happened, in plain language, no spin]

---
Status: Raw Data Ready — awaiting Chronicle session
```

---

## Automation Schedule

| Layer | What | When | How |
|-------|------|------|-----|
| Layer 1 (autonomous) | `chronicle-weekly.py` pulls commits → creates Notion stub | Thursday 2am (overnight bat) | No Claude API needed |
| Layer 2 (Claude Code) | Story written, dial applied, formats produced | Next Claude Code session after stub | `Chronicle this week's entry at dial 3` |
| Aaron review | Open Notion, read Raw Story, approve or redirect | After Layer 2 completes | Status: Draft → Published |
