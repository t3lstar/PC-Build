---
title: "Software To Avoid"
---

## Introduction

This chapter lists software categories that are generally unnecessary or undesirable for this Windows 11 Pro gaming PC.

## Purpose

Avoid tools that add instability, duplicate Windows features, obscure the real fault, or create security risk.

## Estimated Time

10 minutes.

## Difficulty

Beginner.

## Required Tools

- Windows Settings.
- Installed apps list.
- Restore point before removing deeply integrated utilities.

## Warnings

- Do not remove vendor drivers or security components without understanding their role.
- Do not use cleanup tools to make bulk registry or driver changes.
- Do not treat higher benchmark numbers from a booster utility as proof of better stability.

## Avoided Categories

| Category | Why it is usually unnecessary or undesirable | Better approach |
| --- | --- | --- |
| Registry cleaners | Windows and applications expect registry state to be consistent. Bulk cleaning can remove entries that only look unused. | Leave the registry alone unless a vendor support article gives a specific fix. |
| RAM optimisers | Windows memory management already caches and releases memory. Forced clearing can reduce performance and hide real memory pressure. | Use Task Manager and Resource Monitor to identify actual high-memory processes. |
| Generic driver updater tools | They may install wrong, old, bundled, or non-vendor drivers. They also make rollback harder because the source is unclear. | Use AMD, Gigabyte, Samsung, Microsoft, and device-vendor sources. |
| Game boosters | Many duplicate Windows Game Mode, close services blindly, or change settings without a repeatable baseline. | Use Windows Game Mode, update drivers deliberately, and benchmark one change at a time. |
| SSD defragmentation tools | SSDs do not benefit from old hard-drive defrag behaviour and unnecessary writes are not useful. | Let Windows handle SSD optimisation automatically. |
| Third-party antivirus suites | Windows Security is enough for most home gaming systems and avoids duplicate scanning, browser injection, and driver conflicts. | Use Windows Security unless a specific household, employer, or compliance requirement needs another product. |
| RGB and motherboard utility stacks | Multiple low-level utilities can add startup services and duplicate fan, update, or monitoring functions. | Install only the specific utility needed, then remove it if it is not part of daily operation. |
| Automatic overclocking utilities | One-click tuning can change voltage, power, and thermal behaviour before a baseline exists. | Keep defaults until baseline testing is complete; tune only as a separate documented project. |

## Step-by-Step Instructions

1. Open Windows Settings > Apps > Installed apps.
2. Identify utilities that control drivers, cleaning, boosting, fan curves, RGB, overlays, or antivirus.
3. Keep only utilities with a documented purpose in [Recommended Software](/PC-Build/operations/recommended-software/).
4. Remove duplicate monitoring, fan, and GPU tuning tools.
5. Reboot after removing low-level utilities.
6. Confirm Device Manager, Windows Security, AMD Adrenalin, and monitoring still behave normally.

## Verification Checklist

- [ ] No generic driver updater is installed.
- [ ] No registry cleaner is installed.
- [ ] No RAM optimiser is installed.
- [ ] No game booster is installed.
- [ ] No SSD defrag utility is installed.
- [ ] Windows Security is active unless a deliberate alternative is required.
- [ ] Only one fan-control strategy is active.

## Common Mistakes

- Installing a utility because a benchmark guide recommends it without understanding the change.
- Removing Windows Security features for small benchmark gains.
- Letting a motherboard app auto-update BIOS or drivers without review.
- Keeping several overlays active and then troubleshooting stutter.

## Expected Result

The PC avoids unnecessary background software and keeps low-level system changes deliberate.

## Next Chapter

Continue to [Driver Strategy](/PC-Build/operations/driver-strategy/).
