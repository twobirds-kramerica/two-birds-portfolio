# HAL Stack — Backlog
**Owner:** Aaron Kramer | Two Birds Innovation
**Last Updated:** March 31, 2026

> Backlog items for the HAL Stack. Each item has a unique ID (HAL-NNN).

---

## HAL-007 — Portfolio as Live PMO Layer
**Date logged:** March 31, 2026
**Priority:** High
**Phase:** HAL Phase 2

### Problem

Claude Web sessions have no live access to the Two Birds Portfolio backlog,
SESSION-STATE.md, or any local files. Every new chat starts blind.
The portfolio is passive storage, not an active PMO system.

### Vision

The two-birds-portfolio repo becomes the single source of truth for all
Two Birds Innovation work — backlog, sprint state, decisions, architecture,
product roadmap. Any Claude session (Web or Code) can query and write to it.

### Proposed Architecture

- n8n webhook exposes portfolio files as readable JSON endpoints
- Claude Web MCP connects to n8n endpoints
- Claude Code reads/writes directly to local files
- SESSION-STATE.md is the handoff file between all sessions
- NEXT-SPRINT-QUEUE.md is the authoritative backlog for all projects

### Immediate Workaround (active now)

Every Claude Code prompt begins with reading SESSION-STATE.md and
NEXT-SPRINT-QUEUE.md before executing any work.

### Effort & Dependencies

- **Effort estimate:** HAL Phase 2 — medium
- **Blocked on:** n8n install (HAL-001), MCP config (HAL-002)
