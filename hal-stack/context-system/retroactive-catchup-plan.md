<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:10 EST (Toronto)
Confidence: LOW — data export process not verified, depends on Claude.ai features
Known gaps: Claude.ai export format unknown, may not include full chat history
-->

# Retroactive Context Catchup Plan

## Problem

Aaron has had dozens of Claude.ai (web) sessions since January 2026. Those sessions contain decisions, research, and context that are not captured in the context-index. They exist only in Claude.ai's chat history, which is:

- Not searchable across chats
- Not exportable in a structured format (as of April 2026)
- Locked to Anthropic's platform (L1-only)

## Goal

Recover the most valuable context from past sessions and export it into the context bridge system so it's portable and searchable.

## Step-by-Step Plan

### Step 1: Request Claude.ai Data Export (BLOCKER: Aaron)

1. Go to claude.ai → Settings → Account
2. Look for "Export my data" or "Download my data"
3. If available: download and save to `C:\twobirds\two-birds-portfolio\hal-stack\context-system\raw-exports/`
4. If not available: skip to Step 2

**Honest note:** As of April 2026, Claude.ai may not offer full chat export. This step may produce nothing useful. That's fine — move to Step 2.

### Step 2: Manual Recovery Sprint (1-2 hours, Aaron + LLM)

Aaron scrolls through his Claude.ai chat history and identifies the 10 most important sessions. For each:

1. Open the chat
2. Copy the key decisions, artifacts, and context
3. Paste into `context-export-template.md`
4. Save as an export file
5. Add to `context-index.md`

Priority sessions to recover:
- [ ] First DCC architecture decisions
- [ ] Revenue strategy / CA$10K target planning
- [ ] Mike K / Paperwork Labs initial research
- [ ] Faceless brand / influencer concept
- [ ] Government grant research (New Horizons, CRTC)
- [ ] B2B pricing and pilot proposal development
- [ ] Float-free architecture initial research
- [ ] LinkedIn content strategy planning

### Step 3: Future Prevention

Going forward, every significant session ends with a context export. This is built into the CLAUDE.md workflow — "After every session: overwrite logs/RETRO.md and push."

Add to CLAUDE.md (when Aaron approves):
```
After every significant session: fill context-export-template.md, add to context-index.md.
```

## Dependency Note

Step 1 depends on Claude.ai's data export feature, which is an L1 dependency. If Anthropic doesn't offer it, the data stays in their platform. This is exactly the kind of lock-in the sovereignty model is designed to prevent going forward — but for past data, there's no L4 fallback. We can only recover manually (Step 2).

## Timeline

- Step 1: Aaron checks next time he's on claude.ai (5 minutes)
- Step 2: Schedule as a 2-hour session when Aaron has time. Not urgent — the most important recent context is already in SESSION-STATE.md and git history.
- Step 3: Add to CLAUDE.md after Aaron reviews the context system.
