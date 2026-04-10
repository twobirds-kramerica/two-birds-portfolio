<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:15 EST (Toronto)
Confidence: HIGH for EZbook (auto-detected), MEDIUM for others (from existing docs)
Known gaps: Pentium Silver specs incomplete, desktop specs unknown, i5 hostname unknown
-->

# Machine Profile System

A registry of all machines in the Two Birds Innovation fleet. Used to identify which machine is running a session, track what's installed where, and plan hardware upgrades.

**Layer:** L4-native — plain JSON + markdown, no cloud dependency

## How It Works

1. `machines.json` contains one entry per machine with specs, role, and status
2. `register-machine.ps1` auto-detects specs and adds/updates the current machine's entry
3. At session start, Claude Code (or any tool) can check `hostname` against the registry to know which machine it's on

## Current Fleet

| Machine | Role | Status | CPU | RAM |
|---------|------|--------|-----|-----|
| EZbook | Primary | Active | Celeron 5205U | 12 GB |
| i5 Lenovo | Secondary / overnight | Active | i5-6200U | 8 GB |
| Pentium Silver | Legacy fallback | Active | Pentium Silver | Unknown |
| Home Desktop | Future HAL server | Planned | TBD | TBD |

## Adding a New Machine

1. Clone the repos to the new machine
2. Run `register-machine.ps1` — it auto-detects specs and adds to `machines.json`
3. Commit and push
4. Other machines see the new entry on next pull

## Retiring a Machine

1. Set `"status": "retired"` and `"role": "retired"` in `machines.json`
2. Add a `retired_date` to notes
3. Commit and push

## How ID Persists

Machine identity lives in `machines.json` in the git repo, NOT in Claude Code's local config or any cloud service. If Claude Code is reinstalled, the machine is still identified by its hostname matching the registry. This is L4-native — no vendor dependency.

## Files

| File | Purpose |
|------|---------|
| `machines.json` | Machine registry (source of truth) |
| `register-machine.ps1` | Self-registration script |
| `claude-code-identifier.md` | How to identify current machine at session start |
| `README.md` | This file |
