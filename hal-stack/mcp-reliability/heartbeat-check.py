"""Heartbeat check: lightweight Notion read every N tool calls.

Purpose: detect Notion MCP / API disconnection early instead of at the
next write. The 2026-04-22 session's RI-007 (Drive MCP under-scoped)
and the S-041 cp1252 crash both showed that silent MCP-layer failures
can waste credits before a write actually fails; a periodic heartbeat
catches layer-level issues faster than waiting for the next real write.

Design:
- In-process counter `tick()` — call from wrapper code at every MCP
  operation; every N ticks trigger a `ping()`
- `ping()` does a bounded query against a known-cheap data source
  (the Product Backlog by default) with a tight timeout
- Outcomes: OK | SLOW | DISCONNECTED — all three logged with timestamp
- Returns a dict the caller can inspect; `raise_on_disconnect=True`
  turns DISCONNECTED into an exception
- Zero cost when N > ticks since last ping

Usage:
    from heartbeat_check import Heartbeat
    hb = Heartbeat(client, every_n_calls=10)
    hb.tick()   # at every MCP write/read elsewhere
    status = hb.ping(force=True)  # manual check
    if status['state'] == 'DISCONNECTED':
        # pause the loop, alert, or bail

Originated: S-MCP-RELIABILITY-001 (2026-04-22).
"""
from __future__ import annotations

import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

_DEFAULT_LOG = os.environ.get(
    'MCP_RELIABILITY_LOG',
    str(Path(__file__).resolve().parents[2] / 'logs' / 'mcp-write-log.txt'),
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


class HeartbeatError(RuntimeError):
    """Raised when ping detects a disconnection and raise_on_disconnect=True."""


class Heartbeat:
    """Lightweight liveness probe for Notion MCP/API.

    Attributes:
        client: a NotionClient-shaped object with a `query_data_source` method
        every_n_calls: ping frequency (ticks between pings)
        timeout_warn_s: pings slower than this log as SLOW
        log_file: path to append heartbeat results
    """

    def __init__(
        self,
        client: Any,
        every_n_calls: int = 10,
        timeout_warn_s: float = 2.0,
        log_file: str = _DEFAULT_LOG,
        probe_data_source_id: Optional[str] = None,
    ) -> None:
        self.client = client
        self.every_n_calls = max(1, int(every_n_calls))
        self.timeout_warn_s = float(timeout_warn_s)
        self.log_file = log_file
        self._calls_since_ping = 0
        self._last_ping_ts: Optional[float] = None
        self._last_state: str = 'UNKNOWN'
        # Default to Product Backlog data source if caller doesn't override
        self._probe_ds = probe_data_source_id or self._discover_probe_ds()

    def _discover_probe_ds(self) -> Optional[str]:
        try:
            cfg = getattr(self.client, 'config', None) or {}
            return cfg.get('product_backlog_data_source')
        except Exception:
            return None

    def _log(self, state: str, latency_s: float, note: str = '') -> None:
        try:
            Path(self.log_file).parent.mkdir(parents=True, exist_ok=True)
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(
                    f"{_now_iso()} | HEARTBEAT | {state:13} | "
                    f"latency={latency_s:.3f}s | {note}\n"
                )
        except Exception:
            pass  # never block real work

    def tick(self) -> Optional[dict]:
        """Increment counter; ping if threshold reached.

        Returns None if no ping was due, else the ping result dict.
        """
        self._calls_since_ping += 1
        if self._calls_since_ping >= self.every_n_calls:
            return self.ping()
        return None

    def ping(self, force: bool = False, raise_on_disconnect: bool = False) -> dict:
        """Perform a bounded query against a cheap data source.

        Returns a dict: {state, latency_s, ts}.
        State values: OK | SLOW | DISCONNECTED | MISCONFIGURED
        """
        self._calls_since_ping = 0
        self._last_ping_ts = time.time()

        if not self._probe_ds:
            out = {'state': 'MISCONFIGURED', 'latency_s': 0.0,
                   'ts': _now_iso(), 'note': 'no probe_data_source_id'}
            self._log(out['state'], 0.0, out['note'])
            self._last_state = out['state']
            if raise_on_disconnect:
                raise HeartbeatError(out['note'])
            return out

        start = time.time()
        try:
            # Query but don't paginate — the first page is enough to confirm
            # reachability. query_data_source pages internally; for a cheap
            # probe we accept the default behaviour on small data sources.
            _ = self.client.query_data_source(self._probe_ds)
            latency = time.time() - start
            state = 'OK' if latency <= self.timeout_warn_s else 'SLOW'
            out = {'state': state, 'latency_s': latency, 'ts': _now_iso()}
            self._log(state, latency)
            self._last_state = state
            return out
        except Exception as e:
            latency = time.time() - start
            note = f'{type(e).__name__}: {e}'
            out = {'state': 'DISCONNECTED', 'latency_s': latency,
                   'ts': _now_iso(), 'note': note}
            self._log('DISCONNECTED', latency, note)
            self._last_state = 'DISCONNECTED'
            if raise_on_disconnect:
                raise HeartbeatError(note) from e
            return out

    @property
    def last_state(self) -> str:
        return self._last_state


__all__ = ['Heartbeat', 'HeartbeatError']


if __name__ == '__main__':
    # Self-test: import NotionClient, run a single ping, print result
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'nc', Path(__file__).resolve().parents[1] / 'notion-sync' / 'notion-client.py'
    )
    nc_mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(nc_mod)  # type: ignore
        client = nc_mod.NotionClient()
        hb = Heartbeat(client, every_n_calls=1)
        result = hb.ping()
        print(f"Heartbeat: {result['state']} in {result['latency_s']:.3f}s")
        if result.get('note'):
            print(f"  note: {result['note']}")
    except Exception as e:
        print(f'Smoke test failed: {type(e).__name__}: {e}')
        print('This usually means NOTION_API_KEY is missing or the probe DS ID is wrong.')
