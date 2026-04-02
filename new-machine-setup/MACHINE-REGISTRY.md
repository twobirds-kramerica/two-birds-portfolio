# Machine Registry
Last updated: April 2, 2026

| Machine | Name | Specs | Status | Primary Use |
|---|---|---|---|---|
| i5 Lenovo | LenovoMain | i5-6200U, 8GB RAM, 238GB SSD, Win 10 Pro | Active ✅ | Primary build + overnight scheduler |
| Pentium Silver | LenovoHitch | N6000, 4GB RAM, Win 11 Home | Active ✅ | Secondary terminal only |
| New Laptop | TBD | TBD — Aaron to fill in when it arrives | Incoming ⏳ | TBD |
| Home Desktop | TBD | TBD — Aaron to fill in when ready | Incoming ⏳ | TBD |

When a new machine is set up, update this file with specs and primary use.

## Pending Machine Actions

- **Silver laptop (LenovoHitch):** Needs `powercfg /change standby-timeout-ac 0` run in elevated PowerShell. Not yet done — in Aaron's human sprint backlog.
- **New Laptop:** Follow SETUP-NEW-WINDOWS-MACHINE.md when hardware arrives. Clone all repos, register overnight scheduler, verify push access.
- **Home Desktop:** Same as above. May become primary overnight build machine if specs are better than i5.
