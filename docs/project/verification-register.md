# Verification Register

Status: Initial register for Milestones 5 and 6. Last verified: 2026-07-13 12:49 BST.

Use this register for technical claims that need explicit official-source confirmation before they are treated as final.

| Claim | Current status | Required source | Affected page | Resolution |
| --- | --- | --- | --- | --- |
| Motherboard connector positions for any future interactive map | Pending detailed verification | Gigabyte B850 AORUS Elite WiFi7 manual for the exact revision | Future digital twin and `docs/03-motherboard-overview.md` | Do not expose unverified connector positions interactively. |
| Recommended AIO pump/fan header connection path | Partially documented | ARCTIC Liquid Freezer III Pro 360 manual and Gigabyte motherboard manual | `docs/13-aio-installation.md`, future connector reference | Confirm exact recommended header naming before digital twin cable routes. |
| Front-panel pin positions and LED polarity | Reader instructed to use manual | Gigabyte motherboard manual and Lian Li case manual | `docs/16-front-panel-connectors.md`, future connector map | Keep manual verification requirement unless exact pinout is reproduced with source. |
| M.2 preferred slot for the boot SSD | Needs source-backed specificity | Gigabyte motherboard manual | `docs/09-m2-installation.md` | Confirm preferred slot and heatsink guidance before Milestone 5 final QA. |
| BIOS menu names for EXPO, Resizable BAR, Secure Boot, TPM, and Q-Flash | May vary by BIOS version | Gigabyte BIOS manual/support notes for installed BIOS version | `docs/18-bios.md`, `docs/19-expo.md`, future BIOS simulator | Keep future simulator labelled as training only. |
| Expected benchmark scores | Not provided by design | User-recorded baseline after build completion | `docs/23-benchmarks.md`, future benchmark log | Do not invent scores; use baseline procedure and variance guidance. |
| Exact fan count and airflow roles | Documented as 3 bottom intake, 2 side intake, 3 top radiator exhaust | Lian Li case materials and ARCTIC cooler documentation | `docs/04-case-overview.md`, future airflow visualisation | Keep as build assumption until final physical build verification. |
| Product image hotlink reliability | Browser-verified but external | Manufacturer or stable official product pages | `docs/02-components.md` | Treat product images as visual aids only; model numbers remain source of truth. |
