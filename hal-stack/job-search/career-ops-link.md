# Career-Ops — Job Search Pipeline

**Location:** `C:\twobirds\career-ops\`
**Source:** [github.com/santifer/career-ops](https://github.com/santifer/career-ops)
**Installed:** 2026-04-16

---

## What It Is

AI-powered job search automation built on Claude Code. Evaluates job postings against Aaron's CV, generates tailored application materials, scans career portals, and tracks the pipeline.

## How to Run

1. Open Claude Code in the career-ops directory: `cd C:\twobirds\career-ops && claude`
2. Say `/career-ops` followed by a command, or paste a job URL for evaluation
3. The system reads `cv.md` and `config/profile.yml` for Aaron's profile

## Key Commands

| Command | What It Does |
|---------|-------------|
| Paste a job URL | Evaluates the role against Aaron's profile |
| `/career-ops scan` | Scans all configured portals for new postings |
| `/career-ops batch` | Batch-processes multiple job postings |
| `/career-ops pdf` | Generates a formatted CV PDF |

## Configuration Files

| File | Purpose |
|------|---------|
| `cv.md` | Aaron's CV in markdown |
| `config/profile.yml` | Target roles, compensation, location |
| `modes/_profile.md` | Archetypes, narrative, proof points |
| `portals.yml` | Companies and job boards to scan |

## Configured Portals

iA Financial, TELUS, Start.ca, Ontario Public Service, City of St. Thomas, City of London ON, Cohere, Shopify, Indeed Canada (5 queries).

## Doctor Status

All checks passed (2026-04-16): Node.js, dependencies, Playwright, cv.md, profile.yml, portals.yml.

## Guardrails

- Do NOT auto-apply. Aaron reviews every application before submission.
- Do NOT scrape LinkedIn (will fail / violate ToS).
- Playwright runs in headless mode.
