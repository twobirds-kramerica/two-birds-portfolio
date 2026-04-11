<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 01:30 EST (Toronto)
Confidence: HIGH
Known gaps: None
-->

# Claude Code Auto-Export

Copy-paste this block into any Claude Code sprint prompt to get automatic context export at session end. Add it to the FINAL STEP section of your sprint prompts.

## Block to Add to Sprint Prompts

```
FINAL STEP — AUTO-EXPORT CONTEXT:
After updating SESSION-STATE.md, auto-generate a context export.

1. Create hal-stack/context-system/exports/[YYYY-MM-DD]-[session-title].md
   using the template in context-export-template.md.
2. Fill in ALL fields by reviewing the work done this session.
3. Add a one-line entry to context-system/context-index.md (newest first).
4. Include this export in the final commit.

Aaron should NOT need to fill anything out. Generate the export from 
the session's actual work. If uncertain about a field, mark it with 
"[VERIFY]" so Aaron can correct in 30 seconds.
```

## How to Use

Add the block above to the FINAL STEP section of any sprint prompt. Claude Code (or any AI coding tool) will auto-generate the export as part of its normal session-end duties.

## Example Integration

Your sprint prompt might end with:

```
FINAL STEP: Update SESSION-STATE.md with session entry.
[paste auto-export block here]
Final commit, push to master.
```

## What Gets Generated

A markdown file in `exports/` with:
- Session metadata (date, project, layer, tool, machine)
- Every decision made with reasoning
- Open questions for Aaron
- Next actions
- List of files created/modified
- Key context for future sessions

## Aaron's Role

**Glance. Correct. Confirm.** 30 seconds max. If the export looks right, do nothing — it's already committed. If something's wrong, edit the file and commit the fix.
