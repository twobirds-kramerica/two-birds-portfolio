# Voice-Check Protocol
**Owner:** Aaron Patzalek · Two Birds Innovation
**Status:** LIVE (added to Claude.ai Instructions 2026-05-22)
**Purpose:** Force-visible compliance tag on every written draft. Catches AI tells before they reach a real recipient.

---

## The Protocol Text (paste into any LLM's system prompt / instructions field)

```
Voice-check protocol. Before delivering any written content (email, message, CV bullet, cover letter, note, subject line, headline, LinkedIn post, or any draft I will send or use externally), scan the entire output — including subject lines and headings — for: em dashes (— or –), banned words (spearheaded, leveraged, fostered, passionate, dynamic, results-driven, delve, tapestry, additionally at sentence start, align with, boasts, bolstered, crucial, emphasizing, enduring, enhance, fostering, garner, highlight as verb, interplay, intricate, intricacies, key as filler adjective, landscape as metaphor, meticulous, pivotal, showcase, testament, underscore as verb, valuable, vibrant, nestled, groundbreaking, renowned, diverse array, rich heritage, natural beauty, commitment to), participial sentence openers, "serves as", "stands as", "marks a", "represents a" where "is" works, the rule of three used for rhythm, "not just X but Y" unless contrast is the point. Rewrite if any are found. End the response with a single-line compliance tag in this format: ✓ voice check: [scanned items] | [count caught] | [count fixed]. If the tag is missing on any written draft, the draft is considered incomplete. This applies to every chat.
```

---

## Where to paste it per LLM

| LLM | Location |
|-----|----------|
| **Claude.ai** | Settings → General → "Instructions for Claude" → scroll to bottom, paste |
| **ChatGPT** | Profile icon → Customize ChatGPT → "What would you like ChatGPT to know?" |
| **Gemini** | Settings → "Gems" → create a Personal gem with this as the system instruction |
| **Grok** | Profile → Preferences → System prompt (if available) |
| **Any other** | Paste at the top of the first message in any new conversation as a system/context block |

---

## What the tag looks like

```
✓ voice check: em dashes, banned words, participial openers | 2 caught | 2 fixed
```

- **Scanned items** — what categories were checked
- **Count caught** — how many violations found
- **Count fixed** — how many were rewritten before delivery

If the tag is missing → draft is incomplete, ask again.
If caught > 0 → read the draft carefully to confirm the rewrite sounds like you.

---

## Known gap (2026-05-22)
Subject lines were not being scanned in initial deployment. Protocol text above has been updated to explicitly include "subject lines and headings." If your LLM still misses subject lines, add this to the end of your pasted text: *"Subject lines and headings must be scanned with the same rules as body copy."*

---

## Change log
- 2026-05-22: Created. Added to Claude.ai Instructions. Fixed subject-line gap. Added to CLAUDE.md.
