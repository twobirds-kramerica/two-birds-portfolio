# Pro Plan Sprint Queue — Two Birds Innovation
**Created:** March 28, 2026
**Purpose:** Ordered sprint recommendations for the Pro plan
**Rule:** Bug fixes → content gaps → new features. Max 5 phases per sprint.

---

## Sprint 1 — ✅ COMPLETE (March 29–31, 2026)
**Repo:** digital-confidence
**Priority:** 🔴 High — user-facing issues affect trust

| Phase | What to Build | Status |
|-------|--------------|--------|
| 1 | Formspree backup: test monthly export, confirm Web3Forms secondary is live | ✅ Verified |
| 2 | Module quiz: test all 95 questions load correctly from JSON | ✅ Verified |
| 3 | Fix any 404 errors from sitemap URLs (run link-checker.yml, resolve broken links) | ✅ Fixed — 17 broken links resolved (March 31) |
| 4 | Add offline fallback for data/*.json files to service worker PRECACHE_URLS | ✅ Added (March 29) |
| 5 | Test full onboarding flow on iOS Safari (real device) and document any bugs | ✅ iOS Safari fixes pushed (March 29) |

---

## Sprint 1 (Active) — HAL Stack: n8n Install + Prompt Tracking
**Repo:** two-birds-portfolio / local machine
**Priority:** 🔴 High — intelligence infrastructure

| Phase | What to Build | Why It Matters |
|-------|--------------|----------------|
| 1 | Install n8n: `npm install -g n8n && n8n start` | Workflow automation engine — foundation for all HAL Phase 2 |
| 2 | Create basic prompt tracking workflow in n8n | Log Claude Code session summaries for knowledge management |
| 3 | Test n8n webhook trigger from a simple HTTP request | Verify n8n is reachable and functional |
| 4 | Document n8n setup in hal-stack/N8N-SETUP.md | Knowledge transfer + reproducibility |
| 5 | Create first automated workflow: DCC content freshness check | Practical value from day one |

---

## Sprint 2 — Career Coach Beta Programme
**Repo:** career-coach
**Priority:** 🔴 High — revenue-path product

| Phase | What to Build | Why It Matters |
|-------|--------------|----------------|
| 1 | Add email capture form on beta landing page (Formspree, no account required) | Need user contact info for feedback loop |
| 2 | Write BETA-FEEDBACK-GUIDE.md — how to give structured feedback, what to test | Unstructured beta = useless data |
| 3 | Add "Report an issue" button in app (opens mailto with context auto-populated) | Lower barrier for bug reports |
| 4 | Add persistent beta banner with feedback CTA across all views | Remind users they are in beta, invite feedback |
| 5 | Conduct 5 interviews with job seekers, document 3 top pain points | Validate or invalidate current feature set |

---

## Sprint 3 — DCC Content Gaps
**Repo:** digital-confidence
**Priority:** 🟡 Medium — content completeness

| Phase | What to Build | Why It Matters |
|-------|--------------|----------------|
| 1 | Add Modules 20 (Online Privacy) and 21 (Device Maintenance) with full content | Coverage gap: two major senior concerns not yet covered |
| 2 | Write 10 new tips articles (next topics: Wi-Fi security, battery care, identifying misinformation) | Tips hub is a traffic driver — more content = more organic reach |
| 3 | Write 5 new AEO answer pages targeting Canadian senior search queries | AEO pages drive organic discovery and Google position zero |
| 4 | Update all module metadata (dateModified) to current date in JSON-LD | Freshness signals for Google |
| 5 | Write FR translations for modules 16–19 (currently EN only) | Language accessibility commitment |

---

## Sprint 4 — Kevin's Apartment Decision
**Repo:** kevins-apartment-search
**Priority:** 🟡 Medium — personal time-sensitive tool

| Phase | What to Build | Why It Matters |
|-------|--------------|----------------|
| 1 | Update all listings data (verify which are still available) | Stale data = wasted viewings |
| 2 | Add "Decision Made" mode: archive listings, highlight chosen unit | Clean up after decision |
| 3 | Export decision report as printable PDF (use window.print()) | Useful record for lease signing |
| 4 | Add landlord contact log per listing (name, phone, last contact date) | Tracks follow-up history |
| 5 | Archive repo after move-in with final summary | Close the loop cleanly |

---

## Sprint 5 — DCC B2B Outreach Execution
**Repo:** digital-confidence / two-birds-portfolio
**Priority:** 🟡 Medium — revenue enablement

| Phase | What to Build | Why It Matters |
|-------|--------------|----------------|
| 1 | Send library outreach sequence to 5 London/Elgin county library branches | First revenue conversation |
| 2 | Send credit union sequence to 3 local credit unions | Second highest-probability B2B segment |
| 3 | Create one-page PDF leave-behind (export from /sales-materials/one-pager.html) | Leave-behind for in-person meetings |
| 4 | Set up dedicated B2B contact email and route to inbox | Need professional contact path |
| 5 | Add case study placeholder to /b2b/ page with "Coming soon" and beta pilot invitation | Social proof gap — start building it |

---

## Sprint 6 — Clarity AI Tool v1.0 Public Launch
**Repo:** clarity (local only)
**Priority:** 🟢 Low — future product

| Phase | What to Build | Why It Matters |
|-------|--------------|----------------|
| 1 | Push Clarity to GitHub (create twobirds-kramerica/clarity repo) | Currently local only — no backup |
| 2 | Add meta tags, favicon, og:image, and deploy to GitHub Pages | Make it publicly accessible |
| 3 | Add Formspree feedback form to Clarity | Collect user reactions |
| 4 | Write landing page copy explaining the decision-reflection concept | Product needs to explain itself |
| 5 | Share with 3 trusted users for early feedback | Validate core concept before investing more |

---

## Sprint 7 — DCC Analytics & Growth
**Repo:** digital-confidence
**Priority:** 🟢 Low — growth/measurement

| Phase | What to Build | Why It Matters |
|-------|--------------|----------------|
| 1 | Set up Google Search Console (submit sitemap, verify domain) | Track organic search performance |
| 2 | Review GA4 event tracking — confirm module completions, quiz passes, and feedback submissions fire | Core funnel events must be tracked |
| 3 | Add scroll depth tracking to module pages (25%, 50%, 75%, 100%) | Understand engagement depth |
| 4 | Build admin/growth-dashboard.html with week-over-week comparisons | Simple internal dashboard |
| 5 | Write /_docs/analytics-guide.md — how to read the dashboards and act on data | Knowledge transfer to future team members |

---

## Sprint 8 — Aaron Patzalek Consulting Site Launch
**Repo:** aaron-patzalek (local only)
**Priority:** 🟢 Low — consulting presence

| Phase | What to Build | Why It Matters |
|-------|--------------|----------------|
| 1 | Push to GitHub and deploy to GitHub Pages | Currently local only |
| 2 | Add contact form (Formspree) | Core conversion mechanism |
| 3 | Write 2 service pages (strategy consulting, digital transformation) | Differentiation and SEO |
| 4 | Add case study section (anonymised project outcomes) | Credibility for B2B prospects |
| 5 | Connect custom domain if purchased | Professional presence |

---

## Sprint 9 — DCC Mobile PWA Improvements
**Repo:** digital-confidence
**Priority:** 🟢 Low — user experience

| Phase | What to Build | Why It Matters |
|-------|--------------|----------------|
| 1 | Generate real apple-touch-icon.png (180x180 PNG from SVG placeholder) | iOS home screen icon displays correctly |
| 2 | Add "Add to Home Screen" prompt after module completion | Increases return visits |
| 3 | Improve service worker: add all module HTML and data files to offline cache | Full offline access to modules |
| 4 | Add install prompt banner (PWA beforeinstallprompt) on iOS Safari | Drive app-like installation |
| 5 | Test offline mode end-to-end: complete a module, pass quiz, offline | Verify offline promise is kept |

---

## Sprint 10 — Two Birds Innovation Site
**Repo:** two-birds-innovation (local only)
**Priority:** 🟢 Low — company presence

| Phase | What to Build | Why It Matters |
|-------|--------------|----------------|
| 1 | Audit current state of site — what exists, what is complete | Understand starting point |
| 2 | Push to GitHub and deploy to GitHub Pages | Needs to be live |
| 3 | Add product showcase: DCC, Career Coach, Clarity with screenshots | Company portfolio page |
| 4 | Add services page: digital transformation, AI for SMBs, web development | Consulting inquiry driver |
| 5 | Connect hello@twobirds.ca to a contact form (Formspree) | Professional inquiry path |

---

## Prioritisation Summary

| Sprint | Repo | Priority | Est. Phases |
|--------|------|----------|-------------|
| 1 | DCC | 🔴 Bug fixes | 5 |
| 2 | Career Coach | 🔴 Revenue path | 5 |
| 3 | DCC | 🟡 Content | 5 |
| 4 | Kevin's Apt | 🟡 Time-sensitive | 5 |
| 5 | DCC / Portfolio | 🟡 Revenue | 5 |
| 6 | Clarity | 🟢 New product | 5 |
| 7 | DCC | 🟢 Growth | 5 |
| 8 | Aaron Patzalek | 🟢 Consulting | 5 |
| 9 | DCC | 🟢 PWA | 5 |
| 10 | Two Birds | 🟢 Presence | 5 |
