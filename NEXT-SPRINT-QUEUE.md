# Next Sprint Queue — Two Birds Innovation

**Last Updated:** 2026-03-31
**Context:** Transitioning from Max Plan. HAL Stack foundation is complete. Ready for Pro Plan or continued free-tier building.
**Owner:** Aaron Kramer | Two Birds Innovation

---

## How to Use This Queue

Each sprint below is a fully scoped unit of work. They are ordered by strategic priority — do them in sequence if possible, but any can be run independently.

Pick one. Open a new Claude Code session. Paste the sprint heading and bullet list as a build prompt. Run autonomously.

---

## Sprint 1 — n8n Installation and Prompt Queue Automation
**Priority:** High — unblocks US-002, US-003 from USER-STORIES.md
**Estimated session time:** 2–3 hours (some manual steps on i5)
**Repos:** digital-confidence, two-birds-portfolio

### Tasks
- [ ] Install n8n on i5 Lenovo: `npm install -g n8n && n8n start`
- [ ] Create admin account at http://localhost:5678
- [ ] Build Workflow 1: Gmail PROMPT-QUEUE label → SQLite row (PENDING)
- [ ] Build Workflow 2: GitHub push webhook → match commit → update SQLite (COMPLETE)
- [ ] Set up Cloudflare Tunnel for webhook endpoint access
- [ ] Export workflow JSON to `hal-stack/n8n/workflows/`
- [ ] Update `hal-stack/ROADMAP.md` with completed items
- [ ] Update Quality Dashboard HAL panel: n8n status → ✅ Operational

---

## Sprint 2 — DCC Modules 18 and 19 (Senior Tech Stars + Digital Legacy)
**Priority:** High — content completion milestone
**Estimated session time:** 3–4 hours
**Repos:** digital-confidence

### Tasks
- [ ] Create `module-18.html` — Senior Tech Stars: celebrating seniors who teach others
- [ ] Create `module-19.html` — Digital Legacy: passwords, accounts, what happens when you pass away
- [ ] Both modules: full EN/FR bilingual, quiz, What You Learned enrichment
- [ ] Add to `data/module-summaries.json` and `data/module-qas.json`
- [ ] Add to sitemap.xml and nav
- [ ] Update DCC home page module count (currently says 17, will be 19)
- [ ] Add module-18 and module-19 to `content-count-report.yml` checks

---

## Sprint 3 — DCC B2B Landing Page and Outreach Package
**Priority:** High — revenue path
**Estimated session time:** 2–3 hours
**Repos:** digital-confidence

### Tasks
- [ ] Create `/b2b/index.html` — DCC white-label pitch for libraries and credit unions
- [ ] Page sections: what DCC is, who it is for, usage data, partnership tiers, contact CTA
- [ ] Create `/b2b/one-pager.html` — printable PDF-ready one-pager version
- [ ] Add B2B link to resources hub nav
- [ ] Create `_b2b/email-sequence.md` — 3-email cold outreach sequence for Ontario public libraries
- [ ] Update sitemap.xml

---

## Sprint 4 — Career Coach Privacy Beta and Roadmap
**Priority:** Medium — product maturation
**Estimated session time:** 2 hours
**Repos:** career-coach

### Tasks
- [ ] Add privacy notice: "All job data is stored only in your browser. Nothing leaves your device."
- [ ] Add data export button: downloads all jobs as JSON file
- [ ] Add data clear button with confirmation modal
- [ ] Update README.md with beta status, feature list, and roadmap
- [ ] Create `ROADMAP.md` in career-coach repo: Phase 2 (AI analysis integration), Phase 3 (Claude API)

---

## Sprint 5 — Aaron Patzalek Consulting Site
**Priority:** Medium — revenue path (fastest)
**Estimated session time:** 3–4 hours
**Repos:** aaron-patzalek (new or existing)

### Tasks
- [ ] Check if `aaron-patzalek` repo exists; create from two-birds-project-template if not
- [ ] Build single-page consulting site: hero, services, case studies (DCC, Career Coach), contact
- [ ] Services: Product Management, AI Integration, Digital Transformation
- [ ] Case study 1: DCC — built in 72 hours, 19 modules, WCAG 2.1 AA
- [ ] Case study 2: Career Coach — AI-powered job tracking and analysis tool
- [ ] CTA: aaron.patzalek@gmail.com | LinkedIn URL
- [ ] Deploy to GitHub Pages

