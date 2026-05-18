# Story Dial — True Story: My AI Journey

**Project:** `hal-stack/story-dial/`
**Created:** 2026-05-18
**Owner:** Aaron Patzalek / Two Birds Innovation

---

## What This Is

Story Dial turns raw AI build activity into publishable content — honest, defensible, and tuned to the audience you're writing for.

**Input:** Raw data from git commits, SESSION-STATE.md, Notion build log — what actually happened, with receipts.

**Dial:** A setting (1–5) that adjusts how the story is told, mapped to personas and distribution channels.

**Output:** Formatted content ready to post — LinkedIn Short, LinkedIn Long, Blog outline, or intimate step-by-step — depending on dial position.

The stories are always grounded in what actually shipped. The dial changes the lens, not the facts.

---

## Why It Exists

Two Birds is building in public. The Agency Log is the record of that building. Story Dial makes the record publishable without inflating it.

"Based on a true story" is the standard. Every claim needs a receipt. The $479K lesson (#003) is the founding rule: optimistic projections framed as projections, not outcomes.

---

## Project Files

| File | Purpose |
|------|---------|
| `scribe-rules.md` | Two hard rules governing all story output |
| `dial-spec.md` | Dial positions 1–5: persona definitions + channel mapping |
| `raw-data-sources.md` | What feeds the raw layer (git, SESSION-STATE, Notion) |
| `chronicle-weekly.py` | Autonomous Thursday script — raw data collection → Notion stub |

---

## How to Use

### Run the weekly chronicle (autonomous)
The overnight bat runs this Thursday at 2am:
```
python hal-stack/story-dial/chronicle-weekly.py
```
Creates a Notion Agency Log page with raw data populated. Status: `Raw Data Ready`.

### Produce formatted output (Claude Code session)
When a `Raw Data Ready` page exists:
```
Chronicle this week's entry at dial 3.
```
Claude Code reads the raw data, applies scribe rules, writes the full entry at the specified dial position.

### Change the dial
```
Chronicle at dial 1.    → Big bang / attention headline
Chronicle at dial 3.    → Standard LinkedIn (default)
Chronicle at dial 5.    → Technical / intimate step-by-step
```

---

## The Agency Log

Entries live in Notion under Command Center / Agency Log.

| # | Title | Date | Dial Used |
|---|-------|------|----------|
| #003 | The $479K Question | April 21, 2026 | 3 (corrected) |
| #004 | The 2 AM Discovery | May 8, 2026 | 3 |
| #005 | The Three Reviewers | May 16, 2026 | 3 |
| #006 | (next entry — May 22, 2026) | — | — |

---

## Naming

Candidate publish name: **"True Story: My AI Journey"** or **"True Story: AI Builder."**
The "true story" framing is the north star — receipts for every claim.
