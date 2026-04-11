<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 02:35 EST (Toronto)
Confidence: HIGH — based on patterns from 15 sessions
Known gaps: None
-->

# Sprint Prompt Writing

**Domain:** Engineering / Operations
**Layer Compatibility:** L1-L4

## What It Does
Creates effective Claude Code sprint prompts with proper structure, commit discipline, session state updates, and context export. Works with any AI coding tool, not just Claude Code.

## Prerequisites
- `SESSION-STATE.md` — current state
- `NEXT-SPRINT-QUEUE.md` or `hal-stack/backlog/epics.md` — what to work on
- `context-system/claude-code-auto-export.md` — auto-export block

## Instructions

1. **Read SESSION-STATE.md.** Know what was done last, what's pending, what's blocked.
2. **Define the objective.** One sentence: what does this sprint produce?
3. **Break into phases.** Each phase is a commit-sized chunk. Order by dependency and priority.
4. **Set time targets.** Estimate per phase. Total sprint should be 2-4 hours max.
5. **Write the RULES section.** Include:
   - Commit after each phase
   - Quality over completeness
   - No scope creep — improvements go to backlog
   - Plain language, draft labelling, timestamps
6. **Write the FINAL STEP.** Must include:
   - Update SESSION-STATE.md
   - Auto-generate context export (paste block from `claude-code-auto-export.md`)
   - Final commit and push
7. **Include context.** If the sprint builds on prior work, include the relevant SESSION-STATE entries or file paths. Don't assume the AI remembers prior sessions.
8. **Set priority order.** If time runs short, which phases get cut? State explicitly.

## Quality Checklist
- [ ] Objective is one clear sentence
- [ ] Phases are ordered by dependency
- [ ] Each phase has a commit message specified
- [ ] RULES section includes commit discipline
- [ ] FINAL STEP includes SESSION-STATE.md update and context export
- [ ] Time targets are realistic (not optimistic)
- [ ] Priority order specified for time-short scenarios
- [ ] Context from prior sessions included where needed

## Referenced By
- Naveen (VP Engineering) — reviews sprint prompts for scope and quality
- Val (Chief of Staff) — ensures sprint prompts respect Aaron's time constraints
- Sam (Senior Dev) — writes implementation-level sprint prompts
