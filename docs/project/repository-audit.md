# Repository Audit

Status: Initial Milestones 5 and 6 audit. Last verified: 2026-07-13 12:49 BST.

## Current Repository State

The repository is an existing MkDocs Material documentation site for a custom gaming PC build. It is published through GitHub Pages at `https://t3lstar.github.io/PC-Build/`.

Current branch state at audit time:

- Branch: `main`
- Remote: `https://github.com/t3lstar/PC-Build.git`
- Latest commit audited: `602d91d Mark HTML site polish complete`
- Working tree before audit edits: clean
- GitHub Pages workflow: latest inspected deployment completed successfully

The repository has one applicable instruction file:

- `AGENTS.md`

No nested `AGENTS.md` files were found inside the repository.

## Existing Milestone Status

| Milestone | Repository status | GitHub issue status |
| --- | --- | --- |
| Milestone 1: Repository Scaffolding | Complete | `#4` closed |
| Milestone 2: Core Content | Complete | `#1` closed |
| Milestone 3: Technical Diagrams | Complete | `#2` closed |
| Milestone 4: Polish | Complete for the GitHub Pages HTML release | `#3` closed |

Milestones 1-4 should be preserved. New work should extend the existing documentation rather than recreating it.

## Build Specification Verification

The repository currently describes the confirmed build as:

| Area | Current repository value | Audit status |
| --- | --- | --- |
| CPU | AMD Ryzen 7 7800X3D | Matches requested specification |
| CPU cooler | ARCTIC Liquid Freezer III Pro 360 | Matches requested specification |
| Motherboard | Gigabyte B850 AORUS Elite WiFi7 | Matches requested specification; revision-specific details require continued verification |
| Memory | 32GB DDR5-6000 CL30 AMD EXPO | Matches requested specification; exact preferred kit is documented in the bill of materials |
| Storage | Samsung 990 EVO Plus 2TB NVMe | Matches requested specification |
| GPU | Gigabyte Radeon RX 9060 XT Gaming OC 16GB | Matches requested specification |
| Case | Lian Li O11 Dynamic Mini V2 Flow | Matches requested specification |
| PSU | ASUS TUF Gaming 1000W Gold | Matches requested specification |
| Operating system | Windows 11 Pro on USB installation media | Matches requested specification |

## Technical Debt

- Many pages still show `Status: Initial Milestone 2 content`, even though the HTML site is publication-ready. Milestone 5 should standardise revision/status metadata.
- PDF and standalone printable manual generation are intentionally deferred. The current `pdf` and `printable` script targets are reserved placeholders.
- `requirements.txt` includes PDF-related dependencies even though PDF output is deferred. Milestone 5 should decide whether to keep, pin, or split those dependencies.
- The local `.venv` inspected during audit reported Python 3.14.5, while repository guidance expects Python 3.12.
- Local Node reported v25.2.1, while repository guidance expects Node.js 24.
- Build performance in the iCloud-backed working directory is slow.
- A local HTML build attempt failed once with `OSError: [Errno 89] Operation canceled` while reading `docs/appendix/faq.md`. The file was readable immediately afterward, and GitHub Actions builds are passing, so this is treated as a local filesystem/iCloud risk.

## Documentation Gaps

- No `docs/project/` planning area existed before this audit.
- No dedicated verification register existed before this audit.
- No roadmap file existed outside `MILESTONES.md`.
- The README is useful but does not yet cover the larger Milestone 5 and 6 roadmap in detail.
- Checklists exist, but Milestone 5 requires a more complete consolidated checklist set.
- Troubleshooting exists, but Milestone 5 requires decision trees for specific boot, thermal, driver, USB, network, and stability faults.
- Benchmarking guidance exists, but Milestone 5 requires a stronger baseline methodology without invented expected scores.
- Maintenance guidance exists, but Milestone 5 requires scheduled maintenance and update procedures.
- Connector and cable references exist across chapters and diagrams, but Milestone 5 requires stronger appendices and verification tracking.

## Automation Gaps

Current automation:

- `./scripts/build.sh html`
- `./scripts/build.sh all` as an HTML build alias
- GitHub Actions workflow for pull request build and `main` branch GitHub Pages deployment

Missing or deferred automation:

- Markdown linting
- Spelling checks
- Internal link validation beyond MkDocs strict build behavior
- External link validation
- Mermaid validation
- PlantUML rendering or drift detection
- SVG validation
- Asset validation
- PDF generation
- Printable output generation
- Full local CI wrapper
- Digital twin JSON Schema validation and tests

## Diagram Gaps

Existing diagram assets include Mermaid, PlantUML, and rendered SVG diagrams under `docs/assets/diagrams/`.

Known gaps for Milestone 5 and 6:

- Troubleshooting decision trees are not yet present.
- Diagram generation is not automated.
- Drift detection between diagram source files and rendered SVGs is not automated.
- Connector positions for a future digital twin must be verified before interactive display.
- Static fallbacks for future interactive diagrams must be planned before implementation.

## GitHub State

At audit time:

- Existing issues: `#1` through `#4`, all closed.
- Existing GitHub milestones: none.
- Existing labels: GitHub defaults plus `documentation`.
- Issue templates reference labels such as `diagram`, `build`, and `compatibility`, but those labels were not present.

Milestone 5 and 6 planning should create GitHub milestones and structured issues without duplicating existing closed milestone issues.

Post-audit planning state:

- Milestone 5 GitHub milestone: https://github.com/t3lstar/PC-Build/milestone/1
- Milestone 5 issues: `#5` through `#18`
- Milestone 6 GitHub milestone: https://github.com/t3lstar/PC-Build/milestone/2
- Milestone 6 issues: `#19` through `#34`

## Risks and Assumptions

- Official manual details must remain authoritative for connector positions, headers, BIOS behavior, and compatibility evidence.
- Retailer links and externally hosted product images can change or fail independently of the repository.
- PDF generation previously proved slow and exposed local native dependency issues; Milestone 5 should reintroduce it deliberately.
- The future digital twin must not imply exact physical visibility or connector positions unless verified.
- GitHub Pages must remain a static-site deployment; no server-side state should be introduced.
- Local progress features for Milestone 6 should use browser-local storage only and must not require an account.

## Proposed Implementation Sequence

1. Create Milestone 5 and 6 planning documents.
2. Update root repository instructions so future sessions understand Milestones 5 and 6.
3. Add `docs/project/verification-register.md`.
4. Add `docs/project/milestone-05-06-validation-report.md` and keep it current as validation expands.
5. Create GitHub milestones for Milestone 5 and Milestone 6.
6. Create structured GitHub issues for the recommended Milestone 5 and 6 work.
7. Implement Milestone 5 before Milestone 6.
8. For Milestone 6, complete an architecture ADR and data-model vertical slice before broader interactivity.
