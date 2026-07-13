# Upgrades

Status: Initial Milestone 2 content. Last verified: 2026-07-13.

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

| Area | Guidance |
| --- | --- |
| RAM | Prefer replacing the full kit with a verified matched kit. Do not add a second separate kit casually. |
| SSD | Additional M.2 NVMe storage is acceptable if the selected slot supports the drive size and heatsink arrangement. |
| GPU | Confirm length, thickness, PCIe power connectors, and anti-sag support. |
| CPU | Confirm BIOS support before replacing the processor. |
| Cooling | Confirm radiator thickness, fan position, and tube routing. |
| PSU | Replace the PSU and cables as a set if changing PSU model. |

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

Return to the [Home](index.md) page or use the appendix pages for checklists, BIOS settings, drivers, and reference material.
