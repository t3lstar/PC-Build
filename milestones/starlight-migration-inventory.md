---
title: "Starlight Source Inventory"
---
Status: Repository-only source inventory. Last verified: 2026-07-13 18:42 BST.

## Purpose

Track the clean Astro Starlight source layout, routes, assets, and validation coverage for Milestone 7.

This is a repository planning record, not a public site page.

## Current Counts

- Starlight content pages: 45 complete manual, Operations, appendix, and digital twin pages.
- Build guide pages: 22 clean routes under `/build-guide/`.
- Operations pages: 12 clean routes under `/operations/`.
- Appendix pages: 9 clean routes under `/appendix/`.
- Digital twin MDX pages: 1 route at `/digital-twin/first-slice/`.
- Reader-facing asset folder: 1 folder at `public/assets/`.

## Source Ownership

| Area                  | Location                   | Ownership rule                                      |
| --------------------- | -------------------------- | --------------------------------------------------- |
| Documentation content | `src/content/docs/`        | Canonical source for all published pages            |
| Interactive views     | `src/components/`          | Astro components used by MDX pages                  |
| Site styling          | `src/styles/starlight.css` | Starlight theme overrides and digital twin styling  |
| Public assets         | `public/assets/`           | Images, diagrams, icons, generated QR code assets   |
| Digital twin data     | `data/digital-twin/`       | Framework-neutral build data and JSON Schema        |
| Build scripts         | `scripts/`                 | Local build, validation, QR generation, data checks |
| Project records       | `milestones/`              | Milestones, ADRs, verification, and release records |

## Route Strategy

| Content area | Route pattern                | Notes                                    |
| ------------ | ---------------------------- | ---------------------------------------- |
| Home         | `/`                          | Starlight landing page                   |
| Build guide  | `/build-guide/<chapter>/`    | Human-readable chapter routes            |
| Operations   | `/operations/<chapter>/`     | Post-build operating handbook            |
| Appendix     | `/appendix/<reference>/`     | Reference and support material           |
| Digital twin | `/digital-twin/first-slice/` | Interactive documentation first slice    |

Numbered chapter URLs are intentionally not preserved. This is a development-stage documentation site and the clean Starlight route structure is the source of truth.

## Validation Coverage

| Check                     | Command or script                     | Coverage                                               |
| ------------------------- | ------------------------------------- | ------------------------------------------------------ |
| Astro and Starlight types | `npm run check:astro`                 | Astro components, MDX integration, strict TypeScript   |
| Markdown linting          | `npm run lint:markdown`               | Markdown style and malformed table/link structures     |
| Static build              | `npm run starlight:build`             | Full GitHub Pages-compatible static output             |
| Site validator            | `scripts/validate-starlight.py`       | Route inventory, links, assets, digital twin fallbacks |
| Data validation           | `scripts/validate-data.py`            | Digital twin JSON Schema and cross-references          |
| QR validation             | `scripts/generate-qrcodes.py --check` | Official-link QR assets and manifest                   |

## Completion State

- Build guide pages have been moved to clean Starlight routes.
- Operations pages are first-class public Starlight routes for monitoring, software, drivers, fan control, backups, security, troubleshooting, benchmarking, maintenance, and upgrades.
- Appendix pages have been moved to clean Starlight routes.
- ADR, verification, migration inventory, audit, and historical QA records are repository records, not public Starlight pages.
- Milestone 5 and 6 validation archive pages were removed because they no longer add value to the current public site.
- Repository audit, documentation structure, standalone accessibility audit, ADR, verification register, and Starlight migration inventory pages were removed from the public site because repository records and validation now cover their useful information.
- Reader-facing diagram and image assets live under `public/assets/`.
- The GitHub Pages workflow builds and deploys `dist/`.
- The old source directory, old site configuration, and old build scripts have been removed.
