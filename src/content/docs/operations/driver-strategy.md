---
title: "Driver Strategy"
---

## Introduction

This chapter defines when to update drivers and firmware, when to wait, how to roll back, and how to verify the result.

## Purpose

Keep the system stable by treating chipset, GPU, BIOS, SSD firmware, and Windows updates as controlled changes.

## Estimated Time

15-45 minutes per update cycle.

## Difficulty

Moderate.

## Required Tools

- [Gigabyte B850 AORUS Elite WiFi7 support](https://www.gigabyte.com/Motherboard/B850-AORUS-ELITE-WIFI7-rev-1x/support).
- [AMD drivers and support](https://www.amd.com/en/support/download/drivers.html).
- [Samsung Magician](https://semiconductor.samsung.com/consumer-storage/magician/).
- Windows Update.
- Restore point.
- Benchmark and monitoring logs.

## Warnings

- Do not update BIOS casually.
- Do not update BIOS, chipset, GPU, Windows feature version, and fan software on the same day unless recovering from a fault.
- Do not use third-party driver updater tools.
- Do not interrupt BIOS or firmware updates.

## Update Strategy

| Area | When to update | When not to update | Rollback strategy | Verification after update |
| --- | --- | --- | --- | --- |
| AMD chipset driver | New build, stability fixes, Windows feature update issues, AMD release relevant to AM5/chipset stability. | Immediately before important work or when the system is stable and release notes are irrelevant. | Reinstall previous known-good package if retained; use restore point if needed. | Device Manager clean, sleep/wake works, USB/network stable, benchmark sanity check. |
| AMD GPU driver | Game support, security, stability, bug fix, known issue resolved, new GPU feature needed. | Day-one release before important gaming session, or if current driver is stable and release notes do not matter. | AMD installer rollback/cleanup first; DDU only for persistent driver corruption. | Radeon app opens, monitor refresh correct, 3DMark/game test passes, no driver timeout. |
| Samsung SSD firmware | Samsung Magician reports relevant firmware update or a documented stability/compatibility fix. | During unstable power, active backups, or without current file backup. | Firmware rollback may not be available; rely on backup and vendor guidance. | SMART health normal, drive visible, CrystalDiskMark sanity check if needed. |
| Gigabyte motherboard BIOS | CPU compatibility, memory stability, security, firmware bug, Q-Flash recovery, or documented issue relevant to this build. | Purely because a newer BIOS exists. | Keep previous BIOS file if Gigabyte supports rollback; record settings before update. | BIOS detects CPU, RAM, SSD, fans; EXPO state reviewed; Windows boots; baseline checks repeated. |
| Windows Update | Security, reliability, driver prerequisites, normal monthly patching. | During benchmark baseline capture or immediately before an important gaming session if restart risk is unacceptable. | Windows recovery options, restore point, uninstall recent update where supported. | No required restart, Device Manager clean, games and drivers still behave normally. |

## Step-by-Step Instructions

1. Record the current BIOS, chipset, GPU, SSD firmware, and Windows version.
2. Read the relevant release notes or support page.
3. Confirm the update has a reason.
4. Create a restore point for driver and Windows changes.
5. Confirm backups before BIOS or SSD firmware changes.
6. Update one area at a time.
7. Reboot when required.
8. Record the new version and result.
9. Run the shortest relevant verification test.
10. Wait before making another low-level change unless the first change failed.

## Verification Checklist

- [ ] Previous version is recorded.
- [ ] New version source is official.
- [ ] Update reason is recorded.
- [ ] Restore point or backup exists where appropriate.
- [ ] Only one low-level change was made.
- [ ] Device Manager is clean.
- [ ] Relevant benchmark or game sanity check passed.
- [ ] Rollback note is recorded.

## Common Mistakes

- Updating everything because one driver is available.
- Forgetting to record the old version.
- Updating BIOS without saving current settings.
- Using DDU before trying the official AMD installer path.
- Running benchmarks immediately while Windows Update still has pending work.

## Expected Result

Drivers and firmware stay current enough for stability and security without turning updates into uncontrolled variables.

## Next Chapter

Continue to [Monitoring](/PC-Build/operations/monitoring/).
