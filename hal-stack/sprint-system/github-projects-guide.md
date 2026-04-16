# GitHub Projects Guide — Two Birds Innovation Backlog

**Created:** 2026-04-16
**Project URL:** https://github.com/users/twobirds-kramerica/projects/1

---

## Overview

The "Two Birds Innovation Backlog" is a GitHub Projects V2 board that provides visibility across all Two Birds repos in one place. It replaces the need for Jira/Monday/paid tools while staying sovereign.

**Primary source of truth:** `sprint-queue.md` (execution queue)
**Visibility layer:** GitHub Projects (dashboard, filtering, scoring)
**Audit trail:** `SESSION-STATE.md` (detailed session logs)

---

## Custom Fields

| Field | Type | Purpose |
|-------|------|---------|
| Product | Single-select | Which product this work is for |
| Priority | Single-select | P0 (critical) through P3 (nice to have) |
| Type | Single-select | Feature, Bug, Task, Sprint, Research |
| Risk | Single-select | Low, Medium, High, Critical |
| Layer | Single-select | L1-L4 sovereignty mapping |
| Sprint | Text | Sprint ID (e.g., S-016) |
| Owner | Text | Who is responsible |
| Effort | Number | Story points (1-13) or hours |
| Impact | Number | 1-5 scale |
| Reach | Number | 1-5 scale |
| Confidence | Number | 1-5 scale |
| RICE Score | Number | Reach x Impact x Confidence / Effort |
| Due Date | Date | Target completion |

---

## Views (Create Manually in Web UI)

GitHub Projects V2 views must be created in the web UI. Go to the project URL and click "+ New view" for each:

### 1. Product Swimlanes
- **Type:** Board
- **Group by:** Product field
- **Use for:** See all work across products side by side

### 2. Sprint Board
- **Type:** Board
- **Group by:** Status
- **Filter:** `label:sprint`
- **Use for:** Current sprint execution tracking

### 3. Priority Backlog
- **Type:** Table
- **Sort by:** Priority (ascending)
- **Group by:** Product
- **Use for:** Backlog grooming, sprint planning

### 4. Risk Heatmap
- **Type:** Table
- **Filter:** `Risk:High,Critical`
- **Use for:** Quick risk assessment

### 5. Roadmap
- **Type:** Roadmap
- **Date field:** Due Date
- **Use for:** Timeline planning

### 6. RICE Scored
- **Type:** Table
- **Sort by:** RICE Score (descending)
- **Use for:** Data-driven prioritisation

### 7. By Layer
- **Type:** Board
- **Group by:** Layer
- **Use for:** Sovereignty review — see which layers have the most work

### 8. Blocked Items
- **Type:** Table
- **Filter:** `label:blocked`
- **Use for:** Unblocking work

---

## How to Create Issues

### From Claude Code
```
gh issue create -R twobirds-kramerica/two-birds-portfolio \
  -t "S-NNN: Title" \
  -b "Priority: P1 | Layer: L1 | Product: DCC | Type: Sprint" \
  -l sprint -l P1
```

Then add to project:
```
gh project item-add 1 --owner twobirds-kramerica \
  --url https://github.com/twobirds-kramerica/two-birds-portfolio/issues/NNN
```

### From GitHub Web
1. Go to any repo → Issues → New Issue
2. Select a template (bug, feature, sprint, task)
3. Fill in fields
4. After creation: go to project → Add item → search for the issue

---

## RICE Scoring

Calculate manually and enter in the RICE Score field:

```
RICE = (Reach x Impact x Confidence) / Effort
```

| Factor | Scale | Example |
|--------|-------|---------|
| Reach | 1-5 | How many users affected? 1=Aaron only, 5=all DCC users |
| Impact | 1-5 | How much does it matter? 1=cosmetic, 5=revenue-critical |
| Confidence | 1-5 | How sure are you? 1=guess, 5=data-backed |
| Effort | 1-13 | Fibonacci story points or hours |

Higher RICE = higher priority. Use the "RICE Scored" view to see the ranked list.

---

## Workflow Integration

### Sprint lifecycle
1. Create issue using sprint template
2. Add to project, set custom fields
3. Execute sprint in Claude Code (sprint-queue.md is still the execution trigger)
4. Update issue status when done (close issue)
5. Update SESSION-STATE.md (primary audit trail)

### The dual-track model
- **sprint-queue.md** = what runs next (Claude Code reads this)
- **GitHub Projects** = visibility dashboard (Aaron and future team read this)
- Both are updated. Neither replaces the other.

---

## Migration Path to Jira (If Needed Later)

If Two Birds grows and needs Jira:
1. Export all issues via `gh api` (JSON)
2. Import into Jira via CSV or REST API
3. Custom fields map directly to Jira custom fields
4. RICE scoring transfers cleanly
5. Atlassian GitHub integration links repos to Jira tickets

This is documented, not recommended. GitHub Projects covers current needs at zero cost.

---

## gh CLI Quick Reference

```bash
# List project items
gh project item-list 1 --owner twobirds-kramerica

# Create issue and add to project
gh issue create -R REPO -t "title" -b "body" -l label
gh project item-add 1 --owner twobirds-kramerica --url ISSUE_URL

# Edit project item fields
gh project item-edit --id ITEM_ID --project-id PROJECT_ID --field-id FIELD_ID --text "value"

# Close issue
gh issue close NUMBER -R REPO --reason completed

# List issues
gh issue list -R REPO --label sprint --state open
```

Note: On this machine, use full path: `"/c/Program Files/GitHub CLI/gh.exe"` or set alias: `alias gh='"/c/Program Files/GitHub CLI/gh.exe"'`
