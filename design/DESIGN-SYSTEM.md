# Design System — Two Birds Innovation

**Date:** April 5, 2026
**Applies to:** All Two Birds products
**Principle:** Professional enough for a CA$2,500 audit firm. Warm enough for a 74-year-old.

---

## Section 1 — Typography System

### Font Stack (Float-Free — No External Dependencies)
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, sans-serif;
```

### Scale

| Element | Desktop | Mobile (≤768px) | Line Height |
|---------|---------|----------------|-------------|
| h1 | 2.5rem (40px) | 1.75rem (28px) | 1.2 |
| h2 | 2rem (32px) | 1.5rem (24px) | 1.2 |
| h3 | 1.5rem (24px) | 1.25rem (20px) | 1.3 |
| Body | 1rem (16px) | 1rem (16px) | 1.6 |
| Small/caption | 0.875rem (14px) | 0.875rem (14px) | 1.4 |

**Rules:**
- Body text never below 16px on any device
- Max line length: 70 characters (`max-width: 38em`)
- Paragraph spacing: 1.5em between paragraphs

---

## Section 2 — Colour System

### Two Birds Innovation Brand

| Token | Hex | Usage | WCAG on White |
|-------|-----|-------|--------------|
| `--primary` | #1B3A4B | Headings, nav, authority | 10.2:1 AAA ✅ |
| `--secondary` | #2EC4B6 | Links, accents, innovation | 3.0:1 (large text only) |
| `--accent` | #FF9F1C | CTAs, warmth, energy | 2.5:1 (backgrounds only) |
| `--neutral` | #F8F9FA | Page background | N/A |
| `--text` | #1A1A2E | Body text | 16.1:1 AAA ✅ |
| `--text-muted` | #4A5568 | Secondary text | 7.0:1 AAA ✅ |
| `--success` | #2D6A4F | Positive states | 6.5:1 AA ✅ |
| `--warning` | #F4A261 | Caution states | 2.7:1 (with dark text) |
| `--error` | #E63946 | Error states | 4.6:1 AA ✅ |

### DCC Palette (Warmer)

| Token | Hex | Usage |
|-------|-----|-------|
| `--dcc-primary` | #2B4590 | Trust, stability |
| `--dcc-warm` | #F4A261 | Approachability |
| `--dcc-bg` | #FAFAF8 | Warm white (less clinical) |
| `--dcc-text` | #2D3748 | Soft black (easier on older eyes) |

---

## Section 3 — Component Library

### Hero Section
```html
<section class="hero">
  <div class="container">
    <h1>[Clear headline — what this product does]</h1>
    <p class="hero-sub">[One sentence value proposition]</p>
    <a href="#cta" class="btn btn-primary btn-lg">[Action verb] — It's Free</a>
  </div>
</section>
```
**Rules:** CTA above fold on all devices. Headline ≤10 words. No jargon.

### Trust Badge Row
```html
<div class="trust-badges">
  <span class="badge">WCAG AA Accessible</span>
  <span class="badge">Bilingual EN/FR</span>
  <span class="badge">Free for Patrons</span>
  <span class="badge">Made in Ontario</span>
</div>
```

### CTA Button Sizes
| Size | Class | Height | Font | Use |
|------|-------|--------|------|-----|
| Large | `.btn-lg` | 56px | 1.1rem | Primary page CTA |
| Default | `.btn` | 44px | 1rem | In-content actions |
| Small | `.btn-sm` | 36px | 0.875rem | Secondary actions |

**All buttons:** min-width 44px, min-height 44px, border-radius 8px.

### Pricing Card
```html
<div class="price-card [featured]">
  <h3>[Tier Name]</h3>
  <div class="price">$X,000</div>
  <div class="period">per year</div>
  <p class="desc">[What's included]</p>
  <a href="#" class="btn btn-primary">Get Started</a>
</div>
```

---

## Section 4 — Psychology and Persuasion

### Trust Signals (DCC)
- Social proof: "Used by seniors across Ontario" (when true)
- Authority: WCAG AA badge, bilingual flag, "Built by a 20-year PM"
- Free with no catch: state it prominently, explain why (community mission)
- Familiar personas: Brenda, Harold, Margaret, Frank, Dorothy — relatable

### Conversion Principles (Clarity, Two Birds)
- Loss aversion: "Businesses that don't adapt lose ground to competitors who do"
- Specificity: "CA$2,500 flat fee. 30 days. One clear deliverable."
- Honest scarcity: "I take 2 audit clients per month"
- Proof over promises: "7 live products in 90 days" with live links

### Anxiety Reduction (DCC, Career Coach)
- Progress indicators: "Module 3 of 29 — keep going"
- Reassurance loops: Confidence Check every 500 words
- Low stakes: "Nothing you click here can break anything"
- Exit always available: "You can stop and come back anytime"
- Data ownership: "Your data stays in your browser. Always."
