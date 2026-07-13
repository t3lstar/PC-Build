# Milestone 7: Full Starlight Migration

Status: In progress locally.

GitHub milestone: <https://github.com/t3lstar/PC-Build/milestone/3>

Tracking issues: <https://github.com/t3lstar/PC-Build/issues/36> through <https://github.com/t3lstar/PC-Build/issues/44>

## Purpose

Complete the clean Astro Starlight site with full manual source, clean routes, validation, and GitHub Pages publication.

## User Value

- Readers get one consistent Starlight documentation experience.
- The digital twin is part of the main documentation site.
- Future interactive documentation can evolve without maintaining two parallel site systems.
- The repository has one clean static-site build path.

## Scope

- Inventory all Starlight pages.
- Move build guide chapters into clean Starlight routes.
- Move appendix, ADR, project, milestone, and validation pages into clean Starlight routes.
- Rebuild Starlight navigation.
- Use clean human-readable routes instead of numbered chapter routes.
- Move diagram, image, QR, and digital twin assets into the Starlight asset model.
- Expand validation and link checks.
- Switch GitHub Pages to Starlight output.
- Remove old source, configuration, workflow, and dependency files.
- Record final QA and release evidence.

## Out of Scope

- Rewriting technical content without a migration need.
- New hardware feature work unrelated to Starlight migration.
- PDF generation.
- Browser screenshot automation unless separately approved.

## Dependencies

- Milestone 6 published digital twin first slice.
- Existing complete manual content.
- Existing Starlight scaffold.
- Node.js 24 local and CI runtime.
- Python 3.12 `.venv` for data and QR validation.

## Deliverables

- [x] Starlight source inventory.
- [x] Full build guide chapter migration.
- [x] Appendix and project page migration.
- [x] Full Starlight navigation.
- [x] Clean Starlight route strategy.
- [x] Diagram and asset compatibility.
- [x] Expanded Starlight validation.
- [x] Starlight GitHub Pages workflow.
- [x] Old source and build path removed.
- [ ] Final QA report.

## Acceptance Criteria

- [x] Every source page is available under `src/content/docs/` or deliberately removed as obsolete.
- [x] Numbered chapter routes are removed in favour of clean Starlight routes.
- [x] Starlight navigation exposes the full manual.
- [x] Digital twin remains published and accessible locally.
- [x] Diagram and image assets render from `public/assets/`.
- [x] Validation covers pages, internal links, Markdown linting, Astro checks, and critical assets.
- [ ] GitHub Pages deploys the Starlight site successfully.
- [ ] Milestone 7 issues are closed only after live deployment verification.

## Issue Breakdown

- [x] [#36: M7: Create Starlight migration parity inventory](https://github.com/t3lstar/PC-Build/issues/36) - implemented locally.
- [x] [#37: M7: Port build guide chapters to Starlight](https://github.com/t3lstar/PC-Build/issues/37) - implemented locally.
- [x] [#38: M7: Port appendix and project docs to Starlight](https://github.com/t3lstar/PC-Build/issues/38) - implemented locally.
- [x] [#39: M7: Rebuild Starlight navigation and route strategy](https://github.com/t3lstar/PC-Build/issues/39) - implemented locally.
- [x] [#40: M7: Migrate diagrams and asset behavior to Starlight](https://github.com/t3lstar/PC-Build/issues/40) - implemented locally.
- [x] [#41: M7: Expand Starlight validation and link checks](https://github.com/t3lstar/PC-Build/issues/41) - implemented locally.
- [x] [#42: M7: Switch GitHub Pages deployment to Starlight](https://github.com/t3lstar/PC-Build/issues/42) - implemented locally.
- [x] [#43: M7: Remove old build path](https://github.com/t3lstar/PC-Build/issues/43) - implemented locally.
- [ ] [#44: M7: Full Starlight migration final QA and release](https://github.com/t3lstar/PC-Build/issues/44)

## Completion Checklist

- [x] Update `MILESTONES.md`.
- [x] Update README and CONTRIBUTING.
- [x] Validate local Starlight build.
- [x] Validate route and asset parity.
- [ ] Verify GitHub Pages deployment.
- [ ] Close Milestone 7 issues only after deployment evidence is recorded.
