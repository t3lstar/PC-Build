# Milestone 5 and 6 Validation Report

Status: Initial validation report. Last verified: 2026-07-13 13:04 BST.

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

## Manual Verification Still Required

- Exact motherboard connector positions for interactive display.
- Exact fan and pump header recommendations.
- Exact front-panel pinout reproduction if copied into documentation.
- M.2 slot preference and heatsink details.
- BIOS menu names for the BIOS version used during the build.
- Real benchmark baseline values after the physical machine is assembled and tested.
