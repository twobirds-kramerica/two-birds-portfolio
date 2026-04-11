<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 02:35 EST (Toronto)
Confidence: HIGH
Known gaps: None
-->

# Skill Library

Reusable instruction sets any persona can reference. Skills are HOW-TO procedures, not characters with opinions.

## Skills vs Personas

| | Skills | Personas |
|---|--------|---------|
| **Purpose** | Consistent execution of known processes | Judgment, perspective, pushback |
| **Has opinions?** | No | Yes |
| **Can refuse?** | No — follows instructions | Yes — and should |
| **Example** | "Run the sovereignty audit checklist" | "VP Engineering says we shouldn't adopt this tool" |

## How to Create a New Skill

1. Copy `skill-schema.md`
2. Fill in all fields
3. Save as `skills/[skill-name].md`
4. Reference from relevant persona definitions

## How Personas Reference Skills

In a persona definition:
```
### Skills Referenced
- `sovereignty-audit.md` — when evaluating new tools
- `brand-identity-review.md` — when reviewing visual output
```

The persona decides WHEN to use the skill. The skill defines HOW to execute.

## Layer Compatibility

All skills should be L1-L4 compatible by default. If a skill requires a specific tool or service, document the L4 fallback.
