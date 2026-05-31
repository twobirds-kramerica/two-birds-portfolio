# Two Birds Innovation — Strategic Roadmap
Last updated: 2026-05-31
Owner: Aaron Patzalek
CLI role: reference only — execution tracked in Notion + Command Center

---

## HOW THIS FILE WORKS

This file captures strategic priorities that are too big for a single Notion sprint item
but too important to lose in session state. CLI next-sprint engine reads Notion; this file
feeds Command Center planning sessions. Copy the relevant section into your Command Center
chat when working on financial strategy or product roadmap.

---

## PRIORITY 1 — NHSP Grant Path (DCC Institutional Revenue)

**Why this is P1:** NHSP is the fastest path to recurring institutional revenue for DCC.
Libraries and senior centres have funded mandates and existing relationships with seniors.
A single successful grant cycle could generate $5k–$100k/yr in licence revenue with
minimal product work beyond what is already built.

**Aaron's gate:** DCC must be in real users' hands before applying. No beta testers,
no reviewed product yet. Premature to apply in 2026 — but the path needs to be built now.

### The Nuances

**What NHSP actually requires:**
- Eligible lead applicants: non-profit orgs, community groups, municipalities, provincial
  governments. Two Birds Innovation (for-profit) CANNOT be the lead applicant.
- Two Birds can be a named project partner/supplier — the library or senior centre applies,
  cites DCC as the curriculum platform, and pays the licence from grant money.
- Concept-stage projects ARE eligible — you describe what you plan to build/deliver,
  not what exists today. The project runs 12–24 months after funding is awarded.
- Applications typically open: September–November each year.
  Decisions typically: February–April following year.
  Project execution: starts 2–6 months after decision.

**Timeline implication:**
- Apply: fall 2026 → Decision: spring 2027 → Delivery: summer 2027–2028
- Product in real users' hands needed by: **summer 2027 at the latest**
- That is 12–14 months from now — achievable if DCC beta starts fall 2026

**What "product in users' hands" means for this context:**
- At least 1 partner library or senior centre using DCC with real senior learners
- At least basic usage data (module completions, time on site)
- Aaron able to speak to one real outcome story
- Does NOT require polished v2 wizard, commercial layer, or paid tiers

**The two revenue paths:**

| Path | What Aaron does | Upside | Effort |
|------|-----------------|--------|--------|
| Indirect licensing | Letter of support + licence agreement | $500–$2k/yr per library. If 10 get funded = $5k–$20k/yr recurring | Low — just sign letters |
| Direct grant partner | Co-apply with 1 library as delivery partner | Up to $50k for product development, facilitator training, content | Medium — grant writing + partner relationship |

**Recommended path:** Start with indirect (letters of support). One converted institutional
client becomes a case study. Case study unlocks direct grant applications.

### Research Still Needed (route to Command Center)

1. Which Ontario libraries are already running digital literacy programs for seniors?
   (Start: London Public Library, St. Thomas Public Library, Middlesex County Library)
2. Do any have existing NHSP relationships or staff who write grants?
3. What does a typical NHSP project budget look like — how much goes to curriculum vs. delivery?
4. Is there an NHSP call for proposals open right now for 2026–27?
5. What is the minimum viable DCC beta that satisfies "product in real users' hands"?

### Gate Conditions Before Applying

- [ ] DCC has been used by at least 10 real seniors (not Aaron, not family)
- [ ] At least 1 partner organisation has given feedback on the programme
- [ ] Aaron can describe one concrete learning outcome from a real user
- [ ] Basic usage metrics are captured (module completions, time on page)

---

## PRIORITY 2 — DCC Beta Programme (enables NHSP gate)

Before NHSP can be pursued, DCC needs real users. The beta programme is the gate.

**Minimum viable beta:**
- 10–20 seniors from one community (library, senior centre, church group)
- Facilitated session OR self-directed with check-in
- Simple feedback form (Google Form is fine)
- Aaron reviews 3–5 completed modules with a real learner and observes friction points

**How to get there:**
- Approach one local organisation in St. Thomas or London ON
- Offer to run a free 2-hour "Digital Confidence Centre" session for their seniors group
- Collect module completion data + 5-minute feedback survey
- Use findings to file first real case study

**Timeline target:** Beta running by September 2026

---

## PRIORITY 3 — KevsCasa Commercialisation (settlement agency pilot)

Kevin's personal search is the current use case. July 30 is the deadline.
The commercial path (Newcomer Housing Navigator for settlement agencies) was confirmed
as uncontested in the May 2026 competitive research.

**Gate condition:** Kevin finds his apartment. Site remains polished and functional.

**Next step after Kevin:** Identify 1–2 IRCC-funded settlement agencies in Ontario
(ACCES Employment, Centre for Immigrant and Community Services) for a pilot conversation.
This was filed as a P2 Notion action on 2026-05-29.

---

## PRIORITY 4 — Clarity Revenue Path

Clarity is a lead-generation tool for Aaron's consulting practice today.
The competitive research confirmed it fills an uncontested Canadian gap.

**Current state:** Free tool, no auth, no backend. FORMSPREE_ENDPOINT not yet set.

**Revenue path 1 (consulting leads):** Someone runs a diagnostic, emails Aaron, books a call.
Gate condition: FORMSPREE_ENDPOINT configured so email capture is live. 5-minute Aaron task.

**Revenue path 2 (productised):** Clarity charges per diagnostic. Requires Cloudflare Worker
proxy to remove API key barrier. Medium effort, high unlock — any SME owner can use it
without technical knowledge.

---

## FOR COMMAND CENTER

When routing this to your Command Center / financial-plus conversation, key questions to answer:

1. What is the fastest path to $5k/month recurring — NHSP licensing or consulting pipeline?
2. Does Aaron pursue direct NHSP as delivery partner, or just be the curriculum supplier?
3. Is there a grant writer or community org connection in Aaron's existing network?
4. What is the beta programme design — who are the 10–20 first real DCC users?
5. Can KevsCasa settlement agency pilot be done before or after Kevin's apartment search closes?
