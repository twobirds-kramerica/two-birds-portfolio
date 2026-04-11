<!--
STATUS: v0.2 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:10 EST (Toronto)
Updated: 2026-04-11 01:30 EST (Toronto)
Confidence: HIGH
Known gaps: None
-->

# Context Export Template

## For AI Auto-Generation (preferred)

Paste this prompt into any LLM at the end of a session. It generates the export. Works with Claude, GPT, Gemini, Llama, anything.

### "Archive This Session" Prompt

```
Review our entire conversation and generate a context export in this exact format. Be thorough but concise. Only include decisions that matter for future sessions — skip routine implementation details.

## Session Metadata

| Field | Value |
|-------|-------|
| **Date** | [today's date] |
| **Title** | [one-line description of what this session accomplished] |
| **Project** | [project tag: DCC, Career Coach, Clarity, TBI, HAL, Portfolio, etc.] |
| **Layer** | [L1/L2/L3/L4 — what sovereignty layer was this session operating at?] |
| **Tool** | [Claude Code / Claude Web / GPT / Gemini / Manual / etc.] |
| **Machine** | [if known] |
| **Duration** | [approximate] |

## Decisions Made

| Decision | Confidence | Reversible? | Notes |
|----------|-----------|-------------|-------|
[List every judgment call. Include WHY, not just WHAT.]

## Open Questions

- [ ] [questions that weren't resolved — things Aaron needs to decide]

## Next Actions

1. [most important next step]
2. [second]
3. [third]

## Artifacts Created

| File | Repo | Description |
|------|------|-------------|
[List files created or modified with paths]

## Key Context for Future Sessions

[2-3 sentences capturing the most important thing a future session needs to know about this one. What changed? What's the new state of the world?]
```

## For Manual Use (L4 fallback)

If no AI is available, copy the template above and fill it in yourself. Takes about 5 minutes. Only do this for significant sessions — new architecture, major decisions, research findings. Skip it for routine bug fixes.

## Where to Save

Save as: `hal-stack/context-system/exports/YYYY-MM-DD-session-title.md`
Then add one-line entry to `context-index.md`.
