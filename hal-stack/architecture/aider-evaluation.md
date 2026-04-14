# Aider L2 Evaluation -- Claude Code Fallback Assessment

**Date:** April 14, 2026
**Machine:** EZbook (Windows 11, Celeron 5205U, 12GB RAM)
**Result:** INSTALLATION BLOCKED -- no Python/pip on this machine

## Phase 1: Installation

**Attempted:** `pip install aider-chat` and `pipx install aider-chat`
**Result:** Neither pip nor pipx is available on EZbook.

Python on EZbook is a Windows Store stub (`C:\Users\getkr\AppData\Local\Microsoft\WindowsApps\python.exe`) that redirects to the Microsoft Store instead of running Python. No real Python installation exists. No pip, no pipx.

**To unblock:** Install Python from python.org (not the Microsoft Store version). This adds pip automatically. Then `pip install aider-chat` should work.

Estimated time to unblock: 15 minutes (download Python installer, run, then `pip install aider-chat`).

## Phase 2: Test

**Not run.** Blocked on Phase 1.

## Assessment Based on Public Information

Aider is open-source (Apache 2.0), supports multiple LLM backends (Claude, GPT, Gemini, Ollama for local), and works via terminal. Key facts:

| Attribute | Aider | Claude Code |
|-----------|-------|-------------|
| License | Apache 2.0 (open source) | Proprietary (Anthropic) |
| LLM backends | Any (BYOK) | Claude only |
| Local model support | Yes (Ollama) | No |
| Cost | Free tool + API costs | Claude Pro subscription |
| L4 compatibility | Yes (with Ollama) | No |
| Git integration | Built-in | Built-in |
| Windows support | Yes (Python required) | Yes (Node required) |
| Context window | Depends on model | Depends on plan |

**Sovereignty assessment:** Aider is the strongest L2/L4 fallback for Claude Code. It's open-source, works with any LLM, supports local models via Ollama, and has built-in git integration. The only barrier is Python installation, which is a one-time 15-minute task.

## Recommendation

**Viable L2 fallback: YES.**

Aider should be installed on the i5 Lenovo (which may already have Python) or on EZbook after Python is installed. It does not replace Claude Code for daily work (Claude Code's context management and CLAUDE.md integration are superior), but it is a solid fallback if:
- Claude Code becomes unavailable
- Anthropic changes pricing
- A sovereignty drill requires L2 testing
- Aaron wants to test a different LLM on a specific task

## Next Steps

1. Install Python on EZbook (python.org, not Store version) -- 15 min
2. `pip install aider-chat` -- 2 min
3. Run Aider with a simple test edit on a non-critical file
4. Compare quality, speed, and usability vs Claude Code
5. Update decapitation-checklist.md with verified swap time

## Decapitation Checklist Update

The Claude Code entry in `decapitation-checklist.md` currently says:
- L2 swap: "30 minutes" (estimated, not tested)

Updated assessment:
- L2 swap (Aider): 15 minutes (install Python) + 2 minutes (install Aider) + 5 minutes (configure API key) = **22 minutes on a clean machine, 7 minutes if Python already installed**
- Swap is NOT yet tested. Marking as "documented but unverified" until Python is installed.
