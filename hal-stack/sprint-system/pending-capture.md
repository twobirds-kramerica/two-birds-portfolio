# Pending Capture Queue

Items captured from Claude.ai chats that need to be merged into the real backlog on the next Claude Code run.

## Format

Each item uses this template:

```
---
TIMESTAMP: [when captured]
SOURCE: [which chat, if known]
PRIORITY: P1 / P2 / P3
TYPE: human-backlog / story / epic / blocker / issue
CATEGORY: HAL Stack / DCC / Two Birds / Employment / Personal
ITEM: [one sentence]
CONTEXT: [2-3 sentences why it matters]
ACTION: [what needs to happen]
---
```

## How to Add Items

In any Claude.ai chat, say "capture: X" or "add X to backlog." The Claude instance generates a short Claude Code prompt that appends a formatted block to this file. Aaron pastes it on his next Claude Code session.

See `capture-prompt.md` for the full instructions any Claude instance follows.

## How Items Get Merged

Every Claude Code sprint starts by checking this file. If items exist:

1. Parse each item
2. Route to correct destination (human-backlog.md, stories.md, or epics.md) based on TYPE
3. Preserve priority, category, and context
4. Delete merged items from this file
5. Commit: `chore(hal): merged N captured items from pending queue`

## Current Queue

---
TIMESTAMP: 2026-04-11 23:15 EST (Toronto)
SOURCE: Claude.ai chat
PRIORITY: P3
TYPE: story
CATEGORY: HAL Stack
ITEM: Verify capture command loop works end-to-end
CONTEXT: Added capture-prompt.md to GitHub and new Claude.ai userPreferences that reference it. Testing the full flow: Claude.ai generates prompt → Aaron pastes into Claude Code → pending-capture.md gets updated → next sprint merges it.
ACTION: Paste the prompt below into Claude Code. Verify pending-capture.md shows the new entry. Confirm the commit message appears in git log. Report back in Claude.ai what worked.
---
