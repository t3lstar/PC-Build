---
title: "Maintenance Schedule"
---

## Introduction

This chapter defines routine care for the completed PC.

## Purpose

Keep temperatures, airflow, storage health, driver state, and maintenance records under control over time.

## Estimated Time

10-30 minutes monthly; 45-90 minutes for deeper cleaning.

## Difficulty

Beginner.

## Required Tools

- Microfibre cloth.
- Low-pressure electric air duster or compressed air used carefully.
- Cable ties or hook-and-loop straps.
- Hardware monitoring software.
- Notes file for maintenance records.

## Warnings

- Power down and unplug the PC before physical cleaning.
- Hold fans still when cleaning them with air.
- Do not use household vacuum nozzles directly on components.
- Do not spray liquid cleaner into the case.
- Do not update BIOS casually; update for a reason.

## Step-by-Step Instructions

1. Monthly, inspect front, side, bottom, and top ventilation paths for dust.
2. Check idle CPU and GPU temperatures against the temperature reference.
3. Compare current readings with the [gaming optimisation](/PC-Build/build-guide/gaming-optimisation/) monitoring baseline.
4. Check that all fans spin normally and do not make new noise.
5. Review Windows Update and driver update state.
6. Every 3-6 months, power down, unplug, open the case, and clean dust filters.
7. Hold fans still and clear dust from fan blades and radiator fins.
8. Check cable ties and straps for pressure or rubbing.
9. Check SSD free space, storage layout, and health using vendor or monitoring software.
10. Record any BIOS, driver, hardware, or cooling changes.

Use the maintenance log templates in the [checklists appendix](/PC-Build/appendix/checklists/) to record monthly checks, driver/firmware changes, and hardware changes.

## Maintenance Schedule

- After build: record baseline temperatures, benchmark results, BIOS version, driver versions, fan behaviour, SSD health, backup state, and BitLocker recovery-key state.
- Weekly during the first month: check idle temperatures, fan noise, Windows Update state, SSD free space, and backup status so the new-build baseline becomes familiar.
- Monthly: check temperatures, dust filters, fan noise, SSD free space, Windows Update, driver state, backup health, and Windows Security status.
- Quarterly: clean accessible filters, inspect fan blades, inspect cable clearance, review software startup entries, and verify a sample file restore.
- Six monthly: open the case for deeper dust inspection, clean radiator and fan paths, inspect cable ties, review BIOS and driver release notes, and refresh recovery media if needed.
- Annual: review upgrade goals, backup strategy, BitLocker key storage, benchmark baseline, firmware state, fan curves, and installed utility list.
- Before major game installs: confirm SSD free space.
- Before long benchmark sessions: confirm radiator path is clear and monitoring software can see CPU, GPU, SSD, and fan readings.
- Before BIOS updates: read release notes and confirm the update is relevant.
- After driver updates: record the previous version, new version, reason, and result. Re-run a short stability check if the update affects chipset, GPU, network, or storage drivers.
- After hardware changes: re-run baseline checks, update your build notes, and compare with the previous benchmark baseline.

## Checklist By Interval

| Area | After build | Weekly first month | Monthly | Quarterly | Six monthly | Annual |
| --- | --- | --- | --- | --- | --- | --- |
| Cleaning | Confirm panels and filters are seated. | Visual dust check. | Filter check. | Clean filters. | Clean filters, fans, radiator path. | Review case placement and airflow. |
| Dust filters | Record initial state. | Inspect. | Inspect. | Clean. | Clean. | Replace if damaged. |
| Firmware | Record BIOS and SSD firmware. | No routine change. | Review only if symptoms exist. | Read release notes. | Update only for a reason. | Review support lifecycle. |
| Drivers | Record chipset, GPU, network, audio. | Watch for obvious issues. | Review versions. | Update if release notes justify it. | Revalidate if updated. | Review driver strategy. |
| Windows | Fully update after build. | Check restart state. | Patch normally. | Review feature update timing. | Check recovery options. | Review installed apps. |
| SSD health | Record Samsung Magician state. | Check free space. | Check health and temperature. | Check firmware notes. | Run benchmark only if needed. | Review storage capacity. |
| Storage layout | Confirm main `C:` volume. | No routine change. | Check library and capture locations. | Archive old captures. | Review large folders. | Plan second physical drive if needed. |
| Benchmark verification | Capture baseline. | No routine retest. | Retest only if symptoms exist. | Retest after driver/firmware changes. | Retest after cooling changes. | Refresh baseline if system changed. |
| Cable inspection | Inspect after cable management. | Listen for fan contact. | Visual check if panels are open. | Inspect ties and grommets. | Inspect strain and rubbing. | Review before upgrades. |
| Fan inspection | Record baseline noise. | Listen for new noise. | Check speeds. | Clean blades. | Clean and inspect bearings/noise. | Review curves. |
| Temperature review | Record idle/load baseline. | Compare idle. | Compare idle and light load. | Compare against baseline. | Compare after cleaning. | Refresh baseline if needed. |
| Backup verification | Configure backup. | Confirm first backup completes. | Check backup status. | Restore one test file. | Review recovery USB. | Full backup review. |

