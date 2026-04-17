# Release Process — Two Birds Innovation

**Version:** 1.0 | **Created:** 2026-04-17

---

## The 4-Layer Change Management System

### Layer 1: Issue-Linked Commits
Every commit that completes work should reference the GitHub Issue number:
```
feat(dcc): add module 22 — smartphone basics (closes #57)
fix(css): contrast ratio on nav links (fixes #58)
```
`closes #N` and `fixes #N` auto-close the issue when merged to master.

### Layer 2: GitHub Releases
When a meaningful batch of work ships, create a release:
```bash
"/c/Program Files/GitHub CLI/gh.exe" release create v0.2.0 \
  --title "v0.2.0 — DCC Beta Launch" \
  --generate-notes \
  --target master
```
`--generate-notes` uses `.github/release.yml` to auto-categorise PRs/commits by label.

### Layer 3: Auto-Generated CHANGELOG
The GitHub Action at `.github/workflows/changelog.yml` triggers on every release publish. It rebuilds `CHANGELOG.md` from all releases automatically.

### Layer 4: Label-Based Categorisation
`.github/release.yml` groups release notes by label:
- **Features & Sprints** — `sprint`, `feature`
- **Bug Fixes** — `bug`
- **Infrastructure** — `hal-stack`
- **Branding** — `branding`, `dcc`
- **Career** — `career`
- **Documentation** — `documentation`, `task`
- **Human Actions** — `human-action`

---

## How to Create a Release

### From Claude Code
```bash
GH="/c/Program Files/GitHub CLI/gh.exe"

# Create release with auto-generated notes
"$GH" release create v0.1.0 \
  --title "v0.1.0 — Foundation" \
  --generate-notes \
  --target master \
  -R twobirds-kramerica/two-birds-portfolio
```

### Version Numbering
- **v0.x.x** — pre-revenue, building foundation
- **v1.0.0** — first revenue or first public launch
- Increment: patch (bug fix), minor (feature), major (breaking change)

---

## Sprint Workflow Integration

1. Create GitHub Issue (use sprint template)
2. Reference issue number in commits: `closes #N`
3. When sprint completes, issue auto-closes
4. Periodically (weekly or after major milestones): create a release
5. CHANGELOG auto-generates from release notes
6. SESSION-STATE.md remains the primary audit trail

---

## Quick Reference

| Action | Command |
|--------|---------|
| Create release | `gh release create vX.Y.Z --title "title" --generate-notes` |
| List releases | `gh release list` |
| View release | `gh release view vX.Y.Z` |
| Delete release | `gh release delete vX.Y.Z` |
| Check changelog | Read `CHANGELOG.md` (auto-generated) |
