"""S-PRIMARY-SOURCE — append a standardized primary-source citation
appendix to every DCC Kids Research DB row that I wrote today which
cites Piaget / Erikson / Vygotsky / Kohlberg at the textbook level.

Pure append; does not modify any existing citations. Each affected
row's Research-Source field gets a single paragraph listing the
primary publications so readers can trace any framework claim to
a verifiable source.

Run once:   python _s_primary_source_upgrade.py
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


APPENDIX = (
    "\n\nPRIMARY-SOURCE APPENDIX (developmental frameworks referenced "
    "above). Added 2026-04-21 to pair every textbook-level paraphrase "
    "with a traceable publication:\n"
    "• Piaget, J. (1952). The Origins of Intelligence in Children "
    "(M. Cook, Trans.). New York: International Universities Press. "
    "Original French: La Naissance de l'Intelligence Chez l'Enfant (1936).\n"
    "• Erikson, E. H. (1950/1963). Childhood and Society. New York: "
    "W. W. Norton & Company.\n"
    "• Erikson, E. H. (1968). Identity: Youth and Crisis. New York: "
    "W. W. Norton & Company.\n"
    "• Vygotsky, L. S. (1978). Mind in Society: The Development of "
    "Higher Psychological Processes (M. Cole, V. John-Steiner, "
    "S. Scribner, & E. Souberman, Eds.). Cambridge, MA: Harvard "
    "University Press.\n"
    "• Kohlberg, L. (1969). Stage and sequence: The cognitive-"
    "developmental approach to socialization. In D. A. Goslin "
    "(Ed.), Handbook of Socialization Theory and Research. "
    "Chicago: Rand McNally."
)

# Rows shipped 2026-04-21 that cite at least one of the four frameworks
ROWS = [
    ("349a09cf-876a-8118-8e9a-f1228d597509", "True things and story things"),
    ("349a09cf-876a-81c0-9d73-c5997f72a204", "Telling a grown-up (7-9)"),
    ("349a09cf-876a-8136-8c50-df26892b81c6", "Making my own thing first"),
    ("349a09cf-876a-8153-9a64-f3f460ed1f3a", "Two-factor authentication"),
    ("349a09cf-876a-8192-af6c-d7ec8f7e578b", "Making something useful for someone else"),
    ("349a09cf-876a-816a-a0b2-d5b4bc4aa532", "Sextortion resistance"),
    ("349a09cf-876a-811d-b763-c94c8fdef76e", "Password manager"),
    ("349a09cf-876a-8163-8d69-ebbca1da0b2a", "Lateral reading + AI check"),
    ("349a09cf-876a-8124-a6ff-cdda22772fd9", "Remix credit"),
    ("349a09cf-876a-8122-9afb-c334a458b2eb", "Pile-on exit"),
    ("349a09cf-876a-816f-b441-c4bfce802a0b", "App permissions pause-and-show"),
    ("349a09cf-876a-819e-88b5-d4ed38ef43cf", "AI tutor vs shortcut"),
]


def main() -> int:
    client = nc.NotionClient()
    print(f"Appendix length: {len(APPENDIX)} chars\n")
    results = []
    for pid, label in ROWS:
        print(f"--- {label} ({pid[:8]}...) ---")
        try:
            client.append_to_rich_text(pid, "Research-Source", APPENDIX)
            print("OK")
            results.append((True, label))
        except Exception as e:
            print(f"FAIL: {type(e).__name__}: {e}")
            results.append((False, label))
        print()

    ok = sum(1 for r in results if r[0])
    print("=" * 60)
    print(f"SUMMARY: {ok} of {len(ROWS)} rows updated.")
    for ok_flag, label in results:
        print(f"  {'OK  ' if ok_flag else 'FAIL'} — {label}")
    return 0 if ok == len(ROWS) else 1


if __name__ == "__main__":
    sys.exit(main())
