---
title: "Windows Installation"
---

## Introduction

This chapter installs Windows 11 Pro from the USB installer that is already assumed to be available.

## Purpose

Create a clean Windows installation on the Samsung 990 PRO 2TB NVMe SSD.

## Estimated Time

45-90 minutes.

## Difficulty

Beginner to moderate.

## Required Tools

- Windows 11 Pro USB installer.
- Keyboard and mouse.
- Monitor connected to the GPU.
- Network connection.
- Windows licence or activation entitlement.

## Warnings

- Windows setup can erase drives. Confirm the selected drive before deleting partitions.
- Do not install Windows to a secondary or temporary drive.
- Keep the PC connected to stable power during installation.
- Do not remove the USB installer until Windows setup has copied files and rebooted.

## Step-by-Step Instructions

1. Insert the Windows 11 Pro USB installer.
2. Boot the system and choose the USB installer from the boot menu.
3. Select Windows 11 Pro when prompted for edition.
4. Choose custom installation.
5. Select the Samsung 990 PRO 2TB NVMe SSD.
6. Delete existing partitions only if this is a new or intentionally wiped drive.
7. Install Windows to the unallocated space on the SSD.
8. Let setup copy files and reboot.
9. Remove the USB installer when Windows begins booting from the SSD.
10. Complete the out-of-box setup.
11. Connect to the network.
12. Run Windows Update before installing optional applications or games.
13. Activate Windows 11 Pro.
14. Leave BitLocker off until Windows, drivers, Secure Boot, TPM, and basic stability are confirmed.
15. Keep the default single main `C:` volume unless the [SSD Storage Plan](/PC-Build/operations/storage-plan/) is deliberately changed later.

## Verification Checklist

- [ ] Windows boots from the NVMe SSD.
- [ ] Windows edition is Pro.
- [ ] The installation drive is the Samsung 990 PRO.
- [ ] Network is available.
- [ ] Windows Update runs successfully.
- [ ] Windows activation is complete or clearly pending.
- [ ] No unnecessary setup media remains selected as first boot device.
- [ ] BitLocker is left off until the optional BitLocker guide is completed.
- [ ] Windows created the required system partitions automatically.
- [ ] Main usable storage is the `C:` volume.

## Common Mistakes

- Installing the wrong Windows edition.
- Leaving the USB installer as the first boot device.
- Deleting partitions on the wrong drive.
- Creating separate OS and data partitions without a clear reason.
- Installing applications before Windows Update and drivers.
- Forgetting to activate Windows.
- Enabling BitLocker before the recovery key has been stored safely.

## Expected Result

Windows 11 Pro is installed cleanly on the NVMe SSD and ready for driver installation. Storage planning and BitLocker remain optional post-build operations chapters.

## Next Chapter

Continue to [Driver Installation](/PC-Build/build-guide/driver-installation/).
