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
TIMESTAMP: 2026-04-16 22:55 EST
SOURCE: Claude.ai chat
PRIORITY: P1
TYPE: blocker
CATEGORY: Personal
ITEM: Windows voice dictation not working on new laptop — blocks all voice-first workflows
CONTEXT: Aaron's primary input method is voice dictation. The new laptop (provided by Phil/Employment Services) was preloaded and may not have Windows properly activated. Voice dictation (Win+H) requires Windows activation. This blocks Claude.ai input, Claude Code input, and general productivity. Aaron believes it comes with one year of Office but is unsure about Windows activation status.
ACTION: Check Windows activation status (Settings > System > Activation). If not activated, find the product key (often on a sticker on the bottom of the laptop, or in Settings > System > About). If Windows is activated and dictation still doesn't work, check Settings > Privacy > Speech and ensure Online Speech Recognition is turned on. Also check Settings > Time & Language > Speech.
---
