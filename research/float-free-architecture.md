# Float Free Architecture — Vendor Independence Audit

**Prepared for:** Aaron Patzalek, Two Birds Innovation
**Date:** April 4, 2026
**Doctrine:** "Float with freedom 100%" — if any vendor disappeared or tripled their price tomorrow, Two Birds floats free within 24 hours.

---

## Section 1 — Current Vendor Map

| Vendor | What We Use It For | Monthly Cost | Lock-in Risk | What Breaks If Gone | Free Alternative | Migration (hrs) |
|--------|-------------------|-------------|-------------|---------------------|-----------------|----------------|
| **Anthropic** | Claude API (Career Coach, Clarity), Claude Code CLI, claude.ai Max | CA$142.80 | High | AI features in 2 products stop, coding velocity drops | Gemini (free 1M tokens), Ollama (local) | 2 hrs |
| **GitHub** | 10 repos, Pages hosting, Actions CI | Free | Critical | All code hosting + all live sites go dark | Codeberg (free), Gitea (self-hosted) | 4 hrs |
| **Google** | Maps Embed API (Kevin's), Gmail, Analytics (GA4) | Free | Medium | Maps in Kevin's break, email disrupted, analytics stop | OpenStreetMap, ProtonMail, Plausible | 3 hrs |
| **Cloudflare** | CDN for DCC, DNS (if configured) | Free | Low | CDN layer removed, minor perf hit | Direct GitHub Pages, Fastly free tier | 1 hr |
| **Formspree** | DCC feedback form submissions | Free (50/mo) | Low | Feedback forms stop submitting | Web3Forms (already active), Formgrid | 15 min |
| **Web3Forms** | DCC backup form submissions | Free (250/mo) | Low | Backup form path stops | Formgrid, n8n webhook | 15 min |
| **Pexels/Pixabay** | Image sourcing (not runtime) | Free | None | No runtime impact — images already downloaded | Unsplash, local photos | 0 hrs |
| **Windows/Microsoft** | i5 machine OS, Task Scheduler | Owned | Low | Overnight builds stop | Linux (Ubuntu) + cron | 4 hrs |
| **n8n** | Local automation (planned) | Free (self-hosted) | None | Automation stops — manual workaround available | Cron + shell scripts | 2 hrs |
| **LastPass** | Secrets management | Free/Paid | Medium | Credential access disrupted | Bitwarden (free, open-source) | 1 hr |

---

## Section 2 — Three Backup Layers

### AI / LLM

| Layer | Provider | Cost | Quality | Setup |
|-------|----------|------|---------|-------|
| **L1 (Primary)** | Anthropic Claude | CA$142.80/mo (Max) or pay-per-token | Excellent | Current |
| **L2 (Free corporate)** | Google AI Studio (Gemini 2.5 Flash) | Free — 1M tokens/min | Very good | `llmSetProvider('gemini', key)` |
| **L3 (Self-hosted)** | Ollama + Llama 3 (local) | CA$0 — runs on i5 | Good (slower) | `ollama pull llama3 && llmSetProvider('ollama')` |
| **L4 (Build own)** | Fine-tune open model on Two Birds data | CA$0–$100 | Unknown | Not needed — L2/L3 are sufficient |

**Switch procedure:** Change one line in `llm-provider.js`: `llmSetProvider('gemini', key)` or `llmSetProvider('ollama')`. Already built and ready.

### Code Hosting

| Layer | Provider | Cost | Capacity | Setup |
|-------|----------|------|----------|-------|
| **L1 (Primary)** | GitHub | Free | Unlimited public repos | Current |
| **L2 (Free corporate)** | [Codeberg](https://codeberg.org) | Free (non-profit, open-source) | Unlimited repos | `git remote add codeberg [url] && git push codeberg` |
| **L3 (Self-hosted)** | [Gitea](https://gitea.io) on home desktop | Free | Limited by disk | Docker install, 30 min setup |
| **L4 (Build own)** | Raw file server + SSH | Free | Bare minimum | Not recommended |

**Switch procedure:** All code is already on `C:\twobirds\`. Push to Codeberg. Update remotes. Done.

### Static Hosting

| Layer | Provider | Cost | Performance | Setup |
|-------|----------|------|------------|-------|
| **L1 (Primary)** | GitHub Pages | Free | Good (CDN cached) | Current |
| **L2 (Free corporate)** | [Cloudflare Pages](https://pages.cloudflare.com) | Free — unlimited bandwidth | Excellent (300+ edge locations) | Connect repo, auto-deploy |
| **L3 (Self-hosted)** | [Caddy](https://caddyserver.com) on home desktop + Cloudflare Tunnel | Free | Depends on internet | 1 hr setup |
| **L4 (Build own)** | Python `http.server` + tunnel | Free | Poor | Emergency only |

**Other free options:** Netlify (100GB/mo free), Render (free static), DigitalOcean App Platform (3 free static sites).

### Form Handling

| Layer | Provider | Cost | Limit | Setup |
|-------|----------|------|-------|-------|
| **L1 (Primary)** | Formspree | Free | 50 submissions/mo | Current |
| **L2 (Backup)** | Web3Forms | Free | 250 submissions/mo | Current (already active) |
| **L3 (Self-hosted)** | [Formgrid](https://formgrid.dev) (Docker) or n8n webhook | Free | Unlimited | 1 hr Docker setup |
| **L4 (Build own)** | n8n receives POST → saves to SQLite | Free | Unlimited | 30 min workflow build |

### Secrets Management

| Layer | Provider | Cost | Security | Setup |
|-------|----------|------|----------|-------|
| **L1 (Primary)** | LastPass | Free/Paid | Good (breached 2022) | Current |
| **L2 (Free corporate)** | [Bitwarden](https://bitwarden.com) | Free (unlimited devices) | Excellent (open-source, never breached) | 15 min import |
| **L3 (Self-hosted)** | [Vaultwarden](https://github.com/dani-garcia/vaultwarden) (Docker) | Free | Maximum control | 1 hr Docker setup |
| **L4 (Build own)** | GPG-encrypted local file | Free | Depends on practice | 10 min |

**Recommendation:** Switch primary to Bitwarden immediately. Open-source, never breached, free plan includes unlimited devices (LastPass restricts to one device type on free). Export from LastPass → import to Bitwarden takes 15 minutes.

### Email / Communications

| Layer | Provider | Cost | Features | Setup |
|-------|----------|------|----------|-------|
| **L1 (Primary)** | Gmail | Free | Full suite, MCP integration | Current |
| **L2 (Free corporate)** | [ProtonMail](https://proton.me) | Free (1GB) or CA$5/mo | E2E encrypted, Swiss privacy | 30 min setup |
| **L3 (Self-hosted)** | [Mailcow](https://mailcow.email) (Docker) | Free (needs domain + server) | Full control | 4+ hrs (not recommended for solo) |
| **L4 (Build own)** | Not needed — email is commodity | — | — | — |

### Automation

| Layer | Provider | Cost | Capability | Setup |
|-------|----------|------|-----------|-------|
| **L1 (Primary)** | n8n (local, planned) | Free | Visual workflows, 400+ integrations | 30 min install |
| **L2 (Backup)** | Windows Task Scheduler + .bat scripts | Free | Basic but reliable | Current |
| **L3 (Self-hosted)** | Cron (Linux) + shell scripts | Free | Universal, simple | 15 min per job |
| **L4 (Build own)** | Python scheduled scripts | Free | Full flexibility | Per-script |

---

## Section 3 — The 24-Hour Escape Plan

### If Anthropic Disappeared at 9 AM

By 9 AM tomorrow:
1. Open Career Coach `llm-provider.js` → change `localStorage.setItem('llm_provider', 'gemini')` (5 min)
2. Same for Clarity (5 min)
3. Get free Gemini API key from [ai.google.dev](https://ai.google.dev) (10 min)
4. Test both products with Gemini (15 min)
5. Update overnight build script to use Aider or Continue.dev instead of Claude Code (30 min)
6. All products running, all users unaffected. **Total: 1 hour.**

### If GitHub Disappeared at 9 AM

By 9 AM tomorrow:
1. All code is on `C:\twobirds\` — nothing lost (0 min)
2. Create Codeberg account at codeberg.org (5 min)
3. Create organisation `twobirds-innovation` (2 min)
4. For each repo: `git remote add codeberg https://codeberg.org/twobirds-innovation/[repo].git && git push codeberg --all` (30 min for 10 repos)
5. Set up Cloudflare Pages for DCC, Career Coach, Clarity (45 min)
6. Update DNS if custom domains exist (15 min)
7. All code hosted, all sites live. **Total: 2 hours.**

### If Google Disappeared at 9 AM

By 9 AM tomorrow:
1. Kevin's Maps embed: replace with OpenStreetMap iframe (15 min)
2. Gmail: set up forwarding to ProtonMail (20 min, need ProtonMail account)
3. GA4: remove tracking scripts or switch to [Plausible](https://plausible.io) (30 min)
4. Notify contacts of new email (ongoing)
5. Core functionality restored. **Total: 1 hour** (email migration ongoing).

### If Cloudflare Disappeared at 9 AM

By 9 AM tomorrow:
1. DCC is hosted on GitHub Pages — Cloudflare is only CDN layer (0 min impact)
2. If DNS was through Cloudflare: update nameservers at registrar to point directly to GitHub Pages (30 min)
3. Minor performance decrease, no functional impact. **Total: 30 minutes.**

### If Formspree Disappeared at 9 AM

By 9 AM tomorrow:
1. Web3Forms is already active as backup — forms auto-fail-over (0 min)
2. Update `DC_FORMSPREE_ENDPOINT` in `js/feedback-github.js` to point to Web3Forms as primary (5 min)
3. **Total: 5 minutes.** Already mitigated.

### If LastPass Disappeared at 9 AM

By 9 AM tomorrow:
1. Export vault from LastPass (if still accessible) or use cached local data (10 min)
2. Import to Bitwarden (10 min)
3. Update browser extension (5 min)
4. **Total: 25 minutes.**

---

## Section 4 — Float Free Scorecard

### Current Score: 48/100

| Category | Current | Max | Status |
|----------|---------|-----|--------|
| Code Independence | 10 | 20 | 🟡 Amber — GitHub only, no mirror |
| Hosting Independence | 5 | 20 | 🔴 Red — single provider |
| AI Independence | 15 | 20 | 🟢 Green — portability layer built |
| Secrets Independence | 10 | 15 | 🟡 Amber — .env done, no backup vault |
| Automation Independence | 5 | 15 | 🔴 Red — Task Scheduler only |
| Forms Independence | 6 | 10 | 🟢 Green — dual provider |
| **Total** | **48** | **100** | **🟡 Amber** |

### Target Scores with Each Layer

| Action | Effort | Cost | Score Gain | New Total |
|--------|--------|------|-----------|-----------|
| Codeberg mirror (all repos) | 1 hr | $0 | +5 | 53 |
| Document self-hosted git (Gitea) | 30 min | $0 | +5 | 58 |
| Cloudflare Pages for top 3 | 1 hr | $0 | +10 | 68 |
| Document Caddy self-hosted | 30 min | $0 | +5 | 73 |
| Test OpenAI fallback | 30 min | $0 | +5 | 78 |
| Switch to Bitwarden | 30 min | $0 | +5 | 83 |
| Install n8n | 30 min | $0 | +5 | 88 |
| Document cron backup | 15 min | $0 | +5 | 93 |
| n8n form webhook | 30 min | $0 | +4 | 97 |

**Path to 80+: 4 hours of work, CA$0 cost.**
**Path to 97: 6 hours of work, CA$0 cost.**

---

## Section 5 — Implementation Roadmap

### Week 1 (April 4-10) — Quick Wins (+30 points)
| Day | Action | Effort | Gain |
|-----|--------|--------|------|
| Fri | Set up Codeberg account, mirror top 3 repos | 🧠 30 min | +5 |
| Sat | Connect Cloudflare Pages to DCC | 🧠 20 min | +5 |
| Sun | Connect Cloudflare Pages to Career Coach + Clarity | 🧠 20 min | +5 |
| Mon | Switch LastPass → Bitwarden | 🧠 30 min | +5 |
| Tue | Test Gemini as OpenAI fallback in Career Coach | 🧠 30 min | +5 |
| Wed | Document self-hosted git + Caddy options | Claude Code 30 min | +10 |

**Week 1 target: 78/100**

### Week 2 (April 11-17) — Automation Layer (+15 points)
| Day | Action | Effort | Gain |
|-----|--------|--------|------|
| Fri | Install n8n on i5 | 🧠 30 min | +5 |
| Sat | Document cron backup procedures | Claude Code 15 min | +5 |
| Sun | Build n8n form webhook as Formspree L3 backup | 🧠 30 min | +4 |
| Mon | Mirror remaining 7 repos to Codeberg | 🧠 30 min | +0 (already counted) |

**Week 2 target: 93/100**

### Month 2+ — Maintain and Review
- Quarterly sovereignty audit (next: July 4, 2026)
- Test one escape plan end-to-end each quarter
- Update scorecard after each implementation

---

## Sources
- [Free LLM APIs 2026](https://www.analyticsvidhya.com/blog/2026/01/top-free-llm-apis/)
- [Ollama Alternatives](https://localllm.in/blog/complete-guide-ollama-alternatives)
- [Free Static Hosting](https://appwrite.io/blog/post/best-free-static-website-hosting)
- [Formspree Alternatives 2026](https://formgrid.dev/blog/formspree-alternatives-in-2026-open-source-cheaper-and-self-hostable)
- [Bitwarden vs LastPass 2026](https://cybernews.com/best-password-managers/bitwarden-vs-lastpass/)
- [Cloudflare Pages](https://pages.cloudflare.com)
- [Codeberg](https://codeberg.org)
