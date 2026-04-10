<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:05 EST (Toronto)
Confidence: HIGH — drawn from Aaron's stated values across 11 sessions
Known gaps: None
-->

# HAL Stack — Design Principles

These principles govern every decision in the HAL Stack. When two principles conflict, the one listed higher wins.

## 1. Sovereignty

No single vendor can hold Aaron's business hostage. Every component has a documented escape path. Data lives in portable formats. See `sovereignty-principles.md` for the full four-layer model.

**Layer:** L1-L4

## 2. Low-Cost / Free-Tier First

Aaron is a solo parent building a business. Monthly costs must stay under CA$50 for all infrastructure combined. Free tiers are preferred. Paid tiers are acceptable only when the free alternative would cost more in Aaron's time than the subscription saves.

**Current monthly:** ~CA$27 (Claude Pro) + CA$0 (everything else on free tiers)

## 3. Automation Over Manual

If Aaron does something more than twice, it should be automated. But automation must be sovereign — a cron job or shell script (L4) beats a cloud workflow (L1) for critical paths.

**Layer:** L4-native preferred for critical automation

## 4. Voice-First (Target)

Aaron's time is constrained by parenting. The target interface is voice: speak a command, HAL executes, reports back. Keyboard/terminal is the current interface; voice is the roadmap.

**Layer:** L1 (cloud STT) initially, L4 (local Whisper) target

## 5. Canadian Residency

Data should stay in Canada where possible. When using cloud services, Canadian or privacy-respecting jurisdictions preferred. This is both a values choice and a competitive advantage for Canadian government/library clients.

**Impact:** Influences VPS provider choice (L3), data storage location

## 6. Modular Reuse

Every component built for HAL should be separable. If a subsystem is good enough, it could become a product (e.g., prompt tracking → DevLoop). Design with clean boundaries.

**Layer:** L1-L4

## 7. Plain Language

All documentation in plain English (Canadian spelling). No jargon walls. Aaron's clients are library directors and credit union managers, not DevOps engineers. If HAL docs can't be understood by a smart non-technical person, they're too complex.

## 8. Static Over Dynamic

Products ship as static HTML/CSS/JS. No Node frameworks. No server-side rendering. No databases for client-facing products. This is a constraint that enables sovereignty — static files can be hosted anywhere.

**Layer:** L4-native by design
