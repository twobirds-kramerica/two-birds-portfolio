"""Route a sprint failure to Notion + aaron-todos, without halting the loop.

Designed to be called from any sprint's FINAL STEP when something went wrong
that a human needs to act on. Two output surfaces:

  1. Notion Product Backlog: new row, Priority=P1, Status=Blocked, Owner=Aaron,
     Type=Human Action. Notes includes the sprint ID, failing step, error
     output, and recommended fix.
  2. aaron-todos-YYYY-MM-DD.md: one-line P1 entry under "Autonomous failure
     routed here" section, so the todos file remains the single canonical
     human-review surface.

The caller's sprint continues (returns 0) regardless of whether routing
succeeded. This is the explicit opposite of halting on error: sprint-loop
durability > single-failure escalation.

USAGE (from any sprint script):

    from failure_router import route_failure

    try:
        do_sprint_step()
    except Exception as e:
        route_failure(
            sprint_id="S-FOO-BAR",
            step="Step 3: deploy to Vercel",
            error=str(e),
            recommended_fix="Complete Vercel OAuth at https://vercel.com/oauth/device",
            product="DCC",
        )
        # sprint continues to next step or exits cleanly

CLI USAGE (for shell-script sprints):

    python hal-stack/sprint-system/failure-router.py \\
        --sprint-id S-FOO-BAR \\
        --step "Step 3: deploy to Vercel" \\
        --error "No credentials found" \\
        --fix "Complete Vercel OAuth" \\
        --product DCC

Exit codes:
  0 — routing succeeded on at least one surface (Notion or aaron-todos)
  1 — routing failed on both surfaces (caller should still not halt the loop)
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent

_nc_spec = importlib.util.spec_from_file_location(
    "notion_client_mod", REPO_ROOT / "hal-stack" / "notion-sync" / "notion-client.py"
)
_nc = importlib.util.module_from_spec(_nc_spec)  # type: ignore
_nc_spec.loader.exec_module(_nc)  # type: ignore


def _today_todos_path() -> Path:
    """Return the aaron-todos file for today, creating a dated stub if needed."""
    today = datetime.now().strftime("%Y-%m-%d")
    dated = REPO_ROOT / "hal-stack" / "sprint-system" / f"aaron-todos-{today}.md"
    if dated.exists():
        return dated
    # Fall back to the most recent existing aaron-todos-* file (tonight's work
    # all lives in aaron-todos-2026-04-21.md, which stays canonical until the
    # next day's file is created).
    candidates = sorted(
        (REPO_ROOT / "hal-stack" / "sprint-system").glob("aaron-todos-*.md"),
        reverse=True,
    )
    return candidates[0] if candidates else dated


def _append_to_todos(
    sprint_id: str, step: str, error: str, recommended_fix: str, notion_id: str | None
) -> bool:
    """Append a P1 entry under an 'Autonomous failures routed here' section."""
    path = _today_todos_path()
    if not path.exists():
        path.write_text(
            f"# Aaron — To-Do Backlog from {datetime.now().strftime('%Y-%m-%d')}\n\n",
            encoding="utf-8",
        )

    marker = "## P1 — Autonomous failures routed here"
    block = (
        f"\n- [ ] **{sprint_id} — {step}**\n"
        f"  Error: {error}\n"
        f"  Recommended fix: {recommended_fix}\n"
        f"  Notion: `{notion_id or 'n/a (Notion routing failed)'}`\n"
        f"  Logged: {datetime.now().strftime('%Y-%m-%d %H:%M')} EST by failure-router.py\n"
    )

    try:
        content = path.read_text(encoding="utf-8")
        if marker in content:
            insert_at = content.index(marker) + len(marker)
            new_content = content[:insert_at] + block + content[insert_at:]
        else:
            new_content = content.rstrip() + f"\n\n---\n\n{marker}\n{block}\n"
        path.write_text(new_content, encoding="utf-8")
        return True
    except Exception:
        return False


def route_failure(
    sprint_id: str,
    step: str,
    error: str,
    recommended_fix: str,
    product: str | None = None,
) -> int:
    """Route a failure to Notion + aaron-todos. Returns 0 on any success, 1 on total failure."""
    notion_id: str | None = None
    notion_ok = False

    try:
        client = _nc.NotionClient()
        page = _nc.create_backlog_item(
            client,
            item=f"{sprint_id} — autonomous failure: {step}",
            priority="P1",
            status="Blocked",
            owner="Aaron",
            type_="Human Action",
            product=product,
            notes=(
                f"Auto-filed by failure-router.py at {datetime.now().strftime('%Y-%m-%d %H:%M')} EST.\n\n"
                f"**Sprint:** {sprint_id}\n"
                f"**Failing step:** {step}\n"
                f"**Error:**\n```\n{error}\n```\n"
                f"**Recommended fix:** {recommended_fix}\n\n"
                f"The sprint loop was NOT halted by this failure — subsequent sprints continued. "
                f"This item is Aaron's to unblock when convenient."
            ),
        )
        notion_id = page.get("id")
        notion_ok = True
        print(f"FAILURE-ROUTER: filed Notion entry {notion_id}")
    except Exception as e:
        print(f"FAILURE-ROUTER: Notion routing failed: {e}", file=sys.stderr)

    todos_ok = _append_to_todos(sprint_id, step, error, recommended_fix, notion_id)
    if todos_ok:
        print(f"FAILURE-ROUTER: appended to {_today_todos_path().name}")
    else:
        print(f"FAILURE-ROUTER: aaron-todos append failed", file=sys.stderr)

    return 0 if (notion_ok or todos_ok) else 1


def _cli() -> int:
    p = argparse.ArgumentParser(description="Route a sprint failure to Notion + aaron-todos.")
    p.add_argument("--sprint-id", required=True)
    p.add_argument("--step", required=True)
    p.add_argument("--error", required=True)
    p.add_argument("--fix", dest="recommended_fix", required=True)
    p.add_argument("--product", default=None)
    args = p.parse_args()
    return route_failure(
        sprint_id=args.sprint_id,
        step=args.step,
        error=args.error,
        recommended_fix=args.recommended_fix,
        product=args.product,
    )


if __name__ == "__main__":
    sys.exit(_cli())
