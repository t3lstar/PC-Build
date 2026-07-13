---
title: "Starlight Source Inventory"
---
Status: Active Milestone 7 inventory. Last verified: 2026-07-13 18:05 BST.

## Purpose

Track the clean Astro Starlight source layout, routes, assets, and validation coverage for Milestone 7.

## Current Counts

| Source area                | Count | Notes                                                     |
| -------------------------- | ----: | --------------------------------------------------------- |
| Starlight content pages    | 40    | Complete manual, appendix, project, ADR, and digital twin |
| Build guide pages          | 26    | Clean routes under `/build-guide/`                        |
| Appendix pages             | 9     | Clean routes under `/appendix/`                           |
| Project and ADR pages      | 3     | Clean routes under `/project/` and `/adr/`                |
| Digital twin MDX pages     | 1     | `/digital-twin/first-slice/`                              |
| Reader-facing asset folder | 1     | `public/assets/`                                          |

## Source Ownership

| Area                  | Location                   | Ownership rule                                      |
| --------------------- | -------------------------- | --------------------------------------------------- |
| Documentation content | `src/content/docs/`        | Canonical source for all published pages            |
| Interactive views     | `src/components/`          | Astro components used by MDX pages                  |
| Site styling          | `src/styles/starlight.css` | Starlight theme overrides and digital twin styling  |
| Public assets         | `public/assets/`           | Images, diagrams, icons, generated QR code assets   |
| Digital twin data     | `data/digital-twin/`       | Framework-neutral build data and JSON Schema        |
| Build scripts         | `scripts/`                 | Local build, validation, QR generation, data checks |

## Route Strategy

| Content area | Route pattern                | Notes                                    |
| ------------ | ---------------------------- | ---------------------------------------- |
| Home         | `/`                          | Starlight landing page                   |
| Build guide  | `/build-guide/<chapter>/`    | Human-readable chapter routes            |
| Appendix     | `/appendix/<reference>/`     | Reference and support material           |
| ADR          | `/adr/<decision>/`           | Architecture decision records            |
| Project      | `/project/<record>/`         | Current validation and migration records |
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
- Appendix, ADR, and project pages have been moved to clean Starlight routes.
- Milestone 5 and 6 validation archive pages were removed because they no longer add value to the current public site.
- Repository audit, documentation structure, and standalone accessibility audit pages were removed because current README, Starlight navigation, digital twin content, and validation now cover their useful information.
- Reader-facing diagram and image assets live under `public/assets/`.
- The GitHub Pages workflow builds and deploys `dist/`.
- The old source directory, old site configuration, and old build scripts have been removed.
