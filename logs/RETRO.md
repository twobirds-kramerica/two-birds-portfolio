# Retro
Date: April 4, 2026
Session: Full security audit — all 10 repos

Findings:
- 0 CRITICAL, 0 HIGH, 2 MEDIUM, 5 LOW
- No Anthropic API keys in any repo (Career Coach + Clarity correctly use localStorage)
- Google Maps Embed key in kevins-apartment-search (MEDIUM — needs referrer restriction in Google Cloud Console)
- Web3Forms key in DCC (MEDIUM — public by design, working as intended)
- Formspree IDs, GA ID, Clarity placeholder, GitHub token placeholder — all LOW

Actions taken:
- .gitignore updated in all 10 repos (added .env, .env.local, .env.production)
- .env template created at C:\twobirds\.env (empty structure, not tracked)
- research/security-audit-results.md created with full findings (127 lines)
- All 10 repos committed and pushed

Human action needed:
- P1: Restrict Google Maps API key to *.github.io referrers in Google Cloud Console (5 min)

Commits across repos:
- 0c45812 (DCC: gitignore from earlier session)
- 4bc2b79 career-coach, 2de323c clarity, 743cfe3 kevins, 70ffdab tbi, ec2c673 aaron-p
- 920eb91 cmd-centre, 26f5195 quality, faf69b6 elite-karate, 6bc73aa + e95e6e5 portfolio

Last updated: 2026-04-04 at 01:33 EST (Toronto)
CDN note: If Retro shows stale data, wait 5 minutes and type Retro again.
