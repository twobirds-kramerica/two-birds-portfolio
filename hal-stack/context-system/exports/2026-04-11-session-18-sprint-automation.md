## Session Metadata

| Field | Value |
|-------|-------|
| **Date** | 2026-04-11 |
| **Title** | Sprint automation system — queue, triggers, retro, human backlog |
| **Project** | HAL |
| **Layer** | L1-L4 |
| **Tool** | Claude Code (Opus 4.6, 1M context) |
| **Machine** | EZbook (EZJumper) |
| **Duration** | ~1 hour |

## Decisions Made

| Decision | Confidence | Reversible? | Notes |
|----------|-----------|-------------|-------|
| Sprint queue stores complete prompts, not references | HIGH | Yes | Each sprint entry contains the full Claude Code prompt ready to paste |
| "Next sprint" = read queue, run first READY item | HIGH | Yes | Simple, predictable, phone-friendly |
| Retro uses GitHub raw URL as bridge | MEDIUM | Yes | Workaround for Claude.ai's inability to read local files |
| Human backlog is one flat file, not per-session | HIGH | Yes | Single source of truth beats scattered "morning actions" lists |
| 8 sprints queued with 5 READY | HIGH | Yes | S-001 (keyword map) runs next |

## Open Questions

- [ ] Does `next-sprint.bat` actually launch Claude Code correctly on Windows?
- [ ] Should CLAUDE.md's "next sprint" trigger be updated to point at the new queue?

## Next Actions

1. Aaron uploads Two Birds logo to LinkedIn
2. Aaron tries "next sprint" command for the first time
3. Aaron knocks off NOW items from human-backlog.md

## Key Context for Future Sessions

Session 18 completes the sprint automation loop. Aaron can now run sprints with a two-word command and review results from his phone. The sprint queue has 8 entries with 5 ready to run. The human backlog consolidates 11 open action items from Sessions 11-17 into one file. The retro system has a known gap (Claude.ai can't read local files directly) that's worked around via GitHub raw URL. The next "next sprint" will execute S-001 (Voice Keyword Command Map).
