# Milestone 6 Final QA

Status: Complete and published. Last verified: 2026-07-13 16:54 BST.

## Purpose

Record the final QA state for Milestone 6 after the checkpoint push, GitHub Actions verification, digital twin route publication, and GitHub issue closure.

## Scope Reviewed

- Digital twin ADR and Starlight migration decision.
- Structured digital twin data and JSON Schema validation.
- Interactive Starlight first-slice components.
- Static fallbacks and no-JavaScript behavior.
- Official-link QR code generation and validation.
- Local-only maintenance history behavior.
- MkDocs project documentation remains buildable while the Starlight first slice is published under `/digital-twin/first-slice/`.

## Local Implementation State

| Issue | Local state |
| --- | --- |
| `#19` Digital twin architecture ADR | Implemented locally. |
| `#20` Build data model and JSON Schema | Implemented locally. |
| `#35` Astro Starlight first slice | Implemented locally. |
| `#21` Verified component and connector dataset | Implemented locally. |
| `#22` Interactive case view | Implemented locally. |
| `#23` Motherboard connector map | Implemented locally. |
| `#24` Cable-routing mode | Implemented locally. |
| `#25` Guided build-sequence mode | Implemented locally. |
| `#26` Airflow visualisation | Implemented locally. |
| `#27` Exploded assembly view | Implemented locally. |
| `#28` Educational BIOS simulator | Implemented locally. |
| `#29` Driver and firmware source dashboard | Implemented locally. |
| `#30` Official-link QR codes | Implemented locally. |
| `#31` Maintenance and upgrade history | Implemented locally. |
| `#32` Accessibility and static fallbacks | Implemented locally. |
| `#33` Data, interaction, and accessibility tests | Implemented locally. |
| `#34` Final QA and release | Published and verified. |

## Validation Evidence

Run the following commands from `/Users/simondawson/Herd/PC-Build` with the project `.venv` active:

```bash
. .venv/bin/activate
./scripts/validate.sh all
./scripts/validate.sh starlight
```

Expected coverage:

- `./scripts/validate.sh all` validates digital twin data, QR assets, documentation structure, local Markdown links, and MkDocs HTML output.
- `./scripts/validate.sh starlight` builds the Astro Starlight site and runs `scripts/validate-starlight.py` against source files and built HTML.

Latest local result:

| Check | Result |
| --- | --- |
| `./scripts/validate.sh all` | Passed. MkDocs reported 1.33 seconds; shell wall-clock total was 2.547 seconds. |
| `./scripts/validate.sh starlight` | Passed. Astro built 8 static pages in 1.80 seconds; shell wall-clock total was 5.038 seconds. |
| Built Starlight output size | `dist/` is 3.3M. |
| QR asset size | `public/assets/qrcodes/` is 176K. |
| GitHub Actions release run | Passed. Run `29264219489` deployed commit `21e4fc0`. |
| Live digital twin route | Passed. `https://t3lstar.github.io/PC-Build/digital-twin/first-slice/` returned HTTP 200 and contains the Starlight digital twin. |

## Release State

Milestone 6 is released as a combined GitHub Pages artifact. MkDocs remains the main manual, and the Starlight digital twin first slice is published under `https://t3lstar.github.io/PC-Build/digital-twin/first-slice/`.

GitHub issues and the GitHub milestone were closed after:

- The checkpoint commits are pushed to `main`.
- GitHub Actions pass.
- The published GitHub Pages site is verified.
- Issue closure comments include deployment evidence.

## Known Limitations

- Browser-level screenshot regression is not automated because Playwright is not installed in the project.
- Browser-level accessibility scanning is not configured; current validation uses source and built-HTML checks.
- Exact visual coordinates are still schematic where the dataset marks them partially verified or deferred.
- Real benchmark baseline values still require the physical build to be assembled and tested.
