# Decapitation Checklist — GitHub (Repos + Pages)

**Component:** GitHub repos (#3) + GitHub Pages (#4)
**Story:** S1.1
**Current layer:** L1 (free tier)
**Risk:** LOW
**Last updated:** 2026-04-17

---

## What We Depend On

| Dependency | What It Does | Impact If Lost |
|-----------|-------------|----------------|
| GitHub repos (10) | Code hosting, version control, collaboration | None — git is distributed, every machine has full clones |
| GitHub Pages | Static site hosting for DCC, portfolio, TBI, etc. | Sites go offline until re-hosted elsewhere |
| GitHub Issues + Projects | Backlog tracking, sprint visibility | Lose dashboard but sprint-queue.md is the execution queue |
| GitHub Actions | Changelog auto-generation | Lose automation, can generate manually |

## Current Repos

| Repo | Has Local Clone? | Codeberg Mirror? | Pages Enabled? |
|------|-----------------|-----------------|----------------|
| two-birds-portfolio | YES (EZbook) | TODO | No |
| digital-confidence | YES (EZbook) | TODO | YES |
| aaron-patzalek | YES (EZbook) | TODO | TODO |
| career-coach | YES (EZbook) | TODO | YES |
| clarity | YES (EZbook) | TODO | YES |
| two-birds-innovation | YES (EZbook) | TODO | YES |
| kevins-apartment-search | YES (EZbook) | TODO | YES |
| quality-dashboard | YES (EZbook) | TODO | YES |
| two-birds-command-centre | YES (EZbook) | TODO | YES |
| elite-karate-site | YES (EZbook) | TODO | TODO |

## L2 Fallback — Codeberg

**Action plan (30 min, one-time):**
1. Create Codeberg account at codeberg.org
2. For each repo: `git remote add codeberg https://codeberg.org/twobirds/[repo].git`
3. Push all repos: `git push codeberg master`
4. Add to overnight build script: push to both GitHub and Codeberg

**Status:** Documented in `sovereignty/codeberg-status.md`. Remotes not yet added.

## L3 Fallback — Gitea on VPS

**Action plan (2-3 hours):**
1. Spin up a VPS (DigitalOcean, Hetzner, ~US$5/month)
2. Install Gitea (Docker or binary)
3. Push all repos
4. Update remotes

## L4 Fallback — Local Only

**Action plan (15 min):**
1. Every repo is already cloned locally
2. Sprint S-006 sets up Pentium Silver as pull-only mirror
3. Stop pushing — work continues offline

## GitHub Pages L2 — Cloudflare Pages

**Action plan per site (15 min):**
1. Log into Cloudflare dashboard
2. Add site → connect GitHub repo
3. Build settings: none (static files)
4. Update DNS CNAME to point to Cloudflare Pages URL

**Status:** Some sites partially configured. Needs verification.

## Emergency Procedure

If GitHub goes down or account is suspended:
1. All code is local — no data loss
2. Push to Codeberg (if mirrors set up): `git push codeberg master`
3. Re-host Pages on Cloudflare Pages or Netlify (15 min per site)
4. Update DNS if needed
5. Issues/Projects lost — sprint-queue.md is the backup

## Quarterly Drill Checklist

- [ ] Verify all 10 repos cloned locally with `git status`
- [ ] Push one repo to Codeberg mirror (confirm it works)
- [ ] Verify GitHub Pages sites load (spot-check 3)
- [ ] Confirm Cloudflare Pages fallback is configured for at least DCC
- [ ] Check that overnight build script includes dual push
