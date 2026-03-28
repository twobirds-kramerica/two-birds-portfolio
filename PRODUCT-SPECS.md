# Product Specs — Two Birds Innovation
**Last Updated:** March 28, 2026
**Owner:** Aaron Kramer

One-page spec per product. Seven products total.

---

## 1. Digital Confidence Centre (DCC)

**What it does:** A digital literacy training platform for Canadian seniors (age 70+). Covers 19 modules including scam protection, online banking, video calls, social media safety, grocery delivery, ride-sharing, AI basics, and more. Bilingual (English/French).

**Who it's for:** Seniors in Ontario, primarily iPad/iPhone users. B2B partners include libraries, credit unions, community organisations, and home care providers.

**Tech stack:** Static HTML, CSS, JavaScript. GitHub Pages + Cloudflare. Formspree + Web3Forms for forms. Anthropic API not used in core modules (reserved for future AI guide).

**Live URL:** https://twobirds-kramerica.github.io/digital-confidence/

**Revenue model:**
- B2B white-label licensing: $4,800 Starter / $12,000 Pro / $24,000 Enterprise per year
- Grant funding: New Horizons for Seniors ($25k), Ontario Trillium Foundation ($48.5k) in pipeline
- Consulting: paid implementation support for partner organisations

**Next milestone:** First B2B partner outreach meeting. Confirm Formspree beta endpoint. Submit New Horizons grant application.

---

## 2. Career Coach

**What it does:** An AI-powered job application coaching tool. Users paste a job description and upload their CV. The tool scores the match, highlights gaps, and generates customised cover letters and application materials. Tracks applications across sessions.

**Who it's for:** Job seekers at any career stage who want to maximise their application quality. Currently free (beta).

**Tech stack:** Static HTML, CSS, JavaScript. Anthropic API (claude-3-haiku) for scoring and letter generation. LocalStorage for session persistence. GitHub Pages.

**Live URL:** https://twobirds-kramerica.github.io/career-coach/

**Revenue model:**
- Freemium: free tier (3 analyses/month), Pro tier ($10/user/month — not yet activated)
- B2B: employer-side coaching tools (future)

**Next milestone:** Beta user recruitment. Formspree beta endpoint confirmation. Stripe integration for Pro tier.

---

## 3. Clarity

**What it does:** An AI-assisted SME diagnostic tool. Business owners answer structured prompts about their situation, constraints, and goals. The tool runs a SWOT analysis, maps effort vs impact, generates AI summaries, and captures leads for a consultation call with Aaron.

**Who it's for:** Small and medium business owners who feel stuck, overwhelmed, or unclear on priorities. Primary lead generation tool for Aaron's consulting practice.

**Tech stack:** Static HTML, CSS, JavaScript. Anthropic API for reflection summaries. Formspree for lead capture. LocalStorage for session history.

**Live URL:** Local only — needs GitHub remote and Pages enabled.

**Revenue model:** Lead generation → $2,500 AI Workflow Audit or $4,000/month consulting retainer. No direct product revenue.

**Next milestone:** Push to GitHub. Create remote repo. Enable GitHub Pages. Test Formspree lead capture.

---

## 4. Aaron Patzalek Consulting Site

**What it does:** A professional consulting site for Aaron Patzalek (product strategy, discovery, team coaching, advisory). Showcases services, rates, background, and includes a contact form.

**Who it's for:** Organisations and teams looking for fractional product leadership, discovery facilitation, or AI workflow consulting.

**Tech stack:** Static HTML, CSS, JavaScript. Formspree for contact form. GitHub Pages.

**Live URL:** Local only — needs GitHub remote and Pages enabled.

**Revenue model:**
- AI Workflow Audit: $2,500 (one-time)
- Fractional AI Leadership: $4,000/month retainer

**Next milestone:** Push to GitHub. Enable Pages. Share URL with Aaron Patzalek for review.

---

## 5. Aaron Kramer Personal Brand Site

**What it does:** Personal brand site for Aaron Kramer. Positions Aaron as a senior PM, founder, and innovator. Includes background, projects, principles, and a contact section.

**Who it's for:** Potential clients, collaborators, and employers. Secondary audience: journalists and grant reviewers.

**Tech stack:** Static HTML, CSS, JavaScript. GitHub Pages.

**Live URL:** https://twobirds-kramerica.github.io/aaron-kramer/

**Revenue model:** No direct revenue. Supports consulting and DCC outreach credibility.

**Next milestone:** Add Google Search Console verification. Link from DCC and Two Birds Innovation site.

---

## 6. Two Birds Innovation Site

**What it does:** Company website for Two Birds Innovation. Showcases all products, mission, values, blog, and contact. Single-page deep space design.

**Who it's for:** Prospective B2B partners, grant reviewers, and anyone who needs to understand who Two Birds Innovation is.

**Tech stack:** Static HTML, CSS, JavaScript. Formspree for contact. GitHub Pages.

**Live URL:** Local only — needs GitHub remote (A12 action item).

**Revenue model:** No direct revenue. Brand credibility and conversion funnel for DCC and consulting.

**Next milestone:** Aaron creates GitHub repo. Push via Claude Code. Enable Pages. Submit to Google Search Console.

---

## 7. Kevin's Apartment Search

**What it does:** A personalised apartment-hunting dashboard for a specific user (Kevin). Shows active listings with neighbourhood safety ratings, transit proximity, pet policy, and notes. AI insights powered by Anthropic API.

**Who it's for:** One user (Kevin). Private, not public-facing.

**Tech stack:** Static HTML, CSS, JavaScript. JSON data file for listings. GitHub Actions for automated listing checks. GitHub Pages.

**Live URL:** https://twobirds-kramerica.github.io/kevins-apartment-search/

**Revenue model:** None. Personal project.

**Next milestone:** No active work queued. Monitor for new listing requests from Kevin.

---

*Two Birds Innovation | St. Thomas, Ontario | March 2026*
