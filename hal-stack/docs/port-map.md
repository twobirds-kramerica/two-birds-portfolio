# HAL Stack Port Map

| Service | Port | Protocol | Status | Notes |
|---------|------|----------|--------|-------|
| n8n web UI | 5678 | HTTP | ⏳ Pending | Automation engine dashboard |
| OpenCode server | 3000 | HTTP/WS | ⏳ Pending | Remote Claude Code from mobile |
| LightRAG server | 9621 | HTTP | ⏳ Pending | Knowledge graph API |
| LightRAG graph UI | 9621 | HTTP | ⏳ Pending | /webui path |

## Firewall Notes
- All services run on localhost only by default
- OpenCode requires port forwarding or VPN for remote access
- n8n webhook endpoint needs to be reachable by GitHub for push events
  → Use ngrok or Cloudflare Tunnel for external webhook access

## ngrok Quick Start (for n8n webhooks)
```
npm install -g ngrok
ngrok http 5678
```
Copy the HTTPS URL → use as webhook endpoint in GitHub settings.
Note: Free ngrok URL changes on restart. Pin with a paid account or use Cloudflare Tunnel.

## Cloudflare Tunnel (Permanent, Free Alternative to ngrok)
```
winget install Cloudflare.cloudflared
cloudflared tunnel login
cloudflared tunnel create hal-n8n
cloudflared tunnel route dns hal-n8n n8n.your-domain.com
cloudflared tunnel run hal-n8n
```
