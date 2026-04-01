# April 2026 Sprint Plan — Two Birds Innovation
**Created:** March 31, 2026
**Owner:** Aaron Kramer
**Rule:** Max 5 phases per sprint. Commit after every phase. Static HTML/CSS/JS only.

---

## Sprint 1 — n8n Install + Basic Prompt Tracking Workflow (HAL)
**Week of:** April 1, 2026
**Repo:** local machine + two-birds-portfolio
**Priority:** 🔴 High — intelligence infrastructure foundation

| Phase | What to Do | Notes |
|-------|-----------|-------|
| 1 | Install n8n globally | `npm install -g n8n && n8n start` |
| 2 | Create prompt tracking workflow | Log Claude Code session summaries (date, repo, phases, outcome) |
| 3 | Test webhook trigger | Verify n8n responds to HTTP requests |
| 4 | Document setup | hal-stack/N8N-SETUP.md — ports, credentials, startup command |
| 5 | Create first practical workflow | DCC content freshness check — flag modules not updated in 30+ days |

**Success criteria:** n8n running locally, one workflow operational, setup documented.

---

## Sprint 2 — LightRAG Install and DCC Ingest (HAL Intelligence)
**Week of:** April 8, 2026
**Repo:** local machine + two-birds-portfolio
**Priority:** 🔴 High — knowledge management

| Phase | What to Do | Notes |
|-------|-----------|-------|
| 1 | Install LightRAG (Python) | `pip install lightrag` — local RAG engine |
| 2 | Write DCC content ingestion script | Feed all module HTML, tips, and answer pages into RAG index |
| 3 | Test query interface | Ask "What does Module 5 cover?" and verify sourced response |
| 4 | Ingest non-DCC content | Career Coach, portfolio docs, strategy files |
| 5 | Document RAG setup + query examples | hal-stack/LIGHTRAG-SETUP.md |

**Success criteria:** LightRAG running locally, DCC content indexed, accurate answers to content queries.

---

## Sprint 3 — Google Search Console Verification + Sitemap Submission
**Week of:** April 15, 2026
**Repo:** digital-confidence
**Priority:** 🟡 Medium — SEO/discovery

| Phase | What to Do | Notes |
|-------|-----------|-------|
| 1 | Verify DCC domain in Google Search Console | Use HTML tag method (already have placeholder in index.html) |
| 2 | Submit sitemap.xml and sitemap-news.xml | Both files confirmed valid March 31 |
| 3 | Review initial crawl data after 48 hours | Check for indexing errors, coverage issues |
| 4 | Fix any crawl errors reported by GSC | Likely: canonical tags, mobile usability |
| 5 | Set up weekly GSC check routine | n8n workflow or calendar reminder |

**Success criteria:** DCC indexed in Google, sitemap accepted, no critical crawl errors.

---

## Sprint 4 — First B2B Outreach Email to 3 Library Contacts (Revenue)
**Week of:** April 22, 2026
**Repo:** digital-confidence (email sequences in /_b2b/)
**Priority:** 🟡 Medium — first revenue conversation

| Phase | What to Do | Notes |
|-------|-----------|-------|
| 1 | Identify 3 library contacts in Elgin/London region | St. Thomas Public Library, London Public Library, Elgin County Library |
| 2 | Personalise outreach email from /_b2b/outreach-sequences/ | Use library-specific template, reference local senior population |
| 3 | Send first email to all 3 contacts | From hello@twobirds.ca |
| 4 | Create follow-up tracker in portfolio | Track responses, meeting requests, next steps |
| 5 | Prepare one-pager PDF for meeting leave-behind | Export from /sales-materials/one-pager.html using window.print() |

**Success criteria:** 3 emails sent, follow-up scheduled for 7 days, one-pager ready.

---

## Sprint 5 — LinkedIn Post: Gap Framing Post (Brand)
**Week of:** April 29, 2026
**Repo:** digital-confidence (social content in /_social/)
**Priority:** 🟢 Low — brand awareness

| Phase | What to Do | Notes |
|-------|-----------|-------|
| 1 | Write gap-framing LinkedIn post | "We teach kids to code but not seniors to stay safe online" angle |
| 2 | Create supporting visual (Canva or screenshot of DCC homepage) | Eye-catching image for engagement |
| 3 | Post to Aaron's LinkedIn profile | Include link to DCC and relevant hashtags |
| 4 | Cross-post adapted version to Two Birds Innovation page | Slightly different angle for company page |
| 5 | Track engagement for 48 hours and document results | Impressions, clicks, comments — record in /_social/ |

**Success criteria:** Post published, engagement tracked, lessons documented for future posts.

---

## April Summary

| Sprint | Focus | Priority | Key Outcome |
|--------|-------|----------|-------------|
| 1 | n8n install (HAL) | 🔴 High | Local workflow automation running |
| 2 | LightRAG + DCC ingest (HAL) | 🔴 High | Knowledge base queryable |
| 3 | Google Search Console (SEO) | 🟡 Medium | DCC discoverable in search |
| 4 | Library outreach (Revenue) | 🟡 Medium | First B2B conversations started |
| 5 | LinkedIn gap post (Brand) | 🟢 Low | Public brand presence established |

**Monthly theme:** Move from building to growing. Infrastructure is solid — now focus on discovery, revenue, and intelligence.

---

*Two Birds Innovation | St. Thomas, Ontario | Always forward. Never quit. Grow bravely. Support with care.*
