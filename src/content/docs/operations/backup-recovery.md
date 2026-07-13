---
title: "Backup and Recovery"
---

## Introduction

This chapter defines practical recovery coverage for Windows, personal files, game saves, BitLocker recovery, and recovery media.

## Purpose

Make recovery possible before driver, firmware, storage, or Windows problems occur.

## Estimated Time

30-90 minutes for initial setup; 10-20 minutes for routine verification.

## Difficulty

Beginner to moderate.

## Required Tools

- Windows Backup or chosen file backup tool.
- External drive or cloud backup target.
- USB drive for Windows recovery media.
- Microsoft account or secure password manager for BitLocker recovery key storage.

## Warnings

- Do not store the only BitLocker recovery key on the encrypted PC.
- Do not publish recovery keys, account names, licence keys, or backup screenshots.
- Do not assume game saves are backed up by every launcher.
- Test recovery media before relying on it.

## Recovery Layers

| Layer | Purpose | Recommended use |
| --- | --- | --- |
| Restore point | Roll back system files/settings after driver or software changes. | Create before optional utilities, major drivers, and risky configuration changes. |
| File backup | Recover documents, saves, configs, screenshots, and personal data. | Continuous cloud backup or scheduled external backup. |
| System image or full-disk backup | Recover the full system state after major failure. | Use if you want faster bare-metal recovery than reinstalling Windows. |
| Recovery USB | Boot recovery tools if Windows does not start. | Create after Windows is stable and keep labelled. |
| BitLocker recovery key | Unlock encrypted drive after firmware/security/hardware changes. | Store in Microsoft account and password manager or printed secure copy. |
| BIOS profile record | Restore BIOS settings after update or clear CMOS. | Photograph or write down EXPO, fan, boot, Secure Boot, TPM, and virtualisation settings. |

## Step-by-Step Instructions

1. Turn on Windows System Protection for the Windows drive.
2. Create a manual restore point after the stable baseline.
3. Choose file backup coverage for documents, saved games, photos, config exports, and maintenance logs.
4. Create a Windows recovery drive.
5. Confirm BitLocker state before BIOS or TPM changes.
6. Back up the BitLocker recovery key outside the PC.
7. Export or record FanControl, benchmark, and BIOS settings where possible.
8. Test that backups can be browsed and at least one harmless file can be restored.
9. Record the date of the last successful recovery test.

## Verification Checklist

- [ ] Restore point creation is tested.
- [ ] Personal files are backed up.
- [ ] Recovery USB exists.
- [ ] BitLocker recovery key is stored outside the PC.
- [ ] FanControl and benchmark records are backed up.
- [ ] A restore test has been performed.
- [ ] Backup date is recorded.

## Common Mistakes

- Confusing restore points with file backups.
- Saving the only recovery key on the encrypted drive.
- Forgetting game saves stored outside common folders.
- Never testing recovery media.
- Updating BIOS before checking BitLocker recovery-key access.

## Expected Result

The PC can recover from driver faults, Windows issues, failed storage, lost settings, or encryption recovery prompts with less risk.

## Sources Reviewed

- [Microsoft System Restore](https://support.microsoft.com/en-us/windows/experience/backup-recovery/system-restore)
- [Microsoft System Protection](https://support.microsoft.com/en-us/windows/experience/backup-recovery/system-protection)
- [Microsoft Windows Backup](https://support.microsoft.com/en-us/windows/experience/backup-recovery/back-up-and-restore-with-windows-backup)
- [Microsoft Recovery Drive](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-drive)
- [Microsoft BitLocker recovery key](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key)

## Next Chapter

Continue to [Security](/PC-Build/operations/security/).
