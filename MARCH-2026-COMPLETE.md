# March 2026 — Complete Build Record
**Dates:** March 25–28, 2026
**Owner:** Aaron Kramer, Two Birds Innovation
**Plan:** Max Plan → Pro Plan transition mid-sprint

---

## Totals Across All Repos

| Metric | Count |
|--------|-------|
| Total HTML pages (DCC) | 241 |
| Total JS files (DCC) | 75 |
| Total GitHub Actions workflows (DCC) | 15 |
| Career Coach HTML pages | 3 |
| Kevin's Apartment pages | 3 |
| Total repos active | 6 |
| Estimated total commits (March 25–28) | 35+ |

---

## Digital Confidence Centre — Feature Complete List

### Core Module Ecosystem
- 20 learning modules (Module 1–19, plus Module 2.5)
- Module 2.5: 8 fully built sections (e-Transfer, appointments, Maps, apps, video calls, iCloud, data usage, updates)
- 95 quiz questions (5 per module) stored in data/module-quizzes.json
- Adaptive final quiz: skips mastered modules
- module-quiz.js: fetches from JSON, shows explanations, fires completion event
- module-nav.js: prev/next navigation + time estimates on all 20 modules
- module-ecosystem.js: injects "What You Learned" + enriches Q&A accordions
- data/module-summaries.json: 3 specific tips per module (20 modules)
- data/module-qas.json: 3–5 specific Q&As per module (20 modules)
- Quick Answers accordions on all module pages (4+ Q&As each)
- Sources & References block on all module pages

### Homepage & Navigation
- Homepage V2 personalisation: recommended module, device tip, continue-where-you-left-off
- 4-step onboarding overlay (goal → message → device → name), bilingual, one-time
- What's New section (JSON-driven, 3 cards)
- Scam of the Month card (JSON-driven, orange border, high visibility)
- Share DCC section (pre-populated mailto, green card, bilingual)
- Newsletter subscription slot on every module page

### Search Intelligence
- Levenshtein "did you mean?" suggestions
- Voice search (Web Speech API, graceful fallback)
- Search result previews with 60-char excerpts
- Recent searches (localStorage, clickable chips)
- Search analytics logging (admin/search-analytics.html)

### Print Centre
- "Build My Cheat Sheet" — generates printable HTML from selected modules
- Email option with pre-populated mailto
- Print CSS: 18pt minimum, black on white, DCC branding, date generated
- data/cheat-sheet-tips.json: 3 tips per module (21 modules)
- Quick Reference Cards: 5 printable cut-out cards at /resources/quick-reference-cards.html

### Scam Awareness
- Scam Simulator: 55 scenarios across 11 rounds
- Scam Alerts page: 13 current alerts
- data/scam-of-month.json: March 2026 — AI Voice Cloning (High)
- Scam deep dives: 13 detailed guide pages

### Accessibility & UX
- WCAG 2.1 AAA target: ARIA live announcements, keyboard shortcuts, reading guide
- 5-level font size system (S/M/L/XL/XXL/XXXL)
- High contrast mode, reduce animations, text spacing
- Friendly confirm dialogs (error-prevention)
- Floating ? Help button on all module pages
- Reading guide with IntersectionObserver paragraph highlighting

### Content Ecosystem
- 30 AEO answer pages (/answers/)
- 20 tips articles (/tips/)
- 13 scam deep dives (/resources/scam-deep-dives/)
- FR standalone pages (/fr/, /faq-fr.html)
- GEO-targeted content (/geo-content/)
- Glossary (JS-driven, 100+ terms)
- Resources hub (7 sub-pages)

### B2B & Revenue
- White-label demo (/white-label-demo/)
- B2B landing page (/b2b/)
- 6 email outreach sequences (28 emails) in /_b2b/outreach-sequences/
- ROI calculator (/b2b/roi-calculator.html)
- Grant applications: New Horizons, OTF, Starter Co Plus

### Infrastructure
- Service Worker (offline support, cache-v2)
- Sitemap.xml: 178 URLs, 0 duplicates
- sitemap-news.xml: news articles
- robots.txt: both sitemaps, correct disallow rules
- manifest.json (PWA)
- 15 GitHub Actions workflows
- Google Analytics 4 (consent-gated)
- Formspree feedback (50/month free tier)

---

## Career Coach — Feature Complete List

- AI job scoring (Anthropic API, composite score, 6 dimensions)
- CV customisation with "defendability" slider
- Red Flags Detector (collapsible ⚠️ section, coloured chips)
- Cover Letter Templates (5 frameworks, AI personalisation)
- Salary Negotiation Coach (range estimate, opening script, tactics)
- Application tracker (status, dates, notes)
- Application Report (print-ready HTML, opens in new tab)
- Export CSV
- Job history (localStorage)
- Industry insights panel
- Voice input
- FR toggle (bilingual)
- Beta landing page (privacy-first, zero tracking)

**Revenue model:** Free with Anthropic API key; future: hosted tier $9–$29/month

---

## Kevin's Apartment Search — Feature Complete List

- 15+ listings with filtering and sorting
- Commute calculator (Google Maps to 187 Fairway Ave)
- Move-in checklist (8 items, localStorage per listing)
- Move-in readiness score (X/8 checked)
- Expiry warning (21+ days old with no verification)
- Share listing button (mailto pre-populated)
- Price history tracking
- Neighbourhood safety badges
- Listing comparison tool
- Decision report
- Contact/verify button per listing
- Daily refresh timestamp via GitHub Actions

---

## Revenue Model per Product

| Product | Model | Status |
|---------|-------|--------|
| Digital Confidence Centre | B2B white-label + grant-funded | In market |
| Career Coach | Freemium (API key required) | Beta |
| Kevin's Apartment | Personal tool | Active use |
| Clarity | Free decision tool | Prototype |
| Aaron Patzalek site | Consulting lead gen | Local |

---

## Next Milestones per Product

### Digital Confidence Centre
1. Load test with 100 concurrent users on GitHub Pages
2. Recruit 10 beta testers from St. Thomas area for module feedback
3. Submit New Horizons Senior grant application (deadline: April 2026)
4. Launch B2B outreach sequence to 5 London-area libraries
5. Add modules 20+ (suggested: Online Privacy, Device Maintenance)

### Career Coach
1. Set up hosted instance with Anthropic API key pre-loaded
2. Conduct 5 user interviews with active job seekers
3. Add LinkedIn profile import (copy-paste parsing)
4. Build salary benchmark database from Canadian job boards
5. Explore privacy-compliant beta programme for 20 users

### Kevin's Apartment
1. Update listings weekly until decision is made
2. Add "Contacted" / "Viewed" / "Applied" status per listing
3. Remove expired listings (30+ days old, no update)
