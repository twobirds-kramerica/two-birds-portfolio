# Two Birds Innovation — Revenue Roadmap
**Created:** March 30, 2026
**Owner:** Aaron Kramer

---

## Current Revenue State

| Product | Status | Revenue |
|---------|--------|---------|
| Digital Confidence Centre | Free public tool | $0 — grant/B2B target |
| Career Coach | Beta (free) | $0 — Pro tier planned |
| Aaron Patzalek Consulting | Active | Consulting fees |
| Clarity Business Tool | Beta | $0 — SaaS planned |

---

## Path to Revenue

### Stream 1 — DCC Institutional Licensing (B2B)
**Target:** Libraries, community health centres, seniors' residences, hospitals
**Price point:** $500–$2,000/year per institution (white-label, custom branding)
**Timeline:** Q2–Q3 2026
**Blockers:** B2B demo instance needs polishing; needs a contact/quote flow

**Actions:**
- [ ] Build B2B demo landing page (`/b2b`) — request a demo form
- [ ] Create one-pager PDF for in-person pitch to St. Thomas Public Library
- [ ] Apply for Ontario Seniors' Community Grant (deadline TBD)
- [ ] Apply for CanCode / Digital Literacy federal grant stream

---

### Stream 2 — Career Coach Pro
**Target:** Individual job seekers (especially laid-off mid-career Canadians)
**Price point:** $19/month or $149/year
**Free tier:** 5 analyses/month, no CV customisation
**Pro tier:** Unlimited analyses, CV generator, salary negotiation, full export
**Timeline:** Q3 2026
**Blockers:** Backend needed to manage API keys and billing

**Actions:**
- [ ] Choose backend: Supabase (auth + DB) + Stripe (billing)
- [ ] Build API key proxy so users don't need Anthropic accounts
- [ ] Gate Pro features behind auth check
- [ ] Set up landing page with pricing (pricing.html already exists)

---

### Stream 3 — Clarity (B2B SaaS)
**Target:** Small Canadian business owners
**Price point:** $29/month per business
**What it does:** AI business health report (SWOT, priorities, quick wins)
**Timeline:** Q4 2026
**Blockers:** Currently uses Anthropic API directly from browser — needs proxy

**Actions:**
- [ ] Build backend proxy for API calls
- [ ] Add auth (email magic link or Google OAuth)
- [ ] Create report history / save reports
- [ ] Referral programme for early adopters

---

### Stream 4 — Aaron Patzalek Consulting
**Current model:** Project-based consulting (strategy, digital literacy, grants)
**Target:** Scale to retainer model ($2,500–$5,000/month per client)
**Timeline:** Now → ongoing

**Actions:**
- [ ] Add availability calendar to aaron-patzalek site
- [ ] Add Calendly embed for discovery call booking
- [ ] Create 3 service packages (Starter / Growth / Partner)
- [ ] Write 2 case studies from DCC and Career Coach builds

---

## 12-Month Revenue Target

| Stream | Q2 2026 | Q3 2026 | Q4 2026 |
|--------|---------|---------|---------|
| DCC B2B | First pilot deal | 3–5 institutions | 10 institutions |
| Career Coach | Beta (free) | Launch Pro | 50 paying users |
| Clarity | Beta | Beta | Launch |
| Consulting | $5K/month | $7K/month | $10K/month |

---

## Grant Opportunities

| Grant | Amount | Deadline | Notes |
|-------|--------|----------|-------|
| Ontario Seniors' Community Grant | $10K–$50K | Rolling | DCC is a strong fit |
| CanCode Digital Literacy | $25K–$100K | TBD 2026 | Requires non-profit partner |
| Ontario Creates (Digital) | $10K–$50K | Annual | Requires Ontario residency |
| Canada Digital Adoption Program | Up to $15K | Ongoing | For small businesses |

---

*Review and update quarterly. Next review: July 1, 2026.*
