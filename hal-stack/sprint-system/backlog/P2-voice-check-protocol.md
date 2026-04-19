---
id: P2-voice-check-protocol
priority: P2
status: READY
created: 2026-04-13
category: infrastructure
owner: Aaron
---

# P2 — Voice-check protocol for Claude compliance

## Problem

Claude repeatedly slips on writing-style rules that are already set in user preferences and project memory. Specifically: em dashes, banned words (spearheaded, leveraged, fostered, passionate, dynamic, results-driven, delve, tapestry, and the full banned list in user preferences), participial sentence openers, and other AI tells. The rules are reaching Claude. Compliance is the failure point, not configuration.

## Impact

Drafts Claude produces for Aaron (emails, notes, CV bullets, cover letters, outgoing content of any kind) must sound like Aaron wrote them. Every slip that escapes into a sent message costs credibility with a real recipient. Relying on Aaron to catch every slip manually is not sustainable across months of job search activity.

## Resolution

Add a voice-check protocol to Claude.ai user preferences. Mechanism: force Claude to output a single-line compliance tag at the bottom of every written draft, confirming it scanned for em dashes, banned words, participial openers, and AI tells. If the tag is missing, the draft is considered incomplete. This makes silent slips impossible. The tag is either there and accurate, there and wrong (visible to Aaron immediately), or missing (also visible).

### Exact text to add to user preferences

> Voice-check protocol. Before delivering any written content (email, message, CV bullet, cover letter, note, any draft I will send or use externally), scan the output for: em dashes, banned words (spearheaded, leveraged, fostered, passionate, dynamic, results-driven, delve, tapestry, additionally at sentence start, align with, boasts, bolstered, crucial, emphasizing, enduring, enhance, fostering, garner, highlight as verb, interplay, intricate, intricacies, key as filler adjective, landscape as metaphor, meticulous, pivotal, showcase, testament, underscore as verb, valuable, vibrant, nestled, groundbreaking, renowned, diverse array, rich heritage, natural beauty, commitment to), participial sentence openers, "serves as", "stands as", "marks a", "represents a" where "is" works, the rule of three used for rhythm, "not just X but Y" unless contrast is the point. Rewrite if any are found. End the response with a single-line compliance tag in this format: ✓ voice check: [scanned items] | [count caught] | [count fixed]. If the tag is missing on any written draft, the draft is considered incomplete. This applies to every chat.

## Why this is the most hands-off mechanism available

No fully hands-off solution exists. Claude cannot be fine-tuned from the chat interface. User preferences and project memory are the only configuration layers Aaron controls, and both already contain the writing-style rules. The gap is compliance, not configuration.

The voice-check tag is the lowest-effort mechanism that makes compliance visible and verifiable. Aaron does not have to proactively police every draft. The tag either appears accurate, appears inaccurate (caught on a glance), or is missing (also caught on a glance). Failures become cheap to surface without requiring Aaron to re-read every draft with a magnifying glass.

## Escalation path

If Claude starts skipping the tag or faking it, flag it in the moment, ask Claude to own the skip, and consider whether the instruction needs to be re-emphasized at the top of user preferences rather than buried lower. If that also fails, the problem is structural and the only fallback is Aaron reviewing every draft manually before sending.

## Related items

- P1: GitHub MCP connector not installed in Claude.ai (blocking direct commits from chat sessions)
- Logged in Notion: Two Birds Innovation hub, sub-page "P2 — Voice-check protocol (Claude compliance)"
- Source session: Job Search Workbench build, April 13, 2026

## Acceptance criteria

- [ ] Voice-check protocol text added to Claude.ai user preferences
- [ ] Verified in a fresh chat that Claude emits the voice-check tag on a test draft
- [ ] Verified the tag catches a deliberately-inserted em dash in a test draft
- [ ] Documented in hal-stack/protocols/voice-check.md for reference
