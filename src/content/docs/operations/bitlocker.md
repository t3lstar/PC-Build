---
title: "BitLocker Drive Encryption"
---

## Introduction

This chapter explains the optional BitLocker setup for the Windows 11 Pro drive.

BitLocker encrypts the Samsung 990 PRO boot SSD so personal files are harder to access if the PC or SSD is stolen. It is not a backup system and it does not prevent malware or account compromise while Windows is unlocked.

## Purpose

Decide whether BitLocker is appropriate, enable it safely if desired, store the recovery key outside the PC, and understand when the recovery key may be required.

## Estimated Time

20-45 minutes for setup; encryption continues in the background.

## Difficulty

Beginner to moderate.

## Required Tools

- Windows 11 Pro administrator account.
- Microsoft account, password manager, printed record, or another secure recovery-key storage location.
- Internet access if saving the recovery key to a Microsoft account.
- Backup target for important files.

## Warnings

- Do not enable BitLocker until Windows, drivers, activation, Secure Boot, TPM, and basic stability are confirmed.
- Do not store the only recovery key on the encrypted PC.
- Do not publish or screenshot the recovery key.
- Do not update BIOS, clear TPM, replace the motherboard, or change Secure Boot settings without confirming recovery-key access first.
- Do not treat BitLocker as a backup. If files are deleted, corrupted, or overwritten, encryption will not recover them.

## Pros and Cons

| Benefit | Trade-off |
| --- | --- |
| Protects personal files if the PC or SSD is stolen. | Recovery key is required if Windows asks for recovery and automatic unlock fails. |
| Uses Windows 11 Pro built-in tooling. | Adds one more item to manage before BIOS, TPM, Secure Boot, or motherboard changes. |
| Works well with TPM and Secure Boot when configured correctly. | Losing the recovery key can make the encrypted Windows installation inaccessible. |
| Low maintenance after setup. | Troubleshooting from recovery media can require the recovery key. |

## When To Enable BitLocker

Enable BitLocker after:

1. Windows 11 Pro is installed and activated.
2. Windows Update has completed.
3. AMD chipset, Gigabyte, network, audio, and Radeon drivers are installed.
4. Device Manager has no unknown devices.
5. Secure Boot and TPM are enabled and stable.
6. A restore point or backup plan exists.
7. You have chosen at least two recovery-key storage locations.

Delay BitLocker if:

- The PC is still failing stability checks.
- BIOS settings are still changing frequently.
- You cannot access a safe recovery-key storage location.
- You are about to update BIOS or change hardware.

## Recovery-Key Storage Plan

Use at least two storage locations:

- Microsoft account recovery-key storage, if you use a Microsoft account.
- Password manager secure note.
- Printed copy stored with other important household records.
- USB flash drive stored away from the PC.

Avoid:

- Saving the only key in Documents, Downloads, Desktop, or a screenshot on the encrypted PC.
- Storing the key in the same bag or box as the PC.
- Publishing the key in notes, photos, logs, support tickets, or screenshots.

## Step-by-Step Instructions

1. Complete Windows installation, driver installation, and the first stable baseline.
2. Back up important files before enabling encryption.
3. Open Start.
4. Type `BitLocker`.
5. Open **Manage BitLocker**.
6. Find the Windows drive.
7. Select **Turn on BitLocker**.
8. Choose recovery-key backup options before encryption starts.
9. Save the recovery key to at least two safe locations.
10. Confirm that the recovery key can be accessed from another device.
11. Choose the option to encrypt used disk space only for a new Windows installation.
12. Choose the modern encryption mode unless Windows indicates a compatibility reason not to.
13. Start encryption.
14. Keep the PC powered while encryption begins.
15. Restart if prompted.
16. Open **Manage BitLocker** again and confirm that BitLocker is on for the Windows drive.
17. Record only the BitLocker state and recovery-key storage locations in your private maintenance notes. Do not record the key in public notes.

## Before BIOS, TPM, Secure Boot, or Hardware Changes

Before changing low-level settings:

1. Confirm the recovery key is accessible from another device.
2. Back up important files.
3. Record the current BIOS version and changed settings.
4. Make only one firmware or security change at a time.
5. Reboot and confirm Windows unlocks normally before making another change.

If Windows asks for the recovery key, match the displayed key ID to the stored recovery key and enter the 48-digit recovery key.

## Verification Checklist

- [ ] Windows 11 Pro is activated.
- [ ] Secure Boot is enabled or its state is known.
- [ ] TPM is enabled or its state is known.
- [ ] Important files are backed up.
- [ ] Recovery key is stored outside the PC.
- [ ] Recovery key can be retrieved from another device.
- [ ] BitLocker is on for the Windows drive.
- [ ] BIOS, TPM, and Secure Boot changes are not planned before key access is verified.

## Common Mistakes

- Enabling BitLocker before the build is stable.
- Saving the only recovery key on the encrypted drive.
- Updating BIOS without checking recovery-key access.
- Confusing BitLocker with backup.
- Publishing recovery-key screenshots or recovery IDs.
- Forgetting that recovery media, System Restore, reset operations, and hardware changes may ask for the key.

## Expected Result

BitLocker is either deliberately left off, or it is enabled with recovery-key access confirmed outside the PC.

## Sources Reviewed

- [Microsoft BitLocker overview](https://support.microsoft.com/en-us/windows/security/encryption/bitlocker-overview)
- [Microsoft BitLocker Drive Encryption](https://support.microsoft.com/en-us/windows/security/encryption/bitlocker-drive-encryption)
- [Microsoft Back up your BitLocker recovery key](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key)
- [Microsoft Find your BitLocker recovery key](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key)

## Next Chapter

Continue to [Security](/PC-Build/operations/security/).
