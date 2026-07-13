# Milestone 5: Professional Engineering Edition

Status: In progress.

GitHub milestone: https://github.com/t3lstar/PC-Build/milestone/1

Tracking issues: https://github.com/t3lstar/PC-Build/issues/5 through https://github.com/t3lstar/PC-Build/issues/18

## Purpose

Raise the existing GitHub Pages manual into publication-quality engineering documentation with stronger verification, maintenance, validation, and printable/PDF readiness.

## User Value

- A first-time builder can follow the guide beside the PC with fewer assumptions.
- Future maintenance and upgrades are recorded consistently.
- Technical claims are traceable to official sources or marked pending.
- Contributors have clear validation commands before publishing changes.

## Scope

- Standardise documentation structure where useful.
- Improve README, roadmap, contribution guidance, and project status.
- Create a verification register and resolve high-risk technical claims.
- Expand checklists, troubleshooting decision trees, maintenance schedules, monitoring guidance, and benchmark methodology.
- Add validation scripts for documentation, links, spelling, diagrams, SVGs, assets, and full local CI where practical.
- Improve GitHub Actions validation.
- Reintroduce reproducible PDF and printable output deliberately.
- Expand appendices for connectors, cables, logs, recovery, and verification.

## Out of Scope

- Interactive digital twin implementation.
- Invented benchmark scores.
- Photorealistic generated diagrams for technical references.
- Unverified connector maps.
- Server-side services or account-based state.

## Dependencies

- Completed Milestones 1-4.
- Existing MkDocs Material site.
- Official manufacturer manuals and support pages.
- Stable local Python 3.12 environment.
- Node.js 24 if Node-based validation tooling is introduced.

## Deliverables

- [ ] Repository audit and verification register.
- [ ] Consistent page structure and revision metadata.
- [ ] Improved README and contribution guidance.
- [ ] Expanded build, maintenance, and troubleshooting checklists.
- [ ] Mermaid troubleshooting decision trees.
- [x] Monitoring and optimisation guide.
- [x] Maintenance schedules and logs.
- [x] Benchmark baseline methodology.
- [x] Validation scripts and local CI wrapper.
- [ ] GitHub Actions validation expansion.
- [ ] Reproducible HTML and PDF/printable outputs.
- [ ] Expanded appendices and connector references.
- [ ] Final Milestone 5 QA report.

## Acceptance Criteria

- [ ] HTML builds cleanly locally and in GitHub Actions.
- [ ] PDF and standalone printable outputs build reproducibly or have a documented blocker.
- [ ] No known broken internal links remain.
- [ ] Critical technical claims are verified or explicitly marked pending.
- [ ] Troubleshooting decision trees render correctly.
- [ ] Maintenance and benchmarking guidance is complete.
- [ ] Validation commands are documented and repeatable.
- [ ] GitHub issues reflect delivered work.

## Validation Commands

Initial expected commands:

```bash
. .venv/bin/activate
./scripts/build.sh html
./scripts/build.sh all
```

Run the local validation wrapper when checking milestone changes:

```bash
. .venv/bin/activate
./scripts/validate.sh all
```

## Risks

- PDF generation may require dependency isolation and local/CI parity work.
- External links and product images can change.
- Official manual details may vary by motherboard revision or BIOS version.
- Over-standardising pages could make short appendices noisy.

## Assumptions

- The existing component list remains unchanged.
- GitHub Pages remains the primary publication target.
- PDF/printable output should be implemented only when it is reproducible and reasonably fast.

## Issue Breakdown

- [x] [#5: M5: Audit and technical verification register](https://github.com/t3lstar/PC-Build/issues/5)
- [x] [#6: M5: Standardise documentation structure and navigation](https://github.com/t3lstar/PC-Build/issues/6)
- [x] [#7: M5: Improve README, roadmap and contribution guidance](https://github.com/t3lstar/PC-Build/issues/7)
- [x] [#8: M5: Create build and maintenance checklists](https://github.com/t3lstar/PC-Build/issues/8)
- [x] [#9: M5: Add troubleshooting decision trees](https://github.com/t3lstar/PC-Build/issues/9)
- [x] [#10: M5: Complete monitoring and optimisation guide](https://github.com/t3lstar/PC-Build/issues/10) - implemented locally; GitHub issue remains open until the milestone checkpoint push passes Actions.
- [x] [#11: M5: Complete maintenance schedules and logs](https://github.com/t3lstar/PC-Build/issues/11) - implemented locally; GitHub issue remains open until the milestone checkpoint push passes Actions.
- [x] [#12: M5: Establish benchmark baseline methodology](https://github.com/t3lstar/PC-Build/issues/12) - implemented locally; GitHub issue remains open until the milestone checkpoint push passes Actions.
- [x] [#13: M5: Add documentation validation scripts](https://github.com/t3lstar/PC-Build/issues/13) - implemented locally; GitHub issue remains open until the milestone checkpoint push passes Actions.
- [x] [#14: M5: Implement GitHub Actions validation](https://github.com/t3lstar/PC-Build/issues/14)
- [ ] [#15: M5: Improve MkDocs Material site and print styling](https://github.com/t3lstar/PC-Build/issues/15)
- [ ] [#16: M5: Make HTML and PDF builds reproducible](https://github.com/t3lstar/PC-Build/issues/16)
- [ ] [#17: M5: Expand appendices and connector references](https://github.com/t3lstar/PC-Build/issues/17)
- [ ] [#18: M5: Milestone 5 final QA and release](https://github.com/t3lstar/PC-Build/issues/18)

## Definition of Done

- [ ] Deliverables are implemented or explicitly deferred with reasons.
- [ ] Validation report lists passed checks, warnings, limitations, and manual verification still required.
- [ ] GitHub milestone and issues are current.
- [ ] Documentation remains suitable for a first-time PC builder.

## Completion Checklist

- [ ] Update `MILESTONES.md`.
- [ ] Update project status documentation.
- [ ] Run validation.
- [ ] Verify GitHub Actions.
- [ ] Close Milestone 5 issues only when acceptance criteria are met.

## Suggested Implementation Order

1. Verification register and documentation structure.
2. README, contribution, and roadmap updates.
3. Checklists and troubleshooting trees.
4. Monitoring, maintenance, and benchmark content.
5. Validation scripts and CI.
6. PDF/printable build work.
7. Appendix expansion.
8. Final QA and release.
