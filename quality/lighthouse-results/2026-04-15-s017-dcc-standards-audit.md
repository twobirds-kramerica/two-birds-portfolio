# S-017 DCC Standards Audit Results

**Date:** 2026-04-15
**Audited against:** `standards/ENGINEERING-STANDARDS.md` v1.0
**Repo:** digital-confidence
**Files sampled:** 5 HTML pages + full CSS scan + repo-wide grep checks

---

## Audit Scores

| Category | Score | Status |
|----------|-------|--------|
| HTML semantics | 70/100 | FAIR — noscript h1 (cosmetic), email label fixed |
| CSS tokens | 44/100 | POOR — 914 hardcoded hex, but core vars exist |
| Accessibility | 85/100 | GOOD — focus, skip links, tap targets, contrast all present |
| Performance | 80/100 | GOOD — no heavy JS, font-swap, static HTML |
| SEO/AEO | 55→75/100 | IMPROVED — og:image added to 20 geo-content pages |
| Security | 15→25/100 | IMPROVED — CSP added to index + about |
| Dependencies | 90/100 | GOOD — no npm, system font fallbacks |

---

## Remediated This Sprint

| Fix | Files | Impact |
|-----|-------|--------|
| Email input label (a11y) | index.html | Linked `<label>` added, screen reader compliance |
| Placeholder GSC meta | index.html | Commented out fake verification code |
| og:image missing | 20 geo-content pages | Social sharing now shows preview image |
| CSP meta tag | index.html, about.html | Content Security Policy for XSS protection |

---

## Not Remediated (Documented for Future Sprints)

### HIGH priority — next sprint candidates

| Issue | Scope | Effort | Sprint |
|-------|-------|--------|--------|
| CSP meta on remaining ~240 pages | All HTML | Medium (batch script) | Future |
| SRI attributes on GA4/Clarity scripts | All pages with analytics | Medium | Future |
| CSS token migration (914→0 hardcoded hex) | main.css (6500 lines) | Large (incremental) | Future |
| 103 non-a11y !important declarations | main.css | Large (specificity refactor) | Future |
| JSON-LD structured data on about.html | 1 file | Low | Future |

### MEDIUM priority

| Issue | Scope | Notes |
|-------|-------|-------|
| Duplicate OG tags in tips pages | ~21 files | Second set overrides first |
| Noscript double h1 | 28 files | Cosmetic — screen readers ignore noscript when JS enabled |
| Token naming mismatch (--brand-teal vs --dcc-teal) | main.css | Functionally equivalent, naming convention only |
| og:image on tips/answers pages | ~50 files | Not checked this sprint |

### LOW priority

| Issue | Notes |
|-------|-------|
| About.html missing JSON-LD | Has good OG tags, schema optional |
| Some sub-16px font sizes in UI chrome | Badges, timestamps — not body text |

---

## CSS Token Adoption Detail

| Metric | Value |
|--------|-------|
| Total hex occurrences in main.css | 952 |
| In :root definitions (legitimate) | 37 |
| Hardcoded in declarations | 914 |
| var() calls | 717 |
| **Token adoption rate** | **44%** |
| Top offender: #1565C0 hardcoded | 81 instances |
| Top offender: #FFFFFF hardcoded | 88 instances |

**Note:** Many "hardcoded" colours are component-specific values (quiz, scam simulator, read-aloud, etc.) that don't have token equivalents. A realistic target is ~70% adoption, not 100%.

---

## Recommendation

The DCC site is functional and accessible. The biggest gaps are security (CSP/SRI coverage) and CSS token debt. Recommended approach:

1. **Batch CSP script** — write a script to inject CSP meta into all HTML files (30 min sprint)
2. **CSS token migration** — tackle incrementally by component section, not all at once
3. **SRI** — GA4 and Clarity are dynamically injected, making SRI complex. Document as accepted risk or switch to static script tags.
