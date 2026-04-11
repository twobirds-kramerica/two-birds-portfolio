<!--
STATUS: v0.1 — AUTO-EXTRACTED
Created: 2026-04-11 15:45 EST (Toronto)
Source: Conversation #112, 54 messages, 2026-04-09
-->

# Max Plan Limits and Pro Plan Concerns

## Summary
Aaron hit usage limits on the Max plan and was concerned about what happens when he drops to the Pro plan. This is a direct sovereignty/cost concern — the Claude usage ceiling affects productivity. 54 messages suggest a detailed exploration of the issue.

## Decisions Made
- Concern flagged about Pro plan limits vs Max plan capacity
- Need to manage Claude usage more efficiently (this led to E7: Claude Code Quota Optimisation in the backlog)

## Key Context for Current HAL Stack
- Validates E7 epic (quota optimisation)
- The model-routing system in the persona framework partly addresses this — using Haiku/Sonnet for lower-tier personas reduces Opus consumption
- This concern is what makes the L4 (local LLM) path strategically important, not just theoretically important
