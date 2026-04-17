# Decapitation Checklist — Cloudflare

**Component:** Cloudflare DNS/CDN (#6)
**Story:** S1.3
**Current layer:** L1 (free tier)
**Risk:** MEDIUM (DNS is the least sovereign component)
**Last updated:** 2026-04-17

---

## What We Depend On

| Dependency | What It Does | Impact If Lost |
|-----------|-------------|----------------|
| Cloudflare DNS | Resolves domain names to GitHub Pages IPs | All custom domains stop working |
| Cloudflare CDN | Caches and accelerates static assets | Sites slow but still accessible via GitHub Pages URLs |
| Cloudflare SSL | Provides HTTPS for custom domains | Browser security warnings |

## DNS Records to Document

**ACTION REQUIRED:** Aaron to export DNS records from Cloudflare dashboard and paste here.

```
TODO: Aaron logs into Cloudflare → select domain → DNS → Export
Paste the zone file or screenshot the records here.
```

Current domains managed (estimated):
- twobirdsinnovation.com (if purchased)
- Any custom domains pointing to GitHub Pages

## L2 Fallback — Registrar DNS

**Swap procedure (30-60 min):**
1. Export DNS zone from Cloudflare dashboard (Download → BIND format)
2. Log into domain registrar (Namecheap, Google Domains, etc.)
3. Switch DNS servers from Cloudflare to registrar-native
4. Import records manually
5. Wait for DNS propagation (up to 48 hours, typically 2-4 hours)

## L3 Fallback — Self-hosted DNS

Not practical for a solo operation. DNS requires always-on servers with redundancy.

## L4 Fallback — None

DNS is an internet service by definition. No L4 equivalent exists.

**Mitigation:**
- All DNS records documented in this repo
- GitHub Pages sites accessible via `*.github.io` URLs without any DNS
- If custom domains are lost, update all links to use github.io URLs

## Emergency Procedure

If Cloudflare goes down or account is locked:
1. Sites still accessible via `twobirds-kramerica.github.io/*` URLs
2. Switch DNS to registrar (if zone file exported and documented)
3. Or: switch to Cloudflare Pages as hosting (removes GitHub Pages dependency too)

## Quarterly Drill Checklist

- [ ] Export DNS zone file from Cloudflare dashboard and save to this repo
- [ ] Verify custom domains resolve correctly
- [ ] Confirm github.io URLs still work as fallback
- [ ] Check Cloudflare account status (no billing issues, no abuse flags)
