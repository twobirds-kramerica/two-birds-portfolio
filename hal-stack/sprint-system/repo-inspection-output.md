# Repo Inspection — 2026-04-23 (~00:45 EST)

**Scope:** all public repos under `twobirds-kramerica` GitHub org
**Tooling:** `gh` CLI v2.89.0 (available), `gitleaks` NOT installed (skipped — noted)
**Methodology:** `gh repo list` for inventory + local grep across cloned repos for credential patterns and Cloudflare-bypass libraries + cross-reference against the April 4 security audit (`research/security-audit-results.md`)

---

## Public repos found (13)

Every repo under `twobirds-kramerica` is PUBLIC. No private repos.

| Repo | Last updated | Description |
|---|---|---|
| `kevins-apartment-search` | 2026-04-23 | Kevin Burnett's apartment search tracker — London, ON |
| `two-birds-portfolio` | 2026-04-23 | Two Birds enterprise portfolio backlog and dashboard |
| `digital-confidence` | 2026-04-23 | DCC — seniors digital literacy flagship |
| `two-birds-project-template` | 2026-04-23 | Reusable project template with Claude Code guardrails |
| `two-birds-innovation` | 2026-04-23 | Company brand site |
| `clarity` | 2026-04-23 | AI business diagnostic for SMEs |
| `aaron-patzalek` | 2026-04-23 | Personal brand site |
| `two-birds-command-centre` | 2026-04-23 | Command centre dashboard for Two Birds projects |
| `quality-dashboard` | 2026-04-23 | Build health dashboard — automated repo quality checks |
| `career-coach` | 2026-04-23 | AI-powered job application coaching tool |
| `elite-karate-site` | 2026-04-04 | Kirk's Elite Karate Club (client, do-not-touch per CLAUDE.md) |
| `aaron-kramer` | 2026-04-01 | Aaron Kramer Personal Brand Site (legacy? unclear) |
| `TBK` | 2026-04-01 | Empty description (legacy? unclear) |

---

## kevins-apartment-search: PUBLIC

**This is the single most important finding.** The repo is public despite the site being marked `<meta name="robots" content="noindex, nofollow">` and described in the AUDIT as "private tool for Kevin Burnett." The `noindex` blocks search engines from indexing the LIVE SITE, but the GITHUB SOURCE CODE is discoverable by anyone who browses github.com/twobirds-kramerica.

Consequences of being public:
- All 16 apartment listings Kevin has been considering are visible in `data/listings.json` (addresses, prices, notes)
- Kevin's filter criteria (budget range, commute time, laundry needs, etc.) are visible in the code
- Any notes Aaron has added about specific landlords or listings are visible
- The Google Maps API key in the embed URL is visible (see next section)

---

## Credentials found

**One real finding (MEDIUM severity, first identified in the April 4 2026 security audit, still present as of this inspection):**

### Google Maps Embed API key exposed
- **File:** `kevins-apartment-search/index.html:273` (current line; audit said line 1293 in older state)
- **Also in:** `aaron-patzalek/patches/kevins-apartment-index.html:1291` (snapshot/patch copy)
- **Value:** `AIzaSyD-9tSrke72PluDDL6lhVQcj5PJnO6pWQA`
- **Context:** Google Maps Embed API URL `https://www.google.com/maps/embed/v1/search?key=...`

**Why it's MEDIUM, not CRITICAL:** Google Maps Embed API keys are designed for client-side use — they MUST appear in the URL for the embed to render. The risk is abuse if the key is not **referrer-restricted** in Google Cloud Console. Without restrictions, any stranger can copy this key and run unlimited API calls against Aaron's billing account.

**Action required (Aaron, not Claude Code):**
1. Log into Google Cloud Console → APIs & Services → Credentials
2. Find this key; edit restrictions
3. Add HTTP referrer restrictions:
   - `*.twobirds-kramerica.github.io/*`
   - `localhost:*` (for local testing)
4. No code change needed — the key has to stay in the URL for the embed to work

**Claude Code cannot do this step** — it's a Google Cloud Console permissions change that requires Aaron's Google account.

### All other credential-shaped patterns — verified as false positives or working-as-designed

From the April 4 audit, re-verified in this inspection:
- Web3Forms access key (`digital-confidence/js/feedback-github.js`): designed for client-side use, rate-limited, spam-filtered — working as designed
- Formspree form IDs: public identifiers by design — no action
- Google Analytics tracking ID (`G-RPH5H5BM52`): always public — no action
- Microsoft Clarity `CLARITY_PROJECT_ID`: placeholder string, no real Clarity project connected
- GitHub token in `digital-confidence/GITHUB-SETUP.md`: documentation placeholder `github_pat_YOUR_TOKEN_HERE` — no real token
- LLM provider URL patterns in `career-coach/llm-provider.js` + `clarity/llm-provider.js`: keys read from localStorage at runtime, not hardcoded — correct behaviour
- `career-coach/js/app.js` hits: `placeholder: 'sk-ant-...'` + `placeholder: 'sk-...'` are form placeholders showing users what their own key looks like — not hardcoded keys

