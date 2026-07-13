---
title: "Upgrade Planning"
---

## Introduction

This chapter explains how to plan future upgrades without breaking the build's compatibility assumptions.

## Purpose

Keep future CPU, RAM, SSD, GPU, cooling, PSU, and case changes deliberate and documented.

## Estimated Time

30-60 minutes for planning; installation time depends on the upgrade.

## Difficulty

Moderate.

## Required Tools

- Current bill of materials.
- Motherboard manual.
- Case manual.
- PSU cable inventory.
- Manufacturer support pages.

## Warnings

- Do not buy upgrades only from retailer titles. Confirm manufacturer model numbers.
- Do not mix memory kits.
- Do not assume a larger GPU fits because the current GPU fits.
- Do not reuse modular PSU cables from another PSU.
- Do not update BIOS unless the upgrade needs it or release notes justify it.

## Step-by-Step Instructions

1. Define the upgrade goal: performance, capacity, noise, thermals, connectivity, or reliability.
2. Record the current baseline before changing hardware.
3. Check motherboard socket, chipset, BIOS, slot, and memory support.
4. Check case clearance for GPU length, GPU thickness, radiator placement, and PSU length.
5. Check PSU wattage and connector requirements.
6. Check operating system and driver implications.
7. Update the bill of materials before purchase if the upgrade becomes a permanent build option.
8. Install one hardware change at a time.
9. Boot at default settings after the change.
10. Re-run relevant benchmark and temperature checks.

## Upgrade Notes

| Area    | Guidance                                                                                                         |
| ------- | ---------------------------------------------------------------------------------------------------------------- |
| RAM     | Prefer replacing the full kit with a verified matched kit. Do not add a second separate kit casually.            |
| SSD     | Additional M.2 NVMe storage is acceptable if the selected slot supports the drive size and heatsink arrangement. |
| GPU     | Confirm length, thickness, PCIe power connectors, and anti-sag support.                                          |
| CPU     | Confirm BIOS support before replacing the processor.                                                             |
| Cooling | Confirm radiator thickness, fan position, and tube routing.                                                      |
| PSU     | Replace the PSU and cables as a set if changing PSU model.                                                       |

## Upgrade Types

| Upgrade | Planning checks | BIOS implications | Driver implications | Validation after upgrade |
| --- | --- | --- | --- | --- |
| Additional NVMe drive | Check M.2 slot support, heatsink, lane sharing, screw/latch hardware, and thermal path. | Usually none unless storage detection issues occur. | Windows may install storage driver automatically; Samsung Magician only applies to Samsung drives. | Confirm drive detection, format intentionally, check temperature, run storage sanity test. |
| GPU replacement | Check GPU length, thickness, weight support, PCIe power, PSU headroom, and display outputs. | Usually none unless Resize BAR or compatibility setting needs review. | Remove old driver only when changing vendor or fixing faults; install official GPU driver. | Run 3DMark/game test, check power cable seating, temperature, fan behaviour. |
| RAM increase | Prefer a new matched kit; verify motherboard QVL or vendor compatibility. | BIOS update may be needed for memory compatibility; EXPO must be retested. | No Windows driver change, but memory instability can appear as app or game crashes. | Run MemTest86 and normal workload checks. |
| CPU change | Check AM5 support, BIOS version, cooler compatibility, and power/thermal behaviour. | BIOS update may be required before installing a newer CPU. | Chipset driver update may be sensible after CPU/platform change. | Check BIOS detection, temperatures, Cinebench, OCCT short test. |
| Fan replacement | Check size, connector type, PWM/DC mode, airflow direction, and cable path. | Header mode or fan curve may need review. | FanControl profile may need recalibration. | Confirm RPM readings, airflow direction, noise, and thermal response. |
| AIO replacement | Check radiator support, thickness, tube routing, pump header, fan headers, and mounting hardware. | Fan/pump curve review required. | FanControl profile may need recalibration. | Check pump reading, CPU idle/load temperature, leak/noise inspection. |
| PSU reuse or replacement | Check wattage, quality, connectors, cable compatibility, and warranty age. | Usually none. | No driver change. | Use only cables from the selected PSU, verify boot/load stability. |

## Verification Checklist

- [ ] Upgrade goal is documented.
- [ ] Current baseline is recorded.
- [ ] Compatibility evidence is documented before purchase.
- [ ] Required BIOS version is known if relevant.
- [ ] Physical clearances are checked.
- [ ] PSU connectors and wattage are checked.
- [ ] Post-upgrade tests are planned.

## Common Mistakes

- Buying RAM with the same speed but different ICs or profiles and mixing it with the existing kit.
- Ignoring GPU thickness and support bracket clearance.
- Assuming all M.2 slots behave identically.
- Updating BIOS after installing a CPU that required the update beforehand.
- Forgetting to update the documentation after a successful upgrade.

## Expected Result

Future upgrades can be planned, installed, tested, and documented without invalidating the build guide.

## Next Chapter

Return to the [Home](/PC-Build/) page or use the appendix pages for checklists, BIOS settings, drivers, and reference material.
