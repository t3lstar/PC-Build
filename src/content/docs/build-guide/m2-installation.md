---
title: "M.2 SSD Installation"
---

## Introduction

This chapter installs the Samsung 990 PRO 2TB NVMe SSD into a motherboard M.2 slot.

## Purpose

Install the Windows and game storage drive correctly with the motherboard heatsink in place.

## Estimated Time

10-20 minutes.

## Difficulty

Beginner to moderate.

## Required Tools

- Precision Phillips screwdriver if the M.2 heatsink uses screws.
- Anti-static wrist strap.
- Samsung 990 PRO 2TB SSD.
- Gigabyte B850 AORUS Elite WiFi7 user manual.

## Warnings

- Do not touch the SSD edge connector.
- Do not overtighten M.2 screws.
- Do not stack a motherboard heatsink on top of an SSD model that already has a tall heatsink.
- Do not forget to remove protective film from the motherboard M.2 thermal pad.
- Do not install a SATA M.2 drive; this build uses NVMe.

## Step-by-Step Instructions

1. Identify the `M2A_CPU` slot. This is the preferred boot SSD slot for this build because it is CPU-connected and supports PCIe 5.0 x4/x2 SSD capability with Ryzen 7000-series CPUs.
2. Remove the M.2 heatsink covering `M2A_CPU`.
3. Confirm the slot is set for an 80mm `2280` drive position.
4. Remove any protective film from the heatsink thermal pad.
5. Hold the Samsung 990 PRO by its edges.
6. Insert the SSD into the M.2 connector at a shallow angle.
7. Lower the free end of the SSD onto the standoff or latch point.
8. Secure the SSD with the motherboard latch or screw.
9. Reinstall the M.2 heatsink so the thermal pad contacts the SSD controller and NAND area.
10. Tighten the heatsink screws evenly and lightly.

## Verification Checklist

- [ ] SSD is M.2 2280 NVMe.
- [ ] SSD is installed in `M2A_CPU`.
- [ ] SSD is fully inserted into the connector.
- [ ] SSD is secured at the 2280 position.
- [ ] Thermal pad protective film is removed.
- [ ] M.2 heatsink is reinstalled.
- [ ] No M.2 screw or latch is loose.

## Common Mistakes

- Leaving plastic film on the thermal pad.
- Installing the drive at the wrong length position.
- Overtightening the heatsink.
- Using a heatsink-version SSD under the motherboard heatsink.
- Forgetting which slot contains the Windows drive.
- Installing a SATA M.2 drive; the motherboard M.2 connectors support PCIe/NVMe SSDs only.

## Expected Result

The Samsung 990 PRO 2TB drive is installed under a motherboard heatsink and ready to be detected during BIOS and Windows setup.

## Sources Reviewed

- [Gigabyte B850 AORUS Elite WiFi7 user manual 1101](https://download.gigabyte.com/FileList/Manual/mb_manual_b850-aorus-elite-wf7_1101_e.pdf)
- [Samsung 990 PRO data sheet](https://download.semiconductor.samsung.com/resources/data-sheet/samsung_nvme_ssd_990_pro_datasheet_rev.2.0.pdf)

## Next Chapter

Continue to [Memory Installation](/PC-Build/build-guide/memory-installation/).
