# Automation Governance — Rules 1-4

Rules for all HAL Stack automation. Prevents the class of bugs where scripts
assume Notion's schema and break silently when a status option name changes.

---

## Rule 1: Verify Before Acting

Every automation script reads current state before making changes.
- `next-sprint.py` fetches fresh Notion data, picks "Ready", THEN sets "In Progress"
- Never assume a sprint is still in the expected state — always fetch first
- Pre-flight checklist: `.claude/verification-checklist.md`

## Rule 2: Status Strings Come from One Place

**Source of truth: `.claude/status-semantics.yaml`**

No script may hardcode a status string. Load it at runtime:

```python
import re
from pathlib import Path

def load_status_semantics(repo_root: Path) -> dict:
    path = repo_root / ".claude" / "status-semantics.yaml"
    data: dict = {}
    try:
        with open(path, encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                m = re.match(r'^(\w+)\s*:\s*(.+)$', line)
                if not m:
                    continue
                key, val = m.group(1), m.group(2).strip()
                if val.startswith('['):
                    data[key] = re.findall(r'"([^"]+)"', val)
                else:
                    data[key] = val.strip('"')
    except OSError:
        pass
    return data

sem = load_status_semantics(repo_root)
auto_pick      = sem.get("auto_pick_status",    "Ready")
in_progress    = sem.get("in_progress_status",  "In Progress")
done_statuses  = sem.get("done_statuses",        ["Done"])
```

If Notion's status options ever change, update `status-semantics.yaml` once.
All scripts pick up the new values without code edits.

## Rule 3: Sprint Shape Is Defined in One Place

**Source of truth: `.claude/sprint-schema.json`**

Scripts that produce or consume sprint objects must conform to this schema.
Required fields: `notion_id`, `item`, `priority`, `status`.

Quick validation (no external deps):
```python
import json
from pathlib import Path

schema = json.loads((repo_root / ".claude" / "sprint-schema.json").read_text())
required = schema.get("required", [])
missing = [f for f in required if f not in sprint_dict]
if missing:
    raise ValueError(f"Sprint missing required fields: {missing}")
```

## Rule 4: Every Sprint Ends with a Next Action

Every sprint ends with exactly one of:
1. A "Next recommended action for Aaron" block in SESSION-STATE.md, OR
2. A "Next sprint: S-XXX" recommendation if the loop should continue autonomously

Sprints left "In Progress" in Notion longer than 24h are flagged as orphaned
by `loop-pr-babysitter.md`. Rule 4 prevents dead ends in the automation chain.

---

**SSOT files (read these, not hardcoded values):**
| File | What it owns |
|------|-------------|
| `.claude/status-semantics.yaml` | Notion status strings + auto-pick logic |
| `.claude/sprint-schema.json` | Sprint payload shape + required fields |
| `.claude/verification-checklist.md` | Pre-flight checks before each sprint |
| `.claude/automation-governance.md` | These rules |

*Phase 1 created: 2026-05-08 — Automation Governance System*
*Phase 2 (next week): `audit-sprints.py` nightly enforcement*
*Phase 3 (week after): system prompt reads SSOT on startup*