## Maintenance Triggers

Perform an out-of-schedule maintenance check when any of these occur:

- CPU, GPU, or SSD temperature is materially worse than the original baseline in similar room conditions.
- Fans ramp more often than usual or make new scraping, ticking, or vibration noise.
- Games begin stuttering after a driver, Windows, launcher, or game update.
- Device Manager shows a warning icon or unknown device.
- The PC has been moved, shipped, cleaned, or opened.
- The rear side panel becomes difficult to close because of cable pressure.
- SSD free space is low enough to affect updates, game installs, captures, or shader caches.
- A Windows feature update, BIOS update, GPU driver update, or chipset driver update is installed.

## What To Record

Keep logs concise. Do not share serial numbers, licence keys, account names, screenshots with personal data, or invoice details.

| Log                         | Record                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------ |
| Monthly maintenance         | Date, dust state, idle temperatures, fan noise, SSD free space, action taken.              |
| Driver and firmware changes | Previous version, new version, source, reason, result, rollback note if needed.            |
| Hardware changes            | Part changed, compatibility check, affected cables, baseline repeated, result.             |
| Thermal changes             | Room temperature if known, CPU/GPU/SSD readings, fan behaviour, dust state.                |
| Fault investigation         | Symptom, first observed date, recent changes, troubleshooting decision tree used, outcome. |

## Update and Rollback Rules

1. Update Windows normally, but avoid changing BIOS and GPU drivers on the same day unless a fault requires it.
2. Install chipset and GPU drivers from official sources only.
3. Do not update BIOS casually. Update BIOS for a documented compatibility, stability, security, or hardware-support reason.
4. Create a restore point before optional utilities, launcher stacks, capture software, or major driver changes.
5. Keep the previous known-good driver installer or source link noted until the new setup has been tested.
6. If a change causes crashes, display corruption, missing devices, or worse temperatures, roll back the most recent change first.

## Cleaning Procedure

1. Shut down Windows fully.
2. Switch off the PSU and unplug mains power.
3. Move the case to a clean, stable workspace.
4. Remove panels and filters according to the case chapter.
5. Hold fans still before using air.
6. Clear filters, radiator fins, fan blades, bottom intake paths, side intake paths, and top exhaust paths.
7. Inspect cable ties and straps for rubbing, pressure, or fan contact.
8. Refit filters and panels.
9. Boot and confirm fan readings, pump reading if exposed, and idle temperatures.
10. Record the maintenance action.

## Verification Checklist

- [ ] Filters are clean.
- [ ] Radiator airflow path is clear.
- [ ] Fans spin normally.
- [ ] Temperatures are consistent with baseline.
- [ ] SSD has sufficient free space.
- [ ] Game libraries and captures follow the SSD storage plan.
- [ ] Windows Update state is known.
- [ ] Driver and BIOS changes are recorded.
- [ ] No cable is rubbing against a fan.
- [ ] Any fault investigation is linked to the troubleshooting chapter.

## Common Mistakes

- Using too much air pressure on fans.
- Letting fans free-spin while cleaning.
- Updating BIOS without a relevant reason.
- Ignoring gradual temperature increases.
- Losing track of which update changed behaviour.
- Filling the SSD until performance and update space suffer.

## Expected Result

The PC remains clean, cool, stable, and documented throughout normal use.

## Next Chapter

Continue to [Backup and Recovery](/PC-Build/operations/backup-recovery/).
