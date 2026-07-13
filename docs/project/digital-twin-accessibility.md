# Digital Twin Accessibility and Fallback Audit

Status: Active Milestone 6 audit. Last verified: 2026-07-13 16:35 BST.

## Purpose

Track the accessibility and non-interactive fallback requirements for the Astro Starlight digital twin.

## Implemented Coverage

| Area | Current implementation | Status |
| --- | --- | --- |
| Keyboard operation | Interactive controls use native buttons, visible focus states, and `aria-pressed` where a selected state exists. | Implemented locally. |
| Screen reader structure | Interactive sections use labelled regions, SVG titles/descriptions, live detail panels where selection changes, and descriptive alt text for QR codes. | Implemented locally. |
| Static fallbacks | Each interactive mode has a static list, ordered list, table, or source list that preserves the same essential information. | Implemented locally. |
| No-JavaScript behavior | The digital twin page includes a no-JavaScript notice and retains static fallback content in the page HTML. | Implemented locally. |
| Reduced motion | Animated route, airflow, and exploded-view transitions have `prefers-reduced-motion` handling. | Implemented locally. |
| Verification labelling | Data-backed views display verified, partially verified, or deferred status instead of hiding uncertainty. | Implemented locally. |
| Local privacy | Maintenance history entries are stored only in browser `localStorage`; no server persistence is introduced. | Implemented locally. |

## Static Fallback Inventory

| Feature | Fallback |
| --- | --- |
| Case view | Static zone list. |
| Connector map | Static connector list. |
| Cable-routing mode | Static cable route list. |
| Guided build sequence | Static ordered build sequence. |
| Airflow visualisation | Static airflow list. |
| Exploded assembly view | Static assembly-layer list. |
| BIOS simulator | Static BIOS training flow. |
| Driver and firmware dashboard | Static official-source list. |
| QR code section | Static official-link list. |
| Maintenance and upgrade history | Printable history template. |

## Remaining Manual Checks

- Browser screenshot checks are still manual because Playwright is not installed in the project yet.
- Automated accessibility testing is deferred to issue `#33`.
- Exact interactive coordinates remain schematic until board-photo or manual-diagram coordinate verification is added.
