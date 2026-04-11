<!--
STATUS: v0.2 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:03 EST (Toronto)
Updated: 2026-04-11 02:20 EST (Toronto)
Confidence: MEDIUM — swap times are estimates, not tested. Pricing unverified.
Known gaps: L4 local LLM quality untested. Some L3 hosting costs approximate.
-->

# Decapitation Checklist — Full Audit

Every component Two Birds Innovation depends on, assessed for sovereignty at all four layers.

## Summary Dashboard

| # | Component | Current | L2 Ready? | L3 Ready? | L4 Ready? | Risk | Priority |
|---|-----------|---------|-----------|-----------|-----------|------|----------|
| 1 | Claude Code CLI | L1 | Documented | Documented | Documented | LOW | Later |
| 2 | Claude.ai (web) | L1 | Documented | No | Documented | LOW | Later |
| 3 | GitHub (repos) | L1 | Documented | Documented | Documented | LOW | Soon |
| 4 | GitHub Pages | L1 | Documented | Documented | Documented | LOW | Soon |
| 5 | Formspree | L1 | Active (Web3Forms) | Documented | No | LOW | Later |
| 6 | Cloudflare (DNS/CDN) | L1 | Documented | Documented | No | MEDIUM | Later |
| 7 | OpenAI Whisper API | Planned L1 | Documented | Documented | Documented | LOW | Later |
| 8 | Context bridge | L4-native | N/A | N/A | N/A | NONE | Never |
| 9 | Persona/swarm system | L1-L4 | N/A | N/A | N/A | NONE | Never |
| 10 | Node.js / npm | L4-native | N/A | N/A | N/A | NONE | Never |
| 11 | PowerShell scripts | L4-native | N/A | N/A | N/A | LOW | Later |
| 12 | Windows OS | L4 | Documented | N/A | N/A | LOW | Later |

---

## 1. Claude Code CLI

```
Current Layer: L1
Vendor: Anthropic (Claude Pro, CA$27/month)
Data Portable?: YES — all output is local files in git repos

L2: Aider (open-source, BYOK) or Cursor IDE (~US$20/mo)
    Swap: 30 min. Install tool, point at repos. CLAUDE.md → adapt to tool's context format.
L3: Aider + OpenRouter (cloud API, open-source client)
    Swap: 1 hour. Repos stay. Prompts are markdown.
L4: Aider + Ollama + DeepSeek-Coder (fully local)
    Swap: 2-4 hours. Needs 16GB+ RAM for decent code models.
    Quality loss: SIGNIFICANT for complex multi-file edits.

Risk: LOW — all work product lives in git, not in Claude.
Priority: Later — working well, no urgency to build fallback.
```

## 2. Claude.ai (Web Chat)

```
Current Layer: L1
Vendor: Anthropic (included in Pro plan)
Data Portable?: PARTIAL — chat history locked in Anthropic. Export requested.

L2: ChatGPT, Gemini, Perplexity for research
    Swap: 5 min. Open browser, paste context-loader-prompt.md.
L3: No direct equivalent — web chat is inherently cloud.
L4: Ollama + Open WebUI (local chat interface)
    Swap: 1-2 hours. Install Ollama + WebUI. Paste context-loader-prompt.md.
    Quality: Adequate for brainstorming. Weaker for deep analysis.

Risk: LOW — chat is a convenience. Critical work happens in Claude Code.
Priority: Later. The context bridge system reduces dependency.
```

## 3. GitHub (Code Hosting)

```
Current Layer: L1
Vendor: Microsoft/GitHub (free tier)
Data Portable?: YES — git repos are fully local. Every machine has a clone.

L2: Codeberg (EU-hosted, non-profit), GitLab
    Swap: 30 min per repo. Add remote, push. Update CI config.
L3: Gitea on VPS (~US$5/mo)
    Swap: 2-3 hours. Install Gitea, push all repos, update remotes.
L4: Local git on Pentium Silver. No remote. Just local repos.
    Swap: 15 min. Already cloned. Just stop pushing.
    See: local-backup.md for architecture.

Risk: LOW — git is inherently distributed. Every clone is a full backup.
Priority: Soon — the local backup script (E11) should be built.
```

## 4. GitHub Pages (Static Hosting)

```
Current Layer: L1
Vendor: Microsoft/GitHub (free)
Data Portable?: YES — static HTML/CSS/JS files. Host anywhere.

L2: Cloudflare Pages (already configured for some sites)
    Swap: 15 min per site. Push to Cloudflare, update DNS.
L3: Netlify, Vercel, or any static host on VPS (nginx)
    Swap: 30 min per site. Upload files, configure domain.
L4: Local web server (Python http.server, nginx on desktop)
    Swap: 5 min. Only accessible on local network.

Risk: LOW — static files are the most portable thing in computing.
Priority: Soon — Cloudflare Pages should be confirmed as live L2.
```

