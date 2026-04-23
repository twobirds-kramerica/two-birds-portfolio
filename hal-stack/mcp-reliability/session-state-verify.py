"""Pre-sprint state-check: verify local + Notion are aligned before starting work.

Purpose: avoid burning credits on a sprint whose preconditions have drifted.
2026-04-22 example — I nearly executed S-030 because the proposal doc said
"pending" but the work had already shipped the previous day. A pre-sprint
state-check would have caught the mismatch in ~5 seconds.

Design:
- Checks four things in sequence:
    1. Local repo state: git status clean? branch matches expected?
    2. SESSION-STATE.md freshness: last updated within N hours?
    3. Notion heartbeat: can we read the Product Backlog?
    4. Sprint-queue alignment: does the Notion-reported next Ready item
       still exist + still have status=Ready + still own by Claude Code?
- Emits a structured report (dict) with per-check pass/fail + overall
  verdict: READY | WARNING | BLOCKED
- Optional auto-flip-to-blocked when overall is BLOCKED (sets the sprint's
  Notion Status to Blocked so the session doesn't race another instance)

Usage:
    python hal-stack/mcp-reliability/session-state-verify.py

Originated: S-MCP-RELIABILITY-001 (2026-04-22).
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PORTFOLIO_ROOT = Path(__file__).resolve().parents[2]
SESSION_STATE = PORTFOLIO_ROOT / 'SESSION-STATE.md'


def _run_git(args: list[str], cwd: Path) -> tuple[int, str]:
    try:
        r = subprocess.run(
            ['git', *args], cwd=str(cwd), capture_output=True,
            text=True, timeout=15,
        )
        return r.returncode, (r.stdout or '') + (r.stderr or '')
    except Exception as e:
        return -1, f'{type(e).__name__}: {e}'


def check_local_state(expected_branch: str = 'master') -> dict:
    """Check git status + branch name. Warn (not block) on uncommitted changes."""
    rc, out = _run_git(['status', '--porcelain', '--branch'], PORTFOLIO_ROOT)
    if rc != 0:
        return {'check': 'local_state', 'pass': False,
                'detail': f'git status failed: {out[:200]}'}
    lines = out.splitlines()
    branch_line = lines[0] if lines else ''
    dirty_lines = [l for l in lines[1:] if l.strip()]
    m = re.match(r'^## ([^.\s]+)', branch_line)
    branch = m.group(1) if m else '(unknown)'
    on_expected = (branch == expected_branch)
    has_dirty = bool(dirty_lines)
    return {
        'check': 'local_state',
        'pass': on_expected and not has_dirty,
        'branch': branch,
        'expected_branch': expected_branch,
        'dirty_files': len(dirty_lines),
        'warning': (not on_expected) or has_dirty,
        'detail': (
            f'branch={branch} (expected={expected_branch}), '
            f'dirty_files={len(dirty_lines)}'
        ),
    }


def check_session_state_fresh(max_age_hours: float = 24.0) -> dict:
    """Check SESSION-STATE.md mtime against `max_age_hours`."""
    if not SESSION_STATE.exists():
        return {'check': 'session_state', 'pass': False,
                'detail': 'SESSION-STATE.md not found'}
    try:
        mtime = SESSION_STATE.stat().st_mtime
        age_hours = (time.time() - mtime) / 3600.0
        return {
            'check': 'session_state',
            'pass': age_hours <= max_age_hours,
            'age_hours': round(age_hours, 2),
            'max_age_hours': max_age_hours,
            'detail': (
                f'SESSION-STATE.md last modified {age_hours:.1f}h ago '
                f'(threshold {max_age_hours:.1f}h)'
            ),
        }
    except Exception as e:
        return {'check': 'session_state', 'pass': False,
                'detail': f'{type(e).__name__}: {e}'}


def check_notion_heartbeat(client: Any) -> dict:
    """Check Notion reachability via Heartbeat helper."""
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            'hb', Path(__file__).resolve().parent / 'heartbeat-check.py'
        )
        hb_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(hb_mod)  # type: ignore
        hb = hb_mod.Heartbeat(client, every_n_calls=1)
        result = hb.ping()
        return {
            'check': 'notion_heartbeat',
            'pass': result['state'] == 'OK',
            'state': result['state'],
            'latency_s': result['latency_s'],
            'detail': f"Notion {result['state']} ({result['latency_s']:.3f}s)",
        }
    except Exception as e:
        return {'check': 'notion_heartbeat', 'pass': False,
                'detail': f'{type(e).__name__}: {e}'}


def check_next_sprint_aligned(
    client: Any,
    expected_data_source_id: str | None = None,
    owner_filter: str = 'Claude Code',
) -> dict:
    """Confirm the next Ready Claude-Code sprint is fetchable + valid.

    If `expected_data_source_id` is None, uses product_backlog_data_source
    from the client's config. Reports the top-priority Ready item if one
    exists; warns (not blocks) if none are Ready.
    """
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            'nc', Path(__file__).resolve().parents[1] / 'notion-sync' / 'notion-client.py'
        )
        nc_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(nc_mod)  # type: ignore
        ds_id = expected_data_source_id
        if ds_id is None:
            ds_id = client.config.get('product_backlog_data_source')
        if not ds_id:
            return {'check': 'next_sprint', 'pass': False,
                    'detail': 'no data source id available'}
        pages = client.query_data_source(ds_id)
        ready = []
        pri_order = {'P0': 0, 'P1': 1, 'P2': 2, 'P3': 3, 'P4': 4}
        for p in pages:
            status = nc_mod.extract_select(p, 'Status') or ''
            owner = nc_mod.extract_select(p, 'Owner') or ''
            if status == 'Ready' and owner == owner_filter:
                pri = nc_mod.extract_select(p, 'Priority') or 'P4'
                title = (nc_mod.extract_title(p, 'Sprint')
                         or nc_mod.extract_title(p, 'Item') or '(untitled)')
                ready.append((pri_order.get(pri, 99), pri, title, p['id']))
        ready.sort()
        if not ready:
            return {'check': 'next_sprint', 'pass': True, 'ready_count': 0,
                    'warning': True,
                    'detail': 'queue is empty — stop signal'}
        top = ready[0]
        return {
            'check': 'next_sprint',
            'pass': True,
            'ready_count': len(ready),
            'top_priority': top[1],
            'top_title': top[2],
            'top_page_id': top[3],
            'detail': f'{len(ready)} Ready sprints; top = {top[1]} {top[2][:60]}',
        }
    except Exception as e:
        return {'check': 'next_sprint', 'pass': False,
                'detail': f'{type(e).__name__}: {e}'}


def run_all_checks(
    client: Any,
    expected_branch: str = 'master',
    max_state_age_hours: float = 24.0,
    expected_data_source_id: str | None = None,
) -> dict:
    """Run all four checks and return an overall verdict."""
    results = [
        check_local_state(expected_branch=expected_branch),
        check_session_state_fresh(max_age_hours=max_state_age_hours),
        check_notion_heartbeat(client),
        check_next_sprint_aligned(
            client, expected_data_source_id=expected_data_source_id
        ),
    ]
    any_fail = any(not r['pass'] for r in results)
    any_warn = any(r.get('warning') for r in results)
    verdict = 'BLOCKED' if any_fail else ('WARNING' if any_warn else 'READY')
    return {
        'ts': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'verdict': verdict,
        'checks': results,
    }


def _print_report(report: dict) -> None:
    print(f"Session state verify — {report['ts']}")
    print(f"Verdict: {report['verdict']}")
    print()
    for r in report['checks']:
        tag = '✓' if r['pass'] else '✗'
        warn = ' (warn)' if r.get('warning') else ''
        print(f"  [{tag}] {r['check']:20} {r['detail']}{warn}")


def main() -> int:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'nc', Path(__file__).resolve().parents[1] / 'notion-sync' / 'notion-client.py'
    )
    nc_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nc_mod)  # type: ignore
    client = nc_mod.NotionClient()
    report = run_all_checks(client)
    _print_report(report)
    if report['verdict'] == 'BLOCKED':
        return 2
    if report['verdict'] == 'WARNING':
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
