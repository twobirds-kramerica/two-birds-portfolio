# Digital Confidence Centre — Logo

**Version:** v1.0-final (V07 heart-bulb selected)
**Date created:** April 11, 2026
**Selected by:** Aaron Patzalek

---

## Official Logo: V07 — Heart + Light Bulb

A light bulb with a heart inside, on a warm teal (#00897B) background. The bulb represents understanding ("the aha moment"). The heart represents care ("we're kind about it"). Together they say "Digital Confidence Centre" without a word.

## Brand Context

The Digital Confidence Centre (DCC) is a free digital literacy programme for Canadian seniors, built by Two Birds Innovation (placeholder name). It helps people who feel overwhelmed by technology learn at their own pace, with no registration required.

**Mission:** "You are not behind. You are right on time."

## Relationship to Parent Brand

DCC is a **child brand** of Two Birds Innovation. Distinct identity:

| | Two Birds Innovation | Digital Confidence Centre |
|---|---------------------|-------------------------|
| **Logo** | Chevrons (>) (<) | Heart-bulb |
| **Colour** | Blue (#0066CC) | Warm Teal (#00897B) |
| **Tone** | Direct, challenging | Warm, patient |
| **Audience** | B2B partners | End users, seniors |

## File Inventory

### Primary Logo (teal background)

| File | Dimensions | Use Case |
|------|-----------|----------|
| `dcc-logo.svg` | Scalable | Master vector |
| `dcc-1024.png` | 1024×1024 | Social media profiles |
| `dcc-512.png` | 512×512 | General web use |
| `dcc-256.png` | 256×256 | High-res favicon |
| `dcc-128.png` | 128×128 | Standard favicon |
| `dcc-64.png` | 64×64 | Small favicon |
| `dcc-favicon.ico` | 16/32/48/64 | Browser favicon (multi-size ICO) |
| `dcc-og.png` | 1200×630 | Open Graph / social sharing |

### Transparent & Monochrome Variants

| File | Use Case |
|------|----------|
| `dcc-white-on-transparent.svg` | Dark backgrounds |
| `dcc-dark-on-transparent.svg` | Light backgrounds, print on white |
| `dcc-monochrome-black.svg` | Single-colour print |
| `dcc-monochrome-white.svg` | Watermarks, reversed-out print |

## Colour Specification

| Swatch | Name | HEX | RGB | CMYK (approx) |
|--------|------|-----|-----|---------------|
| ■ | DCC Teal | #00897B | 0, 137, 123 | 80, 10, 45, 10 |
| □ | White | #FFFFFF | 255, 255, 255 | 0, 0, 0, 0 |
| ■ | Dark Teal | #004D40 | 0, 77, 64 | 90, 30, 60, 40 |

## Favicon Replacement for DCC Site

To replace the current favicon (which incorrectly uses the Two Birds parent logo):

1. Copy `dcc-favicon.ico` to `digital-confidence/` repo root
2. Copy `dcc-256.png` to `digital-confidence/assets/`
3. In every HTML file, update: `<link rel="icon" type="image/x-icon" href="dcc-favicon.ico">`
4. Commit and push

Sprint S-002 in `hal-stack/sprint-system/sprint-queue.md` automates this.
