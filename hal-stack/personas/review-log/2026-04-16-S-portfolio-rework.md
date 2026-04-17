# Sprint Review: Portfolio Site Deep Rework

**Date:** 2026-04-16
**Stage:** 2 (Alpha — Aaron reviews before public)
**Panel:** Theo, Maya, Priya, Ava + Scrappy Pack
**Sprint type:** Content + Frontend

---

## Panel Reviews

### Theo (Brand Strategist) — APPROVED
The brand story now accurately reflects brand-name-research.md. The chevrons section explains headwinds/tailwinds, the intersection point, and the fraternal paths metaphor. Sovereignty over autonomy is clearly stated as the differentiator. The motto and mantra appear in the philosophy banner. The visual anchor (><) is described in context, not just mentioned. DCC is correctly labelled "Beta" with no external link. Products show honest statuses: Beta, In Development, Architecture. The "7 products shipped in 90 days" claim is removed. **This matches the brand docs.**

### Maya (Content Director) — APPROVED with note
Copy is direct, genuine, and reads like Aaron wrote it rather than a copywriter. No banned words detected. The twin girls language is personal without being saccharine — "The name is personal and deliberate: everything I build is, at its core, for them" is honest. The restaurant origin story ("when the Friday night rush hits, you either have a system or you have chaos") grounds the process improvement narrative in lived experience rather than credentials. The Staples entry is consolidated correctly with the progressive path noted. **Note:** The philosophy banner quote has smart quotes — verify these render correctly in all browsers.

### Priya (QA / Testing) — APPROVED
Skip link present. All form inputs have linked labels. ARIA labels on nav, decorative elements marked `aria-hidden="true"`. Heading hierarchy: h1 (hero) → h2 (sections) → h3 (subsections) → h4 (skill groups), no skips. Mobile hamburger with `aria-expanded`. CSP meta tag present. JSON-LD Person schema present. `prefers-reduced-motion` respected. og:image meta tag present (file needs to be created). **No accessibility regressions.**

### Ava (CMO) — APPROVED
This page would make a Chamber of Commerce contact take Aaron seriously as a founder. The career timeline shows progression and breadth. The brand story section gives depth that most portfolio sites lack — it explains *why* the company exists, not just *what* it does. The sovereignty framing positions Two Birds as principled, not just functional. The "In development" badges on Clarity and Career Coach are honest, which is better than empty promises. **Would recommend Aaron share this URL once og:image and headshot are resolved.**

---

## Scrappy Pack

### Mack (Cash) — APPROVED
"The products section is honest about what makes money (nothing yet) and what exists (DCC beta). That honesty will serve you better with a Chamber audience than false confidence."

### Tess (Visibility) — APPROVED
"The brand story section is shareable content. Post the sovereignty vs autonomy paragraph on LinkedIn as a standalone thought piece."

### Grit (Time) — APPROVED
"One sprint to rewrite the whole site content. Good use of time. Don't touch it again until you have real testimonials or a headshot."

### Patch (Simplicity) — APPROVED
"Same 3-file structure. No new dependencies. The philosophy banner is just HTML and CSS. Clean."

### Sage (Long game) — APPROVED
"The restaurant origin story is the most human thing on this page. It makes the 20 years of product work feel earned, not claimed. Keep it."

---

## Drew's Synthesis

**Verdict:** APPROVED

**Summary:** All panel members approve. No REWORK items. The content now accurately reflects the brand docs, career history is complete and consolidated, product statuses are honest, and the brand story section gives the site genuine depth. Stage 2 DoD met.

**Pre-launch items (before Stage 3):**
1. Create og-card.png (1200x630 social sharing image)
2. Add real headshot or approve AI-generated image
3. Test Formspree endpoint
4. Verify smart quotes render in all browsers

---

## Aaron's Final Call

**Decision:** _[PENDING — Aaron to review and decide]_
