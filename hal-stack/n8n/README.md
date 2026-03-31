# n8n — HAL Automation Engine

## What n8n Does for HAL
n8n is the automation backbone of the HAL Stack. It connects Gmail, GitHub, and local
services without writing custom backend code. Think: Zapier, but self-hosted and free.

## Installation
```
npm install -g n8n
n8n start
```
Access at: http://localhost:5678
Create admin account on first visit.

## Planned Workflows

### 1. Prompt Queue Monitor
- Trigger: Gmail label PROMPT-QUEUE applied
- Action: Write to SQLite, send confirmation email

### 2. Build Completion Detector
- Trigger: GitHub push webhook
- Action: Match commit → update prompt status → email confirmation

### 3. Morning Build Report
- Trigger: Cron 7 AM EST daily
- Action: Pull last 5 GitHub commits, open GitHub Issue, email summary

### 4. Failure Alert
- Trigger: Claude Code error pattern detected (via log file watch)
- Action: Immediate email to aaron.patzalek@gmail.com

### 5. Weekly LinkedIn Reminder
- Trigger: Cron Monday 8 AM EST
- Action: Pull next post from aaron-linkedin-posts.json, open GitHub Issue

## Workflow Files
Store exported n8n workflow JSON in this `workflows/` directory.
Export: n8n UI → Workflows → ... → Export
Import: n8n UI → Workflows → Import from file

## External Access (for GitHub webhooks)
n8n runs on localhost:5678 by default.
For GitHub webhooks to reach it, use Cloudflare Tunnel:
```
cloudflared tunnel run hal-n8n
```
See /docs/port-map.md for full tunnel setup instructions.
