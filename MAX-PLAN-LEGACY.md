# Max Plan Legacy — Two Birds Innovation
**Created:** March 30, 2026
**Purpose:** Definitive record of everything built in the Max Plan multi-repo sprint (March 25–30, 2026)

---

## What "Max Plan" Means

The Max Plan was a series of fully autonomous Claude Code build sprints across
all Two Birds Innovation repositories. Each session picked up where the last left off
with no manual intervention between phases. This document records the final state.

---

## Repos Touched

| Repo | Purpose | State at End |
|------|---------|--------------|
| `brenda-digital-confidence` | DCC — seniors digital literacy platform | Production-ready |
| `career-coach` | AI job application tool | Beta-ready |
| `kevins-apartment-search` | Kevin's personal apartment search | Active use |
| `aaron-patzalek` | Aaron Patzalek consulting site | Live with availability indicator |
| `clarity` | AI business health report tool | Beta with sample report |
| `two-birds-portfolio` | Archive + documentation | This file |

---

## DCC — Complete Build Log

### Infrastructure
- Service worker with cache-first JSON strategy
- 15 GitHub Actions workflows (content count, accessibility reminder, sitemap freshness, uptime)
- Sitemap with 178 URLs, zero duplicates
- robots.txt blocking internal paths, allowing AI crawlers

### Content
- 19 modules (1–17 + 18 Staying Connected + 19 Digital Legacy)
- Quick Answers accordion on all modules
- data/module-summaries.json — 3 bullets per module
- data/module-qas.json — 3–5 Q&As per module
- data/answers-index.json — searchable answer index
- data/tips-index.json — tips library index

### Features
- Final quiz (60 questions, adaptive skip for mastered modules)
- Certificate of completion with cert number
- Leaderboard (localStorage, top 5 history)
- Scam simulator (55 scenarios)
- FAQ with fuzzy search (Fuse.js)
- Glossary with 60+ terms
- Print centre
- YouTube intercept modal (prevents accidental navigation)
- Panic button (scam help guide)
- Voice input on all form fields
- Dyslexia-friendly font toggle
- High contrast toggle
- Text spacing toggle
- Reading guide

### Localisation (FR/EN)
- All navigation, footer, module titles
- Dynamic JS strings: feedback modal, settings dialogs, help button
- Quiz: adaptive notice, leaderboard, certificate share
- Onboarding wizard, welcome splash

### SEO / Schema
- Open Graph on all 81 pages
- FAQPage JSON-LD on scam deep-dive pages
- Article schema with speakable on tip pages
- GEO schema targeting Ontario
- Both sitemaps in robots.txt

### Accessibility
- prefers-reduced-motion in main.css and exercises.css
- All modals: role="dialog", aria-modal="true", aria-label/labelledby
- All accordions: aria-expanded on buttons
- All inputs: associated labels
- 10 render-blocking scripts fixed with defer

---

## Career Coach — Complete Build Log

- Claude Haiku 4.5 for job analysis
- Claude Sonnet 4.6 for salary negotiation
- Composite score formula (ATS 30% + Fit 25% + Salary 20% + Risk 15% + Rec 10%)
- Keyboard shortcuts modal (?, N, Ctrl+Enter, Escape)
- Salary negotiation modal (AI-generated, bilingual)
- Red flags detector (7 categories)
- Industry insights (9 Canadian sectors)
- Cover letter templates (5 templates, bilingual)
- Job search stats card (analysed, avg score, recommended, days active)
- Print stylesheet for job detail
- Export CSV + HTML application report
- Demo job posting (Acme Health Tech PM role)
- Voice input on all onboarding fields
- French/English toggle throughout
- Storage quota error handling

---

## Kevin's Apartment — Complete Build Log

- 15+ listings with full data (price, neighbourhood, amenities)
- Neighbourhood safety ratings (community-sourced)
- Leaflet.js map with listing pins
- Favourites (heart button, filter)
- Notes (per-listing private notes)
- Move-in checklist (7 items, progress badge)
- **Decision Ready badge** (favourited + note + 6/7 checklist items)
- Comparison panel (up to 3 listings)
- Commute calculator (Google Maps link)
- Expiry warnings (listings older than 14 days flagged)
- Share listing (Web Share API)
- Printable decision report
- 3 GitHub Actions workflows (daily refresh, stale listings daily, stale listings weekly)

---

## Sprint Metrics

| Metric | Value |
|--------|-------|
| Total commits across all repos | ~60 |
| Total HTML files touched | 90+ |
| Total JS files modified | 12 |
| Total CSS files modified | 3 |
| Python scripts written | 4 (audit + bulk fixes) |
| GitHub Actions workflows created | 18 |
| Build sessions | 4 (March 25, 26, 28, 29–30) |
| Autonomous phases executed | 30+ |

---

*This document is the final record of the Max Plan sprint. Future work tracked in WIP-DASHBOARD.md.*
