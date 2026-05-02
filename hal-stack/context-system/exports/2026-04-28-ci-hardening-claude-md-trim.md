# CI Hardening + CLAUDE.md Token Audit

## Session Metadata

| Field | Value |
|-------|-------|
| **Date** | 2026-04-25 + 2026-04-28 (two short sessions, combined here) |
| **Title** | Portfolio CI hardening (axe-core + link-check + gitleaks) + CLAUDE.md trimmed 80% |
| **Project** | HAL Stack / Portfolio |
| **Layer** | L1 |
| **Tool** | Claude Code CLI |
| **Machine** | EZbook (assumed) |
| **Duration** | ~45 min total across both sessions |

## Decisions Made

| Decision | Confidence | Reversible? | Notes |
|----------|-----------|-------------|-------|
| Add axe-core + link-check CI to portfolio repo | High | Yes | Mirrors pattern from digital-confidence and clarity. Fails build on critical WCAG violations only; serious/moderate reported in summary. Weekly link-check opens GitHub issue on broken URLs. |
| Add gitleaks as Job 3 to portfolio ci.yml | High | Yes | `gitleaks/gitleaks-action@v2`, full history scan (`fetch-depth: 0`), fails build on committed secrets. No GITLEAKS_LICENSE needed for public repo. First run establishes clean baseline. |
| Trim CLAUDE.md from ~2,250 tokens to ~415 tokens | High | Yes (old content in governance files) | 5 non-negotiable rules stay inline. All governance rules, engagement rules, backlog format, personas, Notion sync details moved to pointer files. Every session now loads ~1,800 fewer tokens. |
| Create 3 new governance pointer files | High | Yes | `hal-stack/governance/rules.md` (governance), `hal-stack/governance/engagement-rules.md` (behavioural), `hal-stack/governance/backlog-format.md` (Notion item format). No rules deleted — all preserved. |
| Reject unknown plugin install (`mksglu/context-mode`) | High | N/A | No verified source provided. `/plugin marketplace add` is not a valid Claude Code command. Aaron agreed to skip. |

## Open Questions

- [ ] Has the first gitleaks CI run passed? (triggered on push of `1184ef8` — check Actions tab for result)
- [ ] Kevin site forward path — still undecided: (a) accept Pages downtime, (b) re-host Cloudflare/Netlify, (c) upgrade GitHub Pro
- [ ] Calendly URL — required before Clarity + TBI `mailto:` → Calendly conversion can ship
- [ ] DCC v2 wizard POC — Aaron evaluation at `/v2/` still pending (coexist / replace / revert decision)
- [ ] Google Maps API key — HTTP referrer restrictions needed in Google Cloud Console

## Next Actions

1. Open GitHub Actions tab on `twobirds-kramerica/two-birds-portfolio` and confirm the gitleaks job passed its first full-history scan
2. Provide Calendly URL so the `mailto:` → Calendly conversion can be executed on Clarity + TBI (P1 revenue move, ~30 min sprint)
3. Evaluate DCC v2 wizard at `https://twobirds-kramerica.github.io/digital-confidence/v2/` — click through module-1, test help overlay, test mobile width — and pick one of: replace / coexist / revert

## Artifacts Created

| File | Repo | Description |
|------|------|-------------|
| `.github/workflows/ci.yml` | two-birds-portfolio | 3-job CI: axe-core + link-check + gitleaks. Commit `3ca1bf2` + `dd91a4b` + `1184ef8` |
| `hal-stack/governance/rules.md` | two-birds-portfolio | All governance rules extracted from CLAUDE.md |
| `hal-stack/governance/engagement-rules.md` | two-birds-portfolio | Sparring Partner, Confidence %, N.B., Voice Check, Scrappy Pack rules |
| `hal-stack/governance/backlog-format.md` | two-birds-portfolio | Backlog item template + Notion helper signatures |
| `CLAUDE.md` (rewritten) | two-birds-portfolio | 45 lines, ~415 tokens. Was 227 lines, ~2,250 tokens. Commits `7094cd5` |
| `logs/RETRO.md` (overwritten) | two-birds-portfolio | Now covers 2026-04-23 through 2026-04-28. Was stale at April 21-22. |

## Key Context for Future Sessions

CLAUDE.md is now a 45-line orientation file — the 5 non-negotiable rules + trigger commands + key file pointers. All deeper rules live in `hal-stack/governance/`. If behavioural rules (Voice Check, Sparring Partner, Confidence %) seem to be missing from a session, read `hal-stack/governance/engagement-rules.md`. The portfolio now has 3-job CI (axe-core + link-check + gitleaks) running on every push; gitleaks baseline was established 2026-04-28 against the full ~97-commit history.
