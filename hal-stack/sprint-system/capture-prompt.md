<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 22:42 EST (Toronto)
Confidence: HIGH
Known gaps: None
-->

# Capture Instructions for Claude Instances

When Aaron says "capture: [item]" or asks you to add something to his backlog in any Claude.ai chat, do the following:

## Step 1 — Classify

Infer from context:
- **Priority:** P1 (blocking other work), P2 (important, not blocking), P3 (nice to have)
- **Type:** human-backlog (Aaron does it), story (Claude Code builds it), epic (big theme), blocker (something stuck), issue (bug or problem)
- **Category:** HAL Stack, DCC, Two Birds, Employment, Personal

Only ask Aaron to clarify if truly ambiguous. Default to P2 / story / HAL Stack.

## Step 2 — Generate the Claude Code Prompt

Give Aaron this prompt to paste into Claude Code:

```
Read hal-stack/sprint-system/pending-capture.md and append this item to the Current Queue section, then commit with message "chore(hal): captured item from Claude.ai" and push to master:

---
TIMESTAMP: [today's date and time]
SOURCE: Claude.ai chat
PRIORITY: [P1/P2/P3]
TYPE: [human-backlog/story/epic/blocker/issue]
CATEGORY: [category]
ITEM: [one sentence description]
CONTEXT: [2-3 sentences of why]
ACTION: [what needs to happen]
---
```

## Step 3 — Confirm

Tell Aaron: "Captured. Paste this into Claude Code when you're next at a machine, or it'll get picked up on the next sprint."

## Example

Aaron says: "capture: need to test the DCC feedback form on an actual phone"

You respond with:

> Captured as P2 human-backlog item. Paste this into Claude Code:
>
> `Read hal-stack/sprint-system/pending-capture.md and append this item to the Current Queue, commit "chore(hal): captured item from Claude.ai", push to master:`
>
> ```
> ---
> TIMESTAMP: 2026-04-11 22:42 EST
> SOURCE: Claude.ai chat
> PRIORITY: P2
> TYPE: human-backlog
> CATEGORY: DCC
> ITEM: Test DCC feedback form on a real phone (not desktop browser)
> CONTEXT: Form hardening done in S11 but never tested on actual mobile device. Brenda uses a phone.
> ACTION: Aaron opens DCC on phone, taps feedback button, tries submitting empty → should see inline errors
> ---
> ```

## Mobile Shortcut

If Aaron is on his phone and can't paste a long prompt, he can just type into Claude Code:

```
Read and append to hal-stack/sprint-system/pending-capture.md:
ITEM: [whatever Aaron says]
Then commit and push.
```

Claude Code will fill in the template fields from context.

## Important: Honesty About What Actually Happened

When you generate a capture prompt for Aaron:

1. Tell Aaron: "Paste this into Claude Code when you have a moment. It takes 30 seconds and the item will be properly merged on the next sprint."
2. **Do NOT pretend you have actually added the item.** You have only generated the prompt Aaron needs to run. The item only becomes real when Claude Code executes the append.

## Emergency Captures

If Aaron flags a P1 BLOCKER that needs immediate attention (not just tracking):

1. Still generate the capture prompt above (for tracking)
2. Also immediately tell Aaron what the blocker is, why it matters, and what the fastest resolution path looks like
3. Offer to help handle the blocker directly in the current chat if possible — don't just log it and move on

## Merge Trigger

The next "next sprint" run checks pending-capture.md first (Phase 0 of every sprint). If items exist, they get merged before the sprint work runs. Aaron doesn't need to do anything — the merge is automatic.
