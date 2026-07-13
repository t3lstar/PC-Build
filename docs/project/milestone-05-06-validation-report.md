# Milestone 5 and 6 Validation Report

Status: Active validation report. Last verified: 2026-07-13 15:05 BST.

## Passed Checks

| Check | Command or source | Outcome |
| --- | --- | --- |
| Git branch and status before audit | `git status --short --branch` | Clean `main` branch tracking `origin/main`. |
| Latest GitHub Pages deployment | `gh run list --repo t3lstar/PC-Build --limit 10` | Latest inspected workflow run completed successfully. |
| GitHub issue state | `gh issue list --repo t3lstar/PC-Build --state all --limit 100` | Issues `#1`-`#4` closed; no open issues before Milestone 5/6 planning. |
| Repository instruction discovery | `find .. -name AGENTS.md` scoped to repository result | Root `AGENTS.md` found; no nested repository `AGENTS.md` found. |
| Milestone 5 GitHub milestone | `gh api repos/t3lstar/PC-Build/milestones --paginate` | Created and verified `Milestone 5 - Professional Engineering Edition` at https://github.com/t3lstar/PC-Build/milestone/1 with 14 open issues. |
| Milestone 6 GitHub milestone | `gh api repos/t3lstar/PC-Build/milestones --paginate` | Created and verified `Milestone 6 - Interactive Digital Twin Edition` at https://github.com/t3lstar/PC-Build/milestone/2 with 16 open issues. |
| Milestone 5 issue set | `gh issue list --repo t3lstar/PC-Build --state all --limit 120` | Created and verified issues `#5` through `#18`. |
| Milestone 6 issue set | `gh issue list --repo t3lstar/PC-Build --state all --limit 120` | Created and verified issues `#19` through `#34`. |
| Local HTML build with `.venv` active | `. .venv/bin/activate && ./scripts/build.sh html` | Passed in 139.69 seconds. |
| Local HTML build after issue #5 updates | `. .venv/bin/activate && ./scripts/build.sh html` | Passed in 71.44 seconds. |
| Gigabyte manual availability | `curl -I -L https://download.gigabyte.com/FileList/Manual/mb_manual_b850-aorus-elite-wf7_1101_e.pdf` | Official user manual 1101 URL returned HTTP 200. |
| Gigabyte manual text extraction | Bundled runtime Python with `pypdf`, using temporary files under `/tmp/pc-build-sources/` | Extracted 40 pages from the official manual for local verification; no PDF or extracted text was committed. |
| Milestone 5 issue #5 verification pass | Official Gigabyte, G.SKILL, ARCTIC, Lian Li, and Samsung sources | Updated `docs/project/verification-register.md` plus affected RAM, M.2, AIO, and front-panel chapters. |
| Milestone 5 issue #6 status metadata scan | `rg -n` for stale Milestone 2 status wording | No published Markdown pages retain stale Milestone 2 status wording after the metadata update. |
| Milestone 5 issue #6 chapter next-link scan | Python scan over `docs/[0-9][0-9]-*.md` | Every numbered build chapter has a `Next Chapter` section. |
| Milestone 5 issue #6 project navigation | `mkdocs.yml` review | Added `Documentation Structure` under the Project navigation group. |
| Local HTML build after issue #6 updates | `. .venv/bin/activate && ./scripts/build.sh html` | Passed in 72.17 seconds. |
| Milestone 5 issue #7 roadmap and contribution review | Manual review of `README.md`, `CONTRIBUTING.md`, `MILESTONES.md`, and `milestones/` | README now shows current roadmap status, contribution workflow, project-control docs, and GitHub milestone links; contribution guide now documents issue workflow, technical verification, validation, and generated-output rules. |
| Local HTML build after issue #7 updates | `. .venv/bin/activate && ./scripts/build.sh html` | Passed in 188.75 seconds. |
| Milestone 5 issue #8 checklist review | Manual review of `docs/appendix/checklists.md`, `docs/06-build-preparation.md`, and `docs/25-maintenance.md` | Expanded staged build checklists, maintenance log templates, and cross-links from preparation and maintenance chapters. |
| Local HTML build after issue #8 updates | `. .venv/bin/activate && ./scripts/build.sh html` | Passed in 116.22 seconds. |
| Milestone 5 issue #9 troubleshooting diagram review | Manual review of `docs/24-troubleshooting.md` and `docs/assets/diagrams/mermaid/troubleshooting-*.mmd` | Added four Mermaid decision trees for no power, no display, high temperature, and Windows/driver faults, with matching source assets. |
| Troubleshooting source link check | `curl` for Gigabyte and Microsoft, browser verification for AMD support page | Gigabyte manual and Microsoft recovery page returned HTTP 200. AMD support page was browser-accessible but did not return a normal `curl` status from this environment. |
| Local checkout moved off iCloud Drive | Fresh clone to `/Users/simondawson/Herd/PC-Build`; uncommitted issue #9 changes reapplied | New working copy is outside iCloud Drive. The old iCloud path should not be used for future builds. |
| Local Python 3.12 environment recreated | `uv venv --python 3.12 .venv` and `uv pip install -r requirements.txt` | Created CPython 3.12.12 `.venv` and installed documentation dependencies. |
| Local HTML build after moving checkout | `. .venv/bin/activate && time ./scripts/build.sh html` from `/Users/simondawson/Herd/PC-Build` | Passed. MkDocs reported 0.96 seconds; shell wall-clock total was 3.515 seconds. |
| Local HTML build after documenting checkout move | `. .venv/bin/activate && time ./scripts/build.sh html` from `/Users/simondawson/Herd/PC-Build` | Passed. MkDocs reported 0.91 seconds; shell wall-clock total was 1.346 seconds. |
| Milestone 5 issue #14 CI speed-up | `.github/workflows/deploy-pages.yml` review and GitHub Actions run timings | Switched CI dependency installation to `uv pip install --system -r requirements.txt` while keeping `actions/setup-python@v6` pip caching. |
| GitHub Actions uv action correction | GitHub Actions run `29255643234` annotation review | Removed `astral-sh/setup-uv@v6` because it emitted a Node.js 20 deprecation annotation while GitHub forced it to Node.js 24. |
| Local HTML build after CI speed-up | `. .venv/bin/activate && time ./scripts/build.sh html` from `/Users/simondawson/Herd/PC-Build` | Passed. MkDocs reported 0.93 seconds; shell wall-clock total was 1.362 seconds. |
| Local HTML build after removing Node 20 uv action | `. .venv/bin/activate && time ./scripts/build.sh html` from `/Users/simondawson/Herd/PC-Build` | Passed. MkDocs reported 0.87 seconds; shell wall-clock total was 1.319 seconds. |
| GitHub Actions after CI speed-up correction | Run `29255786168` | Passed. Build job completed in 14 seconds; deploy job completed in 11 seconds. Dependency install step took 5 seconds and build step took 1 second. No Node 20 annotation was shown in the run watch output. |
| Local-first milestone workflow decision | User workflow decision, documented in `README.md`, `CONTRIBUTING.md`, and `docs/project/documentation-structure.md` | Future milestone work should commit locally per issue or issue group, validate locally, and push at agreed milestone checkpoints. GitHub issues should close only after pushed commits pass GitHub Actions. |
| Milestone 5 issue #10 monitoring guide review | Manual review of `docs/22-gaming-optimisation.md`, `docs/23-benchmarks.md`, `docs/25-maintenance.md`, and `milestones/milestone-05-professional-engineering.md` | Expanded monitoring phases, baseline fields, optimisation rules, verification checklist, benchmark handoff, and maintenance comparison guidance. |
| Local HTML build after issue #10 updates | `. .venv/bin/activate && time ./scripts/build.sh html` from `/Users/simondawson/Herd/PC-Build` | Passed. MkDocs reported 0.97 seconds; shell wall-clock total was 1.408 seconds. |

