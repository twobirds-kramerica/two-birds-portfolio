<!--
STATUS: v1.1 — LIVING DOCUMENT — NEEDS AARON REVIEW
Created: 2026-04-11 16:05 EST (Toronto)
Updated: 2026-04-19 — Warm Hearth design system adopted (Option A, 65.5% vote). Fonts selected. Style guide shipped.
Confidence: HIGH for tone, values, and visual direction.
Known gaps: Typography not field-tested with senior audience yet (pending DCC makeover sprint).
Tag: LIVING DOCUMENT — updated as brand evolves.
-->

# Digital Confidence Centre — Brand Guidelines

## Design System — Warm Hearth (adopted 2026-04-19)

**Direction (65.5% org vote, Option A):** kitchen-table warmth, trusted neighbour tone, zero intimidation.

**Palette.** Warm cream background `#FFF8F0`. Warm teal primary `#2A7B6F`. Burnt orange accent `#E8842C` for CTAs and active states. Warm charcoal text `#3D3229`. Warm-toned shadows (teal rgba, never pure black).

**Typography.** Body serif Merriweather (SIL OFL, 72 languages, full French + Spanish). Heading sans-serif Source Sans 3 (SIL OFL, 76 languages, full French + Spanish). Both **self-hosted** in the DCC repo at `fonts/merriweather/` and `fonts/source-sans-3/` — no Google CDN (sovereignty requirement). Full licence at `fonts/LICENSE-OFL.txt`.

**Senior-friendly baseline:** 18px body minimum (16/20/24 via the A-/A/A+ toggle). 56px default tap target (44px floor). 3px accent focus ring with 2px offset. `prefers-reduced-motion` and `prefers-contrast: more` honoured at the token level — no per-component guards needed.

**Canonical references (in the digital-confidence repo):**

- `css/tokens.css` — all design tokens as CSS custom properties
- `css/tokens-dark.css`, `css/tokens-high-contrast.css`, `css/tokens-alt.css` — theme variants + white-label template
- `css/fonts.css` — @font-face declarations with font-display: swap
- `css/components.css` — component styles ("bones")
- `styleguide/index.html` — **living style guide, browsable**
- `styleguide/motion.html` — interaction / animation spec
- `styleguide/COMPETITIVE-AUDIT.md` — benchmark vs. GCF / Be Internet Awesome / Get Safe Online / Age UK / AARP
- `styleguide/MAINTENANCE.md` — governance, partner white-label procedure, accessibility checklist



## Brand Story

### What DCC Is
The Digital Confidence Centre is a free, self-paced digital literacy programme that helps people get comfortable with technology. No registration, no cost, no pressure. Currently focused on Canadian seniors, but welcoming to anyone who feels overwhelmed by the digital world.

### Why It Exists
Technology moves fast. Not everyone got on the train at the same time. DCC exists because being behind isn't a character flaw — it's a circumstance. And circumstances can change with the right support.

### Who It Serves
- Seniors 65+ in Ontario (primary audience)
- Adult children helping their parents navigate technology
- Community organisations supporting seniors (libraries, credit unions, health centres)
- Anyone, anywhere, who needs a patient, judgment-free place to learn

### The Core Promise
**"You are not behind. You are right on time."**

### Relationship to Two Birds Innovation
DCC is a product of Two Birds Innovation, but it has its own identity. Think of it like Dove and Unilever — the child brand has its own personality that's very different from the parent.

