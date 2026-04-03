# Reliability Issues Log
Tracks systemic failures discovered through repeated troubleshooting.
Created: April 2, 2026

---

## RI-001 — GitHub Raw CDN Cache Stale After Push
**Date:** April 2, 2026
**Symptom:** Aaron types "retro" in Claude Web, sees yesterday's LAST-RUN-SUMMARY.md content even though the file was updated and pushed minutes ago.
**Root cause:** GitHub's raw.githubusercontent.com CDN caches files for several minutes after push. No way to force invalidation.
**Systemic fix:** Renamed file from `logs/LAST-RUN-SUMMARY.md` to `logs/RETRO.md` to break the cache URL. Added CDN note as final line of every retro file. PRIMARY retro method is now `cat logs/RETRO.md` in PowerShell (always accurate).
**Status:** FIXED ✅ — new URL, new workflow documented in CLAUDE.md

---

## RI-002 — Remote Control Builds Do Not Execute
**Date:** April 2, 2026
**Symptom:** Aaron pastes a build prompt into Claude Web remote control. Claude acknowledges the prompt but does not execute any file writes, git commands, or commits.
**Root cause:** claude.ai/code/scheduled runs in Anthropic's cloud with a read-only git proxy. It can read repos but cannot push. Remote control prompts are treated as conversation, not execution.
**Systemic fix:** Do not use remote control for builds. Use "Run now" on cloud scheduler for one-off triggers, or Windows Task Scheduler on i5 for overnight automation. Remote control is for reading and planning only.
**Status:** DOCUMENTED ✅ — added to RELIABLE WORKFLOW in CLAUDE.md

---

## RI-003 — Duplicate Work Across Sessions
**Date:** April 2, 2026
**Symptom:** Aaron pastes the same build prompt in a new session. Claude rebuilds files that were already built and pushed in a prior session, wasting 30+ minutes.
**Root cause:** Each Claude Code session starts with no memory of prior sessions. Without reading git log first, Claude has no way to know what already exists.
**Systemic fix:** Standing rule in CLAUDE.md: "Never rebuild something already built — check git log first." Added to every sprint file header: "Run git log --oneline -5 first." Pattern counter rule: if Aaron asks the same thing 3+ times, declare the pattern broken.
**Status:** MITIGATED ✅ — rules in place, but depends on session discipline

---

## RI-004 — Pasted Prompts Arrive After Work Already Done
**Date:** April 2, 2026
**Symptom:** Aaron prepares prompts in advance (e.g., in Gmail drafts or Notes). By the time they are pasted into Claude Code, the work has already been completed in an earlier session. The prompt runs anyway, duplicating effort or conflicting with existing files.
**Root cause:** Prompts are written when the work is needed, but pasted asynchronously — sometimes hours or sessions later. No mechanism to check "is this still needed?" before execution.
**Systemic fix:** Every pasted prompt should begin with "Switch to [repo], run git log --oneline -5 first" so Claude can verify current state before acting. The pattern counter rule catches repeated paste-and-execute cycles.
**Status:** MITIGATED ✅ — git log check is now standard

---

## RI-005 — Claude Says "Done" Without Verification
**Date:** April 2, 2026
**Symptom:** Claude reports a task as complete but the output was not verified (e.g., file exists but content is wrong, push succeeded but CDN shows old data, commit made but not actually pushed).
**Root cause:** Claude optimises for speed and reports completion at the earliest reasonable point rather than triple-checking.
**Systemic fix:** Pattern counter rule: "Never say 'yes it works' unless confirmed 3 times in a row." For critical outputs (RETRO.md, module HTML files), verify: file exists, line count reasonable, bilingual content present, git push confirmed, no errors in output.
**Status:** DOCUMENTED ✅ — pattern counter rule added to CLAUDE.md
