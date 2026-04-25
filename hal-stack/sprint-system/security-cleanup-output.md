# Security Cleanup — 2026-04-24 (~01:50 EST, post rate-limit-refresh continuation)

## kevins-apartment-search: now private? **Yes** — but Pages is now 404

- `gh repo edit ... --visibility private --accept-visibility-change-consequences` succeeded after the first attempt failed because gh requires explicit consequences-flag for visibility changes (a built-in safety mechanism)
- Confirmed via `gh repo view ... --json isPrivate`: `{"isPrivate": true}`
- **HEADLINE ISSUE:** `gh api repos/.../pages` now returns HTTP 404 ("Not Found"). Kevin's live tool at `https://twobirds-kramerica.github.io/kevins-apartment-search/` is **DARK**.
  - **Cause:** the org plan tier (`twobirds-kramerica`) does not include GitHub Pages on private repos. Pages-on-private requires GitHub Pro or higher.
  - **Reversibility:** flip back public via `gh repo edit ... --visibility public --accept-visibility-change-consequences` and Pages auto-restores.
  - **Three forward options for Aaron:**
    - (a) **Accept the downtime** — Kevin uses a local copy of `index.html` opened directly in his browser (the file works offline; no server needed). This is the cheapest path.
    - (b) **Re-host elsewhere** — push the static files to Cloudflare Pages / Netlify / Vercel (free tiers all support private-source + public-output). 15-30 min of work.
    - (c) **Upgrade GitHub plan** to Pro ($4/mo individual) or Team — Pages auto-restores on private repos. Cheapest if Aaron has other repos he'd also like to flip private.

## aaron-patzalek patches file: deleted? **Yes**

- File `patches/kevins-apartment-index.html` removed from `aaron-patzalek` master via `gh api ... --method DELETE`
- Commit on `aaron-patzalek/master`: `a92202af` ("Remove exposed API key snapshot from patches directory (security cleanup)")
- Local working tree synced via `git pull --rebase`: `1 file changed, 2780 deletions(-)`
- **Note on the API key itself:** the same Google Maps Embed API key (`AIzaSyD-9tSrke72PluDDL6lhVQcj5PJnO6pWQA`) is still in `kevins-apartment-search/index.html:273` because Maps Embed REQUIRES the key in the URL for the embed to render. That repo is now private (Step 1) so the source is no longer discoverable, but the GET request from any browser loading the live site (when re-hosted) will still expose the key in the network tab. **The Google Cloud Console referrer-restriction is still required** for full mitigation, regardless of repo visibility.

## CLAUDE.md updated: **Yes**

- Added `REPO VISIBILITY RULE` to STANDING RULES section
- Commit on portfolio master: `65aad2f` ("Add default-private rule for repos with user data")
- Rule includes the Pages-on-private caveat documented above so future repos don't surprise the next operator

## aaron-kramer: **Left alone (per spec)**

- `gh repo view`: `{"isEmpty": false, "isPrivate": false, "updatedAt": "2026-04-01T18:21:12Z"}`
- Has real content (default branch `main`, not empty)
- Last update 2026-04-01 — sprint spec said "If either has recent activity or meaningful content, note it in the output instead and leave it alone." 23 days ago is not recent activity but the repo IS non-empty, so I left it.
- **Recommend Aaron review** what's in this repo and decide manually. It's not in any product wiki; it's the only `aaron-kramer`-prefixed repo (the active brand site is `aaron-patzalek`). Likely legacy from before the last-name-change to Patzalek, but worth a 2-minute look.

## TBK: **Could not flip — repo is archived (HTTP 403 read-only)**

- `gh repo view`: `{"isEmpty": true, "isPrivate": false}` — empty and never had a default branch
- `gh repo edit ... --visibility private`: HTTP 403 "Repository was archived so is read-only"
- **Practical impact:** archived means dormant — no commits possible, no Pages active. The repo is functionally inert even while public. If Aaron wants it private specifically, he'd need to UN-archive first via `gh repo unarchive twobirds-kramerica/TBK`, then flip private with the consequences flag, then re-archive. Three commands. Recommend skipping unless there's a specific reason TBK being public-archived is a concern (e.g., its name conflicting with a brand decision).

## Anything skipped and why

- **Notion SESSION-STATE page update via MCP:** the spec named page ID `348a09cf-876a-815a-802c-c9c182167749`. Per the HAL Stack project_memory I read in S-ARCHAEOLOGY-002 earlier this session, that page ID is the **Glossary / Command Reference**, not a SESSION-STATE page. The portfolio's `SESSION-STATE.md` file IS the session state of record. Updated the file (per the standing SPRINT COMPLETION RULE); skipped writing to the named Notion page because writing the security findings into the Glossary page would mis-locate them. If Aaron wants a Notion mirror, point me at the correct page ID.
- **TBK private flip:** skipped due to archived state (see above). Not a Claude Code limitation; reflects GitHub's read-only-when-archived rule.
- **gitleaks install:** still not present. Recommended in the prior repo-inspection-output.md as a Priority-3 follow-up; not in scope for this Cleanup Sprint.

## Recommended next actions

**Immediate (Aaron, ~5 min total):**
1. Decide between options (a)/(b)/(c) above for Kevin's live site
2. Add referrer restrictions to the Google Maps API key in Google Cloud Console (the only fix that doesn't depend on repo visibility)

**Short follow-up (Aaron, 5-10 min review each):**
3. Inspect `aaron-kramer` repo content; decide if it should be archived, made private, or kept active
4. If concerned about TBK being publicly visible (even though archived/empty), un-archive → flip private → re-archive

**Operational pickup (Claude Code, next sprint):**
5. If Aaron picks option (b) Re-host — scope a sprint to push `kevins-apartment-search/` static files to Cloudflare Pages / Netlify / Vercel
6. If Aaron picks option (c) Upgrade — no Claude Code work needed; Pages auto-restores
7. Install gitleaks + add CI workflow per prior inspection's Priority-3 recommendation

---

## Confidence
**95%.** Three of five steps fully executed; two have honest skip notes (Notion page mis-named in spec; TBK archived). Pages-going-dark on Kevin is a real consequence Aaron now has three documented options for.

The only uncertainty is whether Aaron knew or expected the Pages downtime when he authored the sprint. The spec didn't mention it; my prior repo-inspection-output.md said "GitHub Pages will still serve the site" which was wrong for the org's current plan tier. **Correcting that claim:** Pages-on-private requires Pro or higher; on the org's current plan, flipping to private kills Pages immediately. Updated CLAUDE.md REPO VISIBILITY RULE explicitly captures this trade-off so future operators (Claude or human) see it before flipping.