| | Two Birds Innovation | Digital Confidence Centre |
|---|---------------------|-------------------------|
| **Audience** | B2B partners, institutions | End users, seniors, families |
| **Tone** | Direct, challenging | Warm, patient, encouraging |
| **Colour** | Blue (#0066CC) | Warm Teal (#00897B) |
| **Energy** | "Let's disrupt" | "Let's learn together" |
| **Logo** | Chevrons (code brackets) | TBD (heart-bulb recommended) |

---

## Visual Identity

### Primary Colours

| Swatch | Name | HEX | RGB | CMYK (approx) | Use |
|--------|------|-----|-----|---------------|-----|
| ■ | DCC Teal | #00897B | 0, 137, 123 | 80, 10, 45, 10 | Primary brand colour, backgrounds |
| □ | White | #FFFFFF | 255, 255, 255 | 0, 0, 0, 0 | Text on teal, logo elements |
| ■ | DCC Blue | #1565C0 | 21, 101, 192 | 89, 47, 0, 25 | Links, interactive elements (from current site) |

### Secondary Colours

| Swatch | Name | HEX | RGB | CMYK (approx) | Use |
|--------|------|-----|-----|---------------|-----|
| ■ | Warm Sand | #FFF8E1 | 255, 248, 225 | 0, 2, 12, 0 | Background for content cards, gentle warmth |
| ■ | Success Green | #27AE60 | 39, 174, 96 | 78, 0, 76, 10 | Completion, progress, positive feedback |
| ■ | Gentle Grey | #F5F5F5 | 245, 245, 245 | 0, 0, 0, 4 | Page backgrounds |
| ■ | Text Dark | #333333 | 51, 51, 51 | 0, 0, 0, 80 | Body text |

### Typography

| Use | Recommended | Fallback | Min Size |
|-----|------------|----------|----------|
| **Headings** | Inter (Google Fonts) | -apple-system, sans-serif | 24px |
| **Body text** | Inter | -apple-system, sans-serif | 18px (senior-friendly) |
| **Buttons/CTAs** | Inter SemiBold | sans-serif | 16px |

**Senior-friendly rules:**
- Minimum body text size: 18px (16px absolute minimum)
- Line height: 1.6 or greater
- Maximum line length: 70 characters
- No thin font weights (below 400)

### Logo Usage

**Pending:** Aaron selects from 8 variations in `assets/logos/dcc/variations/`.

**Designer recommendation:**
- V07 (heart-bulb) as the brand mark
- V01 (shield+checkmark) as the favicon

**Logo rules (apply once selected):**
- Minimum clear space: 25% of logo width on all sides
- Minimum digital size: 32px
- Minimum print size: 15mm (slightly larger than Two Birds due to detail)
- Always on teal or white background — never on busy images

---

## Tone of Voice

### How DCC Sounds

- **Patient.** Never rush. Never assume. Explain at the pace of the learner.
- **Warm.** Like a knowledgeable friend, not a teacher. "Kitchen table with a cup of tea."
- **Encouraging.** Celebrate small wins. "You just sent your first email — that's wonderful!"
- **Jargon-free.** "Turn off your phone" not "power cycle your device."
- **Honest.** Don't pretend technology is easy. Acknowledge it's confusing. Then show it's learnable.
- **Canadian.** Canadian English. Canadian references. Ontario context.

### How DCC Does NOT Sound

- Never condescending. "It's so simple!" makes people feel stupid.
- Never urgent. There are no deadlines. No "act now."
- Never technical. If you need a glossary, rewrite the content.
- Never corporate. This isn't a product launch. It's a helping hand.
- Never assuming. "As you probably know..." — they might not. That's why they're here.

### Sample DCC Voice

**Good:** "If your phone is frozen and nothing works, here's what to do. Don't worry — this happens to everyone."

**Bad:** "To resolve an unresponsive device, perform a force restart by pressing and holding the power button and volume down button simultaneously for 10 seconds."

---

## Accessibility Requirements

DCC serves seniors. Accessibility is not optional.

| Requirement | Minimum | Target |
|------------|---------|--------|
| WCAG level | AA | AAA where practical |
| Colour contrast | 4.5:1 for text | 7:1 for body text |
| Font size | 16px minimum | 18px default |
| Tap targets | 44×44px minimum | 48×48px preferred |
| Motion | Reduced motion support | prefers-reduced-motion respected |
| Screen readers | All content accessible | ARIA labels on interactive elements |

---

## Print Considerations

DCC materials may be printed by:
- Seniors printing pages at home (often on older printers)
- Libraries printing handouts for classes
- Community centres making bulletin board flyers

**Guidelines:**
- Use solid colours, not gradients or transparency
- Minimum font size for print: 14pt
- High contrast (dark text on light background)
- Include the URL in large text on every printed page
- QR codes: include but don't depend on — some seniors don't know how to use them

---

## Favicon Replacement Instructions

DCC logo V07 (heart-bulb) has been selected and finalized. All formats are in `assets/logos/dcc/`.

To replace the current favicon:
1. Copy `dcc-favicon.ico` to `digital-confidence/` repo root
2. Copy `dcc-256.png` to `digital-confidence/assets/`
3. Update `<link rel="icon">` tags in all HTML files
4. Commit and push

Sprint S-002 in `hal-stack/sprint-system/sprint-queue.md` automates this.

---

## Trademark & Copyright

### Trademark

**Digital Confidence Centre™**

The ™ symbol can be used immediately without formal registration. It signals intent to claim trademark rights in Canada.

**Display guidance:**
- Use ™ on first mention in formal documents, pitch decks, partnership proposals
- Not required on the website or in casual communications
- One ™ per document is sufficient — first mention only

**Formal registration (CIPO):**
Canadian trademark registration through CIPO provides stronger legal protection. This is a future backlog item (S5.8). Estimated cost: CA$330–$800.

### Copyright

**© 2026 Two Birds Innovation**

Display on:
- Website footer (already present)
- Printed materials
- Partnership documents

**Note:** Parent company name may change from "Two Birds Innovation" (placeholder). Copyright notice updates when final name is selected. See `brand-name-research.md`.

### Usage Restrictions

- The DCC logo may be used by Two Birds Innovation and authorised partners (libraries, credit unions, community centres)
- Partners may display the DCC logo in contexts where they offer the programme
- No modification of the logo without approval
- Attribution: "Digital Confidence Centre is a programme of Two Birds Innovation"

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | Apr 11, 2026 | Initial DCC brand guidelines. 8 logo variations created. |
| v1.1 | Apr 11, 2026 | V07 (heart-bulb) selected. Trademark/copyright added. Favicon instructions updated. |
