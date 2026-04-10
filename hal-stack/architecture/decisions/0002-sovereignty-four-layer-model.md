<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:05 EST (Toronto)
Confidence: HIGH
Known gaps: None
-->

# ADR-0002: Sovereignty Four-Layer Model

**Date:** 2026-04-10
**Status:** Accepted
**Layer:** L1-L4 (this decision applies to all layers)

## Context

Two Birds Innovation runs on a mix of commercial cloud services (Claude, GitHub, Formspree) and local tools (git, static files, Windows Task Scheduler). Aaron needs a framework to ensure no vendor can hold the business hostage, without over-engineering backup systems he doesn't need today.

Prior art: the Float-Free Architecture (March 2026) documented vendor-specific escape plans. This ADR generalises that into a design principle.

## Decision

Adopt a four-layer sovereignty model (L1-L4) as described in `sovereignty-principles.md`. Every component gets tagged with its current layer and must have at least L2 and L4 candidates identified.

Key terms:
- **Decapitation:** dropping from one layer to a lower one
- **Headless Claude:** treating Claude as a swappable LLM backend
- **Layer tag:** L1/L2/L3/L4 label on every component, epic, and tool evaluation

## Consequences

- Every new tool evaluation must include layer compatibility assessment
- Backlog items get layer tags
- Quarterly "decapitation drill" tests one L1→L2 swap
- Slight overhead in documentation, but prevents catastrophic vendor lock-in
- Builds on Float-Free work rather than replacing it
