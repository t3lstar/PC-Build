# Milestone 5 and 6 Validation Report

Status: Active validation report. Last verified: 2026-07-13 13:53 BST.

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

## Manual Verification Still Required

- Exact motherboard connector positions for interactive display.
- Exact front-panel connector coordinates for a future interactive map.
- BIOS menu names for the BIOS version used during the build.
- Real benchmark baseline values after the physical machine is assembled and tested.
