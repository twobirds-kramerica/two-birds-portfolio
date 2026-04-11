<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 02:35 EST (Toronto)
Confidence: HIGH
Known gaps: None
-->

# Sovereignty Audit

**Domain:** Engineering / Legal / Finance
**Layer Compatibility:** L1-L4

## What It Does
Evaluates any tool, service, or component against the four-layer sovereignty model. Produces a decapitation checklist entry and a risk assessment.

## Prerequisites
- `architecture/sovereignty-principles.md` — the four-layer model
- `architecture/decapitation-checklist.md` — the template and existing entries

## Instructions

1. **Identify the component.** What is it? What does it do for Two Birds?
2. **Determine current layer.** Is it L1 (commercial cloud), L2 (alt commercial), L3 (hosted open-source), or L4 (local)?
3. **Assess data portability.** Can Aaron export his data in a standard format (JSON, CSV, markdown)? Or is it locked in the vendor's system?
4. **Identify L2 candidate.** What's the alternative commercial service? How long to switch? What data moves?
5. **Identify L3 candidate.** What open-source equivalent exists? What VPS cost? How long to set up?
6. **Identify L4 candidate.** What runs locally on Aaron's hardware? What's the quality loss? What hardware is needed?
7. **Estimate decapitation cost.** Hours to drop from L1→L2, L1→L3, L1→L4.
8. **Assess risk level.** What happens if this vendor becomes hostile tomorrow? LOW (inconvenience), MEDIUM (disruption), HIGH (business-threatening).
9. **Determine priority.** Should fallback be built NOW, SOON, LATER, or NEVER?
10. **Write the checklist entry.** Add to `decapitation-checklist.md` using the template.

## Quality Checklist
- [ ] All four layers documented (or explicitly marked "no L4 equivalent")
- [ ] Data portability assessed honestly
- [ ] Decapitation costs are in hours, not vague ("low effort")
- [ ] Risk level justified with reasoning
- [ ] Entry added to decapitation checklist
- [ ] Summary dashboard in sovereignty-principles.md updated

## Referenced By
- Naveen (VP Engineering) — before adopting any tool
- Helen (General Counsel) — evaluating vendor contracts
- Raj (CFO) — cost comparison across layers
- Jordan (DevOps) — infrastructure decisions
- Claire (CSO) — strategic vendor dependencies
