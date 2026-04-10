<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:03 EST (Toronto)
Confidence: HIGH — simple vocabulary, no unknowns
Known gaps: None
-->

# Layer Tags — Controlled Vocabulary

Use these tags consistently across all HAL Stack documents: epics, stories, tool evaluations, architecture decisions, and backlog items.

## Tags

| Tag | Meaning | When to Use |
|-----|---------|-------------|
| `L1` | Commercial cloud/SaaS — fast, proprietary | Current default implementation |
| `L2` | Alternative commercial — swap-ready fallback | Documented backup vendor |
| `L3` | Open-source on rented infrastructure | Self-hosted on VPS/cloud |
| `L4` | Open-source on local hardware — fully sovereign | Runs on Aaron's machines, no internet needed |

## Compound Tags

| Tag | Meaning |
|-----|---------|
| `L1-L4` | Works at all four layers (ideal) |
| `L1-L2` | Commercial only, no open-source path yet |
| `L1-only` | Vendor-locked, needs decapitation planning |
| `L4-native` | Built local-first, no cloud dependency |

## Usage in Documents

### In Epics/Stories
```
**Layer:** L1-L4
**Current:** L1 (Claude Code)
**Target:** L1 daily, L4 documented
```

### In Tool Evaluations
```
**Layer Compatibility:** L1-only (proprietary API, no local alternative)
**Recommendation:** Evaluate, do not depend
```

### In Architecture Decisions
```
**Layer Impact:** This decision locks us to L1 unless [mitigation].
```

## Rules

1. Every new epic, story, or tool recommendation MUST have a layer tag.
2. `L1-only` items get flagged for decapitation checklist within one sprint.
3. `L4-native` items get priority in architecture decisions when quality is comparable.
4. When in doubt, tag conservatively (assume more locked-in than you think).
