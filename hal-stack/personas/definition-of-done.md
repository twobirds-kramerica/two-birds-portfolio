# Definition of Done

**Version:** 1.0 | **Created:** 2026-04-16
**Enforced by:** Drew (Program Director)

---

## Baseline DoD (Every Stage, Every Sprint)

These apply regardless of maturity stage:

- [ ] Code committed with clear messages (`type(scope): description`)
- [ ] No placeholder content in user-visible areas (no "lorem ipsum", no "TODO", no "REPLACE_WITH")
- [ ] No banned words (per culture-spec: no "synergy", "leverage", "disrupt" as filler, no "great question")
- [ ] Canadian English spelling throughout
- [ ] No secrets in repo (`.gitignore` covers `.env`, API keys, credentials)
- [ ] SESSION-STATE.md updated with sprint results
- [ ] sprint-queue.md status updated (DONE, BLOCKED, etc.)

---

## Stage-Specific Additions

### Stage 1: Prototype
_Baseline only. No additional requirements._

### Stage 2: Alpha
- [ ] Basic accessibility: heading hierarchy, alt text on images, linked form labels
- [ ] Lighthouse 80+ (performance + accessibility categories)
- [ ] No inline `onclick` handlers (use `addEventListener`)

### Stage 3: Beta
- [ ] WCAG AA compliance: axe-core returns 0 critical and 0 serious issues
- [ ] Lighthouse 90+ (performance, accessibility, SEO)
- [ ] All links verified working (no 404s)
- [ ] Mobile tested at 375px minimum width
- [ ] Content reviewed for tone (matches brand guidelines)
- [ ] CHANGELOG.md updated
- [ ] Drew's review panel has logged APPROVE or REWORK

### Stage 4: Production
- [ ] All Stage 3 criteria
- [ ] CSP meta tag present
- [ ] SRI on external CDN scripts (where feasible)
- [ ] JSON-LD structured data present
- [ ] OG tags present (title, description, image, url)
- [ ] Canonical URL set
- [ ] Privacy policy linked (if user data collected)
- [ ] Brand alignment verified (colours, typography, tone)
- [ ] Drew's full panel review logged in `review-log/`

### Stage 5: Scale
- [ ] All Stage 4 criteria
- [ ] Full boardroom review completed
- [ ] Raj (CFO) signs off on financial impact
- [ ] Claire (CSO) signs off on strategic alignment
- [ ] Rollback plan documented
- [ ] The Hand synthesis logged

---

## REWORK Rules

If any required DoD item fails:
1. Drew issues REWORK verdict with specific fix list
2. Sprint status → BLOCKED (in sprint-queue.md)
3. Fix items documented in review log
4. Sprint re-enters queue as highest priority
5. Aaron can override REWORK with documented reason (logged as "AARON OVERRIDE: [reason]")

Drew does not have authority to override Aaron. Drew has authority to block until Aaron explicitly overrides.
