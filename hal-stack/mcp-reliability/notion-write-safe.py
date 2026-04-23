"""Safe Notion MCP/API write wrapper with retry + write-verification.

Prevents the 2026-04-22 silent-failure class of bugs: a Notion POST succeeds
but the subsequent client logic crashes (e.g., cp1252 stdout on Windows)
before the caller can log success. Also catches the reverse: a POST that
returns malformed data and silently no-ops.

Design:
- `safe_notion_write(operation_fn, operation_name, ...)` wraps any callable
  that makes a Notion write
- Exponential backoff retry (default 2 attempts)
- Response verification: must have `id` OR caller-supplied verifier returns True
- Optional post-write read-back via `verify_read_fn` — reads the written
  object and confirms it exists server-side (catches the case where a
  client-side crash masks a server-side success)
- Every attempt logged to `LOG_FILE` (append-only, ISO timestamps)
- On exhaustion, writes a structured entry to `FALLBACK_FILE` for manual
  recovery — the caller gets None back and can alert or proceed

Usage:
    from pathlib import Path
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'notion_write_safe',
        Path('hal-stack/mcp-reliability/notion-write-safe.py'),
    )
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

    result = mod.safe_notion_write(
        operation_fn=lambda: client.create_page(data_source_id, properties),
        operation_name='create_page:Product Backlog:S-XXX',
    )
    if result is None:
        print('WARN: write failed after retries; see fallback file')

Bundled with this file (same directory):
    heartbeat-check.py       — lightweight Notion fetch every N calls
    session-state-verify.py  — pre-sprint state check

Originated: S-MCP-RELIABILITY-001 (2026-04-22).
"""
from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Optional

# Logs default to the portfolio root so they're visible to SESSION-STATE
# flows. Override via env vars for testing.
_DEFAULT_LOG = os.environ.get(
    'MCP_RELIABILITY_LOG',
    str(Path(__file__).resolve().parents[2] / 'logs' / 'mcp-write-log.txt'),
)
_DEFAULT_FALLBACK = os.environ.get(
    'MCP_RELIABILITY_FALLBACK',
    str(Path(__file__).resolve().parents[2] / 'logs' / 'mcp-write-fallback.json'),
)

LOG_FILE = _DEFAULT_LOG
FALLBACK_FILE = _DEFAULT_FALLBACK


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def _ensure_dir(path_str: str) -> None:
    p = Path(path_str).parent
    p.mkdir(parents=True, exist_ok=True)


def log_write(
    operation: str,
    result: Any,
    success: bool,
    attempt: int = 1,
    log_file: str = LOG_FILE,
) -> None:
    """Append a single-line record of a write attempt.

    Never raises — log failures are silent so they don't mask the real
    operation's outcome. If the log can't be written, we move on.
    """
    try:
        _ensure_dir(log_file)
        tag = 'OK' if success else 'FAIL'
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(
                f"{_now_iso()} | {tag:4} | attempt={attempt} | "
                f"{operation} | {str(result)[:300]}\n"
            )
    except Exception:
        pass  # never let logging fail the write path


def _default_verifier(result: Any) -> bool:
    """Default response verifier — must have either `id` or a non-empty
    `results` / `pages` collection."""
    if not isinstance(result, dict):
        return False
    if result.get('id'):
        return True
    for key in ('results', 'pages', 'page'):
        v = result.get(key)
        if isinstance(v, (list, tuple)) and v:
            return True
        if isinstance(v, dict) and v.get('id'):
            return True
    return False


def _record_fallback(
    operation_name: str,
    attempts: list,
    fallback_file: str = FALLBACK_FILE,
) -> None:
    """Record a failed write in a JSON append-style file for manual recovery.

    Each line is a self-contained JSON object (JSONL format). Safe to tail.
    """
    try:
        _ensure_dir(fallback_file)
        record = {
            'ts': _now_iso(),
            'operation': operation_name,
            'attempts': attempts,
        }
        with open(fallback_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(record, ensure_ascii=False, default=str) + '\n')
    except Exception:
        pass  # best-effort


