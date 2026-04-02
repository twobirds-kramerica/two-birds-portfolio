# HOW TO RUN SPRINTS FROM CLAUDE CODE
No copy-paste needed. No Claude Web hunting. Just type:
- "next sprint" — auto-executes top 3 backlog items
- "sprint-01" — Journey Archive + Prompt Library (COMPLETE ✅)
- "sprint-02" — Language Bank + Command Centre (COMPLETE ✅)
- "sprint-03" — Commit Density Timeline (COMPLETE ✅)

---

# Next Sprint Queue — Two Birds Innovation

**Last Updated:** 2026-04-02 (overnight build)
**Context:** HAL Stack foundation complete. Sprint command system active. Sovereignty sprint complete (6 documents). Commit density timeline built (443 commits visualised). Journey archive chapters 1-3 written. Prompt library with 6 eureka prompts. Command Centre with Language Bank (V2 with Wait For Native), Prompt Library, and Journey Timeline pages. Elite Karate site polished and ready for client review.
**Owner:** Aaron Patzalek | Two Birds Innovation

---

## Completed Since Last Update (April 1, 2026)

- ✅ DCC site health audit — meta tags, broken links, service worker, touch targets, Canadian English
- ✅ DCC print system — all 21 modules in cheat sheet generator
- ✅ Career Coach — privacy modal added to beta, all stability items verified
- ✅ Clarity — full rebuild with API key setup, 7-field form, SWOT grid, quick wins, consultation CTA
- ✅ Aaron Patzalek — full personal brand site with story, projects, pricing, contact
- ✅ Two Birds Innovation — full company site with problem section, 3 tools, Why Two Birds
- ✅ B2B outreach — 9 personalised emails ready, Copy Email 1 buttons on dashboard
- ✅ LinkedIn — 8 posts ready, profile optimisation guide written
- ✅ Intelligence — Mike K outcomes, grant opportunities, Q2 revenue plan
- ✅ Journey archive — chapters 1-3, raw session log, 3 social posts
- ✅ Prompt library — 6 eureka prompts captured
- ✅ Language Bank + Prompt Library pages on Command Centre
- ✅ CLAUDE.md master context + sprint command system
- ✅ Windows Task Scheduler — overnight builds configured
- ✅ TBK and aaron-kramer repos archived
- ✅ Sovereignty sprint — 6 founding documents (audit, GitHub redundancy, LLM portability, prenuptial, IP register, HAL portability)
- ✅ Commit density timeline — 443 commits across 9 repos, raw data + visual HTML chart
- ✅ Journey timeline page on Command Centre — interactive bar chart with hover tooltips
- ✅ Portfolio sync — WIP, session state, sprint queue, last run summary all updated
- ✅ Language Bank V2 — 7 new code words, Wait For Native section, updated friction points
- ✅ Elite Karate site polished — classes, schedule, contact, mobile nav, Canadian English, Two Birds credit

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

## Sprint 11 — Sovereignty Opus Deep Dive
**Priority:** Medium — infrastructure resilience
**Estimated session time:** 2 hours
**Repos:** two-birds-portfolio, career-coach, clarity

### Tasks
- [ ] Implement LLM portability layer (llm-provider.js) from sovereignty/03 spec
- [ ] Integrate into Clarity — replace direct Anthropic fetch
- [ ] Integrate into Career Coach — replace both API call sites
- [ ] Test with Anthropic provider (default)
- [ ] Document provider switching in README

---

## Sprint 12 — CV Feedback Integration
**Priority:** Medium — product enhancement
**Estimated session time:** 2–3 hours
**Repos:** career-coach

### Tasks
- [ ] Add CV upload and parse (client-side, no backend)
- [ ] Claude analyses CV against job posting
- [ ] Generate tailored improvement suggestions
- [ ] Add "Strengthen My CV" button to job detail view
- [ ] Privacy notice: CV never stored, only sent to API during analysis

---

---

## BACKLOG PROJECTS — PENDING CLIENT FEEDBACK

### Elite Karate Site
**Date logged:** April 1, 2026 | **Updated:** April 2, 2026
**Repo:** twobirds-kramerica/elite-karate-site
**Status:** Polished — classes, schedule, contact, mobile nav, Canadian English, Two Birds credit added. Ready for client review.
**Context:** First Claude Code project. Built as free service for Aaron's kids' karate school.
**Owner contact:** Not yet confirmed — pending school owner decision.
**Next action:** Show site to school owner. Demo on mobile. Get yes/no on going live.
**Priority:** P3 — low urgency, goodwill project.
**Live URL:** GitHub Pages is NOT enabled. Enable when client confirms.

---

## AARON MANUAL TASKS — Human Sprint Backlog

