<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:03 EST (Toronto)
Confidence: MEDIUM — L2/L3 swap times are estimates, not tested
Known gaps: L4 local LLM quality for code generation untested on Aaron's hardware
-->

# Decapitation Checklist

A template for documenting the swap path for any L1 component. Every component in the HAL Stack should have one of these filled out.

## Template

```
Component: [name]
Current Layer: [L1/L2/L3/L4]
Current Vendor: [who]
Monthly Cost: [amount]
Data Portable?: [yes/no — what format?]

L2 Swap:
  Candidate: [vendor]
  Swap Time: [estimate]
  Data Migration: [what moves, what doesn't]
  Cost Delta: [more/less/same]
  Tested?: [yes/no/partially]

L3 Swap:
  Candidate: [open-source tool + hosting]
  Swap Time: [estimate]
  Data Migration: [what moves]
  Cost Delta: [VPS cost]
  Tested?: [yes/no]

L4 Swap:
  Candidate: [open-source tool, local only]
  Swap Time: [estimate]
  Hardware Required: [specs]
  Quality Loss: [honest assessment]
  Tested?: [yes/no]

Decapitation Cost Summary:
  L1 → L2: [time + effort]
  L1 → L3: [time + effort]
  L1 → L4: [time + effort]
  Overall Risk: [LOW/MEDIUM/HIGH]
```

---

## Example: Claude Code CLI

```
Component: Claude Code CLI
Current Layer: L1
Current Vendor: Anthropic (Claude Pro plan, CA$27/month)
Monthly Cost: CA$27
Data Portable?: YES — all output is local files, git repos, markdown

L2 Swap:
  Candidate: Cursor IDE (GPT-4/Claude backend), Windsurf, Aider
  Swap Time: 30 minutes
  Data Migration: Repos are local git. CLAUDE.md → adapt to new tool's context format.
  Cost Delta: Cursor ~US$20/mo, Aider free (BYOK)
  Tested?: No — but repos are standard git, no lock-in

L3 Swap:
  Candidate: Aider + OpenRouter (cloud API, open-source client)
  Swap Time: 1 hour
  Data Migration: Repos stay. Prompts are markdown. Aider reads them.
  Cost Delta: OpenRouter pay-per-token, likely cheaper for low usage
  Tested?: No

L4 Swap:
  Candidate: Aider + Ollama + DeepSeek-Coder or CodeLlama (local)
  Swap Time: 2-4 hours (install Ollama, download model, configure Aider)
  Hardware Required: 16GB RAM minimum for decent code models. i5 will be slow. Desktop needed.
  Quality Loss: SIGNIFICANT for complex multi-file edits. Fine for simple changes.
  Tested?: No

Decapitation Cost Summary:
  L1 → L2: 30 min, LOW effort — just install and point at repos
  L1 → L3: 1 hour, LOW effort — Aider + API key
  L1 → L4: 2-4 hours, MEDIUM effort — needs desktop hardware for usable speed
  Overall Risk: LOW — all work product is in git, not in Claude
```

### Key Insight

The reason Claude Code's decapitation cost is LOW is that Aaron's work product lives in git repos as static HTML/CSS/JS and markdown. Claude Code is a tool that edits those files. Any tool that can edit files can replace it. The intelligence quality will vary, but the work is never trapped.

---

## Checklist Queue

Components that need a decapitation checklist filled out:

- [ ] GitHub (repos + Pages hosting)
- [ ] GitHub Actions (CI/CD)
- [ ] Formspree (form submissions)
- [ ] Web3Forms (backup form submissions)
- [ ] Cloudflare (DNS + CDN)
- [ ] Google Analytics (if used)
- [ ] Gmail (notifications + drafts pipeline)
- [ ] Claude.ai web (research + prompt drafting)
- [ ] n8n (when installed)
- [ ] Windows Task Scheduler (overnight builds)
