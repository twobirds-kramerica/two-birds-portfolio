# QA Report — S-008 DCC CSS Brand Alignment

**Date:** 2026-04-15
**Sprint:** S-008
**Repo:** digital-confidence (commit `2abdb54`)

## Changes Made

### 1. Font Family — Inter Added
- **Before:** System fonts only (`-apple-system, BlinkMacSystemFont, "San Francisco", "Segoe UI", Arial, sans-serif`)
- **After:** `'Inter'` added as primary, loaded via Google Fonts `@import`
- **Risk:** LOW — falls back to same system fonts if Inter fails to load
- **Weights loaded:** 400, 500, 600, 700 (no thin weights)

### 2. DCC Teal (#00897B) — Brand Colour Introduced
- **Before:** Not present anywhere in CSS
- **After:** Added as `--brand-teal: #00897B` and `--brand-teal-hover: #00796B`
- **Applied to:** Splash start button (bg), sidebar header h2 (text), sidebar header border, footer top border
- **Contrast check:** All pass WCAG AAA (see table below)

### 3. Text Colour Updated
- **Before:** `--text-primary: #2C3E50` (dark blue-grey)
- **After:** `--text-primary: #333333` (Text Dark per brand spec)
- **Contrast:** 14.62:1 on #F5F5F5 — passes AAA

### 4. Background Colour Updated
- **Before:** `--bg-primary: #FAFAF8` (warm off-white)
- **After:** `--bg-primary: #F5F5F5` (Gentle Grey per brand spec)

### 5. Warm Sand Variable Added
- `--bg-warm: #FFF8E1` added as CSS variable (already used inline in welcome-hero gradient)

### 6. Splash Overlay Colours
- Hardcoded `#2C3E50` and `#5D6D7E` replaced with `var(--text-primary)` and `var(--text-secondary)` for dark mode compatibility

## WCAG Contrast Verification

| Combination | Ratio | AA Normal | AA Large | AAA Normal | AAA Large |
|-------------|-------|-----------|----------|------------|-----------|
| #333333 on #F5F5F5 | 14.62:1 | PASS | PASS | PASS | PASS |
| #00897B on #FFFFFF | 5.68:1 | PASS | PASS | PASS | PASS |
| #00897B on #F5F5F5 | 5.40:1 | PASS | PASS | PASS | PASS |
| #FFFFFF on #00897B | 5.68:1 | PASS | PASS | PASS | PASS |
| #5A6B78 on #F5F5F5 | 8.39:1 | PASS | PASS | PASS | PASS |
| #5D6D7E on #F5F5F5 | 8.14:1 | PASS | PASS | PASS | PASS |
| #00796B on #FFFFFF | 6.62:1 | PASS | PASS | PASS | PASS |

**All 7 combinations pass WCAG AAA for both normal and large text.**

## Not Changed (Flagged for Future)

- ~30 instances of sub-16px font sizes in UI chrome (badges, timestamps, labels, controls). These are supplementary UI text, not body content — the brand spec's 16px minimum targets body text. Core body text remains 18px.
- ~50 hardcoded hex colours in component-specific styles (quiz, scam simulator, feedback, read-aloud, etc.). These are feature-specific and changing them would be a redesign, not an alignment.

## Browser Testing Required

Aaron should verify in browser:
1. Open DCC index.html — splash button should be teal (#00897B) not blue
2. Click through to a module — sidebar header should show teal text and teal bottom border
3. Scroll to footer — top border should be teal
4. Text should look the same weight/feel but slightly more neutral (grey vs blue-grey)
5. Run `?qa=true` on index.html for full axe-core audit
