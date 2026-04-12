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
TIMESTAMP: 2026-04-12 00:15 EST (Toronto)
SOURCE: Claude.ai chat (tonight's session)
PRIORITY: P2
TYPE: story
CATEGORY: HAL Stack
ITEM: Journey archive rediscovery — update journey/ with April 2-12 content
CONTEXT: Tonight Aaron rediscovered the journey/ directory (3 chapters, raw session logs, social posts, commit density timeline). Last entry is April 1. There's a 10-day gap (Sessions 11-21) with no journey coverage. The archive needs chapters 4+ covering the HAL Stack sovereign foundation build, branding sprint, cross-context ingestion, and the sprint automation system.
ACTION: Write journey chapters and raw session notes for April 2-12. Continue the existing narrative style (third-person, magazine-feature, emotionally honest). Update social/ with new LinkedIn post candidates.
---

---
TIMESTAMP: 2026-04-12 00:15 EST (Toronto)
SOURCE: Claude.ai chat (tonight's session)
PRIORITY: P2
TYPE: story
CATEGORY: HAL Stack
ITEM: NB (Notebook) layer idea — capture and evaluate
CONTEXT: Aaron discussed an "NB layer" concept tonight. This needs to be captured as a proper idea with description, use case, and how it fits into the HAL Stack architecture. Details are in tonight's Claude.ai chat — Aaron should add specifics when reviewing this capture.
ACTION: Aaron to clarify the NB layer concept. Then evaluate for fit within HAL Stack and add to backlog if viable. [VERIFY — Aaron: please add detail about what the NB layer is]
---

---
TIMESTAMP: 2026-04-12 00:15 EST (Toronto)
SOURCE: Claude.ai chat (tonight's session)
PRIORITY: P2
TYPE: epic
CATEGORY: Employment
ITEM: Employability project — formalise as a tracked workstream
CONTEXT: Aaron discussed an employability project tonight that should be tracked alongside consulting work. This connects to the 56 employment-related conversations found in the Claude.ai data export (Session 16) and the employment-recovery.md document. It may involve recovering resume/CV assets from Claude.ai project storage.
ACTION: Create a formal epic in the backlog. Define scope: is this active job search, career positioning, or maintaining employability as insurance while building Two Birds? [VERIFY — Aaron: clarify intent]
---

---
TIMESTAMP: 2026-04-12 00:15 EST (Toronto)
SOURCE: Claude.ai chat (tonight's session)
PRIORITY: P1
TYPE: story
CATEGORY: Two Birds
ITEM: Career frame — "AI product evaluator / critical user" positioning
CONTEXT: Aaron identified a career positioning angle tonight: framing himself as an AI product evaluator and critical user, not just a builder. This connects to his 20+ years of product management and his hands-on experience evaluating Claude, GPT, Gemini, and other tools from a non-developer perspective. This is a differentiated positioning that most AI consultants can't claim — he's both a power user and a professional product evaluator.
ACTION: Capture this frame in the brand guidelines and/or culture-spec. Evaluate how it changes the consulting pitch, LinkedIn positioning, and CV narrative. This could be a chapter in the journey archive.
---

---
TIMESTAMP: 2026-04-12 00:15 EST (Toronto)
SOURCE: Claude.ai chat (tonight's session)
PRIORITY: P2
TYPE: story
CATEGORY: HAL Stack
ITEM: Sprint 22-25 draft plans — discussed but not yet built
CONTEXT: Aaron outlined sprint plans for Sessions 22-25 in tonight's Claude.ai chat. These have NOT been converted into sprint-queue.md entries with ready-to-paste prompts. The plans need to be extracted from the chat and formalised.
ACTION: Aaron to paste or summarise the sprint 22-25 plans. Convert each into a sprint-queue.md entry with a complete prompt. [VERIFY — Aaron: paste the draft plans or summarise what S22-S25 should cover]
---

---
TIMESTAMP: 2026-04-12 00:15 EST (Toronto)
SOURCE: Claude.ai chat (tonight's session)
PRIORITY: P1
TYPE: human-backlog
CATEGORY: HAL Stack
ITEM: Feedback — Claude was too reactive, not proactive enough
CONTEXT: Aaron flagged that Claude (across sessions) has been too reactive — waiting for instructions instead of proactively identifying what needs to happen next. Aaron wants the system (personas, sprint prompts, session workflows) to push back MORE, anticipate needs, flag risks unprompted, and bring prepared recommendations rather than waiting to be asked. This is a culture-spec and persona behaviour issue, not a technical bug.
ACTION: Update culture-spec.md with explicit "proactive, not reactive" rule. Review all persona definitions — are any too passive? Update sprint template to include a "proactive flags" section where Claude surfaces concerns before being asked. This is a PATTERN FIX, not a one-time correction.
---

---
TIMESTAMP: 2026-04-12 00:15 EST (Toronto)
SOURCE: Claude.ai chat (tonight's session)
PRIORITY: P1
TYPE: blocker
CATEGORY: Two Birds
ITEM: Priority one urgency question for Aaron's morning
CONTEXT: Aaron flagged a P1 urgency item that needs to be addressed first thing in the morning. The specific question was discussed in tonight's Claude.ai chat but the details need to be confirmed here. [VERIFY — Aaron: what is the P1 morning question? This capture has the priority but not the content.]
ACTION: Aaron reviews this item in the morning and adds the actual question. This blocks sprint planning until answered.
---
