# Sovereignty Sprint — Two Birds Innovation

**Created:** April 1, 2026
**Author:** Aaron Patzalek
**Purpose:** Ensure Two Birds Innovation can survive the loss, price change, or policy shift of any single vendor.

---

## Why This Exists

Two Birds Innovation was built on top of third-party platforms: Anthropic for AI, GitHub for hosting and version control, Google for email and calendar. Each one is excellent. None of them owe Aaron anything.

This sovereignty sprint documents every dependency, maps every risk, and builds a concrete exit plan for each. Not because anything is wrong today — but because the cost of preparing now is hours, while the cost of scrambling later is weeks.

---

## Reading Order

| # | Document | What It Covers |
|---|----------|----------------|
| 1 | [Sovereignty Audit](01-sovereignty-audit.md) | Every vendor dependency mapped with risk rating |
| 2 | [GitHub Redundancy Plan](02-github-redundancy-plan.md) | Mirror repos to Codeberg, deploy via Cloudflare Pages |
| 3 | [LLM Portability Layer](03-llm-portability-layer.md) | JS abstraction to swap between Claude, GPT-4o, Gemini, Ollama |
| 4 | [Vendor Prenuptial](04-prenuptial.md) | Exit triggers, 24-hour checklist, 30-day migration playbook |
| 5 | [IP Register](05-ip-register.md) | All intellectual property documented and timestamped |
| 6 | [HAL Portability Spec](06-hal-portability-spec.md) | Rebuild HAL from scratch with open-source alternatives |

---

## 3 Actions This Week

1. **Create Codeberg account** and mirror the top 3 revenue-critical repos (digital-confidence, career-coach, clarity). Takes 15 minutes.
2. **Create GitHub backup owner account** using twobirdsinnovation@gmail.com — invite as org owner. Takes 10 minutes.
3. **Test the LLM portability layer** in clarity by swapping the API config to a different provider for one test run. Takes 30 minutes.

---

## Doctrine

> "Use the best tools. Own the exit door."

Every vendor relationship should pass the Prenuptial Test: if they doubled their price tomorrow, could Aaron migrate in 30 days without losing a single customer or piece of work? If the answer is no, the mitigation plan in this folder tells you exactly what to fix.
