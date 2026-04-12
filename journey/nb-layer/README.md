# NB Layer -- Nota Bene Journal

## Purpose

Capture moments where the tools were wrong and Aaron caught it. Raw, honest, not polished. Companion to the main journey archive but focused specifically on critical-user moments, not the full narrative arc.

The NB layer is where the sparring partner rule lives in written form. Every entry is evidence that Aaron's instinct to question confident AI output is valuable and reproducible.

## Why It Matters

The main journey archive tells the story of what Aaron built. The NB layer tells the story of how he caught what the tools would not tell him. These are different stories and they deserve different homes.

The NB layer is also a pitch asset. Every entry is a receipt for Aaron's differentiator: non-developer critical evaluator of AI systems. When Aaron applies to AI evaluation gigs, red-team positions, or full-time roles at AI companies, the NB layer is his proof of pattern.

## Entry Format

Each NB entry uses this template:

---

*NB* YYYY-MM-DD -- [short title]

THE MOMENT: [what Aaron was trying to do]

WHAT THE TOOL DID: [the wrong thing, blind spot, or overconfident claim]

HOW HE CAUGHT IT: [the question behind the question, the pushback, the verification step]

WHAT HE LEARNED: [one line]

WHY IT MATTERS: [one line, optional -- why this moment is a brand or career proof point]

---

## Trigger

In any Claude.ai chat, Aaron can write "*NB* [observation]" and the capture system will generate a Claude Code prompt to append the entry to `journey/nb-layer/pending.md`. The entry gets merged into the main NB layer on the next sprint.

## File Structure

- `README.md` -- this file
- `pending.md` -- queue of captured entries waiting to be merged
- `entries/` -- committed NB entries, one file per entry
- `index.md` -- chronological index of all entries (auto-generated)

## Rules for Entries

- Raw, not polished. The point is honesty, not style.
- Name the tool and the specific failure mode. Vague entries are useless as proof.
- Include the pushback verbatim if possible. The pushback is the differentiator.
- If the lesson applies to more than this one moment, say so in one line.
- No editorialising. The facts are the story.

## Relationship to the Main Journey

The main journey (`journey/narrative/`) is the narrative arc of Aaron's career build. The NB layer (`journey/nb-layer/`) is the pattern library of critical-user moments. They cross-reference each other but live in separate folders so the voices stay distinct.
