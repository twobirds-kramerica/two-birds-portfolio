# HAL Stack Service Map

## Current Services (Operational)

| Service | Type | Where | What It Does |
|---------|------|-------|-------------|
| Claude Code CLI | Local | i5 Lenovo | Primary AI build engine |
| Claude Mem | Local | ~/.claude/claude-mem | Memory injection into sessions |
| Superpowers | Local | ~/.claude/superpowers | TDD, micro-planning, brainstorming |
| GSD | Local | ~/.claude/gsd | Autonomous milestone execution |
| Everything CC | Local | ~/.claude/everything-claude-code | Security + curated skills |
| GitHub Actions | Cloud | GitHub | 15 DCC workflows, monitoring, alerts |
| GitHub Pages | Cloud | GitHub | Hosts all live products |
| Formspree | Cloud | formspree.io | DCC feedback form submission |
| Gmail MCP | Cloud | claude.ai | Claude Web ↔ Gmail integration |

## Pending Services

| Service | Type | Install Via | ETA |
|---------|------|------------|-----|
| n8n | Local server | npm install -g n8n | April 2026 |
| OpenCode | Local server | npm install -g opencode | April 2026 |
| LightRAG | Local server | pip install lightrag-hku | May 2026 |
| SQLite (prompt DB) | Local file | Built into Node.js | With n8n |

## Service Dependencies

```
Claude Code
  └── Claude Mem (memory injection)
  └── GSD (task tracking)
  └── Superpowers (methodology)
  └── GitHub (push/pull)
      └── GitHub Actions (monitoring)
      └── GitHub Pages (hosting)

n8n (pending)
  └── Gmail (PROMPT-QUEUE labels)
  └── GitHub webhooks (push events)
  └── SQLite (prompt database)
  └── Email alerts

LightRAG (pending)
  └── DCC repo files (ingested)
  └── Claude Code (via MCP)
```

## Cost Summary

| Service | Cost |
|---------|------|
| Claude Max subscription | ~$100/month |
| GitHub (Free tier) | $0 |
| GitHub Pages | $0 |
| Formspree Free | $0 |
| n8n (self-hosted) | $0 |
| LightRAG (self-hosted) | $0 |
| OpenCode (self-hosted) | $0 |
| **Total infrastructure** | **~$100/month** |
