"""S-R01-PHASE-1f-CYBERTIP-PATCH — add Canadian Cybertip.ca reference
to the sextortion row (349a09cf-876a-816a-a0b2-d5b4bc4aa532).

The original 1f row (shipped 6e975a4) named only US-hosted reporting
channels (Take It Down, tips.fbi.gov, report.cybertip.org). In my
own audit of 1f I flagged 'add Cybertip.ca reference as Canadian-
specific follow-up' — this sprint closes that.

Uses `append_to_rich_text` (helper that predates today, used here
for the first time on new content) to append:
  1. A new paragraph to en-CA-Content naming Cybertip.ca
  2. A new paragraph to Research-Source with the Cybertip.ca +
     Canadian Centre for Child Protection citation

Appends are both under 1900 chars to fit the existing helper's
single-block assumption (chunking-aware append is filed as a
future small helper improvement).

Run once:   python _s_r01_phase_1f_cybertip_patch.py
"""
from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")

spec = importlib.util.spec_from_file_location(
    "nc", os.path.join(HERE, "notion-client.py")
)
nc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nc)


PAGE_ID = "349a09cf-876a-816a-a0b2-d5b4bc4aa532"

EN_CA_APPEND = (
    "\n**Canadian-specific reporting.** In Canada, the equivalent of "
    "the US CyberTipline is **Cybertip.ca** — Canada's national "
    "tipline for the online sexual abuse and exploitation of "
    "children, operated by the Canadian Centre for Child Protection "
    "since 2002. Cybertip.ca processes 2,200+ reports per month and "
    "receives an average of six sextortion reports per day. If "
    "you're a Canadian teen, you can report to Cybertip.ca directly "
    "— they forward serious incidents to law enforcement where "
    "appropriate. **Take It Down still works for you** (the hash-"
    "matching system is cross-border), but Cybertip.ca is the "
    "Canadian-hosted equivalent when you want a Canadian point of "
    "contact."
)

RESEARCH_APPEND = (
    "\nCybertip.ca (cybertip.ca) — Canada's national tipline for the "
    "online sexual abuse and exploitation of children, operated by "
    "the Canadian Centre for Child Protection (C3P) since September "
    "2002. Canadian equivalent to the US-hosted CyberTipline; accepts "
    "reports from Canadians and forwards to law enforcement as "
    "appropriate. As of 2025 Cybertip.ca has received 11,000+ "
    "sextortion incident reports, 5,800+ intimate images reports, and "
    "19,700+ luring/grooming reports; processes 2,200+ reports per "
    "month. Parent org: Canadian Centre for Child Protection "
    "(protectchildren.ca); also operates Project Arachnid (automated "
    "web crawler reducing availability of CSAM). Government of "
    "Canada March 2025 investment announcement "
    "(canada.ca/en/public-safety-canada/news/2025/03/government-of-"
    "canada-invests-in-protecting-children-and-youth-from-online-"
    "sexual-exploitation)."
)


def main() -> int:
    client = nc.NotionClient()

    print(f"en-CA-Content append: {len(EN_CA_APPEND)} chars")
    print(f"Research-Source append: {len(RESEARCH_APPEND)} chars")
    print()

    try:
        print("Appending to en-CA-Content...")
        client.append_to_rich_text(PAGE_ID, "en-CA-Content", EN_CA_APPEND)
        print("OK")

        print("Appending to Research-Source...")
        client.append_to_rich_text(PAGE_ID, "Research-Source", RESEARCH_APPEND)
        print("OK")

        print()
        print(f"SUMMARY: sextortion row {PAGE_ID} updated with Canadian Cybertip.ca reference.")
        return 0
    except Exception as e:
        print(f"FAIL: {type(e).__name__}: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
