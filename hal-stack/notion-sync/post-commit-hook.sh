#!/usr/bin/env bash
# post-commit-hook.sh — Claude Code PostToolUse hook
#
# Triggered when Claude Code runs a `git commit *` Bash command. Appends a
# bulleted-list-item block describing the commit to the Notion page
# "SESSION-STATE (Live)" (348a09cf-876a-815c-a9ed-cd8a4ab2767e).
#
# Mechanical data only (hash / subject / author / files / timestamp). The
# "Next Action: [blocker analysis]" semantic field is written by Claude at
# sprint-completion time via SESSION-STATE.md, not by this hook.
#
# Fails soft: any missing dependency, missing API key, network error, or
# Notion API error exits 0 silently. The hook never blocks a commit.

set -u

NOTION_PAGE_ID="348a09cf-876a-815c-a9ed-cd8a4ab2767e"
NOTION_VERSION="2025-09-03"
TIMEOUT=10

# --- Guards: if anything is missing, exit cleanly. --------------------------
[ -z "${NOTION_API_KEY:-}" ] && exit 0
command -v git  >/dev/null 2>&1 || exit 0
command -v curl >/dev/null 2>&1 || exit 0
command -v jq   >/dev/null 2>&1 || exit 0

# --- Read hook stdin (JSON from Claude Code). -------------------------------
if [ -t 0 ]; then
  STDIN=""
else
  STDIN=$(cat)
fi

# --- Filter: only proceed for `git commit` commands. ------------------------
# The settings.json `if` field already pre-filters, but defence in depth.
CMD=$(printf '%s' "$STDIN" | jq -r '.tool_input.command // empty' 2>/dev/null)
case "$CMD" in
  *git\ commit*) ;;   # includes simple, chained with &&, subshells, here-docs
  *) exit 0 ;;
esac

# --- Collect commit metadata. Exit silently if HEAD can't be read. ----------
cd "$(jq -r '.cwd // empty' <<<"$STDIN" 2>/dev/null || true)" 2>/dev/null || true

git rev-parse --verify HEAD >/dev/null 2>&1 || exit 0
SHORT=$(git rev-parse --short HEAD 2>/dev/null)   || exit 0
HASH=$(git rev-parse HEAD 2>/dev/null)            || exit 0
SUBJECT=$(git log -1 --format=%s 2>/dev/null)     || exit 0
AUTHOR=$(git log -1 --format=%an 2>/dev/null)     || exit 0
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "?")
REPO=$(basename "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null || echo "?")

# First 6 changed files, comma-separated
FILES=$(git show --name-only --format= HEAD 2>/dev/null | head -6 | paste -sd ', ' -)
[ -z "$FILES" ] && FILES="(no files)"

# ISO8601 UTC timestamp
TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# --- Build the Notion PATCH body. -------------------------------------------
# One bulleted_list_item block appended to the page's children.
# Subject is quoted; hash is styled as code.
BODY=$(jq -cn \
  --arg ts      "$TS" \
  --arg short   "$SHORT" \
  --arg subject "$SUBJECT" \
  --arg author  "$AUTHOR" \
  --arg branch  "$BRANCH" \
  --arg repo    "$REPO" \
  --arg files   "$FILES" \
  '{
    children: [
      {
        type: "bulleted_list_item",
        bulleted_list_item: {
          rich_text: [
            { type: "text", text: { content: ($ts + "  ") } },
            { type: "text", text: { content: $short }, annotations: { code: true } },
            { type: "text", text: { content: ("  " + $subject + "  \u2014  " + $author + " on " + $repo + "/" + $branch) } },
            { type: "text", text: { content: ("  [" + $files + "]") }, annotations: { italic: true, color: "gray" } }
          ]
        }
      }
    ]
  }') || exit 0

# --- POST to Notion. Silent on failure. -------------------------------------
HTTP=$(curl -sS -o /dev/null -w "%{http_code}" \
  -X PATCH "https://api.notion.com/v1/blocks/${NOTION_PAGE_ID}/children" \
  -H "Authorization: Bearer ${NOTION_API_KEY}" \
  -H "Notion-Version: ${NOTION_VERSION}" \
  -H "Content-Type: application/json" \
  --max-time "${TIMEOUT}" \
  -d "$BODY" 2>/dev/null || echo "000")

# Log failures (but don't block).
if [ "$HTTP" != "200" ] && [ "$HTTP" != "201" ]; then
  # Best-effort log to hal-stack/notion-sync/SYNC-LOG.md. Swallow errors.
  LOG="$(git rev-parse --show-toplevel 2>/dev/null)/hal-stack/notion-sync/SYNC-LOG.md"
  if [ -n "$LOG" ] && [ -d "$(dirname "$LOG")" ]; then
    printf -- "- %s \u2014 post-commit-hook: HTTP %s on commit %s (%s)\n" \
      "$TS" "$HTTP" "$SHORT" "$SUBJECT" >> "$LOG" 2>/dev/null || true
  fi
fi

exit 0
