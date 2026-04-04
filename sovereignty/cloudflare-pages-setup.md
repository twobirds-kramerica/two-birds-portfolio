# Cloudflare Pages Setup — Backup Static Hosting

**Purpose:** Deploy GitHub Pages sites to Cloudflare Pages as a backup hosting layer.
**Date:** April 4, 2026
**Priority repos:** digital-confidence, two-birds-innovation, clarity

---

## Step-by-Step for Each Repo

### 1. Log into Cloudflare
Go to [dash.cloudflare.com](https://dash.cloudflare.com) and sign in (or create a free account).

### 2. Create a Pages Project
- Click **Workers & Pages** in the left sidebar
- Click **Create** → **Pages** → **Connect to Git**
- Authorise GitHub if prompted
- Select `twobirds-kramerica/digital-confidence`

### 3. Configure Build Settings
- **Project name:** `digital-confidence` (auto-suggested)
- **Production branch:** `main`
- **Build command:** (leave blank — static site, no build step)
- **Build output directory:** `/` (root)
- Click **Save and Deploy**

### 4. Verify
After deploy completes (1-2 min), your site is live at:
`digital-confidence.pages.dev`

### 5. Repeat for Other Repos

| Repo | Branch | Cloudflare Pages URL |
|------|--------|---------------------|
| digital-confidence | main | digital-confidence.pages.dev |
| two-birds-innovation | master | two-birds-innovation.pages.dev |
| clarity | master | clarity.pages.dev |
| career-coach | main | career-coach.pages.dev |
| aaron-patzalek | master | aaron-patzalek.pages.dev |

---

## Auto-Sync

Once connected, Cloudflare Pages **automatically deploys** on every push to the production branch. No additional configuration needed. Both GitHub Pages and Cloudflare Pages stay in sync automatically.

---

## DNS Switch (If GitHub Pages Goes Down)

If you need to switch your primary domain to Cloudflare Pages:

1. Go to Cloudflare Pages → your project → **Custom domains**
2. Add your domain (e.g., `digitalconfidence.ca`)
3. Cloudflare will provide DNS records to add
4. Update your domain registrar's DNS to point to Cloudflare
5. SSL is automatic — no certificate configuration needed

**Without a custom domain:** Simply share the `.pages.dev` URL as the temporary location while GitHub is down.

---

## Estimated Time

| Task | Time |
|------|------|
| Set up first repo (DCC) | 10 min |
| Each additional repo | 5 min |
| All 5 priority repos | 30 min total |

---

## Verification Checklist

- [ ] digital-confidence.pages.dev loads correctly
- [ ] two-birds-innovation.pages.dev loads correctly
- [ ] clarity.pages.dev loads correctly
- [ ] career-coach.pages.dev loads correctly
- [ ] aaron-patzalek.pages.dev loads correctly
- [ ] Push a change to GitHub → verify Cloudflare Pages auto-deploys
