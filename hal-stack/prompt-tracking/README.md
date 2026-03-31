# Prompt Tracking — HAL Stack

## The Problem
Aaron generates build prompts in Claude Web, pastes them into Claude Code on the i5,
and then loses track of which prompts ran, which failed, and which are still queued.
After a context window summary, it's unclear what was actually executed vs planned.

## Current Solution (Works Now — No Setup Required)
Use Gmail drafts as a manual prompt queue.

1. **In Claude Web:** When you generate a build prompt, say:
   "Save this as a Gmail draft with subject: ⏳ UNCONFIRMED PROMPT — [topic]"

2. **In Claude Code:** Paste and run the prompt.

3. **After completion:** Say to Claude Web:
   "Find the Gmail draft with subject ⏳ UNCONFIRMED PROMPT — [topic] and update subject to ✅ CONFIRMED — [topic]"

4. **Morning check:** Open Gmail, search: `subject:⏳` to see what's still queued.

## Target Solution (n8n — April 2026)
See schema.md for the full automated system design.
Once n8n is installed and running on port 5678:
- Prompts automatically logged to SQLite on label creation
- Completions automatically confirmed via GitHub webhook
- Daily email digest of prompt status
- Mobile dashboard showing queue state

## Files
- `schema.md` — Database schema and n8n workflow design
