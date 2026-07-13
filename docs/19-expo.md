# EXPO Memory Setup

Status: Initial Milestone 2 content. Last verified: 2026-07-13 10:53 BST.

## Introduction

This chapter enables the DDR5 EXPO memory profile after the system has already booted successfully at default settings.

## Purpose

Run the approved DDR5 kit at its intended DDR5-6000 CL30 profile while preserving a clear rollback path if memory training fails.

## Estimated Time

15-30 minutes.

## Difficulty

Moderate.

## Required Tools

- Keyboard.
- Motherboard manual.
- Stable AC power.

## Warnings

- Do not enable EXPO before the system has passed a default boot.
- DDR5 memory training after enabling EXPO can take several minutes.
- Do not manually increase memory voltage unless a documented troubleshooting step requires it.
- If the system fails to boot repeatedly, clear CMOS and return to defaults.

## Step-by-Step Instructions

1. Boot into BIOS at default memory settings.
2. Confirm both DIMMs are detected in `A2` and `B2`.
3. Locate the AMD EXPO profile setting.
4. Select the EXPO profile for the installed kit.
5. Confirm the target speed is DDR5-6000 and primary latency matches the kit specification.
6. Save changes and reboot.
7. Allow memory training to complete.
8. Enter BIOS again and confirm the profile is active.
9. Boot into Windows after installation and run a memory stability check before treating the build as complete.

## Rollback Procedure

1. If the system loops or does not display output after several minutes, power it off.
2. Use the motherboard clear-CMOS procedure.
3. Boot back into BIOS defaults.
4. Confirm the memory kit and slot positions.
5. Re-enable EXPO only after the cause is understood.

## Verification Checklist

- [ ] Default boot worked before EXPO was enabled.
- [ ] Memory modules are in `A2` and `B2`.
- [ ] EXPO profile is selected, not an unrelated manual profile.
- [ ] BIOS reports DDR5-6000 after reboot.
- [ ] Windows boots after EXPO is enabled.
- [ ] Memory stability testing is scheduled after driver installation.

## Common Mistakes

- Enabling EXPO before the first default boot.
- Assuming a blank screen during training is immediate failure.
- Mixing memory kits.
- Changing manual timings without a reason.
- Forgetting to save BIOS settings before rebooting.

## Expected Result

The system runs the approved DDR5 memory kit using its EXPO profile and remains bootable.

## Next Chapter

Continue to [Gaming Optimisation](22-gaming-optimisation.md).
