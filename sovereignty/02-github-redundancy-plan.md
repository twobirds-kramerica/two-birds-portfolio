# 02 — GitHub Redundancy Plan

**Date:** April 1, 2026
**Objective:** Ensure all source code and live deployments survive a GitHub outage, account compromise, or policy change.

---

## Current State

- **10 repositories** on github.com/twobirds-kramerica
- **5 live products** deployed via GitHub Pages
- **1 owner account** (aaron.patzalek@gmail.com) — single point of failure
- **No mirrors** anywhere

---

## Step 1: Create Codeberg Mirror (30 minutes)

Codeberg is a free, open-source, git-compatible hosting platform run by a German non-profit. No vendor lock-in. No acquisition risk.

### Setup

1. Go to [codeberg.org](https://codeberg.org) and create an account
   - Username: `twobirds` or `aaronpatzalek`
   - Email: aaron.patzalek@gmail.com
2. Create an organisation: `twobirds-innovation`
3. For each repo, create a mirror:

```bash
# One-time setup per repo — run from C:\twobirds\
cd digital-confidence
git remote add codeberg https://codeberg.org/twobirds-innovation/digital-confidence.git
git push codeberg master --all

cd ../career-coach
git remote add codeberg https://codeberg.org/twobirds-innovation/career-coach.git
git push codeberg master --all

cd ../clarity
git remote add codeberg https://codeberg.org/twobirds-innovation/clarity.git
git push codeberg master --all
```

4. Repeat for remaining repos as time allows. Priority order:
   - digital-confidence (revenue product, 241 pages)
   - career-coach (revenue product)
   - clarity (revenue product)
   - two-birds-portfolio (business intelligence)
   - two-birds-command-centre (operations)
   - aaron-patzalek (personal brand)
   - two-birds-innovation (company site)
   - kevins-apartment-search (portfolio piece)
   - quality-dashboard (internal)
   - elite-karate-site (client project)

### Ongoing Sync

Add to the overnight build script (`run-overnight-build.bat`):

```batch
REM Mirror to Codeberg
cd /d C:\twobirds\digital-confidence
git push codeberg master 2>>C:\twobirds\two-birds-portfolio\logs\codeberg-sync.log
cd /d C:\twobirds\career-coach
git push codeberg master 2>>C:\twobirds\two-birds-portfolio\logs\codeberg-sync.log
cd /d C:\twobirds\clarity
git push codeberg master 2>>C:\twobirds\two-birds-portfolio\logs\codeberg-sync.log
```

---

## Step 2: Cloudflare Pages as Deployment Backup (45 minutes)

Cloudflare Pages is a free static site host. It connects to a git repo and auto-deploys on push. This replaces GitHub Pages if GitHub goes down.

### Setup for DCC (Primary Revenue Product)

1. Log into [dash.cloudflare.com](https://dash.cloudflare.com)
2. Go to **Workers & Pages → Create → Pages → Connect to Git**
3. Select `twobirds-kramerica/digital-confidence`
4. Build settings:
   - Build command: (leave blank — static site)
   - Build output directory: `/` (root)
5. Deploy

The site will be available at: `digital-confidence.pages.dev`

### Custom Domain (Optional)

If Aaron owns `digitalconfidence.ca` or `twobirds.ca`:
1. In Cloudflare Pages → Custom domains → Add
2. Point DNS CNAME to the Pages URL
3. SSL is automatic

### Repeat for Other Products

| Product | Repo | Cloudflare Pages URL |
|---------|------|---------------------|
| DCC | digital-confidence | digital-confidence.pages.dev |
| Career Coach | career-coach | career-coach.pages.dev |
| Clarity | clarity | clarity.pages.dev |
| Aaron Patzalek | aaron-patzalek | aaron-patzalek.pages.dev |
| Two Birds | two-birds-innovation | two-birds-innovation.pages.dev |

---

## Step 3: Backup Owner Account (10 minutes)

**This is a human task — Aaron must do this manually.**

1. Create second GitHub account: `twobirdsinnovation@gmail.com`
2. Go to github.com/twobirds-kramerica → Settings → Members
3. Invite backup account as **Owner**
4. Store credentials in password manager
5. Enable 2FA on backup account

---

## Step 4: Local Backup Script (5 minutes)

All repos are already cloned to `C:\twobirds\`. This is a natural backup. To make it explicit:

```batch
REM Weekly full backup to external drive (if available)
robocopy C:\twobirds\ D:\backup\twobirds\ /MIR /XD node_modules .git
```

---

## Verification Checklist

- [ ] Codeberg account created
- [ ] Top 3 repos mirrored to Codeberg
- [ ] Codeberg sync added to overnight build script
- [ ] Cloudflare Pages set up for DCC
- [ ] Backup GitHub owner account created
- [ ] All credentials stored in password manager

---

## Emergency Playbook: GitHub Goes Down

1. **Immediately:** All code is on local machine at `C:\twobirds\`
2. **Within 1 hour:** Push all repos to Codeberg mirrors
3. **Within 4 hours:** Activate Cloudflare Pages deployments
4. **Within 24 hours:** Update any DNS records pointing to github.io
5. **Within 7 days:** Migrate all issues, CI, and automation to Codeberg or alternative

Total downtime for live products: **under 4 hours** if Cloudflare Pages is pre-configured.
