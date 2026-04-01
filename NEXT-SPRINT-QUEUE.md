# Next Sprint Queue — Two Birds Innovation

**Last Updated:** 2026-03-31 (updated after site health audit sprint)
**Context:** HAL Stack foundation complete. Site health audit complete. Career Coach privacy beta confirmed. Clarity push-ready. Next: n8n install to unlock prompt automation.
**Owner:** Aaron Kramer | Two Birds Innovation

---

## Completed Since Last Update (March 31, 2026)

- ✅ DCC site health audit — meta tags, broken links, service worker, touch targets, Canadian English
- ✅ DCC print system — all 21 modules in cheat sheet generator
- ✅ Career Coach — privacy modal added to beta, all stability items verified
- ✅ Clarity — all push-prep items confirmed, PUSH-TO-GITHUB.md updated
- ✅ Portfolio — NEW-MACHINE-SETUP.md Fast Track v2.0 created

---

## How to Use This Queue

Each sprint below is a fully scoped unit of work. They are ordered by strategic priority — do them in sequence if possible, but any can be run independently.

Pick one. Open a new Claude Code session. Paste the sprint heading and bullet list as a build prompt. Run autonomously.

---

## 🔴 SPRINT 1 (ACTIVE) — n8n Installation and Prompt Queue Automation
**Priority:** High — unblocks US-002, US-003 from USER-STORIES.md
**Estimated session time:** 2–3 hours (some manual steps required on the i5)
**Repos:** digital-confidence, two-birds-portfolio

### Exact Install Commands (run in Windows Terminal as Administrator)
```
npm install -g n8n
n8n start
```
Access at: **http://localhost:5678** — create admin account on first visit.

### Remaining Tasks
- [ ] Install n8n: `npm install -g n8n && n8n start`
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

---

## AARON MANUAL TASKS — Human Sprint Backlog

### GitHub Pages — Enable on 3 Repos
**Date logged:** March 31, 2026
**Priority:** High
**Effort:** 2 minutes

For each repo below, go to **Settings → Pages → Deploy from branch → master → / (root) → Save**
Then verify the URL loads:

- [ ] github.com/twobirds-kramerica/clarity → https://twobirds-kramerica.github.io/clarity
- [ ] github.com/twobirds-kramerica/aaron-patzalek → https://twobirds-kramerica.github.io/aaron-patzalek
- [ ] github.com/twobirds-kramerica/two-birds-innovation → https://twobirds-kramerica.github.io/two-birds-innovation

**Status:** Pending Aaron action.

---

### B2B Library Outreach — Review and Approve
**Date logged:** March 31, 2026
**Priority:** High — revenue facing
**Effort:** 15 minutes

Review 3 library contacts in the DCC B2B outreach dashboard:
https://twobirds-kramerica.github.io/digital-confidence/_b2b/outreach-dashboard.html

Review the 5-email sequence at `/_b2b/outreach-sequences/library-director-sequence.md`
Approve contacts and send Email 1 to each.

**Status:** Pending Aaron approval before any email is sent.

---

### Clarity — Add Real API Key and Test
**Date logged:** March 31, 2026
**Priority:** High
**Effort:** 10 minutes

Once GitHub Pages is live at https://twobirds-kramerica.github.io/clarity:
1. Open the site
2. Enter your Anthropic API key in the form field
3. Test the diagnostic form end to end
4. Confirm the SWOT analysis and recommendations generate correctly

Note: The API key is entered by the user at runtime — it is not hardcoded in the source. It is stored in localStorage for convenience. Consider moving to a backend proxy before any public promotion of Clarity.

**Status:** Pending GitHub Pages activation first.

---

### LinkedIn — First Gap-Framing Post
**Date logged:** March 31, 2026
**Priority:** Medium — brand building
**Effort:** 20 minutes

Write and publish first brand awareness post on LinkedIn.
Theme: the AI gap in Southwestern Ontario SMEs.
Draft exists in April sprint plan (Sprint 5). Review and post.

**Status:** Pending Aaron action.

---

### Human Backlog Review Session
**Date logged:** March 31, 2026
**Priority:** High
**Effort:** 30–60 minutes — schedule for April 1 morning

This backlog is growing. Set aside time tomorrow morning to:
- [ ] Review all items in this section
- [ ] Prioritise and sequence
- [ ] Clear any quick wins (GitHub Pages takes 2 minutes)
- [ ] Flag anything that needs a Claude Code sprint to unblock

**Status:** Schedule for April 1, 2026 morning.

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
