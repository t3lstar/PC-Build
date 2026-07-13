# Starlight Migration Inventory

Status: Active Milestone 7 inventory. Last verified: 2026-07-13 17:02 BST.

## Purpose

Track the full migration from MkDocs Material to Astro Starlight so content, routes, assets, and validation do not drift during Milestone 7.

## Current Counts

| Source | Page count | Notes |
| --- | ---: | --- |
| MkDocs Markdown pages under `docs/` | 46 | Current complete manual and project documentation source, including this inventory page. |
| Starlight pages under `src/content/docs/` | 7 | First slice plus selected migrated pages from Milestone 6. |
| Missing from Starlight | 39 | Must be migrated or explicitly archived during Milestone 7. |

## Existing Starlight Pages

| Starlight source | Current route | Status |
| --- | --- | --- |
| `src/content/docs/index.md` | `/` | Present. |
| `src/content/docs/components.md` | `/components/` | Present; route differs from MkDocs `/02-components/`. |
| `src/content/docs/case-overview.md` | `/case-overview/` | Present; route differs from MkDocs `/04-case-overview/`. |
| `src/content/docs/digital-twin/first-slice.mdx` | `/digital-twin/first-slice/` | Present and published. |
| `src/content/docs/appendix/connectors-cables.md` | `/appendix/connectors-cables/` | Present. |
| `src/content/docs/project/adr-0001-digital-twin-architecture.md` | `/project/adr-0001-digital-twin-architecture/` | Present; route differs from MkDocs `/adr/0001-digital-twin-architecture/`. |
| `src/content/docs/project/digital-twin-accessibility.md` | `/project/digital-twin-accessibility/` | Present. |

## MkDocs Page Inventory

| MkDocs source | Current published route | Starlight target | Migration status |
| --- | --- | --- | --- |
| `docs/index.md` | `/` | `/` | Present; needs parity review. |
| `docs/01-introduction.md` | `/01-introduction/` | `/01-introduction/` | Missing. |
| `docs/02-components.md` | `/02-components/` | `/02-components/` | Partial content exists at `/components/`; route strategy required. |
| `docs/03-motherboard-overview.md` | `/03-motherboard-overview/` | `/03-motherboard-overview/` | Missing. |
| `docs/04-case-overview.md` | `/04-case-overview/` | `/04-case-overview/` | Partial content exists at `/case-overview/`; route strategy required. |
| `docs/05-tools.md` | `/05-tools/` | `/05-tools/` | Missing. |
| `docs/06-build-preparation.md` | `/06-build-preparation/` | `/06-build-preparation/` | Missing. |
| `docs/07-cpu-installation.md` | `/07-cpu-installation/` | `/07-cpu-installation/` | Missing. |
| `docs/08-memory-installation.md` | `/08-memory-installation/` | `/08-memory-installation/` | Missing. |
| `docs/09-m2-installation.md` | `/09-m2-installation/` | `/09-m2-installation/` | Missing. |
| `docs/10-case-build.md` | `/10-case-build/` | `/10-case-build/` | Missing. |
| `docs/11-psu-installation.md` | `/11-psu-installation/` | `/11-psu-installation/` | Missing. |
| `docs/12-motherboard-installation.md` | `/12-motherboard-installation/` | `/12-motherboard-installation/` | Missing. |
| `docs/13-aio-installation.md` | `/13-aio-installation/` | `/13-aio-installation/` | Missing. |
| `docs/14-gpu-installation.md` | `/14-gpu-installation/` | `/14-gpu-installation/` | Missing. |
| `docs/15-cable-routing.md` | `/15-cable-routing/` | `/15-cable-routing/` | Missing. |
| `docs/16-front-panel-connectors.md` | `/16-front-panel-connectors/` | `/16-front-panel-connectors/` | Missing. |
| `docs/17-first-boot.md` | `/17-first-boot/` | `/17-first-boot/` | Missing. |
| `docs/18-bios.md` | `/18-bios/` | `/18-bios/` | Missing. |
| `docs/19-expo.md` | `/19-expo/` | `/19-expo/` | Missing. |
| `docs/20-driver-installation.md` | `/20-driver-installation/` | `/20-driver-installation/` | Missing. |
| `docs/21-windows-installation.md` | `/21-windows-installation/` | `/21-windows-installation/` | Missing. |
| `docs/22-gaming-optimisation.md` | `/22-gaming-optimisation/` | `/22-gaming-optimisation/` | Missing. |
| `docs/23-benchmarks.md` | `/23-benchmarks/` | `/23-benchmarks/` | Missing. |
| `docs/24-troubleshooting.md` | `/24-troubleshooting/` | `/24-troubleshooting/` | Missing. |
| `docs/25-maintenance.md` | `/25-maintenance/` | `/25-maintenance/` | Missing. |
| `docs/26-upgrades.md` | `/26-upgrades/` | `/26-upgrades/` | Missing. |
| `docs/appendix/glossary.md` | `/appendix/glossary/` | `/appendix/glossary/` | Missing. |
| `docs/appendix/faq.md` | `/appendix/faq/` | `/appendix/faq/` | Missing. |
| `docs/appendix/checklists.md` | `/appendix/checklists/` | `/appendix/checklists/` | Missing. |
| `docs/appendix/connectors-cables.md` | `/appendix/connectors-cables/` | `/appendix/connectors-cables/` | Present; needs parity review. |
| `docs/appendix/bill-of-materials.md` | `/appendix/bill-of-materials/` | `/appendix/bill-of-materials/` | Missing. |
| `docs/appendix/drivers.md` | `/appendix/drivers/` | `/appendix/drivers/` | Missing. |
| `docs/appendix/bios-settings.md` | `/appendix/bios-settings/` | `/appendix/bios-settings/` | Missing. |
| `docs/appendix/temperature-reference.md` | `/appendix/temperature-reference/` | `/appendix/temperature-reference/` | Missing. |
| `docs/appendix/publishing.md` | `/appendix/publishing/` | `/appendix/publishing/` | Missing. |
| `docs/adr/0001-digital-twin-architecture.md` | `/adr/0001-digital-twin-architecture/` | `/adr/0001-digital-twin-architecture/` | Partial content exists at `/project/adr-0001-digital-twin-architecture/`; route strategy required. |
| `docs/project/repository-audit.md` | `/project/repository-audit/` | `/project/repository-audit/` | Missing. |
| `docs/project/documentation-structure.md` | `/project/documentation-structure/` | `/project/documentation-structure/` | Missing. |
| `docs/project/verification-register.md` | `/project/verification-register/` | `/project/verification-register/` | Missing. |
| `docs/project/digital-twin-accessibility.md` | `/project/digital-twin-accessibility/` | `/project/digital-twin-accessibility/` | Present; needs parity review. |
| `docs/project/starlight-migration-inventory.md` | `/project/starlight-migration-inventory/` | `/project/starlight-migration-inventory/` | New Milestone 7 page; MkDocs-first until Starlight migration. |
| `docs/project/milestone-05-06-validation-report.md` | `/project/milestone-05-06-validation-report/` | `/project/milestone-05-06-validation-report/` | Missing. |
| `docs/project/milestone-05-final-qa.md` | `/project/milestone-05-final-qa/` | `/project/milestone-05-final-qa/` | Missing. |
| `docs/project/milestone-06-final-qa.md` | `/project/milestone-06-final-qa/` | `/project/milestone-06-final-qa/` | Missing. |

