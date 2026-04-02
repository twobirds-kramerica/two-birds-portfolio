# 01 — Sovereignty Audit

**Date:** April 1, 2026
**Scope:** Every external vendor or platform Two Birds Innovation depends on.

---

## Vendor Dependency Map

### 1. Anthropic API (Claude)
- **What it does:** Powers AI features in Career Coach and Clarity. Claude API calls generate SWOT analyses, job recommendations, and diagnostic results.
- **Cost:** ~CA$20–50/month at current usage (pay-per-token). Could scale significantly with production traffic.
- **Risk:** **High**
  - Single point of failure for two revenue products.
  - No SLA for individual developers. Rate limits can change without notice.
  - Pricing has already changed once (March 2026 Max plan restructure).
- **Migration difficulty:** Medium — API is standard REST/JSON. Alternative LLMs (GPT-4o, Gemini, Ollama) accept similar payloads.
- **Recommended mitigation:**
  - Implement LLM portability layer (see [03-llm-portability-layer.md](03-llm-portability-layer.md))
  - Test Ollama locally for offline fallback
  - Keep monthly spend under CA$100 until revenue exceeds CA$2,000/month

### 2. GitHub (Code Hosting + GitHub Pages)
- **What it does:** Hosts all 10 repositories. GitHub Pages serves 5 live products (DCC, Career Coach, Clarity, Aaron Patzalek, Two Birds Innovation).
- **Cost:** Free (GitHub Free for organisations).
- **Risk:** **High**
  - All source code and all live deployments in one vendor.
  - Account compromise = total business loss.
  - GitHub Pages has no SLA for free tier.
  - Microsoft owns GitHub — acquisition risk is already realised.
- **Migration difficulty:** Low for code (git is portable). Medium for Pages (need alternative static hosting).
- **Recommended mitigation:**
  - Mirror repos to Codeberg (see [02-github-redundancy-plan.md](02-github-redundancy-plan.md))
  - Set up Cloudflare Pages as deployment backup
  - Create backup owner account (human task — already in backlog)

### 3. Claude Code CLI
- **What it does:** Primary development tool. All coding, commits, sprint execution, and automation run through Claude Code.
- **Cost:** Included in claude.ai Max plan (CA$142.80/month as of March 2026).
- **Risk:** **Medium**
  - High productivity dependency but not a production dependency.
  - If unavailable, Aaron can still code manually or use alternative AI coding tools.
  - CLI is a local tool — no data lock-in.
- **Migration difficulty:** Low — all output is standard files and git commits. Nothing proprietary stored in Claude Code.
- **Recommended mitigation:**
  - Keep CLAUDE.md files as documentation (they work for any AI tool with context)
  - Maintain sprint files as human-readable task lists
  - Test Cursor or Windsurf as backup coding environments quarterly

### 4. claude.ai Max Plan
- **What it does:** Provides Claude Code CLI access, Claude Web for research, and higher rate limits.
- **Cost:** CA$142.80/month (upgraded March 23, 2026).
- **Risk:** **Medium**
  - Price could increase. Plan could be restructured or discontinued.
  - Currently the single largest monthly expense.
- **Migration difficulty:** Low — downgrade to Pro (CA$28/month) or switch to API-only billing.
- **Recommended mitigation:**
  - Track monthly cost vs revenue ratio
  - If revenue < CA$500/month by July 2026, downgrade to Pro plan
  - API-only billing as fallback (pay-per-use, no monthly commitment)

### 5. Gmail (via Google Workspace / Free)
- **What it does:** Primary business email (aaron.patzalek@gmail.com). B2B outreach. Client communication.
- **Cost:** Free.
- **Risk:** **Low**
  - Google account compromise would disrupt communication but not destroy products.
  - Email is federated — can switch providers and keep receiving mail with custom domain.
- **Migration difficulty:** Low — standard IMAP/SMTP. Export via Google Takeout.
- **Recommended mitigation:**
  - Set up custom domain email (hello@twobirds.ca) when revenue justifies it
  - Enable 2FA (should already be active)
  - Monthly Google Takeout export of contacts and email

### 6. Gmail MCP (Claude Code Integration)
- **What it does:** Allows Claude Code to read and draft emails via MCP server.
- **Cost:** Free (part of Claude Code ecosystem).
- **Risk:** **Low**
  - Convenience feature only. Not production-critical.
  - If MCP breaks, Aaron drafts emails manually.
- **Migration difficulty:** N/A — no lock-in. MCP is a protocol, not a platform.
- **Recommended mitigation:**
  - No action needed. This is already portable by design.

### 7. Formspree (DCC Feedback Forms)
- **What it does:** Receives feedback form submissions from DCC. CORS-safe endpoint.
- **Cost:** Free tier (50 submissions/month).
- **Risk:** **Low**
  - Easy to replace. Web3Forms already configured as silent backup.
  - No data lock-in — CSV export available.
- **Migration difficulty:** Very Low — change one URL in js/feedback-github.js.
- **Recommended mitigation:**
  - Monthly CSV export (already in DCC CLAUDE.md backup policy)
  - Web3Forms backup already active

### 8. Cloudflare (DCC DNS + CDN)
- **What it does:** DNS management and CDN for Digital Confidence Centre.
- **Cost:** Free tier.
- **Risk:** **Low**
  - DNS is portable. Can switch registrar/nameservers in hours.
  - CDN is a performance layer, not a dependency.
- **Migration difficulty:** Low.
- **Recommended mitigation:**
  - Document DNS records in this repo
  - Keep domain registrar separate from CDN provider

---

## Risk Summary

| Vendor | Risk | Migration | Priority |
|--------|------|-----------|----------|
| Anthropic API | High | Medium | Immediate — build portability layer |
| GitHub | High | Low–Medium | This week — mirror + backup account |
| Claude Code CLI | Medium | Low | Quarterly — test alternatives |
| claude.ai Max | Medium | Low | Monitor — cost vs revenue |
| Gmail | Low | Low | When custom domain ready |
| Gmail MCP | Low | N/A | No action needed |
| Formspree | Low | Very Low | Already mitigated |
| Cloudflare | Low | Low | Document DNS records |

---

## Next Review Date

**May 1, 2026** — re-audit after first month of sovereignty measures in place.