## 5. Formspree (Form Submissions)

```
Current Layer: L1
Vendor: Formspree (free tier, 50/month)
Data Portable?: YES — CSV export available from dashboard.

L2: Web3Forms (ALREADY ACTIVE as silent backup in feedback-github.js)
    Swap: 15 min. Change endpoint URL in JS files.
L3: Formgrid or n8n webhook on VPS
    Swap: 2-3 hours. Set up webhook, update form action URLs.
L4: No direct L4 equivalent for form submission (needs a server to receive).
    Workaround: mailto: link as form action. Ugly but functional.

Risk: LOW — L2 is already live and tested.
Priority: Later — dual-endpoint backup already operational.
```

## 6. Cloudflare (DNS / CDN)

```
Current Layer: L1
Vendor: Cloudflare (free tier)
Data Portable?: PARTIAL — DNS records exportable. CDN cache is ephemeral.

L2: Namecheap DNS, Route53, or registrar-native DNS
    Swap: 30-60 min. Export records, import at new provider.
L3: Self-hosted DNS is possible but not practical for a solo operation.
L4: No L4 equivalent for public DNS. DNS requires internet by definition.
    Mitigation: Document all DNS records in the repo as a backup.

Risk: MEDIUM — DNS is critical infrastructure. Cloudflare going hostile would
    require domain migration. Not instant but not catastrophic.
Priority: Later — document DNS records in repo as insurance.
```

## 7. OpenAI Whisper API (Planned)

```
Current Layer: Planned L1
Vendor: OpenAI (~US$0.006/min — UNVERIFIED)
Data Portable?: N/A — audio goes in, text comes out. No data stored.

L2: Deepgram (200 min/mo free), Google Cloud Speech-to-Text
    Swap: 10 min. Change API endpoint and key.
L3: Whisper (open-source) on VPS
    Swap: 2-3 hours. Same model, self-hosted.
L4: Whisper.cpp on local machine
    Swap: 1-2 hours. Slower on Aaron's hardware but functional.

Risk: LOW — Whisper model is open-source. The API is just convenience.
Priority: Later — not even adopted yet.
```

## 8. Context Bridge System

```
Current Layer: L4-native
Vendor: None — plain markdown files in git
Data Portable?: YES — it IS the portable format.

No decapitation needed. This system was designed to be vendor-agnostic from day one.
A human with a text editor can read and use every file.

Risk: NONE.
```

## 9. Persona / Swarm System

```
Current Layer: L1-L4
Vendor: None — plain markdown definitions. Any LLM can interpret them.
Data Portable?: YES — persona definitions are text files.

At L1: personas use Opus/Sonnet/Haiku for quality differentiation.
At L4: all personas run at Sonnet-equivalent max (local LLM limitation).
Quality degrades at L4 but structure survives.

Risk: NONE — the system is vendor-agnostic by design.
```

## 10. Node.js / npm

```
Current Layer: L4-native
Vendor: OpenJS Foundation (open-source)
Data Portable?: N/A — Node is a runtime, not a data store.

Not a sovereignty risk. Node.js is open-source, widely available,
and installed on all of Aaron's machines. No vendor lock-in.

Risk: NONE.
```

## 11. PowerShell Scripts

```
Current Layer: L4-native (Windows-specific)
Vendor: Microsoft (bundled with Windows)
Data Portable?: YES — scripts are text files.

L2: Bash equivalents (for Linux/Mac if Aaron ever switches OS).
    Swap: 1-2 hours per script to rewrite.
    Note: Git Bash on Windows can run basic bash scripts already.

Risk: LOW — Windows isn't going anywhere. If Aaron switches OS, scripts need porting.
Priority: Later — only relevant if Aaron moves to Linux.
```

## 12. Windows OS

```
Current Layer: L4-native
Vendor: Microsoft
Data Portable?: PARTIAL — repos are portable. OS config is not.

L2: Linux (Ubuntu or similar) — all tools (Node, git, Claude Code) work on Linux.
    Swap: 2-4 hours to set up a new machine. Repos clone instantly.
L4: Linux is inherently L4 (free, open-source, no licensing).

Risk: LOW — Aaron's data lives in git repos, not in the OS.
    Switching OS means reinstalling tools, not recovering data.
Priority: Later — only relevant if Microsoft does something hostile to Windows licensing.
```
