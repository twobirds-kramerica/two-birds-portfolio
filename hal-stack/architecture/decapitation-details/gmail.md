# Decapitation Checklist — Gmail Pipeline

**Component:** Gmail (not in original 12, added as S1.4)
**Story:** S1.4
**Current layer:** L1 (Google free tier)
**Risk:** MEDIUM (single point of failure for all business communication)
**Last updated:** 2026-04-17

---

## What We Depend On

| Dependency | What It Does | Impact If Lost |
|-----------|-------------|----------------|
| Gmail (aaron.patzalek@gmail.com) | All business email — clients, partners, job search, Formspree notifications | Total communication blackout |
| Gmail (getkramer@gmail.com) | Personal + some business overlap | Partial communication loss |
| Google Contacts | Contact database | Lose contact lookup (contacts also on phone) |
| Google Drive | Assessment results, historical CVs, documents | Lose access to Drive-only files |
| Google Calendar | Scheduling | Lose calendar (phone backup exists) |

## Email Addresses in Use

| Email | Purpose | Configured In |
|-------|---------|--------------|
| aaron.patzalek@gmail.com | Primary business, CV, job applications | LinkedIn, Formspree, all sites |
| getkramer@gmail.com | Personal, GitHub account, some legacy | GitHub, Claude Code |

## L2 Fallback — Proton Mail or Outlook

**Swap procedure (1-2 hours):**
1. Create Proton Mail account (free tier, encrypted, privacy-focused)
2. Set up Gmail forwarding to new address (Settings → Forwarding)
3. Update critical accounts: LinkedIn, GitHub, Formspree, job boards
4. Add new email to phone
5. Update email in CLAUDE.md, config files, and portfolio site

**Proton Mail recommended** — aligns with sovereignty principle (Swiss-hosted, encrypted, privacy-first).

## L3 Fallback — Self-hosted email

Not recommended for a solo operation. Email hosting requires SPF, DKIM, DMARC, IP reputation management. Use Proton Mail or Fastmail instead.

## L4 Fallback — None

Email is an internet service. No L4 equivalent.

**Mitigation:**
- Phone number is a fallback contact method
- LinkedIn InMail works without email
- Export Gmail periodically via Google Takeout

## Data Backup

**Google Takeout (quarterly):**
1. Go to takeout.google.com
2. Select: Gmail, Drive, Contacts, Calendar
3. Export as .mbox (email) + .zip (files)
4. Save to local drive and/or Pentium Silver
5. Time: ~30 min to initiate, download when ready

**Status:** TODO — Aaron has not yet run a Google Takeout backup.

## Emergency Procedure

If Gmail is locked or Google account suspended:
1. Phone is immediate fallback for critical contacts
2. LinkedIn InMail for professional contacts
3. Create Proton Mail account (5 min)
4. Notify key contacts (Phil, Mike K, iA Financial) of new address
5. Update Formspree notification email
6. Recovery: Google account recovery process (can take days)

## Quarterly Drill Checklist

- [ ] Run Google Takeout (Gmail + Drive + Contacts)
- [ ] Save export to local drive
- [ ] Verify recovery email and phone number are current in Google account
- [ ] Check that 2FA is enabled on Google account
- [ ] Verify Formspree notifications are arriving
