# Cal.com Setup — Two Birds Innovation

**Last updated:** 2026-05-27
**Status:** Live

## Account

| Field | Value |
|-------|-------|
| Platform | Cal.com hosted (free tier) |
| Account name | Two Birds In… |
| Slug | `twobirds-4n5ajg` |
| Email | twobirdsinnovation@gmail.com |
| Timezone | America/New_York (Eastern) |
| Base URL | `https://cal.com/twobirds-4n5ajg` |

## Active Event Types

| Name | Duration | URL |
|------|----------|-----|
| 15 min meeting | 15 min | `https://cal.com/twobirds-4n5ajg/15min` |
| 30 min meeting | 30 min | `https://cal.com/twobirds-4n5ajg/30min` |
| Secret meeting | 15 min | `https://cal.com/twobirds-4n5ajg/secret` (hidden) |

## Calendar Connections

- **Primary:** Google Calendar connected via OAuth (twobirdsinnovation@gmail.com)
- **Secondary calendars:** ICS feed integration attempted 2026-05-27 — blocked by Cal.com bug (known issue, open GitHub report). Tracked in Notion: `36da09cf-876a-8194-b110-e1632e3c6ce8` (P3)

### ICS Feed Workaround (when resolved)
Each additional Google Calendar exposes a secret iCal URL in Google Calendar → Settings → [calendar name] → "Integrate calendar" → "Secret address in iCal format". Add each URL via Cal.com → Settings → Connected Calendars → ICS Feed.

## Where it's used

- `aaron-patzalek/consulting.html` — 15-min intro call + 30-min discovery call booking buttons

## Sovereignty rationale

Cal.com is open-source (AGPL). The hosted free tier is used for speed to market. Migration path to self-hosted is available at any time — the open-source repo is `calcom/cal.com`. No freemium paywalls for the booking features we use. Booking data is exportable.

Preferred long-term: self-host on a VPS once infrastructure budget justifies it. This resolves the ICS multi-calendar issue natively and removes the Cal.com hosted dependency entirely.
