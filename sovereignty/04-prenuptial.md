# 04 — Vendor Prenuptial Framework

**Date:** April 1, 2026
**Principle:** Use the best tools. Own the exit door.

---

## What Aaron Owns vs What Vendors Provide

### Aaron Owns (Permanently)
- All source code in all 10 repositories (git history is proof of authorship)
- All product architectures and designs
- All written content: DCC modules, journey narrative, email sequences, LinkedIn posts
- All prompt engineering work (EUREKA library, CLAUDE.md files, sprint definitions)
- All frameworks: trust-first design methodology, sovereignty doctrine, Brenda persona
- All brand assets: Two Birds Innovation name, >< symbol, motto
- All customer relationships and business intelligence
- All local copies of code on `C:\twobirds\`

### Vendors Provide (Replaceable)
- **Anthropic:** AI inference (API calls). Does not own prompts, outputs, or product logic.
- **GitHub:** Hosting and version control platform. Does not own the code — git is decentralised.
- **Cloudflare:** DNS routing and CDN. Does not own the domain or content.
- **Google:** Email delivery. Does not own contacts or correspondence (exportable via Takeout).
- **Formspree:** Form submission relay. Does not own feedback data (CSV exportable).

---

## Exit Triggers

Any of these events should activate the 24-hour checklist for the affected vendor:

| Trigger | Action |
|---------|--------|
| Price increase > 20% without notice | Begin migration evaluation |
| Terms of service change affecting IP ownership | Freeze new work on platform, consult lawyer |
| Acquisition by competitor or hostile entity | Begin 30-day migration |
| Service deprecation announced | Begin 30-day migration immediately |
| Data breach affecting Aaron's accounts | Rotate all credentials within 24 hours, evaluate continued use |
| Uptime drops below 95% over 30 days | Activate backup deployment, evaluate alternatives |
| Feature removal that breaks a live product | Patch with alternative, begin migration evaluation |

---

## 24-Hour Exit Checklist (Per Vendor)

When an exit trigger fires, complete these steps within 24 hours:

### Anthropic (API)
- [ ] Switch Clarity and Career Coach to backup provider (OpenAI or Ollama) using portability layer
- [ ] Verify both products work with new provider
- [ ] Update localStorage defaults on live sites
- [ ] Notify any active clients of temporary service change

### GitHub
- [ ] Verify all repos are current on local machine (`git pull` all)
- [ ] Push all repos to Codeberg mirrors
- [ ] Activate Cloudflare Pages deployments for all 5 live products
- [ ] Update DNS records if using custom domains
- [ ] Update all documentation references from github.io to new URLs

### Google (Gmail)
- [ ] Run Google Takeout: export contacts, email, calendar
- [ ] Set up forwarding to backup email address
- [ ] Update business cards, LinkedIn, and all public profiles with new email
- [ ] Notify active contacts of email change

### Cloudflare
- [ ] Export DNS zone file
- [ ] Move nameservers to registrar default or alternative (e.g., Namecheap DNS)
- [ ] Verify all sites resolve correctly

### Formspree
- [ ] Export all submissions as CSV
- [ ] Update `js/feedback-github.js` endpoint to Web3Forms (backup already configured)
- [ ] Test submission on DCC

---

## 30-Day Migration Playbook

For a full vendor exit (not just emergency patch):

### Week 1: Secure and Duplicate
- Export all data from the vendor
- Verify backups are complete and readable
- Set up accounts on replacement platform
- Test replacement with one non-critical product

### Week 2: Migrate Non-Critical
- Move internal tools (Command Centre, Quality Dashboard, Portfolio)
- Update all internal documentation and references
- Verify no broken links or references

### Week 3: Migrate Revenue Products
- Move DCC, Career Coach, Clarity to new platform
- Test all features end-to-end
- Update DNS and public URLs
- Monitor for errors for 48 hours

### Week 4: Clean Up
- Decommission old accounts (do not delete — archive)
- Update all external references (LinkedIn, email signatures, business cards)
- Document lessons learned in sovereignty audit
- Schedule 30-day review of new vendor

---

## Annual Vendor Review

**Schedule:** First week of January each year.

1. Re-run sovereignty audit (01-sovereignty-audit.md)
2. Verify all backups and mirrors are current
3. Test one migration path end-to-end (rotate which vendor each year)
4. Update cost tracking and risk ratings
5. Review any new vendor dependencies added during the year
