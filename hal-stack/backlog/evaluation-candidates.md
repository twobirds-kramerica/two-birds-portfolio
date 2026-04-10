<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:30 EST (Toronto)
Confidence: MEDIUM — evaluations based on public info, not hands-on testing
Known gaps: Pricing and features may have changed since last checked
-->

# HAL Stack — Evaluation Candidates

Tools and services Aaron has flagged for potential use. Each assessed for sovereignty compatibility.

## notebooklm-py

| Field | Value |
|-------|-------|
| **What** | Unofficial Python client for Google NotebookLM |
| **Layer** | L1-only (Google proprietary, unofficial API) |
| **Priority** | P3 |
| **Status** | Parked |
| **Use case** | Audio summaries of documents |
| **Sovereignty risk** | HIGH — unofficial API, could break anytime, Google-locked |
| **Recommendation** | Evaluate for fun, do not depend. No L4 path exists. |
| **Next action** | None — revisit only if a stable API emerges |

## Marketing Skills for AI Agents

| Field | Value |
|-------|-------|
| **What** | Prompt/skill library for marketing tasks |
| **Layer** | L1 (designed for cloud LLMs, but prompts are portable text) |
| **Priority** | P3 |
| **Status** | Not evaluated |
| **Use case** | LinkedIn content, pitch writing, email sequences |
| **Sovereignty risk** | LOW — prompts are plain text, work with any LLM |
| **Recommendation** | Low effort to evaluate. Worth a 30-minute review. |
| **Next action** | Skim library, extract 3-5 useful prompts for Two Birds use cases |

## Remotion

| Field | Value |
|-------|-------|
| **What** | Programmatic video creation in React |
| **Layer** | L1-L4 (open-source, runs locally, React-based) |
| **Priority** | P3 |
| **Status** | Parked |
| **Use case** | Automated video content for LinkedIn, DCC tutorials |
| **Sovereignty risk** | LOW — MIT license, runs locally |
| **Recommendation** | Park until video content is needed. Good L4 option when ready. |
| **Next action** | None until video becomes a priority |

## Banana Claude

| Field | Value |
|-------|-------|
| **What** | Claude interface with Gemini BYOK (bring your own key) |
| **Layer** | L1-only (web tool, Gemini dependency) |
| **Priority** | P3 |
| **Status** | Parked |
| **Use case** | Alternative Claude-like interface for research |
| **Sovereignty risk** | MEDIUM — web tool, two vendor dependencies |
| **Recommendation** | Interesting but not needed while Claude Code works. |
| **Next action** | None |

## Aider

| Field | Value |
|-------|-------|
| **What** | Open-source AI pair programming in terminal |
| **Layer** | L1-L4 (open-source, works with any LLM backend including local) |
| **Priority** | P2 |
| **Status** | Not evaluated |
| **Use case** | L2/L4 fallback for Claude Code |
| **Sovereignty risk** | VERY LOW — MIT license, BYOK, supports Ollama for L4 |
| **Recommendation** | HIGH value as L2/L4 documented fallback. Worth a 1-hour evaluation sprint. |
| **Next action** | Install, test with one small edit on a non-critical repo, document in decapitation checklist |

## Ollama

| Field | Value |
|-------|-------|
| **What** | Local LLM runner — download and run models locally |
| **Layer** | L4-native |
| **Priority** | P2 |
| **Status** | Not installed |
| **Use case** | L4 backbone for intent parsing, code assistance, general LLM tasks |
| **Sovereignty risk** | NONE — fully local, open-source |
| **Recommendation** | Install on desktop when it arrives. Test on i5 Lenovo if curious about performance. |
| **Next action** | Install after desktop arrives, test with Llama 3 and DeepSeek-Coder |
