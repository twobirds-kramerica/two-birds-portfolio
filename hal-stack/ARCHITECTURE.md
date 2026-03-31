# HAL Stack Architecture

## System Diagram

```
INPUTS
Aaron (phone/tablet/laptop) → OpenCode mobile client
Claude Web (claude.ai) → Gmail MCP trigger → n8n listener

PROCESSING LAYER (i5 Lenovo or Desktop)
OpenCode server → Claude Code CLI → GitHub repos
n8n automation engine → Gmail / GitHub / SQLite database
LightRAG server (port 9621) → knowledge graph of all repo files
Claude Mem → persistent memory injected into every session

OUTPUTS
GitHub Pages → live products (7 repos, 200+ URLs)
Gmail → drafts, alerts, weekly reports
Mobile dashboard → build status from phone
Future: API gateway → client tools and white-label products
```

## Port Map
| Service | Port | Status |
|---|---|---|
| LightRAG server | 9621 | Pending |
| n8n web UI | 5678 | Pending |
| OpenCode server | 3000 | Pending |

## Data Flow — Prompt Lifecycle
1. Claude Web generates build prompt
2. Claude Web saves prompt to Gmail draft with label PROMPT-QUEUE
3. n8n watches for PROMPT-QUEUE label → writes entry to SQLite (status: PENDING)
4. Aaron pastes prompt into Claude Code on i5
5. Claude Code runs build → pushes to GitHub
6. n8n webhook receives GitHub push event → updates SQLite (status: COMPLETE)
7. Mobile dashboard reflects current state
8. If failure detected → Gmail alert fires within 5 minutes

## Option A — Minimal HAL (Now)
Cost: Free | Complexity: Low
- i5 as always-on server ✅
- GitHub Actions for automated monitoring ✅
- Gmail MCP for Claude Web memory ✅
- Basic prompt tracking via Gmail labels ✅

## Option B — Standard HAL (Month 2–3)
Adds: LightRAG, n8n, SQLite prompt tracker, mobile dashboard

## Option C — Full HAL (Month 4–6)
Adds: OpenCode remote, voice interface, vector database,
multi-agent routing, API gateway, monitoring dashboard
