# PC Build Documentation Milestones

This project is delivered in controlled milestones so the repository can be built, reviewed, improved, and extended without losing completed work.

## Project Notes

- When new durable project knowledge is discovered, update the relevant documentation in the same change so future sessions can rehydrate from the repository.
- A final-build reference image exists from ChatGPT and may be used as a visual target where appropriate.
- Include real component product imagery in the documentation where it helps visual identification. Prefer externally hosted manufacturer images with source links rather than copying third-party product photography into the repository.
- PDF and standalone printable manual generation are deferred until after the GitHub Pages site is publication-ready.
- All listed components should be treated as mutually compatible unless later verification proves otherwise.
- RAM and SSD alternatives are acceptable if they preserve the intended platform requirements and performance class:
  - RAM: DDR5, AMD EXPO support preferred, 32GB target capacity, DDR5-6000 CL30 target specification.
  - SSD: NVMe M.2 drive, 2TB target capacity, suitable PCIe generation and thermal profile for the motherboard.
- Windows 11 Pro installation media should be assumed to already exist on a USB flash drive.
- Use `Custom Gaming PC Build Manual` as the MkDocs site title.
- Use direct instructional language throughout the documentation.
- Use date and time for page verification metadata, formatted as `YYYY-MM-DD HH:MM TZ`.
- Use `docs/index.md` as the MkDocs home page and `README.md` as the GitHub repository overview.
- Keep rendered appendix pages under `docs/appendix/`.
- Keep rendered assets under `docs/assets/`.
- Keep exact component identification and purchase links in `docs/appendix/bill-of-materials.md`.
- Keep additional build tools and consumables, including Amazon UK convenience links, in `docs/05-tools.md` and `docs/appendix/bill-of-materials.md`.
- Prefer manufacturer product pages for stable reference links and amazon.co.uk for retailer purchase links.
- Treat retailer links as convenience links because price, stock, and listing details can change.
- Compatibility guidance must state the verification result and evidence. Do not leave reader-facing instructions such as "check the QVL" when compatibility can be verified and documented in the repository.
- Use one parameterized build script at `scripts/build.sh` with `html`, `pdf`, `printable`, and `all` targets.
- Include `requirements.txt` for MkDocs and documentation build dependencies.
- Use Python 3.12, Node.js 24, and a local `.venv` for local dependencies; ignore `.venv` in Git.
- Include `CONTRIBUTING.md` with documentation rules.
- Include public repository hygiene files: `LICENSE`, `SECURITY.md`, and GitHub issue templates.
- In Milestone 1, create diagram folders only. Do not create empty diagram placeholder files.
- Publish the documentation as a public GitHub Pages site using GitHub Actions.
- Use the default GitHub Pages URL first; defer any custom domain.
- Assume the GitHub owner is `t3lstar`; if the repository name remains `PC-Build`, the default site URL is `https://t3lstar.github.io/PC-Build/`.
- Pull requests should build the site only. Pushes to `main` should build and deploy the site.
- Ensure the published site output includes `.nojekyll`.
- Technical diagrams are hand-authored documentation assets. Do not use AI-generated artwork for Milestone 3 diagrams.
- Diagrams that readers need to follow the manual should be directly visible on the live site as rendered assets, not only linked as source files.
- Diagrams must remain readable in the live dark theme: use explicit light SVG backgrounds, avoid labels outside the drawing safe area, and prefer numbered legends where cable paths would overlap text.
- Diagrams should support click-to-enlarge overlays on the published site for readability on smaller screens, implemented by tracked site JavaScript rather than a build-time MkDocs image plugin.
- Mermaid and PlantUML files should be retained as source assets, but the reader-facing chapter should embed a rendered SVG so all diagrams can use the same click-to-enlarge overlay.
- Rendered SVG diagrams should preserve the technical detail and labels from their Mermaid or PlantUML source diagrams; do not simplify the reader-facing version in a way that loses build instructions or decision points.
- Use the tracked MkDocs theme configuration and `docs/assets/stylesheets/theme.css` for site-level visual styling.
- Use `docs/project/repository-audit.md`, `docs/project/verification-register.md`, and `docs/project/milestone-05-06-validation-report.md` for Milestones 5 and 6 planning and validation.
- Keep detailed Milestone 5 and Milestone 6 plans under `milestones/`.

## Milestone 1: Repository Scaffolding

Tracking issue: https://github.com/t3lstar/PC-Build/issues/4

Status: Complete.

Create the documentation repository structure and make it ready for content.

### Scope

- Create the required folder structure.
- Add all planned Markdown chapter files as placeholders.
- Add required chapter headings to placeholder pages.
- Add appendix placeholder files under `docs/appendix/`.
- Add `docs/appendix/bill-of-materials.md` as the buying guide placeholder.
- Add asset folders for images, diagrams, icons, and scripts.
- Configure MkDocs Material.
- Define the MkDocs navigation in build order.
- Add `scripts/build.sh` for generating HTML, PDF, and printable documentation.
- Add `README.md`, `CONTRIBUTING.md`, and `requirements.txt`.
- Add `.gitignore` for `.venv/`, generated site output, and local system files.
- Add a GitHub Actions workflow for pull request builds and `main` branch GitHub Pages deployment.
- Add `docs/appendix/publishing.md` explaining the public site build and deployment process.

### Acceptance Criteria

