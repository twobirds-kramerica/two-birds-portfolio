# Security Audit Results — All Two Birds Repos

**Date:** April 4, 2026
**Scope:** All 10 repositories under twobirds-kramerica
**Auditor:** Claude Code (automated scan)

---

## Scan Methodology

Searched all `.html`, `.js`, `.md`, `.json`, and config files for:
- `sk-ant-*` (Anthropic API keys)
- `AIza*` (Google API keys)
- `api_key`, `apikey`, `API_KEY`, `token`, `secret` followed by a string value of 15+ characters
- `PIXABAY`, `PEXELS`, `googleapis.*key=`
- Any hardcoded credential patterns

---

## Findings Summary

| Severity | Count | Action |
|----------|-------|--------|
| CRITICAL | 0 | — |
| HIGH | 0 | — |
| MEDIUM | 2 | Documented, no removal needed |
| LOW | 5 | Documented, no action needed |

**No Anthropic API keys found in any repository.** Both Career Coach and Clarity correctly use `localStorage.getItem()` for user-entered API keys at runtime — keys are never in source code.

---

## Detailed Findings

### Finding 1 — Google Maps Embed API Key
- **File:** `kevins-apartment-search/index.html:1293`
- **Also in:** `aaron-patzalek/patches/kevins-apartment-index.html:1293`
- **Value:** `AIzaSyD-9tSrke72PluDDL6lhVQcj5PJnO6pWQA`
- **Severity:** MEDIUM
- **Assessment:** Google Maps Embed API keys are designed to be in client-side HTML — they must be in the URL for the embed to work. However, this key should be **referrer-restricted** in the Google Cloud Console to only allow requests from `*.github.io` and `localhost`. Without referrer restriction, anyone can use Aaron's key and accumulate API charges.
- **Action required:** Aaron should log into Google Cloud Console → APIs & Services → Credentials → edit this key → add HTTP referrer restrictions: `*.twobirds-kramerica.github.io/*` and `localhost:*`
- **Code removal:** Not applicable — Maps Embed API requires the key in the URL.

### Finding 2 — Web3Forms Access Key
- **File:** `digital-confidence/js/feedback-github.js:647`
- **Value:** `5e0ecf7e-fb33-4541-be2e-1938bce868f4`
- **Severity:** MEDIUM
- **Assessment:** Web3Forms access keys are explicitly designed for client-side use. Their docs state the key goes in frontend code. The key is rate-limited and spam-filtered by Web3Forms. Not a credential leak.
- **Action required:** None. This is working as designed.

### Finding 3 — Formspree Form ID
- **Files:** `digital-confidence/js/feedback-github.js:13`, `js/email-capture.js:24`, `js/setup-wizard.js:475`
- **Value:** `xeerqryj`
- **Severity:** LOW
- **Assessment:** Formspree form IDs are public identifiers, not secret keys. They're designed to be in frontend code. Rate-limited and spam-filtered.
- **Action required:** None.

### Finding 4 — Google Analytics Tracking ID
- **Files:** Multiple HTML files across DCC
- **Value:** `G-RPH5H5BM52`
- **Severity:** LOW
- **Assessment:** GA tracking IDs are always public. Consent-gated in all DCC pages.
- **Action required:** None.

### Finding 5 — Microsoft Clarity Placeholder
- **Files:** Multiple HTML files across DCC
- **Value:** `CLARITY_PROJECT_ID` (placeholder string, not a real key)
- **Severity:** LOW
- **Assessment:** Not a real key — it's a placeholder. No Clarity project has been connected.
- **Action required:** None until Clarity is configured.

### Finding 6 — GitHub Token Placeholder in Docs
- **File:** `digital-confidence/GITHUB-SETUP.md:32`
- **Value:** `github_pat_YOUR_TOKEN_HERE` (placeholder)
- **Severity:** LOW
- **Assessment:** Documentation placeholder only. No real token.
- **Action required:** None.

### Finding 7 — LLM Provider Gemini URL Pattern
- **Files:** `career-coach/llm-provider.js:59`, `clarity/llm-provider.js:59`
- **Value:** URL template that appends `apiKey` from localStorage at runtime
- **Severity:** LOW
- **Assessment:** The key is read from localStorage at runtime, not hardcoded. This is correct behaviour.
- **Action required:** None.

---

## Preventive Measures Applied

### .gitignore Updated (All 10 Repos)
Added to every repository's `.gitignore`:
```
# Environment files
.env
.env.local
.env.production
```

### .env Template Created
`C:\twobirds\.env` created with empty key structure:
```
ANTHROPIC_API_KEY=
PIXABAY_API_KEY=
PEXELS_API_KEY=
```
This file is not tracked by any repo.

### Architecture Note
All Two Birds products are **static HTML/CSS/JS** deployed via GitHub Pages. There is no server-side code, no Node.js, no build process. API keys are entered by users at runtime and stored in `localStorage`. This is a fundamentally different security model from server-side applications — the attack surface is limited to:
1. Keys that must be in client-side HTML (Google Maps Embed) — mitigated by referrer restriction
2. Public service identifiers (Formspree, GA, Web3Forms) — public by design

---

## Recommendations

| Priority | Action | Owner | Effort |
|----------|--------|-------|--------|
| P1 | Restrict Google Maps API key to `*.github.io` referrers | Aaron | 5 min |
| P2 | Configure Microsoft Clarity if needed, or remove placeholder code | Aaron | 10 min |
| P3 | Review Web3Forms usage monthly for spam | Aaron | 5 min/month |

---

## Next Audit

**Schedule:** Monthly, first week of each month. Run the same grep patterns across all repos. Add any new repos created since last audit.
