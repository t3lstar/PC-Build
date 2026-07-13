# PC Build Documentation Milestones

This project is delivered in controlled milestones so the repository can be built, reviewed, improved, and extended without losing completed work.

## Project Notes

- When new durable project knowledge is discovered, update the relevant documentation in the same change so future sessions can rehydrate from the repository.
- The site is an Astro Starlight GitHub Pages site.
- Use `Custom Gaming PC Build Manual` as the Starlight site title.
- Use `src/content/docs/index.md` as the Starlight home page and `README.md` as the GitHub repository overview.
- Keep source documentation under `src/content/docs/`.
- Keep rendered assets under `public/assets/`.
- Keep exact component identification and purchase links in `src/content/docs/appendix/bill-of-materials.md`.
- Keep additional build tools and consumables, including Amazon UK convenience links, in `src/content/docs/build-guide/tools.md` and `src/content/docs/appendix/bill-of-materials.md`.
- Prefer manufacturer product pages for stable reference links and amazon.co.uk for retailer purchase links.
- Treat retailer links as convenience links because price, stock, and listing details can change.
- Compatibility guidance must state the verification result and evidence.
- Use one parameterized build script at `scripts/build.sh` with `html`, `pdf`, `printable`, and `all` targets.
- PDF generation is deferred.
- Use Python 3.12, Node.js 24, and a local `.venv` for local dependencies.
- Include `CONTRIBUTING.md` with documentation rules.
- Include public repository hygiene files: `LICENSE`, `SECURITY.md`, and GitHub issue templates.
- Publish the documentation as a public GitHub Pages site using GitHub Actions.
- Use the default GitHub Pages URL first; defer any custom domain.
- Assume the GitHub owner is `t3lstar`; if the repository name remains `PC-Build`, the default site URL is `https://t3lstar.github.io/PC-Build/`.
- Pull requests should validate and build the site only. Pushes to `main` should validate, build, and deploy the site.
- Ensure the published site output includes `.nojekyll`.
- Technical diagrams are hand-authored documentation assets. Do not use AI-generated artwork for technical diagrams.
- Diagrams that readers need to follow the manual should be directly visible on the live site as rendered assets, not only linked as source files.
- Diagrams must remain readable in the live dark theme: use explicit light SVG backgrounds, avoid labels outside the drawing safe area, and prefer numbered legends where cable paths would overlap text.
- Mermaid and PlantUML files should be retained as source assets under `public/assets/diagrams/`, but reader-facing chapters should embed rendered SVG.
- Use `milestones/verification-register.md` and `milestones/starlight-migration-inventory.md` for current planning and validation records.
- Keep internal planning, ADR, audit, and validation records out of the public Starlight navigation unless they directly help readers build the PC.
- Astro Starlight is the accepted platform for the site and digital twin.
- Digital twin data remains framework-neutral under `data/digital-twin/`.
- QR code SVG assets are generated from official links in `data/digital-twin/build.json` by `scripts/generate-qrcodes.py`. Committed QR assets and their manifest live under `public/assets/qrcodes/`.
- Milestone 7 uses a clean Starlight information architecture. Numbered chapter routes are not preserved.
- Milestone 8 adds `src/content/docs/operations/` as the first-class post-build operating handbook.

## Milestone 1: Repository Scaffolding

Tracking issue: <https://github.com/t3lstar/PC-Build/issues/4>

Status: Complete.

Created the initial repository scaffold, placeholder pages, navigation, build script, public repository hygiene files, and GitHub Pages workflow.

## Milestone 2: Core Content

Tracking issue: <https://github.com/t3lstar/PC-Build/issues/1>

Status: Complete.

Completed the technical build guide chapters and appendix reference pages for a first-time PC builder.

## Milestone 3: Technical Diagrams

Tracking issue: <https://github.com/t3lstar/PC-Build/issues/2>

Status: Complete.

Added technically accurate diagram source and rendered diagram assets for build sequence, airflow, boot process, driver order, hardware layout, power flow, BIOS sequence, headers, slots, cable routing, and front-panel connectors.

## Milestone 4: Polish

Tracking issue: <https://github.com/t3lstar/PC-Build/issues/3>

Status: Complete for the GitHub Pages HTML release.

Refined wording, navigation, diagrams, styling, cross-links, and publication readiness. PDF generation remains deferred.

## Milestone 5: Professional Engineering Edition

GitHub milestone: <https://github.com/t3lstar/PC-Build/milestone/1>

Tracking issues: <https://github.com/t3lstar/PC-Build/issues/5> through <https://github.com/t3lstar/PC-Build/issues/18>

Status: Complete and published.

Detailed plan: [milestones/milestone-05-professional-engineering.md](milestones/milestone-05-professional-engineering.md)

Raised the documentation to publication-quality engineering documentation with stronger verification, checklists, troubleshooting, maintenance, benchmarking, validation automation, CI, and reproducible printable output.

## Milestone 6: Interactive Digital Twin Edition

GitHub milestone: <https://github.com/t3lstar/PC-Build/milestone/2>

Tracking issues: <https://github.com/t3lstar/PC-Build/issues/19> through <https://github.com/t3lstar/PC-Build/issues/35>

Status: Complete and published.

Detailed plan: [milestones/milestone-06-digital-twin.md](milestones/milestone-06-digital-twin.md)

Added an accurate, maintainable interactive representation of the PC that supplements the static build guide while preserving accessibility, static fallbacks, and GitHub Pages compatibility.

## Milestone 7: Full Starlight Migration

GitHub milestone: <https://github.com/t3lstar/PC-Build/milestone/3>

Tracking issues: <https://github.com/t3lstar/PC-Build/issues/36> through <https://github.com/t3lstar/PC-Build/issues/44>

Status: Complete and published.

Detailed plan: [milestones/milestone-07-full-starlight-migration.md](milestones/milestone-07-full-starlight-migration.md)

Completed the clean Astro Starlight site with source parity, clean routes, validation, assets, and GitHub Pages publication. Public pages are limited to the reader guide, appendix, and digital twin; project-management records stay in `milestones/`.

### Acceptance Criteria

- Every source page is available under `src/content/docs/` or deliberately removed as obsolete.
- Numbered chapter routes are removed in favour of clean Starlight routes.
- Starlight navigation exposes the full manual.
- Digital twin remains published and accessible.
- Diagram and image assets render correctly.
- Validation covers migrated pages, internal links, Markdown linting, Astro checks, and critical assets.
- GitHub Pages deploys the Starlight site successfully.

## Milestone 8: Operations, Monitoring and Maintenance Handbook

GitHub milestone: <https://github.com/t3lstar/PC-Build/milestone/4>

Tracking issues: <https://github.com/t3lstar/PC-Build/issues/45> through <https://github.com/t3lstar/PC-Build/issues/57>

Status: Complete and published.

Detailed plan: [milestones/milestone-08-operations-handbook.md](milestones/milestone-08-operations-handbook.md)

Added a first-class Operations section for maintaining, monitoring, securing, troubleshooting, benchmarking, and upgrading the completed PC throughout its lifetime.