- The repository structure matches `AGENTS.md`.
- `mkdocs.yml` exists and includes all chapters in navigation order.
- Every planned Markdown file exists.
- Placeholder pages clearly state their intended content.
- Placeholder chapter pages include the required heading structure from `AGENTS.md`.
- `scripts/build.sh` exists, supports `html`, `pdf`, `printable`, and `all`, and is executable.
- Diagram folders exist without misleading empty diagram files.
- MkDocs can serve or build the placeholder documentation without broken internal links.
- GitHub Actions workflow exists for pull request build checks and `main` branch deployment.
- The deployment workflow prepares `.nojekyll` in the published site output.

## Milestone 2: Core Content

Tracking issue: https://github.com/t3lstar/PC-Build/issues/1

Status: Complete.

Write the complete technical documentation for each chapter.

### Scope

- Complete every Markdown chapter from introduction through upgrades.
- Complete appendix pages for glossary, FAQ, checklists, drivers, BIOS settings, and temperature reference.
- Complete `docs/appendix/bill-of-materials.md` with exact components, manufacturer links, preferred amazon.co.uk purchase links, acceptable alternatives, and compatibility notes.
- Ensure each chapter includes:
  - Introduction
  - Purpose
  - Estimated time
  - Difficulty
  - Required tools
  - Warnings
  - Step-by-step instructions
  - Verification checklist
  - Common mistakes
  - Expected result
  - Next chapter

### Acceptance Criteria

- Each chapter is complete enough for a first-time PC builder to follow.
- Instructions are specific to the listed hardware.
- The bill of materials identifies exact components and clearly separates required specifications from acceptable alternatives.
- Every step is verifiable.
- BIOS, Windows, driver, benchmark, and maintenance content is technically accurate.
- Cross-links between chapters are present and useful.

## Milestone 3: Technical Diagrams

Tracking issue: https://github.com/t3lstar/PC-Build/issues/2

Status: Complete.

Add technically accurate diagrams that support the written build guide.

### Scope

- Add Mermaid diagrams for:
  - Build sequence
  - Airflow
  - Boot process
  - Driver installation order
- Add PlantUML diagrams for:
  - Hardware layout
  - Power flow
  - Boot flow
  - BIOS sequence
- Add SVG diagrams for:
  - Motherboard headers
  - Fan layout
  - Cable routing
  - Front panel connectors
  - PCIe slots
  - Memory slots
  - M.2 slots
  - PSU cable routing
  - Airflow

### Acceptance Criteria

- Diagrams are stored in the correct asset folders.
- Diagram source files are retained where applicable.
- Diagrams are referenced from the relevant chapters.
- Diagrams are technically accurate and based on the actual components.
- No AI-generated artwork is used.

## Milestone 4: Polish

Tracking issue: https://github.com/t3lstar/PC-Build/issues/3

Status: Complete for the GitHub Pages HTML release.

Refine the documentation into a publication-ready manual.

### Scope

- Improve wording, consistency, and chapter flow.
- Add screenshots where appropriate.
- Improve MkDocs Material styling.
- Validate navigation and cross-links.
- Verify HTML generation and the published GitHub Pages site.
- Defer PDF and standalone printable manual generation to a later enhancement.
- Review the final repository for publication readiness.

### Acceptance Criteria

- Documentation builds cleanly as HTML.
- PDF and standalone printable manual generation are documented as deferred.
- Links and navigation work.
- Screenshots and diagrams render correctly.
- The repository is suitable for publication on GitHub.

## Milestone 5: Professional Engineering Edition

GitHub milestone: https://github.com/t3lstar/PC-Build/milestone/1

Tracking issues: https://github.com/t3lstar/PC-Build/issues/5 through https://github.com/t3lstar/PC-Build/issues/18

Status: Planned.

Detailed plan: [milestones/milestone-05-professional-engineering.md](milestones/milestone-05-professional-engineering.md)

Raise the existing documentation to publication-quality engineering documentation with stronger verification, checklists, troubleshooting, maintenance, benchmarking, validation automation, CI, and reproducible PDF/printable output.

### Acceptance Criteria

- HTML builds cleanly locally and in GitHub Actions.
- PDF and standalone printable outputs build reproducibly or have a documented blocker.
- Critical technical claims are verified or explicitly marked pending.
- Troubleshooting decision trees render correctly.
- Maintenance and benchmarking guidance is complete.
- Validation commands are documented and repeatable.
- GitHub issues reflect delivered work.

## Milestone 6: Interactive Digital Twin Edition

GitHub milestone: https://github.com/t3lstar/PC-Build/milestone/2

Tracking issues: https://github.com/t3lstar/PC-Build/issues/19 through https://github.com/t3lstar/PC-Build/issues/34

Status: Planned.

Detailed plan: [milestones/milestone-06-digital-twin.md](milestones/milestone-06-digital-twin.md)

Add an accurate, maintainable interactive representation of the PC that supplements the static build guide while preserving accessibility, static fallbacks, and GitHub Pages compatibility.

### Acceptance Criteria

- Architecture ADR is accepted before implementation choices are locked in.
- Digital twin data validates against JSON Schema.
- Every interactive component maps to structured data.
- Cable routes and connector positions are verified or explicitly marked unverified.
- Static fallbacks remain available.
- Keyboard navigation, visible focus indicators, and reduced-motion behavior work.
- The site remains static and deployable through GitHub Pages.
