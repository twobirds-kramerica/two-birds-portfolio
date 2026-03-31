# HAL Stack — User Stories

**Author:** Aaron Kramer | Two Birds Innovation
**Last Updated:** 2026-03-31
**Status:** Phase 1 stories complete. Phase 2 stories pending n8n install.

---

## US-001 — Morning Build Orientation

**As** Aaron (the primary developer),
**I want** a daily 7 AM summary of what was built and what is queued,
**So that** I can orient myself each morning without reading through GitHub manually.

### Acceptance Criteria
- [ ] GitHub Issue created automatically at 7 AM EST each day
- [ ] Issue contains last 5 commit messages with hashes and relative timestamps
- [ ] Issue contains count of open GitHub Issues by label
- [ ] Issue contains links to all live DCC properties (site, dashboard, career coach)
- [ ] Issue contains a morning checklist (review, check Gmail, push staged changes)
- [ ] Issue is labelled `hal-stack` and `daily-report`

**Current Status:** ✅ Complete — `build-health-report.yml` deployed 2026-03-31

---

## US-002 — Prompt Queue Visibility

**As** Aaron,
**I want** to always know which Claude Code build prompts have been generated but not yet confirmed complete,
**So that** I do not lose track of planned work after a context window summary or session break.

### Acceptance Criteria
- [ ] Every generated prompt is logged with a timestamp and topic summary
- [ ] Each prompt has a status: PENDING | RUNNING | COMPLETE | FAILED
- [ ] Status updates automatically when a matching GitHub commit is pushed
- [ ] If a prompt has been PENDING for more than 24 hours, an alert is sent
- [ ] A dashboard or Issue shows the current queue state at any time

**Current Status:** 🟡 Partial — Gmail draft labels are the interim system; `prompt-queue-monitor.yml` creates 6-hour heartbeat Issues. SQLite + n8n automation pending April 2026.

---

## US-003 — Build Failure Alert

**As** Aaron,
**I want** to receive an immediate notification when a Claude Code build step fails,
**So that** I can address errors the same day and not discover them hours later.

### Acceptance Criteria
- [ ] Claude Code error output is detected within 5 minutes
- [ ] An alert is created (GitHub Issue or email) with the error summary
- [ ] The affected prompt is updated to FAILED status in the prompt database
- [ ] Alert includes the last 3 lines of the error output and the prompt topic

**Current Status:** ⏳ Pending — requires n8n log file watcher (April 2026)

---

## US-004 — LinkedIn Post Scheduling

**As** Aaron,
**I want** a weekly reminder on Tuesdays with the next scheduled LinkedIn post pre-loaded,
**So that** I can post consistently without having to decide what to write each week.

### Acceptance Criteria
- [ ] GitHub Issue created every Tuesday at 8 AM EST
- [ ] Issue contains the scheduled post text from `_social/aaron-linkedin-posts.json` (rotated by ISO week number)
- [ ] Issue shows the recommended day to post and the content pillar
- [ ] Issue also includes an alternative angle and two post templates
- [ ] Issue is labelled `linkedin` and `marketing`

**Current Status:** ✅ Complete — `weekly-linkedin-reminder.yml` updated 2026-03-31 with JSON post pull

---

## US-005 — Machine-Independent Build Access

**As** Aaron,
**I want** to be able to initiate builds from my phone or a second device when I am away from the i5 Lenovo,
**So that** HAL is not dependent on physical presence at one machine.

### Acceptance Criteria
- [ ] OpenCode server running on port 3000 on the i5 Lenovo
- [ ] Port is accessible via Cloudflare Tunnel or VPN from mobile
- [ ] Aaron can review and approve a build plan from his phone
- [ ] No credentials stored in plain text; authentication required

**Current Status:** ⏳ Pending — OpenCode install ETA April 2026

---

## US-006 — Knowledge-Augmented Builds (LightRAG)

**As** Aaron,
**I want** Claude Code to have access to the full DCC codebase as a searchable knowledge graph,
**So that** long-context builds do not forget the architecture of what has already been built.

### Acceptance Criteria
- [ ] LightRAG running on port 9621 with DCC repo files ingested
- [ ] Claude Code can query LightRAG via MCP for codebase context
- [ ] New modules and files are automatically re-ingested on push
- [ ] Query latency under 3 seconds for standard context requests

**Current Status:** ⏳ Pending — LightRAG install ETA May 2026

---

## Story Map Summary

| Story | Title | Status | ETA |
|-------|-------|--------|-----|
| US-001 | Morning Build Orientation | ✅ Complete | Done |
| US-002 | Prompt Queue Visibility | 🟡 Partial (interim only) | April 2026 (full) |
| US-003 | Build Failure Alert | ⏳ Pending | April 2026 |
| US-004 | LinkedIn Post Scheduling | ✅ Complete | Done |
| US-005 | Machine-Independent Build Access | ⏳ Pending | April 2026 |
| US-006 | Knowledge-Augmented Builds | ⏳ Pending | May 2026 |
