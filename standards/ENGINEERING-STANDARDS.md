# Engineering Standards — Two Birds Innovation

**Version:** 1.0
**Created:** 2026-04-15
**Status:** ACTIVE — all new work must comply. Existing work remediated per S-017+.

Every repo under `C:\twobirds\` follows these standards. No exceptions without documented override in the sprint that introduces the deviation.

---

## 1. Code Style

### HTML
- Semantic elements over generic `<div>` / `<span>` (`<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<header>`, `<footer>`)
- All pages must have a single `<h1>`, heading hierarchy must not skip levels
- All `<img>` must have `alt` attributes (decorative images: `alt=""`)
- All `<a>` links must have descriptive text (no "click here")
- Forms: every `<input>` must have a linked `<label>` (via `for`/`id`)
- Language attribute: `<html lang="en-CA">`
- Charset: `<meta charset="UTF-8">`
- Viewport: `<meta name="viewport" content="width=device-width, initial-scale=1">`

### CSS
- CSS custom properties (variables) for all colours, spacing, and typography — never hardcode hex/rgb in component styles
- Mobile-first: base styles for mobile, `min-width` media queries for larger screens
- No `!important` except accessibility overrides
- Class naming: lowercase kebab-case (`.hero-section`, `.card-title`)
- No IDs for styling — IDs for JS hooks and anchor targets only
- Prefer `rem` for font sizes, `px` for borders/shadows, `%` or `vw/vh` for layout

### JavaScript
- Vanilla JS only — no frameworks, no npm, no build steps
- `'use strict';` at top of every file
- `const` by default, `let` when reassignment needed, never `var`
- Event delegation where possible
- No inline `onclick` handlers — use `addEventListener`
- Error handling: `try/catch` around external calls (fetch, file reads)

### File Organisation
- One CSS file per concern (main, print, accessibility, component-specific)
- Shared components in `standards/components/`
- CSS tokens in `standards/tokens.css`
- All paths relative — no absolute filesystem paths in code

---

## 2. Accessibility — WCAG 2.1 AA (Minimum)

| Requirement | Standard | Target |
|------------|----------|--------|
| Colour contrast (normal text) | 4.5:1 minimum | 7:1 where practical |
| Colour contrast (large text) | 3:1 minimum | 4.5:1 where practical |
| Tap/click targets | 44x44px minimum | 48x48px preferred |
| Font size (body) | 16px minimum | 18px for senior-facing (DCC) |
| Line height | 1.5 minimum | 1.6 for body text |
| Focus indicators | Visible on all interactive elements | 3px solid outline, offset 2px |
| Skip navigation | Present on every page | First focusable element |
| Screen reader support | ARIA labels on all interactive elements | Landmark regions on every page |
| Reduced motion | `prefers-reduced-motion` respected | All transitions/animations disabled |
| Keyboard navigation | All functionality keyboard-accessible | Tab order matches visual order |

### Testing
- Run axe-core (`?qa=true` parameter on DCC pages) before shipping
- Manual keyboard-only navigation test on every new page
- Contrast check on every new colour combination before committing

---

## 3. Performance Targets

| Metric | Target | Tool |
|--------|--------|------|
| First Contentful Paint | < 1.5s | Lighthouse |
| Largest Contentful Paint | < 2.5s | Lighthouse |
| Total Blocking Time | < 200ms | Lighthouse |
| Cumulative Layout Shift | < 0.1 | Lighthouse |
| Page weight (HTML + CSS + JS) | < 500KB uncompressed | DevTools |
| Images | WebP preferred, `loading="lazy"` on below-fold | Manual |
| Fonts | `display=swap`, subset if possible | Google Fonts param |

### Rules
- No external JS libraries unless justified in sprint prompt and documented
- CSS `@import` only for Google Fonts — all other CSS via `<link>` tags
- Inline critical CSS for above-fold content on landing pages
- No render-blocking JS in `<head>` — use `defer` or place before `</body>`

---

## 4. SEO & AEO (Answer Engine Optimisation)

### Every Page Must Have
- `<title>` — unique, under 60 characters, front-loaded with primary keyword
- `<meta name="description">` — unique, under 155 characters, includes CTA or value prop
- `<meta name="robots" content="index, follow">` (unless intentionally noindex)
- `<link rel="canonical" href="...">` — self-referencing canonical
- Open Graph tags: `og:title`, `og:description`, `og:image`, `og:url`
- Structured data (JSON-LD) where applicable: Organization, Article, FAQ, HowTo

### AEO-Specific
- FAQ sections use `<details>` / `<summary>` (crawlable, accessible)
- Direct-answer paragraphs at top of content sections (position zero targeting)
- Schema markup for FAQ pages, how-to guides, and course content (DCC)

### Sitemap & Robots
- `sitemap.xml` in repo root, updated when pages added/removed
- `robots.txt` in repo root, permissive with sitemap reference
- `<meta name="last-modified">` or `<meta name="date">` on content pages (feeds freshness system)

---

## 5. Security Baseline

| Rule | Implementation |
|------|---------------|
| No secrets in repos | `.gitignore` covers `.env`, credentials, API keys |
| HTTPS only | Enforced at hosting layer (GitHub Pages, Cloudflare, Vercel) |
| Content Security Policy | `<meta>` CSP header on all pages |
| No inline scripts | All JS in external files (exception: JSON-LD structured data) |
| Form submissions | HTTPS endpoints only, CSRF where applicable |
| Dependencies | Zero npm dependencies (standing rule). CDN-loaded libs must be pinned to specific version with SRI hash |
| Subresource Integrity | `integrity` attribute on all CDN `<script>` and `<link>` tags |

---

## 6. Git Workflow

### Branching
- `master` (or `main`) is the production branch
- Commit directly to master for solo work (current model)
- Feature branches optional for experimental work: `feature/[short-name]`

### Commits
- Commit after every phase within a sprint
- Message format: `type(scope): description`
  - Types: `feat`, `fix`, `chore`, `log`, `docs`, `refactor`, `test`
  - Scope: repo name or feature area
  - Description: imperative mood, under 72 characters
- Examples:
  - `feat(dcc): add module 22 — smartphone basics`
  - `fix(css): contrast ratio on nav links WCAG AA`
  - `chore(hal): merged 3 captured items from pending queue`

### Tags
- Tag releases: `v[major].[minor].[patch]` (e.g., `v1.2.0`)
- Tag significant milestones (optional): `milestone/[name]`

---

## 7. Testing Requirements

### Before Shipping Any Page
- [ ] HTML validates (no unclosed tags, no duplicate IDs)
- [ ] axe-core returns 0 critical / 0 serious issues
- [ ] Page loads in < 2.5s on throttled 3G (Lighthouse)
- [ ] All links work (no 404s)
- [ ] Mobile viewport renders correctly (375px minimum)
- [ ] Keyboard navigation reaches all interactive elements
- [ ] Dark mode (if supported) maintains contrast ratios

### Before Shipping Any Sprint
- [ ] All changed files committed
- [ ] SESSION-STATE.md updated
- [ ] CHANGELOG.md updated (if user-facing changes)
- [ ] Sprint-queue.md status updated

---

## 8. Sovereignty & Dependency Rules

### Zero External Runtime Dependencies
- No npm. No Node frameworks. No build steps. (Standing rule from CLAUDE.md)
- Static HTML/CSS/JS only
- If a library is needed, it must be:
  1. Loaded from a CDN with pinned version + SRI hash
  2. Documented in the sprint that introduces it
  3. Have a documented fallback if the CDN is unavailable

### Approved CDN Sources
| Library | CDN | Use Case | Fallback |
|---------|-----|----------|----------|
| Inter font | Google Fonts | Typography | System fonts |
| axe-core | cdnjs | QA testing only | Manual accessibility check |
| Tailwind CSS | CDN (play) | Utility classes | Custom CSS |

### Dependency Audit
- Every external resource must pass the decapitation test: "If this CDN goes down, does the site still work?"
- Fonts: must have system font fallback stack
- JS libraries: must not be required for core content rendering
- CSS frameworks: must not break layout if CDN fails (progressive enhancement)

---

## Compliance

Every sprint prompt must include a standards checklist (see sprint-template.md). Work that doesn't meet these standards gets flagged in QA and fixed before the sprint is marked DONE.