---

## Sprint 6 — DCC Grants Research and Applications Package
**Priority:** Medium — revenue path (slow burn)
**Estimated session time:** 2 hours
**Repos:** digital-confidence

### Tasks
- [ ] Research: Ontario Trillium Foundation, Heritage Canada Digital Literacy grants
- [ ] Create `_grants/application-tracker.md` — list of grants, deadlines, requirements
- [ ] Create `_grants/letter-of-intent-template.md` — reusable LOI for digital literacy grants
- [ ] Update `_grants/` directory with any existing draft applications
- [ ] Add grant pursuit plan to REVENUE-ROADMAP.md in two-birds-portfolio

---

## Sprint 7 — Clarity AI Tool Rebuild (Full Product)
**Priority:** Medium — product portfolio
**Estimated session time:** 4–5 hours
**Repos:** clarity (existing)

### Tasks
- [ ] Read current clarity/ repo state — `git log --oneline -20`
- [ ] Complete the 5-question diagnostic flow
- [ ] Add result screens: Founder, Builder, Explorer, Connector archetypes
- [ ] Add email capture for "send me my full report" (Formspree)
- [ ] Deploy to GitHub Pages
- [ ] Add to two-birds-portfolio WIP-DASHBOARD.md

---

## Sprint 8 — Kevin's Apartment Search Enhancement
**Priority:** Low — product polish
**Estimated session time:** 2 hours
**Repos:** kevins-apartment-search

### Tasks
- [ ] Add a "Compare" mode: side-by-side view of 2 favourited listings
- [ ] Add score breakdown tooltip on hover (commute, price, amenities)
- [ ] Add print-friendly single-listing detail view
- [ ] Confirm Decision Ready badge logic handles edge cases (no checklist data)

---

## Sprint 9 — LightRAG Installation and DCC Ingestion
**Priority:** Low — infrastructure (May 2026)
**Estimated session time:** 2–3 hours (manual steps on i5)
**Repos:** two-birds-portfolio

### Tasks
- [ ] Install LightRAG: `pip install lightrag-hku`
- [ ] Configure port 9621 and start server
- [ ] Ingest DCC repo files into knowledge graph
- [ ] Test query from Claude Code via MCP
- [ ] Document results in `hal-stack/ROADMAP.md`
- [ ] Update Quality Dashboard: LightRAG status → ✅ Operational

---

## Sprint 10 — Two Birds Innovation Public Site
**Priority:** Low — marketing
**Estimated session time:** 3–4 hours
**Repos:** two-birds-innovation (existing)

### Tasks
- [ ] Read current two-birds-innovation/ repo state
- [ ] Build or update: about page, products section (DCC, Career Coach, Clarity, Kevin's Apt)
- [ ] Add "Work With Us" section pointing to aaron-patzalek consulting site
- [ ] Add links to GitHub Pages for all live products
- [ ] Canadian English audit
- [ ] Deploy to GitHub Pages

---

## Quick Reference — Priority Matrix

| Sprint | Strategic Value | Effort | Revenue Path |
|--------|----------------|--------|--------------|
| 1 — n8n | High | High | Infrastructure |
| 2 — Modules 18/19 | High | Medium | DCC completeness |
| 3 — B2B Landing | High | Medium | Direct revenue |
| 4 — Career Coach Privacy | Medium | Low | Product trust |
| 5 — Consulting Site | High | Medium | Direct revenue (fastest) |
| 6 — Grants | Medium | Low | Indirect revenue |
| 7 — Clarity Rebuild | Medium | High | Product portfolio |
| 8 — Kevin's Apt | Low | Low | Polish |
| 9 — LightRAG | Low | High | Infrastructure |
| 10 — Two Birds Site | Low | Medium | Marketing |

**Recommended order for maximum revenue impact:**
5 → 3 → 2 → 4 → 6 → 1 → 7 → 10 → 8 → 9
