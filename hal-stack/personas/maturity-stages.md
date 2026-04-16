# Maturity Stages

**Version:** 1.0 | **Created:** 2026-04-16

Every product and sprint operates at a maturity stage. The stage determines who reviews, what the ship criteria are, and how much friction is applied. Drew (Program Director) assigns the stage during intake.

---

## Stage 1: Prototype

**Audience:** Internal only. Aaron. Throwaway OK.
**Purpose:** Validate an idea, test a technical approach, or explore a concept.

| Area | Weight | Required Reviewers | Optional |
|------|--------|-------------------|----------|
| Technical | LOW | Drew | Sam |
| Brand | NONE | — | — |
| Legal/Privacy | NONE | — | — |
| Content | NONE | — | — |
| Scrappy Pack | STANDARD | All 5 (always) | — |

**Ship criteria:**
- [ ] Code committed with clear messages
- [ ] No secrets in repo
- [ ] SESSION-STATE.md updated
- [ ] Drew approves or Aaron overrides

---

## Stage 2: Alpha

**Audience:** Internal testing. Aaron + Claude reviewing output.
**Purpose:** Working software that will evolve. Not throwaway.

| Area | Weight | Required Reviewers | Optional |
|------|--------|-------------------|----------|
| Technical | MEDIUM | Drew, Sam (Sr Dev), Priya (QA) | Jordan (if infra) |
| Brand | LOW | — | Theo |
| Legal/Privacy | LOW | — | Anil (if user data) |
| Content | LOW | — | Maya |
| Scrappy Pack | STANDARD | All 5 (always) | — |

**Ship criteria:**
- [ ] All Stage 1 criteria
- [ ] No placeholder content in user-visible areas
- [ ] Basic accessibility check (heading hierarchy, alt text, labels)
- [ ] Lighthouse 80+ (performance + accessibility)

---

## Stage 3: Beta

**Audience:** Trusted testers. Brenda (real senior user). Library partners.
**Purpose:** Real users touching real software. Bugs hurt trust.

| Area | Weight | Required Reviewers | Optional |
|------|--------|-------------------|----------|
| Technical | HIGH | Drew, Sam, Priya | Jordan |
| Brand | MEDIUM | Theo (Brand), Maya (Content) | Ava (if launch) |
| Legal/Privacy | MEDIUM | Anil (Privacy) | Helen (if terms change) |
| Content | HIGH | Maya (Content), Theo (Brand) | Kai (if social) |
| Scrappy Pack | STANDARD | All 5 (always) | — |

**Ship criteria:**
- [ ] All Stage 2 criteria
- [ ] WCAG AA compliance (axe-core 0 critical/serious)
- [ ] Lighthouse 90+ (performance, accessibility, SEO)
- [ ] All links verified working
- [ ] Mobile tested at 375px minimum
- [ ] Content reviewed for tone (warm, patient, jargon-free for DCC)
- [ ] CHANGELOG.md updated

---

## Stage 4: Production

**Audience:** Paying or public users. Anyone on the internet.
**Purpose:** Revenue-generating or reputation-defining. Bugs cost money or trust.

| Area | Weight | Required Reviewers | Optional |
|------|--------|-------------------|----------|
| Technical | HIGH | Drew, Sam, Priya, Jordan | — |
| Brand | HIGH | Ava (CMO), Theo, Maya, Kai | — |
| Legal/Privacy | HIGH | Helen (GC), Anil, Dani (Risk) | Nora (if IP) |
| Content | HIGH | Maya, Theo | Kai (if social launch) |
| Financial | MEDIUM | — | Raj (if pricing), Fatima (if costs) |
| Scrappy Pack | HEAVY CHALLENGE | All 5 (always) | — |

**Ship criteria:**
- [ ] All Stage 3 criteria
- [ ] Security: CSP present, SRI on external scripts, no inline scripts
- [ ] SEO: JSON-LD structured data, OG tags, canonical, sitemap updated
- [ ] Legal: Privacy policy link, copyright notice, terms if applicable
- [ ] Brand: tone, colours, typography match brand guidelines
- [ ] Drew's full panel review logged in `review-log/`

---

## Stage 5: Scale

**Audience:** Revenue-critical. Multiple user segments. Partnerships depend on it.
**Purpose:** The business runs on this. Downtime or quality drops have financial consequences.

| Area | Weight | Required Reviewers | Optional |
|------|--------|-------------------|----------|
| Technical | CRITICAL | Drew, Sam, Priya, Jordan | — |
| Brand | HIGH | Ava, Theo, Maya, Kai | — |
| Legal/Privacy | CRITICAL | Helen, Anil, Nora, Dani | — |
| Financial | HIGH | Raj (CFO), Fatima, Marcus | Lin |
| Strategy | HIGH | Claire (CSO), Ethan | Rosa, Leo |
| Content | HIGH | Maya, Theo | — |
| Scrappy Pack | HEAVY CHALLENGE | All 5 (always) | — |

**Ship criteria:**
- [ ] All Stage 4 criteria
- [ ] Full boardroom review (all departments at Weight 2+)
- [ ] Raj reviews financial impact
- [ ] Claire reviews strategic alignment
- [ ] The Hand synthesizes — unanimous APPROVE or Aaron override with documented reason
- [ ] Rollback plan documented

---

## Current Product Stages

| Product | Current Stage | Justification |
|---------|-------------|---------------|
| DCC | Stage 3 (Beta) | Real users (seniors, libraries), no revenue yet |
| Career Coach | Stage 1 (Prototype) | Internal tool, not shipped to users |
| Clarity | Stage 1 (Prototype) | Concept only, not built |
| Aaron Patzalek site | Stage 2 (Alpha) | Live on GitHub Pages, no users yet |
| Two Birds Innovation site | Stage 2 (Alpha) | Placeholder, minimal traffic |
| HAL Stack | Stage 2 (Alpha) | Internal infrastructure |
| Kevin's Apartment | Stage 1 (Prototype) | Civic tool, limited scope |
| Kirk's Karate | Stage 2 (Alpha) | Client site, pending feedback |

Drew updates this table as products mature.
