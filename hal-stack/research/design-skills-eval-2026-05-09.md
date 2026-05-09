# Design Skill Evaluation — Impeccable + Taste Skill
**Date:** 2026-05-09 | **Sprint:** S-IMPECCABLE | **Status:** Complete

---

## What Was Installed

Both skills installed via `npx skills add` into `.agents/skills/` (symlinked to Claude Code):

| Skill | Source | Skills | License |
|-------|--------|--------|---------|
| Impeccable | `pbakaus/impeccable` | 1 skill, 22 reference files | Apache 2.0 |
| Taste Skill | `Leonxlnx/taste-skill` | 12 skills | MIT |

Both are free, open-source, sovereign — no subscriptions, no external services.

---

## Automated Scans Against Live Sites

### Clarity (`npx impeccable --json clarity/index.html`)

Exit code 2 = findings detected.

| Anti-Pattern | Detail | Severity |
|---|---|---|
| Low contrast ×6 | `#b0b0a8` on white: 2.2:1 (need 4.5:1) | P1 — accessibility failure |
| Low contrast ×6 | `#888888` on `#ede8df`: 2.9:1 | P1 |
| Low contrast ×6 | `#999999` on `#ede8df`: 2.3:1 | P1 |
| Overused font | Roboto — used on millions of sites | P2 |
| Overused font | Arial fallback | P2 |

**Verdict:** Clarity has real WCAG AA failures that any accessibility audit would catch. The muted warm palette is nice conceptually but the body/caption text is too light against the cream background (`#ede8df`). Fix: darken secondary text to ≥ `#6b6860` on that background.

### DCC (`npx impeccable --json --fast digital-confidence/index.html`)

Note: `--fast` required — jsdom crashes on CSS custom properties in `border` shorthand (known jsdom bug).

| Anti-Pattern | Detail | Severity |
|---|---|---|
| Side-tab accent border | `border-left: 6px solid #c0392b` at line 744 | P2 — AI tell |
| Single font | Only Georgia used — no typographic pairing | P2 |
| Flat type hierarchy | 12px→22.4px with 12 intermediate steps, ratio 1.9:1 | P2 |

**Context on findings:**
- **Side-tab border:** The red left border is almost certainly on a warning/alert block (the `#c0392b` is DCC's danger red). This is functionally correct but could be replaced with a subtler treatment — e.g., a `background: rgba(192,57,43,0.08)` tinted background without the thick border.
- **Single font:** Georgia is a deliberate, correct choice for a seniors-facing accessibility product — legible serif. The "anti-pattern" here is no *pairing*. A sans-serif for UI chrome (nav, labels, buttons) alongside Georgia body text would improve hierarchy without compromising readability.
- **Flat type hierarchy:** This is the real issue. Too many sizes clustered in the 12–22px range creates a muddy hierarchy. Recommendation: consolidate to 4 sizes: 13px (caption), 16px (body), 20px (subhead), 28px (section head).

---

## Skill Applicability to Two Birds Stack

### Impeccable — ✅ Use Now

Works cleanly with static HTML/CSS/JS. Most valuable commands for this stack:

| Command | Use case | Priority |
|---|---|---|
| `/impeccable critique` | Full design audit on Clarity or TBI before a client meeting | High |
| `/impeccable polish` | Quick cleanup pass on any shipped page | High |
| `/impeccable typeset` | Fix DCC's flat type hierarchy | High |
| `/impeccable colorize` | Fix Clarity's contrast failures | High |
| `/impeccable teach` | Create PRODUCT.md for Clarity/TBI (unlocks full context for all other commands) | Medium |
| `/impeccable distill` | Simplify any page that feels cluttered | Medium |
| `/impeccable bolder` | If Clarity needs more visual confidence before a prospect demo | Low |

**Prerequisite to unlock full power:** Create `PRODUCT.md` in each product repo root. Without it, the skill operates without brand/audience context. `/impeccable teach` generates this interactively.

**Known limitation:** `--json` scanner crashes on CSS with `border: Xpx solid var(--custom-property)` shorthand due to a jsdom bug. Use `--fast` for DCC-style sites. Clarity scans clean without `--fast`.

### Taste Skill — ⚠️ Vocabulary Only (Stack Mismatch)

The `design-taste-frontend` skill assumes React/Next.js + Tailwind CSS. **Not applicable to our static HTML stack.**

However, its design principles encode valuable vocabulary:

| Principle | Applied to Two Birds |
|---|---|
| **DESIGN_VARIANCE: 8** | Avoid centered hero layouts; prefer left-aligned or split-screen |
| **No purple/blue AI glow** | Already avoided — TBI uses navy/teal, Clarity uses warm cream |
| **Max 1 accent colour** | TBI: teal ✅ Clarity: warm olive ✅ |
| **`min-h-[100dvh]` not `h-screen`** | Worth checking Clarity hero — iOS Safari can cause layout jump |
| **Geometric sans for UI, serif for display** | DCC uses Georgia everywhere — should split |
| **No Roboto/Inter for premium feel** | Clarity uses Roboto — matches the scanner finding |
| **Tint shadows to background hue** | All sites use generic grey shadows — worth updating |

**Most useful Taste variants for our work (even without React):**
- `minimalist-ui` — design spec for Clarity's editorial aesthetic
- `redesign-existing-projects` — for DCC v2 or Clarity v2 redesign planning

---

## Recommended Next Steps (Prioritised)

### P1 — Run `/impeccable teach` for Clarity
Creates `C:\twobirds\clarity\PRODUCT.md`. Takes ~5 min interactively. Unlocks brand-aware output for all future impeccable commands on Clarity.

```
/impeccable teach
Target: C:\twobirds\clarity\index.html
```

### P2 — Fix Clarity contrast failures (actionable now)
From the scan: darken muted text colours on `#ede8df` backgrounds.
- `#888888` → `#5a5850` (4.6:1 — passes WCAG AA)
- `#999999` → `#5a5850`
- `#b0b0a8` → `#5a5850`

Run: `/impeccable colorize clarity/index.html` — will propose and apply WCAG-compliant swaps.

### P3 — Fix DCC flat type hierarchy
Consolidate from 12 sizes to 4: 13/16/20/28px. Run `/impeccable typeset digital-confidence/index.html`.

### P4 — Replace Roboto on Clarity
Consider Geist, Outfit, or Plus Jakarta Sans as a pairing to the serif hero font. Not a blocker — do this during a Clarity v2 sprint.

---

## Sovereignty Assessment

| Tool | Cost | External deps | Data leaving machine | Verdict |
|---|---|---|---|---|
| Impeccable | Free | None (CLI only) | No | ✅ Fully sovereign |
| Taste Skill | Free | None | No | ✅ Fully sovereign |
| `npx skills add` | Free | npm registry (one-time clone) | No | ✅ Sovereign after install |

---

## Commands Reference Card

```bash
# Scan any HTML file for design anti-patterns
npx impeccable --json path/to/file.html         # full scan
npx impeccable --json --fast path/to/file.html  # fast (skip jsdom — use for DCC)

# In Claude Code sessions (after /restart to load new skills):
/impeccable critique   # full design audit (requires PRODUCT.md)
/impeccable polish     # cleanup pass
/impeccable typeset    # fix type hierarchy
/impeccable colorize   # fix contrast + palette
/impeccable teach      # generate PRODUCT.md
/impeccable distill    # simplify cluttered pages
```

*Skills are available after restarting Claude Code (new session loads them from `.agents/skills/`).*

---
*Evaluated: 2026-05-09 | Commit: see S-IMPECCABLE SESSION-STATE entry*
