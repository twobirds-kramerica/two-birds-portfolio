# Open Design — Evaluation
**Date:** 2026-05-09 | **Sprint:** S-OPEN-DESIGN-001 | **Source:** nexu-io/open-design (Apache-2.0)

---

## What Was Installed

`npx skills add nexu-io/open-design` installed **70+ skills** into `.agents/skills/` — far larger than expected. Three distinct families:

| Family | Count | Examples |
|---|---|---|
| **Open Design surfaces** | ~25 | `kami-landing`, `dashboard`, `blog-post`, `email-marketing`, `docs-page`, `digital-eguide`, `design-brief`, `critique` |
| **HTML slide deck variants** (zhangzara series) | ~35 | `html-ppt-zhangzara-cobalt-grid`, `-editorial-tri-tone`, `-monochrome`, `-signal`, etc. |
| **Specialty outputs** | ~10 | `invoice`, `finance-report`, `ib-pitch-book`, `audio-jingle`, `gamified-app` |

Previously installed skills (Impeccable, Taste Skill) are unaffected — they coexist.

---

## How It Actually Works

Open Design is a **code-generation framework**, not a design critique tool. Workflow:

```
1. Author inputs.json   — structured brief: brand, content, imagery
2. npx tsx scripts/compose.ts inputs.json out/index.html
3. Open out/index.html in browser — self-contained, no runtime deps
```

The output is static HTML with CSS inlined. This IS compatible with the Two Birds stack.

**What it is NOT:**
- It does not edit existing pages (you'd generate a parallel version)
- It does not critique or audit existing design (that's Impeccable)
- It is not a visual drag-and-drop tool

---

## Sovereignty Assessment

| Component | Sovereign? | Notes |
|---|---|---|
| Compose step (`npx tsx`) | ✅ Yes | Local TypeScript runner, no network calls |
| Output HTML | ✅ Yes | Fully self-contained, no CDN deps |
| Image generation | ❌ No | Requires `FAL_KEY` (fal.ai API) |
| Image placeholders | ✅ Yes | `scripts/placeholder.ts` generates SVG placeholders without FAL_KEY |
| Skills themselves | ✅ Yes | Apache-2.0, local files, no phone-home |

**Verdict:** Sovereign for all text/layout work. Image generation is the one external dependency, and it's optional — placeholder SVGs work fine for prototyping.

---

## Skills Most Relevant to Two Birds

| Skill | Use case | When to use |
|---|---|---|
| `kami-landing` | Saas-style landing page — could be used for Clarity v2 or TBI redesign | Next major redesign sprint |
| `blog-post` | Styled blog post output | When TBI adds a blog/content marketing section |
| `email-marketing` | Branded HTML email template | Client outreach, newsletter |
| `digital-eguide` | Guide/resource document | DCC module redesign or downloadable resources |
| `design-brief` | Structured design brief generator | Before any redesign sprint — replaces ad-hoc scoping |
| `dashboard` | Data dashboard HTML | Career Coach or Quality Dashboard rebuild |
| `docs-page` | Documentation page | Internal HAL Stack docs that need polish |
| `open-design-landing-deck` | Pitch deck (magazine-style swipe HTML) | Client presentations, prospect demos |
| `critique` | Design review | Overlaps with Impeccable — Impeccable is more thorough |

---

## Gap vs. Current Approach

**Current approach:** Hand-write HTML/CSS per page. Aaron edits directly. Claude Code assists inline.

**Open Design approach:** Write `inputs.json` brief → generate styled HTML → adopt or adapt output.

| Factor | Current | Open Design |
|---|---|---|
| Speed for iteration | Fast (direct edit) | Slow (brief → compose → review → port) |
| Speed for net-new pages | Medium (start from scratch) | Fast (brief → compose → done) |
| Design quality | Depends on sprint | Consistently polished (design systems baked in) |
| Brand consistency | Manual | Enforced by the design system tokens |
| Fit for existing pages | Native | Mismatch (generates parallel, not edits in-place) |
| Learning curve | None (you know the codebase) | Medium (inputs.json schema per surface) |

**The workflow only pays off for net-new pages.** For existing pages (Clarity, TBI, DCC), it would generate a draft you'd then diff against the original — more work than direct editing.

---

## Specific Test: What Would kami-landing Generate for Clarity?

I read the `open-design-landing-deck` skill's visual system ("Atelier Zero"): warm paper background, Inter Tight + Playfair Display, italic-serif emphasis spans, coral terminating dots.

**This aesthetic does not match Clarity's brand:** Clarity uses olive green, cream, Roboto/Georgia, no coral. Using Open Design for Clarity would mean either (a) adopting Atelier Zero and replacing the current brand, or (b) customising the design system tokens — which is non-trivial.

**It COULD work for a Clarity v2 redesign** where we intentionally want a premium editorial feel. The Atelier Zero aesthetic is actually high quality and fits a "premium SMB AI advisory" positioning.

---

## Decision

**Partial adoption: hold for net-new work.**

| Scenario | Decision | Timing |
|---|---|---|
| Existing pages (Clarity, TBI, DCC) | ❌ Don't use — wrong workflow for in-place edits | Never |
| Clarity v2 redesign (full rebuild) | ✅ Use `kami-landing` as the starting point | When Clarity v2 is scoped |
| Client presentations / pitch decks | ✅ Use `open-design-landing-deck` or `html-ppt-pitch-deck` | Next client prospect meeting |
| TBI blog / content marketing | ✅ Use `blog-post` skill | When content strategy begins |
| Client outreach emails | ✅ Use `email-marketing` | When email outreach begins |
| Design critique of existing pages | ❌ Use Impeccable instead — better tool for this job | Already doing this |

---

## Immediate Action (Optional, ~15 min)

Generate a pitch deck for a prospect meeting using `html-ppt-pitch-deck` or `open-design-landing-deck`. This is the lowest-friction use case — no brand conflict, and a polished HTML deck is genuinely useful for selling Clarity or the AI Workflow Audit.

To do it:
```bash
# In a new CC session (skills load on restart):
/open-design-landing-deck
# Brief: Two Birds Innovation · AI Workflow Audit · 8-slide deck
```

---
*Evaluated: 2026-05-09 | 70+ skills installed, available after session restart*
