# Dial Spec — Story Dial
**Version:** 1.0 | **Created:** 2026-05-18

---

## The Dial

A single parameter (1–5) that controls how a story is told.
The facts don't change. The lens does.

```
1 ─────────────────────────────────────────── 5
Big Bang                              Intimate Core
Attention-grabbing                    Step-by-step
Broad audience                        Discerning audience
Scroll-stopper                        Truth-seeker
```

---

## Dial Positions

### Dial 1 — Big Bang

**Persona:** The curious observer. Not necessarily in tech. Scrolling LinkedIn or Twitter/X. Has 3 seconds.
**Channel:** Twitter/X thread starter, LinkedIn hook post (hook only — 1-2 sentences), short-form social
**Voice:** Bold, declarative, one striking claim. Leads with the unexpected.
**Length:** 1-3 sentences max for the hook. Thread can expand.
**Example hook:**
> "I gave AI a veto. Now nothing ships without three experts signing off — and they all live in my laptop."

**Rules:** Hook must be defensible. The bold claim must have a receipt.

---

### Dial 2 — LinkedIn Short

**Persona:** LinkedIn reader who scrolls but occasionally stops. PM, consultant, business owner. Curious about AI in practice.
**Channel:** LinkedIn post (standalone, ~200 words)
**Voice:** Hook → context → insight → one takeaway. Conversational.
**Length:** ~200 words. One clear takeaway.
**Format:** First line is the hook. Paragraph breaks. No jargon.

---

### Dial 3 — LinkedIn Long (Default)

**Persona:** LinkedIn article reader or engaged post reader. Wants the full story. Might share.
**Channel:** LinkedIn article, LinkedIn long-form post, newsletter excerpt
**Voice:** Full narrative arc: setup → problem → action → insight → implication
**Length:** ~600 words. 4-6 sections.
**Format:** Hook → raw story → what I learned → what it means for you → CTA

**This is the default dial setting for S-CHRONICLE-WEEKLY.**

---

### Dial 4 — Blog / Newsletter

**Persona:** Subscriber or blog reader. Has opted in. Wants depth and context.
**Channel:** Two Birds newsletter, blog post, LinkedIn article with more room to breathe
**Voice:** More personal, more honest about uncertainty. Can name specific tools, commits, decisions.
**Length:** 800-1200 words.
**Format:** Masthead context → setup → the build → what worked / what didn't → takeaways → next

---

### Dial 5 — Intimate Core

**Persona:** Fellow founder, technical co-founder candidate, discerning builder. Reads critically. Will fact-check.
**Channel:** Substack deep-dive, founder community post, direct outreach companion piece, investor context
**Voice:** Step-by-step. Technical accuracy required. Commits cited. Uncertainty named.
**Length:** No length limit — as long as it takes to be precise.
**Format:** What I was trying to solve → what I built (with receipts) → where it broke → what I'd do differently → what it actually unlocked

---

## Persona × Channel Matrix

| Dial | Audience Persona | Primary Channel | Secondary |
|------|-----------------|----------------|-----------|
| 1 | Curious observer | Twitter/X | LinkedIn hook |
| 2 | LinkedIn scroller | LinkedIn post | Instagram caption |
| 3 | LinkedIn reader | LinkedIn long post / article | Newsletter teaser |
| 4 | Opted-in subscriber | Newsletter / blog | LinkedIn article |
| 5 | Technical founder / investor | Substack / direct | Founder community |

---

## How to Invoke

In a Claude Code session, after a Raw Data Ready Notion page exists:

```
Chronicle this week's entry at dial [1-5].
```

Or override mid-session:
```
Rewrite the LinkedIn Short at dial 1 — I want a sharper hook.
Rewrite the LinkedIn Long at dial 5 — the audience is founders, not scrollers.
```

The Scribe Rules (honesty + receipts) apply at every dial position. The dial changes the lens, not the integrity of the facts.