### GitHub Pages — Enable on 3 Repos (P1)
**Date logged:** March 31, 2026
**Priority:** P1 — High
**Effort:** 2 minutes each

For each repo below, go to **Settings → Pages → Deploy from branch → master → / (root) → Save**
Then verify the URL loads:

- [ ] github.com/twobirds-kramerica/clarity → https://twobirds-kramerica.github.io/clarity
- [ ] github.com/twobirds-kramerica/aaron-patzalek → https://twobirds-kramerica.github.io/aaron-patzalek
- [ ] github.com/twobirds-kramerica/two-birds-innovation → https://twobirds-kramerica.github.io/two-birds-innovation

**Status:** Pending Aaron action.

---

### B2B Library Email 1 — Approve and Send to 3 Contacts (P1)
**Date logged:** March 31, 2026
**Priority:** P1 — revenue facing
**Effort:** 15 minutes

Review 3 library contacts in the DCC B2B outreach dashboard:
https://twobirds-kramerica.github.io/digital-confidence/_b2b/outreach-dashboard.html

Review the 5-email sequence at `/_b2b/outreach-sequences/library-director-sequence.md`
Approve contacts and send Email 1 to each.

**Status:** Pending Aaron approval before any email is sent.

---

### Archive TBK and aaron-kramer Repos on GitHub (P2)
**Date logged:** April 1, 2026
**Priority:** P2
**Effort:** 5 minutes

Both repos have been superseded:
- TBK → replaced by twobirds-kramerica org
- aaron-kramer → replaced by aaron-patzalek

Go to each repo → Settings → Danger Zone → Archive this repository.

**Status:** Pending Aaron action.

---

### GitHub Backup Owner Account (P2)
**Date logged:** April 1, 2026
**Priority:** P2 — business continuity
**Effort:** 15 minutes

**Steps:**
1. Create a second GitHub account using twobirdsinnovation@gmail.com (or hello@twobirds.ca)
2. Go to github.com/twobirds-kramerica → Settings → Members
3. Invite the backup account as Owner
4. Store backup account credentials in a safe place (password manager or printed copy)

**Risk if not done:** All live products (DCC, Career Coach, Clarity) go dark if main account is compromised.
**See also:** sovereignty/02-github-redundancy-plan.md

**Status:** Pending Aaron action.

---

### Silver Laptop — Disable Sleep on AC Power (P2)
**Date logged:** April 1, 2026
**Priority:** P2
**Effort:** 1 minute

Run in elevated PowerShell:
```
powercfg /change standby-timeout-ac 0
```

Keeps the silver laptop awake when plugged in for overnight builds.

**Status:** Pending Aaron action.

---

### LinkedIn Post 1 — Gap Framing Post (P3)
**Date logged:** March 31, 2026
**Priority:** P3 — brand building
**Effort:** 20 minutes

Write and publish first brand awareness post on LinkedIn.
Theme: the AI gap in Southwestern Ontario SMEs.
Draft exists in DCC marketing assets. Review and post.

**Status:** Pending Aaron action.

---

### Clarity — Add Real API Key and Test
**Date logged:** March 31, 2026
**Priority:** P2 (blocked by GitHub Pages)
**Effort:** 10 minutes

Once GitHub Pages is live at https://twobirds-kramerica.github.io/clarity:
1. Open the site
2. Enter your Anthropic API key in the form field
3. Test the diagnostic form end to end
4. Confirm the SWOT analysis and recommendations generate correctly

**Status:** Pending GitHub Pages activation first.

---

### Show Elite Karate Site to School Owner (P2)
**Date logged:** April 2, 2026
**Priority:** P2 — goodwill, potential portfolio piece
**Effort:** 15 minutes

Site has been polished: classes section, schedule, contact, mobile nav, Canadian English.
Show to school owner on their phone. Get yes/no on going live.
If yes: enable GitHub Pages on twobirds-kramerica/elite-karate-site (2 min).

**Status:** Pending Aaron action.

---

### Codeberg Account — Mirror Top 3 Repos (P2)
**Date logged:** April 1, 2026
**Priority:** P2 — sovereignty
**Effort:** 15 minutes

Create Codeberg account and mirror digital-confidence, career-coach, clarity.
Full instructions in sovereignty/02-github-redundancy-plan.md.

**Status:** Pending Aaron action.

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
| 11 — Sovereignty Deep Dive | Medium | Medium | Infrastructure |
| 12 — CV Feedback | Medium | Medium | Product enhancement |

**Recommended order for maximum revenue impact:**
5 → 3 → 2 → 4 → 6 → 1 → 7 → 11 → 10 → 12 → 8 → 9