def safe_notion_write(
    operation_fn: Callable[[], Any],
    operation_name: str,
    max_retries: int = 2,
    initial_backoff_s: float = 1.0,
    verify_response_fn: Callable[[Any], bool] = _default_verifier,
    verify_read_fn: Optional[Callable[[Any], bool]] = None,
    log_file: str = LOG_FILE,
    fallback_file: str = FALLBACK_FILE,
) -> Optional[Any]:
    """Wrap a Notion write with retry + verification.

    Args:
        operation_fn: zero-arg callable that performs the write.
        operation_name: label for logs (e.g. 'create_page:Product Backlog:S-XXX').
        max_retries: total attempts (NOT extra attempts; 2 = primary + 1 retry).
        initial_backoff_s: seconds for first backoff; doubles each retry.
        verify_response_fn: given the result, returns True if it looks valid.
        verify_read_fn: optional — given the result, perform a server-side
            read and return True if the write is visible. Recommended for
            create_page (caller reads the new page id) when silent-failure
            detection matters most. Skipped if None.
        log_file, fallback_file: override paths (env vars take precedence
            if set at import time).

    Returns:
        The operation result on success, or None on total failure.
    """
    attempts_log: list = []
    backoff = initial_backoff_s

    for attempt in range(1, max_retries + 1):
        err_msg: Optional[str] = None
        result: Any = None
        try:
            result = operation_fn()
        except Exception as e:
            err_msg = f'{type(e).__name__}: {e}'

        if err_msg is not None:
            log_write(operation_name, err_msg, success=False,
                      attempt=attempt, log_file=log_file)
            attempts_log.append({
                'attempt': attempt, 'ts': _now_iso(),
                'outcome': 'exception', 'detail': err_msg,
            })
        else:
            if not verify_response_fn(result):
                log_write(
                    operation_name,
                    f'response verification failed: {result!r}',
                    success=False, attempt=attempt, log_file=log_file,
                )
                attempts_log.append({
                    'attempt': attempt, 'ts': _now_iso(),
                    'outcome': 'bad_response', 'detail': str(result)[:300],
                })
            else:
                # Response looks valid — optionally read-back-verify.
                if verify_read_fn is not None:
                    try:
                        if verify_read_fn(result):
                            log_write(operation_name, result, success=True,
                                      attempt=attempt, log_file=log_file)
                            return result
                        else:
                            log_write(
                                operation_name,
                                f'read-back verification failed; response={result!r}',
                                success=False, attempt=attempt,
                                log_file=log_file,
                            )
                            attempts_log.append({
                                'attempt': attempt, 'ts': _now_iso(),
                                'outcome': 'readback_failed',
                                'detail': str(result)[:300],
                            })
                    except Exception as e:
                        log_write(
                            operation_name,
                            f'read-back verifier raised: {type(e).__name__}: {e}',
                            success=False, attempt=attempt, log_file=log_file,
                        )
                        attempts_log.append({
                            'attempt': attempt, 'ts': _now_iso(),
                            'outcome': 'readback_exception',
                            'detail': f'{type(e).__name__}: {e}',
                        })
                else:
                    log_write(operation_name, result, success=True,
                              attempt=attempt, log_file=log_file)
                    return result

        # If we reach here, this attempt failed. Backoff unless last attempt.
        if attempt < max_retries:
            time.sleep(backoff)
            backoff *= 2

    # All attempts exhausted — record fallback
    _record_fallback(operation_name, attempts_log, fallback_file=fallback_file)
    return None


# ---- Convenience helpers ---------------------------------------------------

def verify_page_exists_fn(client: Any) -> Callable[[Any], bool]:
    """Build a verify_read_fn that confirms a just-created page is
    fetchable server-side. Caller passes a NotionClient.

    Usage:
        result = safe_notion_write(
            operation_fn=lambda: client.create_page(ds_id, props),
            operation_name='create_page:X',
            verify_read_fn=verify_page_exists_fn(client),
        )
    """
    def _verify(result: Any) -> bool:
        pid = None
        if isinstance(result, dict):
            pid = result.get('id')
        if not pid:
            return False
        try:
            page = client.get_page(pid)
            return bool(page and page.get('id') == pid and not page.get('archived'))
        except Exception:
            return False
    return _verify


def verify_select_value_fn(
    client: Any, page_id: str, property_name: str, expected: str,
) -> Callable[[Any], bool]:
    """Build a verify_read_fn for a `set_select` call.

    Usage:
        safe_notion_write(
            operation_fn=lambda: client.set_select(pid, 'Status', 'Done'),
            operation_name='set_select:Status=Done',
            verify_read_fn=verify_select_value_fn(client, pid, 'Status', 'Done'),
        )
    """
    def _verify(_result: Any) -> bool:
        try:
            page = client.get_page(page_id)
            prop = page.get('properties', {}).get(property_name, {})
            sel = prop.get('select') or {}
            return sel.get('name') == expected
        except Exception:
            return False
    return _verify


__all__ = [
    'safe_notion_write',
    'log_write',
    'verify_page_exists_fn',
    'verify_select_value_fn',
    'LOG_FILE',
    'FALLBACK_FILE',
]


if __name__ == '__main__':
    # Minimal smoke: log an entry (no Notion call)
    log_write('smoke-test', 'safe-write module import + log OK', success=True)
    print(f'Smoke OK. Log file: {LOG_FILE}')
