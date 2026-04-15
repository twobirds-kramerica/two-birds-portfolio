# Changelog

All notable user-facing changes to Two Birds Innovation products are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/). Dates in YYYY-MM-DD.

---

## [Unreleased]

(empty)

---

## [2026-04-15] — Aaron Patzalek Portfolio Site (S-018)

### Added
- Single-page portfolio site at `aaron-patzalek` repo
- 6 sections: hero, about, products, approach, CTA, contact
- Uses shared design tokens from `standards/tokens.css`
- JSON-LD Person schema, CSP, OG tags, full accessibility

---

## [2026-04-15] — DCC Standards Audit + Remediation (S-017)

### Fixed
- Email capture input on index.html now has linked `<label>` for screen readers
- Placeholder Google Search Console verification tag commented out (was `REPLACE_WITH_REAL_CODE`)
- 20 geo-content pages now have `og:image` for social sharing previews
- Content Security Policy meta tag added to index.html and about.html

---

## [2026-04-15] — Engineering Standards Foundation (S-016)

### Added
- Engineering standards document (`standards/ENGINEERING-STANDARDS.md`)
- Design system CSS tokens (`standards/tokens.css`)
- Shared component library: nav, hero, card, button, footer, form-input, section-wrapper
- Change management process (`standards/CHANGE-MANAGEMENT.md`)
- This changelog

---

## [2026-04-15] — Engineering Standards Foundation (S-016)

### Added
- **Engineering Standards** — code style, WCAG AA accessibility, performance targets, SEO/AEO requirements, security baseline, git workflow, testing requirements, sovereignty dependency rules
- **Design System Tokens** — CSS custom properties for colours (TBI + DCC brands), typography (Inter), spacing scale, layout constraints, shadows, transitions, dark mode overrides, reduced motion support
- **Component Library** — 7 reusable HTML partials: nav, hero, card (3 variants), button (4 variants + 3 sizes), footer, form-input (with error state), section-wrapper (4 background variants)
- **Change Management** — process for tracking and communicating changes across repos
- **Sprint Template** — updated with mandatory standards compliance checklist

---

## [2026-04-15] — DCC CSS Brand Alignment (S-008)

### Changed
- DCC `main.css` — Inter font added, DCC Teal (#00897B) as primary brand colour on splash CTA/sidebar/footer, text colour aligned to #333333, background to #F5F5F5

---

## [2026-04-15] — Founding Board Persona System

### Added
- Inner Circle: The Hand (synthesizer) + Love Balance Advisor (capacity check)
- Scrappy Pack advisory layer: 5 founder-archetype personas (Mack, Tess, Grit, Patch, Sage)
- Master index (31 personas total) + usage guide

---

## [2026-04-15] — CIPO Trademark Research (S-007)

### Added
- CIPO trademark research document — registration process, 2026 fees, timeline, risk assessment
- Recommendation: defer registration until name finalised + revenue validated

---

## [2026-04-14] — Aider L2 Evaluation (S-005)

### Added
- Aider evaluation as Claude Code L2 fallback — install blocked (no Python), research completed, viable fallback documented

---

## [2026-04-12] — HAL Infrastructure Sprint

### Added
- Voice layer keyword command map (S-001): 13 commands, fuzzy matcher
- Content freshness system (S-003): staleness rules, check script, 252 DCC files scanned
- Context export rule added to CLAUDE.md (S-004)
