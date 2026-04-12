<!--
STATUS: v0.1 — SESSION LOG
Created: 2026-04-11 23:00 EST (Toronto)
Confidence: HIGH
Known gaps: None
-->

# Session 21 Results — Capture System for Human Backlog

## TL;DR

Built the capture side of the retro loop. Any Claude instance can now generate formatted backlog items that Aaron pastes into Claude Code. Items queue in pending-capture.md and auto-merge on the next sprint via mandatory Phase 0. The complete loop is: run → retro → capture → merge.

## What Shipped

| Phase | Description | Commit | Files |
|-------|-------------|--------|-------|
| 1 | Pending capture queue file | `4731c82` (S21 earlier) | 1 |
| 2 | Capture prompt instructions (updated with honesty + emergency rules) | `158d82a` | 1 |
| 3 | Sprint template + queue updated with mandatory Phase 0 | `d0f78d7` | 2 |
| 4 | User preferences addition for Claude.ai | `0b5ecb7` | 1 |
| 5 | Session wrap | this commit | 3 |

## The Complete Loop

```
1. RUN    → Aaron types "next sprint" in Claude Code
2. RETRO  → Aaron pastes retro prompt into Claude.ai
3. CAPTURE → Aaron says "capture: X" in any chat
4. MERGE  → Next sprint auto-merges pending items (Phase 0)
```

## Aaron's Next Actions

1. **Add userPreferences text to Claude.ai settings** — open `hal-stack/sprint-system/user-preferences-addition.md`, copy the text block, paste into Claude.ai Settings → User Preferences. **2 min, one-time setup.**

2. **Test capture** — open a fresh Claude.ai chat, type `capture: test item`. Verify Claude generates a formatted prompt. Paste it into Claude Code to test the full loop. **3 min.**

3. **Verify merge** — next time you type "next sprint," confirm it checks pending-capture.md and merges the test item before running the sprint. **Automatic — just watch.**

## Known Limitations

1. **Capture requires Aaron to paste.** The generated prompt must be pasted into Claude Code for items to actually land. This is intentional — Aaron remains the gatekeeper.
2. **Minimum 1-prompt delay.** Items captured in Claude.ai don't appear in the backlog until Aaron runs the paste in Claude Code. This is the trade-off for keeping Aaron in control.
3. **Depends on GitHub raw URL.** The userPreferences tell Claude.ai to fetch capture-prompt.md from GitHub. If the repo is private or GitHub is down, the fetch fails. Aaron can paste the instructions manually as a fallback.

## Confidence Per Phase

| Phase | Confidence | Notes |
|-------|-----------|-------|
| 1-2: Capture system | HIGH | Simple markdown queue + instructions |
| 3: Sprint template | HIGH | Added mandatory Phase 0 — structural change |
| 4: User preferences | MEDIUM | Depends on Claude.ai actually fetching the URL |
| 5: Session wrap | HIGH | Factual log |
