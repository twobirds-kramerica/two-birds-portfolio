<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-11 16:30 EST (Toronto)
Confidence: MEDIUM — the retro works but has a known gap (Claude.ai can't read local files)
Known gaps: Claude.ai can't read Aaron's local files directly. See workarounds below.
-->

# Retro System — Retrospective Prompt

## How to Run a Retro

After a sprint finishes in Claude Code, open Claude.ai and get a status report.

### Step 1: Get the Sprint Results

You need to give Claude.ai the latest SESSION-STATE.md entry. Options:

**Option A (fastest): GitHub raw URL**
Paste this URL into the Claude.ai chat:
```
https://raw.githubusercontent.com/twobirds-kramerica/two-birds-portfolio/master/SESSION-STATE.md
```
Claude.ai can read this if it has web access. If not, use Option B.

**Option B (always works): Copy-paste**
Open `SESSION-STATE.md` on your machine, copy the latest session entry, paste into Claude.ai.

**Option C (quick): Screenshot**
Screenshot the Claude Code terminal showing the final commit output. Upload to Claude.ai.

### Step 2: Paste the Retro Prompt

After providing the session data, paste this:

```
RETRO — Sprint Retrospective

Read the session data I just provided. Report back with:

1. WHAT SHIPPED — list every file created or modified, one line each
2. STATUS — all good / issues found / human actions needed
3. HUMAN ACTIONS — anything I (Aaron) need to do personally, sorted by urgency:
   - NOW (do immediately)
   - SOON (this week)
   - LATER (when convenient)
4. BLOCKERS — anything that prevents the next sprint from running
5. NEXT RECOMMENDATION — should I:
   a) Run another sprint now (and which one)?
   b) Review something first?
   c) Take a break (it's late / you've been at it a while)?
6. QUESTIONS — anything that needs my decision before more work can proceed

Keep it SHORT. I'm reading this on my phone. Bullet points, not paragraphs.
```

## Known Limitation

**Claude.ai cannot directly read local files or Claude Code output.** There's always a manual step — Aaron must bring the data to Claude.ai via URL, copy-paste, or screenshot.

### Future Solutions

| Option | Effort | How It Works |
|--------|--------|-------------|
| GitHub raw URL | Works now | SESSION-STATE.md is pushed after every sprint. Claude.ai reads it via URL. |
| MCP integration | Future | Claude.ai reads files directly via Model Context Protocol. Not available yet for this setup. |
| n8n webhook | Future | Sprint results auto-posted to a URL Claude.ai can read. Requires n8n. |
| Shared context system | Future | The context bridge eliminates this gap entirely when both sides can read the same index. |

**Best option today: GitHub raw URL (Option A).** It works as long as the sprint pushed to master, which all sprints do.
