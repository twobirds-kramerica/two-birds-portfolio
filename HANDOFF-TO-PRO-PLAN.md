# Handoff to Pro Plan — Two Birds Innovation
**Created:** March 30, 2026
**Author:** Aaron Kramer | Two Birds Innovation

---

## What Was Built (Max Plan Sprint, March 25–30, 2026)

This document summarises the complete handoff state across all active repos
after the autonomous multi-repo build sprint.

---

## Repo Status at Handoff

### Digital Confidence Centre (`twobirds-kramerica/digital-confidence`)
**State:** Production-ready. 19 modules complete. Full bilingual (EN/FR).

| Area | Status |
|------|--------|
| Modules 1–19 | ✅ All complete with Q&A sections, What You Learned, star ratings |
| Open Graph meta | ✅ All 81 pages fixed (og:title, og:description, og:type, og:locale) |
| Schema / SEO | ✅ FAQPage, Article, speakable, GEO indexed, sitemap clean |
| French content | ✅ All dynamic JS strings translated (feedback, settings, help button, quiz) |
| Accessibility | ✅ prefers-reduced-motion, all modals ARIA-compliant |
| Performance | ✅ 10 render-blocking scripts defered, robots.txt updated |
| Service Worker | ✅ PRECACHE_URLS includes all JSON data files |
| GitHub Actions | ✅ 15 workflows validated |

**Remaining work for Pro Plan:**
- Full French translation of `final-quiz.js` question strings (120+ questions — needs human translation)
- Module 2.5 (visual AI) — content review
- B2B demo instance customisation

---

### Career Coach (`twobirds-kramerica/career-coach`)
**State:** Beta-ready. Full feature set deployed.

| Feature | Status |
|---------|--------|
| Core analysis (CV vs job posting) | ✅ Claude Haiku 4.5 |
| Keyboard shortcuts | ✅ |
| Salary negotiation modal | ✅ Claude Sonnet 4.6 |
| Red flags detector | ✅ |
| Industry insights (9 sectors) | ✅ |
| Cover letter templates (5) | ✅ |
| Job search stats card | ✅ March 30 |
| Print stylesheet | ✅ March 30 |
| Export CSV + HTML report | ✅ |
| French / English toggle | ✅ |

**Remaining work for Pro Plan:**
- Backend API key management (so users don't need their own Anthropic key)
- Payment integration for Pro tier
- Email digest / weekly report feature
- Mobile app wrapper (Capacitor or similar)

---

### Kevin's Apartment Search (`twobirds-kramerica/kevins-apartment-search`)
**State:** Active use. Personal tool — not public.

| Feature | Status |
|---------|--------|
| Listings with neighbourhood data | ✅ |
| Favourites, notes, checklist | ✅ |
| Comparison panel | ✅ |
| Decision Ready badge | ✅ March 30 |
| Commute calculator | ✅ |
| Decision report (printable) | ✅ |
| Stale listings automation | ✅ 3 GitHub Actions workflows |

**Status:** Kevin's search is ongoing. No Pro Plan items required.

---

## Recommended Next Sprints (Priority Order)

1. **DCC French quiz translation** — 120+ question strings in final-quiz.js
2. **Career Coach Pro backend** — remove dependency on user-supplied API key
3. **DCC B2B demo customisation** — white-label version for library/hospital demos
4. **Aaron Patzalek site launch** — availability calendar, booking integration
5. **Clarity tool beta launch** — public URL, feedback collection

---

## Key Technical Decisions

- **Static only.** All sites are flat HTML/CSS/JS on GitHub Pages + Cloudflare. No Node.js.
- **Anthropic API.** Career Coach and Clarity use the Anthropic API directly from the browser with `anthropic-dangerous-direct-browser-access: true`. This is suitable for beta but requires a backend for production.
- **Formspree.** DCC feedback uses Formspree (free tier, 50/month). Export CSV monthly before hitting limit.
- **Bilingual pattern.** All DCC JS uses `var fr = (localStorage.getItem('dc-lang') || ...).startsWith('fr')` then ternary operators. Career Coach uses `data-en` / `data-fr` attributes + `applyLang()`.

---

## Contacts & Access

- **GitHub org:** `twobirds-kramerica`
- **Formspree dashboard:** https://formspree.io/f/xeerqryj
- **Cloudflare:** Manage via Aaron's account
- **Domain:** two-birds.ca (pending full launch)
