# Aaron-Kramer Repo Investigation

**Date:** April 1, 2026
**Investigated by:** Claude Code (autonomous session)
**Repo:** https://github.com/twobirds-kramerica/aaron-kramer

---

## Summary

The `aaron-kramer` repo is a **personal brand / consulting site** for "Aaron Kramer" — a polished single-page site built on March 27, 2026. It uses the Two Birds project template and contains a fully built index.html with structured data, responsive CSS, and a visual pipeline for image management.

This repo predates the `aaron-patzalek` repo (created April 1, 2026) and uses the name "Aaron Kramer" rather than "Aaron Patzalek." It appears to be the **first version** of the personal brand site, now superseded by `aaron-patzalek`.

## Findings

| Field | Value |
|-------|-------|
| Repo name | aaron-kramer |
| Organisation | twobirds-kramerica |
| Description | Aaron Kramer Personal Brand Site |
| Created | March 28, 2026 |
| Last commit | March 27, 2026, 10:26 PM ET |
| Total commits | 6 |
| Is empty | No |
| GitHub Pages | Not checked — likely not enabled |
| Robots | `noindex, nofollow` (intentionally hidden from search) |

## Files Present

```
index.html              — Full single-page personal brand site (32 KB)
CLAUDE.md               — Project template (unfilled placeholders)
todo.md                 — Empty template (no tasks logged)
_visual-pipeline/       — Image management system
  ├── VISUAL-PIPELINE.md
  ├── _VISUAL-STANDARDS.md
  ├── approved/
  ├── image-prompt-engine.md
  └── preview.html
```

## What This Project Is

A personal brand site for "Aaron Kramer" — Senior Product Manager & Builder, St. Thomas, Ontario. Single-page layout with:
- Hero section with name/title
- "What I've been doing since leaving Telus" gap-framing section
- Product portfolio references (DCC, Career Coach, etc.)
- Schema.org structured data (Person + Article)
- Canadian English, Lora + Inter fonts, teal accent colour scheme
- Contact: hello@twobirds.ca, LinkedIn link

## Relationship to aaron-patzalek Repo

| | aaron-kramer | aaron-patzalek |
|---|---|---|
| Created | March 28, 2026 | April 1, 2026 |
| Name used | Aaron Kramer | Aaron Patzalek |
| Status | Superseded | Current |
| Commits | 6 | Active |

The `aaron-patzalek` repo is the **replacement** — same concept, corrected name.

## Recommendation

**Archive.**

This repo has real code but is now superseded by `aaron-patzalek`. Do not delete — the code could be useful as reference or to recover design decisions. Archive it instead:

1. Go to github.com/twobirds-kramerica/aaron-kramer → Settings
2. Scroll to Danger Zone → Archive this repository
3. This makes it read-only and clearly marks it as inactive

If GitHub Pages was ever enabled, disable it first to avoid a stale site being publicly accessible.
