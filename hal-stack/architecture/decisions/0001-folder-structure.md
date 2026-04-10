<!--
STATUS: v0.1 — DRAFT — NEEDS AARON REVIEW
Created: 2026-04-10 02:05 EST (Toronto)
Confidence: HIGH
Known gaps: None
-->

# ADR-0001: HAL Stack Folder Structure

**Date:** 2026-04-10
**Status:** Accepted
**Layer:** L4-native (plain folders and markdown)

## Context

HAL Stack needs a folder structure that is:
- Navigable by a human with a file browser (L4)
- Readable by any LLM given the directory listing (L1-L3)
- Extensible without restructuring

## Decision

```
hal-stack/
├── README.md                    — what HAL is, quick start
├── architecture/                — design docs, principles, ADRs
│   ├── overview.md
│   ├── principles.md
│   ├── sovereignty-principles.md
│   ├── decapitation-checklist.md
│   ├── layer-tags.md
│   └── decisions/               — Architecture Decision Records
│       └── 0001-folder-structure.md
├── context-system/              — cross-session context bridge
├── voice-layer/                 — voice-to-machine interface
├── machine-profile/             — hardware registry
├── backlog/                     — epics, stories, evaluations
├── sessions/                    — sprint logs and results
├── n8n/                         — automation workflows (existing)
├── prompt-tracking/             — prompt lifecycle (existing)
├── scripts/                     — utility scripts (existing)
└── docs/                        — reference docs (existing)
```

## Consequences

- Each subsystem gets its own directory with its own README.
- New subsystems are added as new directories, never by modifying existing ones.
- The structure mirrors how Aaron thinks about the system: by capability, not by file type.
