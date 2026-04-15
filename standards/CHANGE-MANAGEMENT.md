# Change Management Process

**Version:** 1.0
**Created:** 2026-04-15

How changes are tracked, communicated, and shipped across all Two Birds Innovation repos.

---

## When to Update the Changelog

Update `CHANGELOG.md` (repo root) when any of these happen:

- **User-facing change** — new page, new feature, visual change, content update
- **Breaking change** — anything that changes existing behaviour
- **New standard or process** — engineering standards, design system, workflow change
- **Infrastructure change** — hosting, CDN, domain, deployment pipeline

Do NOT update the changelog for:
- Internal documentation updates (SESSION-STATE, RETRO, sprint-queue)
- Backlog management
- Context exports

---

## Changelog Format

Follow [Keep a Changelog](https://keepachangelog.com/):

```markdown
## [YYYY-MM-DD] — Short Title (Sprint ID)

### Added
- New features or capabilities

### Changed
- Changes to existing features

### Fixed
- Bug fixes

### Removed
- Removed features or deprecated items

### Security
- Security-related changes
```

---

## Change Categories

| Category | Description | Changelog? | SESSION-STATE? |
|----------|-------------|-----------|---------------|
| User-facing feature | New page, component, or capability | YES | YES |
| Bug fix | Broken functionality restored | YES | YES |
| Visual change | CSS, layout, branding | YES | YES |
| Performance | Speed, size, loading | YES | YES |
| Infrastructure | Hosting, CDN, deployment | YES | YES |
| Internal tooling | HAL stack, sprints, backlog | NO | YES |
| Documentation | READMEs, process docs | NO | YES |

---

## Sprint Integration

Every sprint that produces user-facing changes must:

1. Add entries to `CHANGELOG.md` before the sprint is marked DONE
2. Reference the sprint ID in the changelog entry (e.g., "S-016")
3. Include the date of completion

The sprint template checklist enforces this.

---

## Cross-Repo Changes

When a sprint touches multiple repos (e.g., DCC + portfolio):

1. Update the changelog in the **primary** repo (usually `two-birds-portfolio`)
2. Note which repo was affected in the changelog entry
3. Commit and push both repos

---

## Versioning

Currently not using semantic versioning for sites (they're continuously deployed). The changelog serves as the version history.

If/when products ship as discrete releases, adopt semver:
- **MAJOR** — breaking changes to user experience
- **MINOR** — new features, backward-compatible
- **PATCH** — bug fixes, no feature changes
