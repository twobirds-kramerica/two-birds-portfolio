# HAL Stack — Backlog
**Owner:** Aaron Kramer | Two Birds Innovation
**Last Updated:** April 22, 2026

> Backlog items for the HAL Stack. Each item has a unique ID (HAL-NNN).

---

## HAL-007 — Portfolio as Live PMO Layer
**Date logged:** March 31, 2026
**Status:** SUPERSEDED (2026-04-19) — see Resolution below
**Priority:** (was High)
**Phase:** HAL Phase 2

### Problem (as originally stated)

Claude Web sessions have no live access to the Two Birds Portfolio backlog,
SESSION-STATE.md, or any local files. Every new chat starts blind.
The portfolio is passive storage, not an active PMO system.

### Resolution

Superseded 2026-04-19 by **S-024 Notion Sync** (see `hal-stack/notion-sync/`).
Notion Command Center + Product Backlog are now the bidirectional source of
truth; Claude.ai sessions reach it via the Notion MCP, Claude Code reaches it
via `notion-client.py` helpers. Full round-trip proven end-to-end over
2026-04-19 → 2026-04-22, including two 16-entry retro-file batches with
100% success rate and zero n8n dependency.

The original n8n / MCP-webhook architecture was never built because the Notion
path turned out to be strictly simpler and solved the same problem. HAL-001
(n8n install) and HAL-002 (MCP config for n8n) are also marked superseded.

### Immediate Workaround (was — no longer needed)

Every Claude Code prompt begins with reading SESSION-STATE.md and
NEXT-SPRINT-QUEUE.md before executing any work. This is still the Claude-Code
start-of-session posture for local state, but the authoritative backlog
source now lives in Notion.

### Effort & Dependencies

Zero remaining work on this item. Artefact preserved for historical context.

---

## Next up for HAL

All HAL-007 children closed via S-024. Next HAL-scope work candidates
(not yet filed as HAL-NNN):

- **Voice transcription workflow** — Ito + KDE Connect integration (deferred
  in the 2026-04-22 projects.json refresh). Would unlock hands-free sprint
  invocation.
- **UI Preview Layer** — Lovable or equivalent for quick visual iteration
  on Clarity / Career Coach. Deferred.
- **Credit Intelligence Dashboard** — credit-usage analytics across Claude
  Code + Claude.ai + API. Deferred.
- **Component library + vibe_rules.md** — design-system extraction across
  the 6 shipped products. Deferred until 2 more products ship to avoid
  premature abstraction.

None of these are currently open sprints; all remain deferred until Aaron
prioritises. This file's next update should either formalise one of these
as HAL-008 or confirm the backlog genuinely stays closed.