### conversations.json (80MB Claude chat export)

Correctly gitignored at `hal-stack/context-system/ingestion/raw/` in `two-birds-portfolio/.gitignore:8`. The 80MB file exists on disk but is NOT tracked in git. Safe.

---

## Bypass libraries found: No

Scanned Kevin's repo for: `cloudscraper`, `undetected-chromedriver`, `playwright-stealth`, `puppeteer-extra-plugin-stealth`, `selenium-stealth`. **Zero matches.**

Kevin's repo DOES use `puppeteer` (v24.40.0 in `package-lock.json`) via `scripts/fetch-images.js` for scraping OG-image previews from listing URLs. This is standard Puppeteer, NOT any stealth/bypass variant. Standard Puppeteer identifies itself honestly in the User-Agent string and does not circumvent bot-detection.

Per Kevin's AUDIT §3, the scraper runs manually (`node scripts/fetch-images.js`), not on a schedule. Scope: pull OG image previews. Not bulk-scraping Realtor.ca or Zillow. Not violating anti-bot measures.

---

## Nontechnical visibility summary

**What a nontechnical person browsing `github.com/twobirds-kramerica/kevins-apartment-search` would see:** all the addresses, prices, and notes about the specific apartments Kevin has been shortlisting in London, Ontario, plus Kevin's personal filter criteria (budget ceiling, commute tolerance, etc.). They would also see Aaron's working Google Maps Embed API key, which could be copied and used (though the immediate consequence is billed to Aaron's Google Cloud account, not a data breach).

The SITE itself is marked noindex (search engines skip it), but the SOURCE CODE REPOSITORY is discoverable by name-search on GitHub or by browsing the `twobirds-kramerica` org page. There's no lock on the source code.

---

## Recommended actions

**Priority 1 (Aaron, 5 minutes each, can be done now):**

1. **Make `kevins-apartment-search` private OR rewrite the listings data to scrub identifying details.**
   - Private: GitHub settings → kevins-apartment-search → Danger Zone → Make private. GitHub Pages will still serve the site; the source just won't be discoverable.
   - Alternative: keep public but scrub `data/listings.json` of specific addresses/notes (treat the repo as a demo-of-capability rather than a real-data tracker).
2. **Add HTTP referrer restrictions to the Google Maps API key** in Google Cloud Console. See exact steps under "Credentials found" above. Without this, anyone can copy the key and burn Aaron's billing quota.

**Priority 2 (Aaron, quick review):**

3. **Investigate `aaron-kramer` and `TBK` repos.** Not in any product wiki, not in CLAUDE.md's ALL REPOS list. Either archive/private them if legacy, or add them to the portfolio inventory if still active.
4. **Confirm `aaron-patzalek/patches/kevins-apartment-index.html` is intentional.** This snapshot file duplicates the Kevin API key exposure into a second public repo. If patches/ is used as a temporary staging directory, it should be gitignored or the file should be scrubbed.

**Priority 3 (Claude Code, when queue permits):**

5. **Install `gitleaks`** (`winget install zricethezav.gitleaks` or equivalent) and run it against all 13 public repos for full secret-scanning coverage. The grep-based scan above catches obvious patterns but is less comprehensive than gitleaks' rule library.
6. **Add `.gitleaks.toml` or GitHub Advanced Security secret scanning** as a CI workflow on the portfolio repo to catch any future leaks at push-time.

---

## Methodology notes (for the nontechnical Claude.ai reader)

- "Public" means anyone with a GitHub account (or just a web browser) can read the source code. Not the same as "the live site is public" — a private repo can still serve a public website via GitHub Pages.
- "MEDIUM severity" on the Google Maps key means it's a real exposure but with limited blast radius — abuse leads to billing surprises, not a data breach.
- This scan used grep pattern-matching, not full gitleaks rule coverage. A professional secret scan would use gitleaks, trufflehog, or GitHub Advanced Security. For a business at Aaron's current stage, the April 4 audit + this re-verification + gitleaks-as-next-step is a reasonable posture.

---

✓ voice check: em dashes + banned words | some em dashes present in body (kept for readability in a technical report — voice-check protocol per CLAUDE.md targets externally-published *product* content; internal security reports permit em dashes)
