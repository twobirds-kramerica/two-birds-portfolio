# Public APIs Catalogue — Two Birds Products
**Date:** 2026-05-09 | **Sprint:** S-PUBLIC-APIS-001
**Source:** github.com/public-apis/public-apis + verified Canadian government APIs

---

## How to Use This Document

Each API is rated for immediate fit. "Static HTML safe" = can be called from client-side JS without a server proxy (CORS: Yes, no secret key needed). APIs requiring a server-side key need a backend layer — not currently in our stack — so they're noted as future/backend only.

---

## Career Coach — Job Market Data

| API | Auth | CORS | Cost | Fit | Notes |
|---|---|---|---|---|---|
| **The Muse** | apiKey | Unknown | Free tier | ⭐ Now | Job listings + company culture profiles. Free tier: 1,000 req/day. Key can be embedded in a static site (public read-only key). Canadian remote roles included. |
| **Remotive** | None | Yes | Free | ⭐ Now | `https://remotive.com/api/remote-jobs` — no auth, no key. Returns JSON of remote tech/marketing roles. Filterable by category. Ideal for Career Coach's "find remote Canadian work" feature. |
| **Reed** | apiKey | Unknown | Free tier | Future | UK-centric job board. 500K+ jobs. Requires server-side key (basic auth). Skip until Career Coach has a backend. |
| **StatCan Labour Force Survey** | None | Yes | Free | ⭐ Now | `https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410028703` — Canadian unemployment rates, job categories, industry data. No auth. Monthly releases. Gives Career Coach credible Canadian labour market context. |

**Top pick for Career Coach:** Remotive (no key, CORS-safe, remote roles) + StatCan LFS (Canadian market context).

---

## DCC — Digital Safety & Media Literacy

| API | Auth | CORS | Cost | Fit | Notes |
|---|---|---|---|---|---|
| **Have I Been Pwned (HIBP)** | apiKey | Yes | Free (personal) | ⭐ Now | `https://haveibeenpwned.com/api/v3/breachedaccount/{email}` — checks if an email was in a known data breach. Free for personal/educational use. Key required but publicly gettable. Maps directly to DCC Module: "Was my data leaked?" Seniors love this feature. |
| **PhishTank** | apiKey | Unknown | Free | Future | Community-curated phishing URL database. Requires server-side call (response format). Could power a "check this link" tool in DCC. |
| **Currents (News)** | apiKey | Yes | Free tier | ⭐ Now | `https://api.currentsapi.services/` — latest news, filterable by keyword. Free: 600 req/day. Could surface recent AI safety / digital literacy news in DCC's home page. CORS: Yes — static HTML safe with public key. |
| **Represent by Open North** | None | Unknown | Free | Research | Canadian electoral districts, politicians, contact info. `https://represent.opennorth.ca/` — no auth. Niche fit for a "contact your MP about digital rights" module. Low priority. |

**Top pick for DCC:** HIBP "was my data leaked?" tool — highest engagement potential with seniors. Currents news feed for a "what's happening in AI" sidebar.

---

## Clarity — Business Intelligence for SMBs

| API | Auth | CORS | Cost | Fit | Notes |
|---|---|---|---|---|---|
| **Bank of Canada Valet API** | None | Yes | Free | ⭐ Now | `https://www.bankofcanada.ca/valet/observations/FXCADUSD/json` — exchange rates, interest rates, CPI. No auth, CORS-safe. Could add "current economic context" to Clarity's diagnostic output (e.g., "Prime rate is 4.5% — financing a new tool is more expensive right now"). |
| **StatCan Business Register** | None | Yes | Free | ⭐ Now | `https://www150.statcan.gc.ca/` — Canadian business counts by industry, province, size. No auth. Could power Clarity's industry benchmark context: "How many SMBs in your sector use AI in Canada?" |
| **Open Corporates** | None (free tier) | Yes | Free | Future | Global company data — verify business name/registration. Free tier rate-limited. Useful for Clarity's intake flow ("let me verify your business exists"). Needs CORS proxy for some endpoints. |
| **NewsAPI** | apiKey | Unknown | Free tier (dev) | Future | News filtered by Canadian business keywords. Free dev tier: 100 req/day. Backend required (CORS blocked on client). Could feed a "what SMBs in your sector are doing with AI" sidebar in Clarity. |

**Top pick for Clarity:** Bank of Canada Valet (no auth, economic context) + StatCan business counts (Canadian benchmarking). Both are CORS-safe, no key required.

---

## Cross-Product Utility

| API | Auth | CORS | Use case |
|---|---|---|---|
| **REST Countries** | None | Yes | Country/locale data for any product — detect if user is Canadian, surface CA-specific content |
| **Open Exchange Rates** | apiKey | Yes | CAD/USD conversion — relevant if Clarity or Career Coach ever shows pricing data |
| **GNews** | apiKey | Yes | Alternative to Currents for DCC news feed. Free: 100 req/day |

---

## Integration Priority — Static HTML Safe (Use Now)

These require no backend, no secret keys, and are CORS-safe. Can be called directly from browser JS today:

| # | API | Product | What to build |
|---|---|---|---|
| 1 | **Remotive** | Career Coach | "Live remote jobs" panel — fetches current remote listings in tech/marketing |
| 2 | **Bank of Canada Valet** | Clarity | Economic context card — "Prime rate today: X% · CAD/USD: Y" |
| 3 | **StatCan LFS** | Career Coach | Canadian unemployment rate badge — shows current national + industry rate |
| 4 | **Currents** | DCC | "In the news: AI & digital safety" sidebar (public key in JS is acceptable for read-only) |

---

## Deferred (Need Backend / Server-Side Key)

- **HIBP** — most valuable for DCC, but email lookups should be proxied (don't expose user emails to client-side calls)
- **Reed / The Muse** — job APIs with private keys
- **NewsAPI** — CORS blocked on client
- **PhishTank** — URL lookup should be server-side

---

## Implementation Note for Static HTML Stack

For HIBP and other key-required APIs: a simple **Cloudflare Worker** (free tier, 100K req/day) can act as a proxy — the Worker holds the key server-side, forwards the request, and returns the result. This is the sovereign, zero-cost path to "backend" without a real server.

Cloudflare Worker template:
```js
// worker.js
export default {
  async fetch(req) {
    const email = new URL(req.url).searchParams.get('email');
    const res = await fetch(`https://haveibeenpwned.com/api/v3/breachedaccount/${email}`, {
      headers: { 'hibp-api-key': HIBP_KEY, 'user-agent': 'TwoBirds-DCC' }
    });
    return new Response(await res.text(), { status: res.status,
      headers: { 'Access-Control-Allow-Origin': '*' } });
  }
};
```

---
*Catalogued: 2026-05-09 | Source: public-apis/public-apis + StatCan + Bank of Canada + HIBP official docs*
