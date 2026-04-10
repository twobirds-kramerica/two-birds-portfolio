<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:15 EST (Toronto)
Confidence: HIGH — simple hostname match
Known gaps: None
-->

# Claude Code Machine Identification

How Claude Code (or any tool) identifies which machine it's running on.

## Method

At session start, compare the system hostname against `machines.json`:

### PowerShell One-Liner

```powershell
$h = $env:COMPUTERNAME; $m = (Get-Content hal-stack\machine-profile\machines.json | ConvertFrom-Json).machines | Where-Object { $_.hostname -eq $h }; if ($m) { Write-Host "Machine: $($m.nickname) | Role: $($m.role) | RAM: $($m.specs.ram_gb)GB" } else { Write-Host "UNKNOWN MACHINE: $h — run register-machine.ps1" }
```

### Bash One-Liner (Git Bash / WSL)

```bash
hostname | xargs -I{} grep -A2 '"hostname": "{}"' hal-stack/machine-profile/machines.json
```

## How to Use in CLAUDE.md

Add to any repo's CLAUDE.md:

```
## Machine Detection
Run: hostname
Match against hal-stack/machine-profile/machines.json to identify current machine.
```

## Why This Matters

- Different machines have different capabilities (EZbook has 12GB RAM, i5 has 8GB)
- Overnight builds run on i5, not EZbook
- Future desktop will run always-on services
- Machine identity persists across Claude Code reinstalls because it lives in git

## What Persists

| Where | What | Survives Reinstall? |
|-------|------|-------------------|
| `machines.json` in git | Machine identity, specs, role | Yes |
| Claude Code local config | Session history, preferences | No |
| `CLAUDE.md` in repo | Repo-specific context | Yes |

The critical insight: machine identity lives in the **repo**, not in the **tool**. Any tool that can read a JSON file can identify the machine.