## Warnings

| Check | Command or source | Outcome |
| --- | --- | --- |
| Local Python version | `. .venv/bin/activate; python --version` | Local `.venv` reported Python 3.14.5; repository expects Python 3.12. |
| Shell Python alias | `python --version` | The shell does not expose a `python` command; use the project `.venv` Python or `python3` for one-off local scripts. |
| Local Node version | `node --version` | Local Node reported v25.2.1; repository expects Node.js 24. |
| MkDocs Material warning | `./scripts/build.sh html` | MkDocs Material prints an upstream warning about future MkDocs 2.0 compatibility. |

## Known Limitations

- PDF and standalone printable generation are currently deferred.
- Markdown linting is not configured.
- Spelling checks are not configured.
- Dedicated internal and external link validation is not configured.
- Diagram source-to-SVG generation and drift detection are not automated.
- SVG validation is not configured.
- JSON Schema validation for a future digital twin does not exist yet.
- Milestone 5 and 6 issues are planning issues only; implementation should close them only after their acceptance criteria are met.

## Checks That Could Not Run

| Check | Reason |
| --- | --- |
| PDF generation | Deferred after previous local WeasyPrint/Pillow native dependency and performance issues. |
| Markdown lint | No markdown lint tool or command is currently configured. |
| Spelling | No spelling tool or dictionary is currently configured. |
| Mermaid validation | No Mermaid CLI or validation script is currently configured. |
| PlantUML generation | No PlantUML toolchain or script is currently configured. |
| Accessibility tests | No browser accessibility test tool is currently configured. |

## Failed Checks

| Check | Command | Outcome |
| --- | --- | --- |
| Local HTML build during audit | `. .venv/bin/activate; ./scripts/build.sh html` | Failed once with `OSError: [Errno 89] Operation canceled` while reading `docs/appendix/faq.md`. The file was present and readable immediately afterward. Treat as local iCloud/filesystem risk unless reproduced in CI. |
| Local HTML build without `.venv` active | `./scripts/build.sh html` | Failed with `mkdocs: command not found`, as expected when the local virtual environment is not active. |
| Local `pypdf` install into project `.venv` | `. .venv/bin/activate && python -m pip install pypdf` | Interrupted after slow/no output; used bundled runtime PDF tooling instead. No dependency file was changed. |
| AMD support page `curl` check | `curl -L --head https://www.amd.com/en/support/download/drivers.html` | Returned `000` in this environment, while browser access succeeded. Keep as a link-check caveat rather than a documentation blocker. |

## Manual Verification Still Required

- Exact motherboard connector positions for interactive display.
- Exact front-panel connector coordinates for a future interactive map.
- BIOS menu names for the BIOS version used during the build.
- Real benchmark baseline values after the physical machine is assembled and tested.
