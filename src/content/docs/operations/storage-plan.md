---
title: "SSD Storage Plan"
---

## Introduction

This chapter defines how to use the Samsung 990 PRO 2TB SSD after Windows is installed.

The build uses one fast NVMe SSD for Windows, applications, games, launchers, captures, benchmarks, and active files. The recommended setup is simple: let Windows create its required system partitions and keep one main `C:` volume for normal use.

## Purpose

Set up storage in a way that is easy to maintain, avoids unnecessary partition management, preserves free space, and keeps backup responsibilities clear.

## Estimated Time

20-40 minutes after Windows setup.

## Difficulty

Beginner.

## Required Tools

- Windows Settings.
- File Explorer.
- Samsung Magician.
- Backup target or cloud backup account.
- Game launcher settings if using Steam, Epic, Xbox, GOG, or similar launchers.

## Warnings

- Do not split the SSD into separate OS and data partitions unless you have a specific recovery workflow that needs it.
- Do not treat a second partition on the same SSD as a backup.
- Do not fill the SSD completely. Keep free space available for Windows updates, game updates, shader caches, captures, and SSD maintenance headroom.
- Do not move Windows system folders with registry edits or unsupported tools.
- Do not run old hard-drive defragmentation utilities on the SSD.

## Recommended Layout

| Area | Recommendation | Reason |
| --- | --- | --- |
| Windows system partitions | Let Windows Setup create them automatically. | Windows creates the EFI, Microsoft reserved, recovery, and main Windows partitions it needs. |
| Main volume | Use one main `C:` volume for Windows, applications, launchers, games, active files, and benchmark tools. | One volume is simpler to manage on a single physical SSD. |
| Personal files | Keep normal user folders on `C:` unless backup software or cloud sync requires a different location. | Avoids broken paths and first-time setup confusion. |
| Game libraries | Keep launchers and primary game libraries on the NVMe SSD. | Uses the SSD performance the build was designed for. |
| Captures and exports | Keep active captures on the SSD, then move long-term archives to backup or external storage. | Avoids filling the boot drive with large video files. |
| Backups | Store backups outside the PC or in a cloud backup service. | A partition on the same SSD does not protect against SSD failure. |

## Why Not Split OS and Data

Separate `C:` and `D:` partitions can be useful in some professional imaging workflows, but they are not the best default for this single-SSD gaming build.

Use one main volume because:

- The SSD is one physical device. If it fails, every partition on it is affected.
- Fixed partition sizes can waste space or cause avoidable low-space problems.
- Windows, launchers, game stores, captures, and user folders are easier to manage when paths stay standard.
- Backups, restore points, and recovery media provide more useful protection than partition separation.

Consider a separate data drive later if:

- Game libraries, captures, or video projects outgrow the 2TB SSD.
- You want a dedicated scratch/export drive.
- You want to separate active work from Windows reinstall risk using a second physical drive.

## Free-Space Target

Keep at least 15-20% of the SSD free where practical.

For a 2TB drive, use this as a simple operating rule:

- Above 500GB free: comfortable.
- 300-500GB free: monitor before installing large games or capture workloads.
- Below 300GB free: clean up, move archives, or plan more storage.
- Below 200GB free: treat as a maintenance issue before major Windows, game, or driver updates.

## Step-by-Step Instructions

1. During Windows setup, select the Samsung 990 PRO and install Windows to unallocated space.
2. Let Windows create its required partitions automatically.
3. After Windows setup, keep the main Windows volume as `C:`.
4. Install chipset, network, audio, Radeon, and Samsung Magician software from official sources.
5. Open Samsung Magician and confirm the SSD model, health state, firmware state, temperature, and capacity.
6. Create standard folders under your user profile for documents, downloads, screenshots, captures, and active projects.
7. Configure game launchers to use the NVMe SSD for active games.
8. Configure cloud backup or external backup for documents, saves, configuration exports, and important screenshots.
9. Move old captures, installers, and archives off the SSD when they are no longer active.
10. Check free space monthly and before installing large games or running long capture sessions.

## Game Libraries and Large Files

Use the SSD for:

- Windows.
- Drivers and monitoring tools.
- Active games.
- Game launchers.
- Benchmark tools.
- Active captures and video exports.

Move or archive:

- Old installers.
- Completed video exports.
- Duplicate screenshots.
- Old benchmark logs.
- Games not currently being played if free space is low.

## Backup Rules

Back up the files you cannot easily replace:

- Documents.
- Save games that are not cloud-synced.
- Configuration exports.
- Photos and screenshots you want to keep.
- Benchmark and maintenance logs.
- Recovery-key location notes.

Do not rely on:

- A separate partition on the same SSD.
- Game launcher cloud saves without checking that the specific game supports them.
- Screenshots of recovery keys stored only on the encrypted PC.

## Future Expansion

If storage becomes tight, add a second physical drive rather than repartitioning the Samsung 990 PRO.

Recommended expansion paths:

- Additional M.2 NVMe SSD for game libraries, captures, or active project files.
- External SSD for portable archives and temporary transfer.
- NAS or cloud backup for files that need recovery protection.

Before adding another drive, check the motherboard M.2 slot, heatsink, screw/latch hardware, lane-sharing notes, and thermal path.

## Verification Checklist

- [ ] Windows was installed to unallocated space on the Samsung 990 PRO.
- [ ] Windows created its required system partitions automatically.
- [ ] Main usable volume remains `C:`.
- [ ] Samsung Magician identifies the SSD and reports health.
- [ ] Free-space target is understood.
- [ ] Game launcher library location is known.
- [ ] Important personal files are backed up outside the SSD.
- [ ] Large captures and exports have an archive plan.

## Common Mistakes

- Creating separate OS and data partitions without a clear reason.
- Treating a second partition as a backup.
- Filling the SSD with captures or unused games.
- Moving user folders with unsupported methods.
- Running repeated SSD benchmarks without a troubleshooting reason.
- Ignoring SSD free space before large game updates.

## Expected Result

The Samsung 990 PRO remains simple to manage, has enough free space for normal use, and is protected by real backups rather than partition separation.

## Sources Reviewed

- [Samsung 990 PRO data sheet](https://download.semiconductor.samsung.com/resources/data-sheet/samsung_nvme_ssd_990_pro_datasheet_rev.2.0.pdf)
- [Samsung Magician](https://semiconductor.samsung.com/consumer-storage/magician/)
- [Microsoft Windows Backup](https://support.microsoft.com/en-us/windows/experience/backup-recovery/back-up-and-restore-with-windows-backup)
- [Microsoft BitLocker overview](https://support.microsoft.com/en-us/windows/security/encryption/bitlocker-overview)

## Next Chapter

Continue to [BitLocker Drive Encryption](/PC-Build/operations/bitlocker/).
