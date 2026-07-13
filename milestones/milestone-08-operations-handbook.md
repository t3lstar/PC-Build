# Milestone 8: Operations, Monitoring and Maintenance Handbook

Status: Implemented locally; deployment pending.

GitHub milestone: <https://github.com/t3lstar/PC-Build/milestone/4>

Tracking issues: <https://github.com/t3lstar/PC-Build/issues/45> through <https://github.com/t3lstar/PC-Build/issues/57>

## Purpose

Add a first-class Operations section for maintaining, monitoring, securing, troubleshooting, benchmarking, and upgrading the completed PC throughout its lifetime.

## User Value

- Readers can operate the PC safely after the build is complete.
- Monitoring, drivers, firmware, backups, security, maintenance, and upgrades become deliberate routines.
- Recommended software is documented with official sources, safe settings, update cadence, and removal guidance.
- Troubleshooting and upgrade work can start from known baselines instead of guesswork.

## Scope

- Add Operations navigation and route strategy.
- Move relevant maintenance, troubleshooting, benchmark, and upgrade guidance under Operations.
- Add recommended software and software-to-avoid guidance.
- Add driver, firmware, monitoring, FanControl, backup, security, and maintenance schedule guidance.
- Add validation for Operations routes and recommended software completeness.
- Cross-link relevant build guide and appendix pages.

## Out of Scope

- Inventing benchmark scores.
- Inventing hardware-specific limits that are not officially verified.
- Publishing private maintenance logs, serial numbers, licence keys, account names, or BitLocker recovery keys.
- Adding paid monitoring or tuning requirements where free official or reputable tools are sufficient.

## Dependencies

- Milestone 7 completed Starlight site.
- Existing build guide, appendix, and digital twin content.
- Official vendor and software download/support sources.

## Deliverables

- [x] Operations overview.
- [x] Recommended software reference.
- [x] Software-to-avoid guidance.
- [x] Driver and firmware strategy.
- [x] Monitoring handbook.
- [x] FanControl configuration.
- [x] Benchmark baseline procedure.
- [x] Maintenance schedule.
- [x] Backup and recovery guide.
- [x] Security guide.
- [x] Troubleshooting guide.
- [x] Upgrade planning guide.
- [x] Expanded validation.
- [ ] Final QA and release evidence.

## Acceptance Criteria

- [x] Operations is a first-class Starlight navigation section.
- [x] Existing maintenance, benchmark, troubleshooting, and upgrade guidance is moved or refactored under Operations.
- [x] Every recommended software package has an official source, installation guidance, update guidance, safe configuration, usage cadence, permanence guidance, resource note, alternatives, and uninstall guidance.
- [x] Software-to-avoid guidance explains the technical reasoning.
- [x] Driver and firmware guidance documents update timing, rollback, risks, and verification.
- [x] Monitoring guidance covers CPU, GPU, SSD, motherboard, power, clocks, memory speed, fan speeds, and voltages without inventing unverified limits.
- [x] FanControl guidance covers bottom intake, side intake, top radiator fans, pump handling, sensors, curves, quiet, gaming, and stress-test profiles.
- [x] Backup and security guidance covers restore points, recovery media, BitLocker recovery keys, Windows Security, Secure Boot, TPM, password manager, two-factor authentication, browser safety, driver download safety, and firmware verification.
- [x] Validation covers Operations routes and recommended software completeness.
- [ ] GitHub Pages deploys the Operations section successfully.

## Issue Breakdown

- [x] [#45: M8: Plan Operations information architecture](https://github.com/t3lstar/PC-Build/issues/45)
- [x] [#46: M8: Add Operations overview](https://github.com/t3lstar/PC-Build/issues/46)
- [x] [#47: M8: Build recommended software reference](https://github.com/t3lstar/PC-Build/issues/47)
- [x] [#48: M8: Add software-to-avoid guidance](https://github.com/t3lstar/PC-Build/issues/48)
- [x] [#49: M8: Add driver and firmware strategy](https://github.com/t3lstar/PC-Build/issues/49)
- [x] [#50: M8: Add monitoring handbook](https://github.com/t3lstar/PC-Build/issues/50)
- [x] [#51: M8: Add FanControl configuration](https://github.com/t3lstar/PC-Build/issues/51)
- [x] [#52: M8: Add benchmark baseline procedure](https://github.com/t3lstar/PC-Build/issues/52)
- [x] [#53: M8: Add maintenance schedule](https://github.com/t3lstar/PC-Build/issues/53)
- [x] [#54: M8: Add backup and security guides](https://github.com/t3lstar/PC-Build/issues/54)
- [x] [#55: M8: Expand troubleshooting and upgrade planning](https://github.com/t3lstar/PC-Build/issues/55)
- [x] [#56: M8: Expand Operations validation](https://github.com/t3lstar/PC-Build/issues/56)
- [ ] [#57: M8: Final QA and release](https://github.com/t3lstar/PC-Build/issues/57)

## Completion Checklist

- [x] Update `MILESTONES.md`.
- [x] Update `milestones/README.md`.
- [x] Update Starlight navigation.
- [x] Validate local Starlight build.
- [ ] Verify GitHub Pages deployment.
- [ ] Close Milestone 8 issues only after deployment evidence is recorded.
