<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 02:15 EST (Toronto)
Confidence: HIGH — profiles are configuration, not code
Known gaps: Token costs are estimates
-->

# Engagement Profiles

Pre-built configurations Aaron invokes by name. Each profile sets department weights for a specific context.

---

## QUICK DECISION

For fast calls that don't need deep analysis. "Should I use this npm package?" "Is this commit ready?"

| Department | Weight | Who Speaks |
|-----------|--------|-----------|
| Engineering | 1 | Naveen (VP) |
| Marketing | 0 | — |
| Strategy | 1 | Claire (CSO) |
| Legal-Risk | 0 | — |
| Finance | 1 | Raj (CFO) |
| Operations | 2 | Val (CoS) + Drew (PM) |

**Estimated tokens:** ~3,000
**When to use:** Daily decisions, quick sanity checks, mid-sprint direction calls.

---

## BRAND & LAUNCH

For anything public-facing. Logo decisions, website copy, LinkedIn content, pitch decks.

| Department | Weight | Who Speaks |
|-----------|--------|-----------|
| Engineering | 1 | Naveen |
| Marketing | 3 | Full team (Ava, Theo, Maya, Kai) |
| Strategy | 2 | Claire + Ethan |
| Legal-Risk | 2 | Helen + Anil |
| Finance | 1 | Raj |
| Operations | 1 | Val |

**Estimated tokens:** ~15,000
**When to use:** Launching a product. Publishing content. Making brand decisions. Anything Brenda will see.

---

## ARCHITECTURE DECISION

For technical decisions. Tool selection, sovereignty audit, infrastructure changes.

| Department | Weight | Who Speaks |
|-----------|--------|-----------|
| Engineering | 3 | Full team (Naveen, Sam, Jordan, Priya) |
| Marketing | 0 | — |
| Strategy | 2 | Claire + Rosa |
| Legal-Risk | 1 | Helen |
| Finance | 2 | Raj + Fatima |
| Operations | 1 | Val |

**Estimated tokens:** ~12,000
**When to use:** Choosing a new tool. Designing a system. Evaluating sovereignty implications.

---

## FULL BOARDROOM

Maximum engagement. All departments at full swarm. Every perspective surfaced.

| Department | Weight | Who Speaks |
|-----------|--------|-----------|
| Engineering | 3 | Full team |
| Marketing | 3 | Full team |
| Strategy | 3 | Full team |
| Legal-Risk | 3 | Full team |
| Finance | 3 | Full team |
| Operations | 3 | Full team |

**Estimated tokens:** ~30,000
**When to use:** Major strategic decisions. Pivots. Partnership agreements. Pricing model changes. Use sparingly — this is expensive.

---

## SOLO FOUNDER

Minimal engagement. Just Aaron and his EA. For when he wants to think freely without 22 opinions.

| Department | Weight | Who Speaks |
|-----------|--------|-----------|
| Engineering | 0 | — |
| Marketing | 0 | — |
| Strategy | 0 | — |
| Legal-Risk | 0 | — |
| Finance | 0 | — |
| Operations | 1 | Val (CoS) |

**Estimated tokens:** ~500
**When to use:** Creative brainstorming. Personal reflection. Exploring ideas that aren't ready for team scrutiny.

---

## SOVEREIGNTY REVIEW

For evaluating tools, vendors, lock-in risks, and fallback readiness.

| Department | Weight | Who Speaks |
|-----------|--------|-----------|
| Engineering | 3 | Full team |
| Marketing | 0 | — |
| Strategy | 1 | Claire |
| Legal-Risk | 3 | Full team |
| Finance | 2 | Raj + Fatima |
| Operations | 1 | Val |

**Estimated tokens:** ~18,000
**When to use:** Before adopting any new tool or service. Quarterly decapitation drills. Vendor reviews.

---

## Custom Profiles

Aaron can create custom profiles by setting weights directly:

```
Engineering: 2, Marketing: 1, Strategy: 3, Legal: 0, Finance: 2, Ops: 1
```

Name it and save it. The system is just six numbers.
