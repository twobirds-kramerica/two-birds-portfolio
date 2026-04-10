<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:20 EST (Toronto)
Confidence: MEDIUM — research-based, nothing tested
Known gaps: Actual latency/quality on Aaron's hardware untested. Pricing may have changed.
-->

# Voice Layer — Voice-to-Machine Interface

The voice layer lets Aaron speak commands and hear responses instead of typing. This is critical for a solo parent whose hands are often busy with kids, cooking, or driving.

**Current status:** Research and planning complete. No code built yet.
**Layer target:** L1-L4 (start with cloud, path to fully local)

## What It Must Do

1. **STT (Speech-to-Text):** Hear Aaron speak → produce text
2. **Intent Parsing:** Understand what Aaron wants ("next sprint," "retro," "check DCC")
3. **Command Routing:** Map the intent to the right action (run a command, read a file, etc.)
4. **TTS (Text-to-Speech):** Speak the response back to Aaron

## Sovereignty Constraint

Each component must be independently swappable. The STT engine doesn't care what does the intent parsing. The command router doesn't care what produced the text. Interfaces between components are plain text strings.

```
[Microphone] → STT → "run next sprint" (plain text)
                         ↓
                    Intent Parser → { action: "sprint", args: ["next"] }
                         ↓
                    Command Router → executes action
                         ↓
                    TTS → [Speaker] "Sprint complete. Three items shipped."
```

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `component-breakdown.md` | What each component does, swap interfaces |
| `four-layer-options.md` | L1/L2/L3/L4 candidates per component |
| `aaron-signup-checklist.md` | Minimum accounts to create to start building |
| `build-sprint-plan.md` | First build sprint plan |
| `sovereignty-notes.md` | What's hard to make L4 and why |
