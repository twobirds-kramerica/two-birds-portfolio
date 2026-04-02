# 06 — HAL Portability Spec

**Date:** April 1, 2026
**Objective:** Document every HAL Stack component with a named open-source alternative, so the entire infrastructure can be rebuilt from scratch on a clean machine without any proprietary dependency.

---

## Current HAL Components and Open-Source Alternatives

| Component | Current Tool | Open-Source Alternative | Notes |
|-----------|-------------|----------------------|-------|
| AI Coding | Claude Code CLI | [Aider](https://aider.chat) or [Continue.dev](https://continue.dev) | Aider works with any LLM. Continue is a VS Code extension. Both read context files. |
| AI Inference | Anthropic API | [Ollama](https://ollama.com) + llama3/mistral | Runs locally, no API key, no cost. Quality is lower but functional. |
| Code Hosting | GitHub | [Codeberg](https://codeberg.org) or [Gitea](https://gitea.io) (self-hosted) | Codeberg is free, non-profit. Gitea can run on the i5. |
| Static Hosting | GitHub Pages | [Cloudflare Pages](https://pages.cloudflare.com) or [Caddy](https://caddyserver.com) (self-hosted) | Cloudflare Pages is free. Caddy runs locally with automatic HTTPS. |
| Automation | n8n (planned) | [n8n](https://n8n.io) (already open-source) | Self-hosted, MIT-like licence. No vendor lock-in. |
| Knowledge Graph | LightRAG (planned) | [LightRAG](https://github.com/HKUDS/LightRAG) (already open-source) | Self-hosted. Swap embedding model if needed. |
| Prompt Tracking | Gmail labels + SQLite | SQLite (already local) + flat markdown files | Gmail is the convenience layer. SQLite is the source of truth. |
| Email | Gmail | [Thunderbird](https://www.thunderbird.net) + any SMTP provider | Or self-hosted with [Mail-in-a-Box](https://mailinabox.email). |
| Session Memory | Claude Code memory + CLAUDE.md | Flat markdown files (already portable) | CLAUDE.md works with any AI tool. Memory files are plain text. |
| Overnight Builds | Windows Task Scheduler + bat script | [cron](https://en.wikipedia.org/wiki/Cron) on Linux or Task Scheduler (already local) | The bat script is plain shell. Works on any OS with minor edits. |
| DNS / CDN | Cloudflare | [Caddy](https://caddyserver.com) (reverse proxy) or any DNS provider | DNS records are portable. Export zone file. |
| Form Submissions | Formspree + Web3Forms | Self-hosted with [Staticman](https://staticman.net) or simple POST endpoint | Or [Listmonk](https://listmonk.app) for full email + forms. |

---

## Rebuilding HAL from Scratch — Checklist

**Prerequisites:** A machine with 8GB+ RAM, an internet connection, and git installed.

### Phase 1: Core (2 hours)

- [ ] Install git: `winget install git.git` (Windows) or `apt install git` (Linux)
- [ ] Clone all repos from Codeberg mirrors (or GitHub if available)
- [ ] Install Ollama: download from ollama.com, run `ollama pull llama3`
- [ ] Install Aider: `pip install aider-chat` — configure with Ollama endpoint
- [ ] Verify: open a repo, run Aider, ask it to read CLAUDE.md and explain the project

### Phase 2: Hosting (1 hour)

- [ ] Install Caddy: download from caddyserver.com
- [ ] Create Caddyfile pointing to each product's directory
- [ ] Start Caddy: `caddy run` — all sites available on localhost
- [ ] For public access: configure Cloudflare Tunnel or port forwarding

### Phase 3: Automation (2 hours)

- [ ] Install n8n: `npm install -g n8n` (or Docker: `docker run -it n8n`)
- [ ] Import workflow JSONs from `hal-stack/n8n/workflows/`
- [ ] Configure Gmail connection (or switch to local SMTP)
- [ ] Set up cron job / Task Scheduler for overnight builds

### Phase 4: Knowledge (1 hour)

- [ ] Install LightRAG: `pip install lightrag-hku`
- [ ] Ingest all repo files into knowledge graph
- [ ] Test query: "What modules does DCC have?"
- [ ] Connect to Aider or Claude Code via MCP

### Phase 5: Monitoring (1 hour)

- [ ] Deploy Quality Dashboard from local files
- [ ] Configure health checks for each product URL
- [ ] Set up email alerts for failures (n8n workflow)

**Total rebuild time: ~7 hours from a blank machine.**

---

## What You Lose by Going Fully Open-Source

| Capability | With Claude/GitHub | With Open-Source Only |
|-----------|-------------------|----------------------|
| AI coding quality | Excellent (Opus 4.6) | Good (llama3) — slower, less capable |
| Deployment speed | Instant (GitHub Pages) | 15 min setup (Caddy/Cloudflare Pages) |
| Collaboration | GitHub Issues, PRs | Codeberg has same features |
| Uptime guarantee | 99.9% (GitHub) | Self-managed (depends on i5 uptime) |
| Cost | CA$142.80/month (Max plan) | CA$0/month (electricity only) |

**Verdict:** The open-source stack is viable for survival but not optimal for speed. The recommended approach is: use the best commercial tools while they're affordable, maintain the exit door at all times.

---

## Emergency Scenario: "Everything Commercial Breaks Tomorrow"

1. All code is on `C:\twobirds\` — nothing lost
2. Install Ollama + Aider — coding resumes within 30 minutes
3. Install Caddy — all sites live locally within 1 hour
4. Push repos to Codeberg — code hosted publicly within 2 hours
5. Configure Cloudflare Pages — sites live on the internet within 4 hours
6. Total business downtime: **under 4 hours**
7. Total cost: **CA$0**

The trade-off is speed and AI quality, not capability. Aaron can still build, deploy, and serve customers with zero vendor spend.
