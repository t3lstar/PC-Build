---
title: "Security"
---
Status: Published HTML content. Last reviewed: 2026-07-13 18:34 BST.

## Introduction

This chapter defines a practical security baseline for the completed Windows 11 Pro gaming PC.

## Purpose

Keep Windows, firmware, accounts, browsers, downloads, and recovery keys secure without adding unnecessary utility suites.

## Estimated Time

30-60 minutes for initial setup; 10 minutes monthly.

## Difficulty

Beginner to moderate.

## Required Tools

- Windows Security.
- Windows Update.
- Browser with password-manager support or dedicated password manager.
- Two-factor authentication method.
- Official vendor support links.

## Warnings

- Do not disable Windows Security for benchmark gains.
- Do not download drivers from search ads, mirrors, or generic updater tools.
- Do not store BitLocker recovery keys only on the encrypted PC.
- Do not install browser extensions unless they are needed and trusted.

## Security Baseline

| Area | Recommendation | Verification |
| --- | --- | --- |
| Windows Security | Use Microsoft Defender/Windows Security unless there is a specific requirement for another suite. | Windows Security dashboard has no unresolved action. |
| Secure Boot | Keep enabled unless a documented tool requires a temporary change. | BIOS and Windows System Information show expected state. |
| TPM | Keep enabled for Windows 11 security and BitLocker support. | Windows Security and TPM management detect TPM. |
| BitLocker | Use if encryption is desired; store recovery key safely first. | Recovery key is accessible outside the PC. |
| Password manager | Use browser or dedicated password manager with strong unique passwords. | Important accounts have unique passwords. |
| Two-factor authentication | Enable on Microsoft, email, Steam, Epic, GitHub, and other important accounts. | Recovery codes are stored safely. |
| Browser security | Keep browser updated, minimise extensions, and avoid download ads. | Browser update status is current. |
| Driver download safety | Use AMD, Gigabyte, Samsung, Microsoft, and official tool sites. | Downloads match the documented official links. |
| Firmware verification | Read release notes and verify model before BIOS/firmware updates. | Update reason and version are recorded. |

## Step-by-Step Instructions

1. Run Windows Update until no required restart remains.
2. Open Windows Security and resolve active warnings.
3. Confirm Secure Boot and TPM are enabled.
4. Decide whether to enable BitLocker.
5. Store BitLocker recovery keys outside the PC before firmware changes.
6. Enable two-factor authentication for important accounts.
7. Review browser extensions and remove unused ones.
8. Bookmark official driver and support sources from [Driver Strategy](/PC-Build/operations/driver-strategy/).
9. Create a restore point before installing optional utilities.
10. Review security status monthly or after major updates.

## Verification Checklist

- [ ] Windows Security is healthy.
- [ ] Windows Update state is current.
- [ ] Secure Boot state is known.
- [ ] TPM state is known.
- [ ] BitLocker recovery key access is confirmed if BitLocker is enabled.
- [ ] Important accounts use unique passwords.
- [ ] Two-factor authentication is enabled for important accounts.
- [ ] Driver downloads come from official sources.

## Common Mistakes

- Installing a third-party antivirus because a download site recommends it.
- Disabling Secure Boot and forgetting to re-enable it.
- Updating BIOS without BitLocker recovery-key access.
- Using the same password for Microsoft account, email, and game stores.
- Clicking sponsored driver download results.

## Expected Result

The system keeps the default Windows security model strong and avoids unnecessary security or driver-download risk.

## Sources Reviewed

- [Microsoft BitLocker overview](https://support.microsoft.com/en-us/windows/security/encryption/bitlocker-overview)
- [Microsoft BitLocker recovery key backup](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key)
- [Microsoft Windows Security](https://support.microsoft.com/windows)

## Next Chapter

Continue to [Troubleshooting](/PC-Build/operations/troubleshooting/).
