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

---

## RI-006 — Normal-Mode "Next Sprint" Loop on Empty Queue
**Date:** 2026-04-22
**Symptom:** Aaron types "next sprint" 3+ times in the same normal-mode session. Each call: Notion exit 3, pending-capture empty, sprint-queue.md has only human-task items. Each Claude response lists the same 3-4 candidate sprints and asks Aaron to pick. No forward motion. Today: triggered at ~04:30 EST after a ~75-sprint max-mode run ending ~01:00 EST; queue legitimately drained.
**Root cause:** Normal-mode governance explicitly forbids auto-flipping Backlog→Ready. Max-mode governance explicitly allows it. There is no middle-ground trigger: no single phrase Aaron can type meaning *"just pick the best one and execute — one sprint, not a max-mode chain."* Result: if Aaron expects forward motion and the queue is empty, every "next sprint" returns the same menu and the loop stalls.
**Systemic fix options (pick one — all require Aaron's call):**
  1. **Add trigger phrase** to CLAUDE.md: "**just go**" or "**best-pick sprint**" = authorise Claude to flip the highest-LOE-ranked Backlog or research-proposal item to Ready and execute it once. Single sprint, no chaining, no max-mode persistence. Cheapest fix.
  2. **Pre-fill the queue**: nightly job that promotes 1-2 research-proposal sprints to Ready status if the Claude-Code-owned Ready count drops to zero. Removes the governance choice by not letting the queue empty.
  3. **Hard-stop rule** after 2 consecutive empty-queue "next sprint" calls: Claude refuses to list options a third time and instead declares the pattern + asks the binary (execute X yes/no).
**Status:** FIXED 2026-04-22 via Fix #1 — "just go" trigger phrase added to CLAUDE.md (single-sprint authorization in normal mode; does not chain; does not persist; git-log-grep required pre-pick). Aaron activated max mode after 7 empty-queue triggers this session; "just go" will close the gap for future normal-mode sessions. Fires #2 and #3 of systemic-fix options remain as future-enhancement candidates but Fix #1 is the cheapest and sufficient baseline.

---

## RI-007 — Google Drive MCP Under-Scoped / Large-File MCP Upload Infeasible
**Date:** 2026-04-22
**Symptom:** Aaron requests "upload file X to Google Drive folder Y via Drive MCP." Both `search_files` and `create_file` (folder creation, zero content) return `"Request had insufficient authentication scopes."` even though the MCP is connected.
**Root cause (two stacked issues):**
  1. The Drive MCP OAuth grant is under-scoped — likely has `drive.readonly` or narrower; missing `drive.file` / `drive` / `drive.metadata` for search + create. Aaron needs to re-authorise the MCP with upload + metadata scopes via Claude's MCP settings UI.
  2. Even if scope were granted, the `create_file` tool takes content as a single base64 argument. For files >~5-10 MB this is impractical — a typical Claude conversation export of ~82 MB gzips to ~17 MB, encodes to ~22 MB JSON string, which is at or over most MCP tool argument size limits.
**Systemic fix:**
  1. Re-authorise the Google Drive MCP with write scopes (drive.file at minimum) via Claude.ai MCP settings. Verify with a zero-content folder-creation round-trip.
  2. For large files (>5 MB compressed), use Google Drive desktop sync (drop file into the synced folder on disk, Drive uploads in background) or the browser at drive.google.com. The MCP is not suited to large-payload uploads regardless of scope.
  3. For structured Claude-conversation archives specifically, consider writing a small helper at `hal-stack/notion-sync/` or similar that splits conversations.json into per-conversation files + uploads each individually via the MCP (post-scope-fix). Splits a 82 MB blob into manageable per-file arguments, and gives per-conversation findability in Drive.
**Status:** LOGGED — awaiting Aaron's MCP re-authorisation. Workaround: upload via Drive desktop sync or browser.