## Route Decisions Needed

| Area | Decision needed |
| --- | --- |
| Numbered build chapters | Prefer preserving existing numbered routes such as `/07-cpu-installation/`. |
| Existing unnumbered Starlight first-slice pages | Decide whether to keep as compatibility pages or replace with numbered canonical routes. |
| ADR route | Preserve `/adr/0001-digital-twin-architecture/` or add a compatibility route from the current Starlight project route. |
| Digital twin route | Keep `/digital-twin/first-slice/` as the published interactive route. |
| MkDocs-only project pages | Migrate useful pages; archive obsolete migration-era pages only after final QA. |

## Syntax and Asset Risks

| Risk | Notes |
| --- | --- |
| MkDocs admonitions and details blocks | Must be checked in Starlight; some syntax may need MDX-compatible conversion. |
| Mermaid fences | Starlight does not automatically match the current MkDocs Material Mermaid setup. Prefer rendered SVGs or an approved Astro integration. |
| Diagram lightbox JavaScript | Current click-to-enlarge behavior is MkDocs-specific and must be replaced or retired after equivalent Starlight behavior exists. |
| Local Markdown links | Links that include `.md` source paths may need route conversion. |
| Asset paths | MkDocs `docs/assets/` paths and Starlight `public/assets/` paths need a clear final ownership model. |
| Search | MkDocs search and Starlight Pagefind behavior differ; final deployment should use one production search system. |

## Migration Order

1. Port numbered build guide chapters while preserving existing published routes.
2. Port appendix pages and project pages.
3. Rebuild Starlight sidebar groups.
4. Resolve route compatibility for existing published MkDocs URLs.
5. Verify diagrams, QR assets, and static images.
6. Expand validation to cover migrated pages and internal links.
7. Switch GitHub Pages to Starlight-primary output.
8. Retire or archive MkDocs once live parity is verified.
