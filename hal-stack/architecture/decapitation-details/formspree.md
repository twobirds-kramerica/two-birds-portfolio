# Decapitation Checklist — Formspree

**Component:** Formspree (#5)
**Story:** S1.2
**Current layer:** L1 (free tier, 50 submissions/month)
**Risk:** LOW (L2 already active)
**Last updated:** 2026-04-17

---

## What We Depend On

| Dependency | What It Does | Impact If Lost |
|-----------|-------------|----------------|
| Formspree endpoint | Receives form submissions from DCC feedback + portfolio contact | Forms stop working until endpoint swapped |
| Formspree dashboard | View submissions, export CSV | Lose submission history |

## Current Endpoints

| Site | Endpoint ID | Purpose |
|------|------------|---------|
| DCC (index.html) | `xeerqryj` | Feedback modal + email capture |
| Aaron Patzalek portfolio | `xeerqryj` (shared) | Contact form |

**Issue:** Both sites share one endpoint. Should be separate for clean tracking.

## L2 Fallback — Web3Forms (ALREADY ACTIVE)

Web3Forms is already wired as a silent backup in `feedback-github.js`.

**Swap procedure (15 min):**
1. Change `action="https://formspree.io/f/xeerqryj"` to Web3Forms endpoint URL
2. Update JS files that reference the Formspree endpoint
3. Test submission

## L3 Fallback — Self-hosted webhook

**Action plan (2-3 hours):**
1. Set up n8n or a simple Express endpoint on VPS
2. Configure webhook to receive POST data
3. Store in SQLite or send via email relay
4. Update form action URLs

## L4 Fallback — mailto: link

No server-side form processing possible at L4. Workaround:
- Replace form with `mailto:aaron.patzalek@gmail.com` link
- User's email client opens with pre-filled subject
- Ugly but functional

## Emergency Procedure

If Formspree goes down:
1. Forms show error to users
2. Swap to Web3Forms (already in codebase): change endpoint URL, push
3. 15-minute recovery

## Quarterly Drill Checklist

- [ ] Submit test form on DCC and verify it appears in Formspree dashboard
- [ ] Submit test form on portfolio and verify receipt
- [ ] Verify Web3Forms backup endpoint still works
- [ ] Export Formspree submissions CSV as backup
