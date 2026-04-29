# Retro
Last updated: 2026-04-28 at 21:30 EST (Toronto)
Sessions covered: 2026-04-23 through 2026-04-28

---

## 2026-04-23/24 — Security Cleanup Sprint

**Trigger:** Portfolio security audit revealed `kevins-apartment-search` was public despite tracking Kevin Burnett's actual apartment shortlist.

### What shipped
- `kevins-apartment-search` flipped private (`gh repo edit --visibility private`)
- `aaron-patzalek/patches/kevins-apartment-index.html` deleted (2,780 deletions — Kevin's private data in a public sibling repo)
- REPO VISIBILITY RULE added to CLAUDE.md: any repo with real user data must be private by default, public is opt-in
- Commits: `65aad2f`, `abd5c7b`

### Side-effect
Kevin's GitHub Pages went 404 — Pages-on-private requires Pro tier. Three options documented in `hal-stack/sprint-system/security-cleanup-output.md`: (a) accept downtime, (b) re-host on Cloudflare/Netlify, (c) upgrade plan. Aaron's decision pending.

---

## 2026-04-25 ~10:50 EST — Portfolio CI workflow (P1 sprint)

**Trigger:** Aaron directive; P1 Notion item `34aa09cf-876a-8136-8985-eb72e4d4a290` was In Progress from a prior session.

### What shipped
- `.github/workflows/ci.yml` added to `two-birds-portfolio` (229 lines)
  - Job 1 — axe-core: WCAG 2.0/2.1 A/AA scan of all HTML files on every push/PR; fails on critical violations
  - Job 2 — link-check: scans 11 sibling Two Birds URLs + Notion API + GitHub raw CLAUDE.md; opens issue on weekly broken-link run
- Notion sprint flipped In Progress → Done
- 5 Aaron P1 decisions backlogged to Notion (Kevin site, Google Maps API key, DCC v2 eval, Calendly URL, LinkedIn URL for TBI)
- Commits: `3ca1bf2` (ci.yml), `eaafa95` (SESSION-STATE), `dd91a4b` (printf fix for BROKEN/OK strings starting with `-`)

---

## 2026-04-28 21:24 EST — S-GITLEAKS (just-go sprint)

**Trigger:** Notion exit 3 twice; Aaron typed `just go` after queue-empty report.

### What shipped
- gitleaks/gitleaks-action@v2 added as Job 3 to `ci.yml`
- Full git-history scan (`fetch-depth: 0`) on every push/PR; fails build on any committed secret
- Workflow renamed: `CI (axe-core + link checker + gitleaks)`
- Notion entry filed as Done: `351a09cf-876a-8119-8fad-f35b8771341e`
- Commits: `1184ef8` (gitleaks job), `7c18242` (SESSION-STATE)

---

## 2026-04-28 — CLAUDE.md token audit + trim (this session)

### What shipped
- RETRO.md overwritten (this file)
- CLAUDE.md trimmed from ~2,300 tokens to <500 tokens
- Three new governance pointer files created: `hal-stack/governance/rules.md`, `hal-stack/governance/engagement-rules.md`, `hal-stack/governance/backlog-format.md`

---

## What needs Aaron

- **Kevin site** — pick option (a) accept downtime / (b) re-host / (c) upgrade GitHub Pro
- **Google Maps API key** — add HTTP referrer restrictions in Google Cloud Console
- **DCC v2 wizard POC** — evaluate at `/v2/` and decide: replace long-scroll / coexist / revert
- **Calendly URL** — required to wire mailto → Calendly on Clarity + TBI CTAs (P1 revenue move)
- **LinkedIn URL** — required to add to TBI contact section
- **DCC Kids Research DB rows** — 12 rows waiting for Research → Spec status advance (see `aaron-todos-2026-04-21.md`)

## How to resume

1. `state` — reads SESSION-STATE.md for full context
2. `next sprint` — Notion first; exit 3 fall back to sprint-queue.md
3. Human todos: `hal-stack/sprint-system/aaron-todos-2026-04-21.md`

Last updated: 2026-04-28 at 21:30 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.
