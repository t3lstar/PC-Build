# Milestone 6: Interactive Digital Twin Edition

Status: In progress.

GitHub milestone: https://github.com/t3lstar/PC-Build/milestone/2

Tracking issues: https://github.com/t3lstar/PC-Build/issues/19 through https://github.com/t3lstar/PC-Build/issues/35

## Purpose

Add an accurate, maintainable interactive representation of the PC that supplements the static build guide without compromising reliability.

## User Value

- Builders can inspect component locations, airflow, and cable routes visually.
- The interactive view links directly back to verified written instructions.
- Future upgrades can be planned against structured build data.
- Static documentation remains usable when JavaScript or interactivity is unavailable.

## Scope

- Create a digital twin architecture ADR.
- Migrate the site to Astro Starlight as the direct Milestone 6 target platform through issue `#35`, a controlled first slice before switching production deployment.
- Define a validated build data model and JSON Schema.
- Create verified component, connector, cable, airflow, and sequence data.
- Build a minimal accessible interactive vertical slice first.
- Add case view, component inspection, connector map, cable-routing mode, build-sequence mode, airflow visualisation, exploded assembly view, BIOS training simulator, driver/update dashboard, QR codes, and maintenance/upgrade history as approved by the ADR.
- Add data, interaction, accessibility, responsive, and generated-asset tests.

## Out of Scope

- Heavy 3D implementation before an ADR justifies it.
- Photorealistic or generative-art technical representations.
- Live scraping of driver or BIOS versions without an approved mechanism.
- Server-side accounts, cloud storage, or secrets.
- Unverified connector positions or cable routes.

## Dependencies

- Milestone 5 verification and validation foundations.
- Official manuals for connector and layout verification.
- Static hosting constraints for GitHub Pages.
- Accessibility requirements for keyboard, touch, screen reader, reduced-motion, and high-contrast use.

## Deliverables

- [x] `docs/adr/0001-digital-twin-architecture.md` - accepted; Astro Starlight is the direct target platform.
- [x] Structured build data under `data/` - verified component, connector, cable, airflow, build-sequence, BIOS-state, and reference-link dataset implemented locally for issue #21.
- [x] JSON Schema and validation tests.
- [x] Astro Starlight first slice - implemented locally; production deployment remains MkDocs until the Starlight switch is approved.
- [x] Accessible interactive case view.
- [ ] Clickable component inspection.
- [x] Verified motherboard connector map.
- [x] Cable-routing mode.
- [x] Guided build-sequence mode.
- [x] Airflow visualisation with static fallback.
- [x] Lightweight exploded assembly view.
- [x] Clearly labelled BIOS training simulator.
- [x] Driver and firmware source dashboard.
- [x] QR codes for stable official URLs.
- [x] Local-only maintenance and upgrade history.
- [ ] Accessibility, responsive, and data-integrity tests.

## Acceptance Criteria

- [x] ADR is accepted before implementation choices are locked in.
- [x] Digital twin data validates against JSON Schema.
- [ ] Every interactive component maps to structured data.
- [x] Cable routes and connector positions are verified or explicitly marked unverified in the structured data.
- [x] Static fallbacks remain available for the implemented case view.
- [x] Keyboard navigation and visible focus indicators work for the implemented case view.
- [ ] Reduced-motion behavior is supported.
- [ ] The site remains static and deployable through GitHub Pages.
- [ ] Performance remains reasonable on desktop and tablet.

## Validation Commands

Initial expected commands:

```bash
. .venv/bin/activate
./scripts/build.sh html
```

Validate digital twin data:

```bash
. .venv/bin/activate
./scripts/validate.sh data
```

Future commands should include interaction tests, accessibility checks, and generated-asset drift checks.

## Risks

- Interactive features may drift from static documentation unless data is authoritative.
- Connector accuracy depends on official manual verification.
- 3D assets can increase maintenance burden and page weight.
- Accessibility can regress if visual interaction is implemented without keyboard and static alternatives.

## Assumptions

- The digital twin supplements, not replaces, the written guide.
- The initial vertical slice should be SVG or similarly lightweight unless the ADR proves a stronger need.
- User progress is stored locally without an account.

## Issue Breakdown

- [x] [#19: M6: Digital twin architecture ADR](https://github.com/t3lstar/PC-Build/issues/19) - accepted locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#20: M6: Define build data model and JSON Schema](https://github.com/t3lstar/PC-Build/issues/20) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#35: M6: Migrate site to Astro Starlight first slice](https://github.com/t3lstar/PC-Build/issues/35) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#21: M6: Create verified component and connector dataset](https://github.com/t3lstar/PC-Build/issues/21) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#22: M6: Implement interactive case view](https://github.com/t3lstar/PC-Build/issues/22) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#23: M6: Implement motherboard connector map](https://github.com/t3lstar/PC-Build/issues/23) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#24: M6: Implement cable-routing mode](https://github.com/t3lstar/PC-Build/issues/24) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#25: M6: Implement guided build-sequence mode](https://github.com/t3lstar/PC-Build/issues/25) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#26: M6: Implement airflow visualisation](https://github.com/t3lstar/PC-Build/issues/26) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#27: M6: Implement exploded assembly view](https://github.com/t3lstar/PC-Build/issues/27) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#28: M6: Implement educational BIOS simulator](https://github.com/t3lstar/PC-Build/issues/28) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#29: M6: Add driver and firmware source dashboard](https://github.com/t3lstar/PC-Build/issues/29) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#30: M6: Generate and validate official-link QR codes](https://github.com/t3lstar/PC-Build/issues/30) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [x] [#31: M6: Add maintenance and upgrade history](https://github.com/t3lstar/PC-Build/issues/31) - implemented locally; GitHub issue remains open until the next milestone checkpoint push passes Actions.
- [ ] [#32: M6: Complete accessibility and static fallbacks](https://github.com/t3lstar/PC-Build/issues/32)
- [ ] [#33: M6: Add data, interaction and accessibility tests](https://github.com/t3lstar/PC-Build/issues/33)
- [ ] [#34: M6: Milestone 6 final QA and release](https://github.com/t3lstar/PC-Build/issues/34)

## Definition of Done

- [ ] ADR, data model, implementation, tests, and documentation are aligned.
- [ ] Validation report supports completion.
- [ ] GitHub milestone and issues are current.
- [ ] Static documentation still works without the interactive layer.

## Completion Checklist

- [ ] Update `MILESTONES.md`.
- [ ] Update AGENTS guidance if implementation conventions evolve.
- [ ] Validate data, accessibility, and static-site build.
- [ ] Verify GitHub Pages deployment.
- [ ] Close Milestone 6 issues only when acceptance criteria are met.

## Suggested Implementation Order

1. ADR.
2. Data model and schema.
3. Verified component dataset.
4. Minimal accessible vertical slice.
5. Cable route and airflow modes.
6. Connector map.
7. BIOS simulator and dashboards.
8. QR codes and maintenance records.
9. Full accessibility and regression tests.
10. Final QA and release.
