# Milestone 7: Full Starlight Migration

Status: In progress locally.

GitHub milestone: https://github.com/t3lstar/PC-Build/milestone/3

Tracking issues: https://github.com/t3lstar/PC-Build/issues/36 through https://github.com/t3lstar/PC-Build/issues/44

## Purpose

Migrate the complete PC build manual from MkDocs Material to Astro Starlight while preserving content parity, route behavior, validation, and GitHub Pages publication.

## User Value

- Readers get one consistent Starlight documentation experience.
- The digital twin becomes part of the main documentation site rather than a separately merged slice.
- Future interactive documentation can evolve without maintaining two parallel site systems.
- Existing published URLs are preserved or deliberately redirected.

## Scope

- Inventory all MkDocs and Starlight pages.
- Port numbered build guide chapters.
- Port appendix, ADR, project, milestone, and validation pages.
- Rebuild Starlight navigation.
- Preserve or redirect current published routes.
- Migrate diagram, image, QR, and digital twin asset behavior.
- Expand Starlight validation and link checks.
- Switch GitHub Pages to Starlight-primary output only after parity is proven.
- Retire or archive MkDocs build behavior after the production switch.
- Record final QA and release evidence.

## Out of Scope

- Rewriting technical content without a migration need.
- New hardware feature work unrelated to Starlight migration.
- PDF generation.
- Browser screenshot automation unless separately approved.

## Dependencies

- Milestone 6 published digital twin first slice.
- Existing MkDocs documentation and navigation.
- Existing Starlight first-slice scaffold.
- Node.js 24 local and CI runtime.
- Python 3.12 `.venv` for legacy validation until MkDocs is retired.

## Deliverables

- [x] Migration parity inventory for issue `#36` implemented locally; GitHub issue remains open until the next checkpoint push passes Actions.
- [ ] Full build guide chapter migration.
- [ ] Appendix and project page migration.
- [ ] Full Starlight navigation.
- [ ] Route preservation or redirect strategy.
- [ ] Diagram and asset compatibility.
- [ ] Expanded Starlight validation.
- [ ] Starlight-primary GitHub Pages deployment.
- [ ] MkDocs retirement or archive decision.
- [ ] Final QA report.

## Acceptance Criteria

- [ ] Every MkDocs source page is either migrated to Starlight or explicitly archived.
- [ ] Every important published MkDocs route is preserved or has a documented compatibility route.
- [ ] Starlight navigation exposes the full manual.
- [ ] Digital twin remains published and accessible.
- [ ] Diagram and image assets render correctly.
- [ ] Starlight validation covers migrated pages, internal links, and critical assets.
- [ ] GitHub Pages deploys the Starlight-primary site successfully.
- [ ] Milestone 7 issues are closed only after live deployment verification.

## Issue Breakdown

- [x] [#36: M7: Create Starlight migration parity inventory](https://github.com/t3lstar/PC-Build/issues/36) - implemented locally; GitHub issue remains open until the next checkpoint push passes Actions.
- [ ] [#37: M7: Port build guide chapters to Starlight](https://github.com/t3lstar/PC-Build/issues/37)
- [ ] [#38: M7: Port appendix and project docs to Starlight](https://github.com/t3lstar/PC-Build/issues/38)
- [ ] [#39: M7: Rebuild Starlight navigation and route strategy](https://github.com/t3lstar/PC-Build/issues/39)
- [ ] [#40: M7: Migrate diagrams and asset behavior to Starlight](https://github.com/t3lstar/PC-Build/issues/40)
- [ ] [#41: M7: Expand Starlight validation and link checks](https://github.com/t3lstar/PC-Build/issues/41)
- [ ] [#42: M7: Switch GitHub Pages deployment to Starlight](https://github.com/t3lstar/PC-Build/issues/42)
- [ ] [#43: M7: Retire or archive MkDocs build path](https://github.com/t3lstar/PC-Build/issues/43)
- [ ] [#44: M7: Full Starlight migration final QA and release](https://github.com/t3lstar/PC-Build/issues/44)

## Implementation Order

1. Complete parity inventory.
2. Port build guide chapters.
3. Port appendix and project docs.
4. Rebuild navigation and route compatibility.
5. Migrate diagrams and assets.
6. Expand Starlight validation.
7. Switch GitHub Pages deployment.
8. Retire or archive MkDocs.
9. Final QA and release.

## Completion Checklist

- [ ] Update `MILESTONES.md`.
- [ ] Update README and CONTRIBUTING.
- [ ] Validate local Starlight build.
- [ ] Validate route and asset parity.
- [ ] Verify GitHub Pages deployment.
- [ ] Close Milestone 7 issues only after deployment evidence is recorded.
