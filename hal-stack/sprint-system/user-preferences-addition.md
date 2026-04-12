<!--
STATUS: v0.1 — DRAFT — NEEDS AARON TO ADD TO CLAUDE.AI SETTINGS
Created: 2026-04-11 23:00 EST (Toronto)
Confidence: HIGH
Known gaps: None
-->

# User Preferences Addition for Capture Command

Aaron: add the text below to your Claude.ai userPreferences. Do this once. After that, "capture: X" works in every future chat automatically.

## Where to Add It

1. Open claude.ai
2. Click your name (bottom left) → Settings
3. Find "User Preferences" or "Custom Instructions"
4. Paste the text below at the end of your existing preferences
5. Save

## Text to Add

```
Capture command: When I say "capture: [item]" or tell you to add 
something to my backlog, follow the instructions at 
https://raw.githubusercontent.com/twobirds-kramerica/two-birds-portfolio/master/hal-stack/sprint-system/capture-prompt.md 
— fetch it, read it, and generate the Claude Code prompt I need 
to paste. Do not pretend the item is added until I confirm I've 
run the prompt in Claude Code. If I flag something as P1 or a 
blocker, also help me handle it immediately in the current chat, 
not just log it.
```

## What This Does

After adding this, any Claude.ai chat will:
- Recognise "capture: X" as a backlog command
- Fetch the capture-prompt.md instructions from GitHub
- Generate a ready-to-paste Claude Code prompt
- Be honest that the item isn't real until Aaron runs the prompt
- Handle P1 blockers immediately, not just log them

## Testing

After adding the preference, open a fresh Claude.ai chat and type:

```
capture: test item — verify capture system works
```

Claude should respond with a formatted Claude Code prompt. Paste it into Claude Code to verify the full loop.
