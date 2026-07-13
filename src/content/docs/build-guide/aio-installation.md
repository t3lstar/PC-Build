---
title: "AIO Installation"
---
Status: Verified Milestone 5 content. Last verified: 2026-07-13 13:42 BST.

## Introduction

This chapter installs the ARCTIC Liquid Freezer III Pro 360 on the Ryzen 7 7800X3D and mounts the 360mm radiator in the top of the Lian Li O11 Dynamic Mini V2 Flow.

## Purpose

Install CPU cooling with correct AM5 mounting pressure, radiator orientation, cable routing, and clearance around the motherboard.

Use the [connector and cable reference](/PC-Build/appendix/connectors-cables/) for the simple all-in-one `CPU_FAN` path and the optional individual-control header paths.

## Estimated Time

45-75 minutes.

## Difficulty

Moderate.

## Required Tools

- Phillips #2 screwdriver.
- ARCTIC AM5 mounting hardware.
- ARCTIC Liquid Freezer III Pro 360 online manual.
- Gigabyte B850 AORUS Elite WiFi7 user manual.
- Thermal paste supplied with the cooler unless pre-applied.
- Isopropyl alcohol and lint-free cloth if paste must be cleaned.
- Flashlight.

## Warnings

- The ARCTIC radiator is thicker than many 360mm AIO radiators. Dry-fit before final tightening.
- Route CPU EPS cables before fixing the radiator in place.
- Do not run the pump without the cold plate mounted.
- Do not overtighten pump mounting screws.
- Do not use the wrong screws through the radiator; screws that are too long can puncture the radiator.
- Remove protective film from the cold plate before installation.

## Step-by-Step Instructions

1. Confirm the motherboard is installed and CPU EPS power is connected.
2. Remove the case top radiator bracket or top access panel as needed.
3. Dry-fit the radiator and fans in the top position.
4. Confirm the radiator does not crush CPU EPS cables, fan cables, memory, or motherboard heatsinks.
5. Orient the radiator tubes so they avoid sharp bends and do not interfere with the RAM.
6. Attach the radiator and fans to the top bracket using the correct ARCTIC screws.
7. Install the AM5 mounting hardware according to the ARCTIC manual.
8. Clean the CPU heat spreader only if it has been touched or contaminated.
9. Apply thermal paste if the cooler does not already have suitable paste applied.
10. Remove the protective film from the pump cold plate.
11. Lower the pump block straight onto the CPU.
12. Tighten the mounting screws gradually and evenly.
13. Connect the pump/fan cable according to the chosen ARCTIC cable mode.
14. For the simple build path, use the ARCTIC all-in-one cable and connect it to `CPU_FAN`. This gives one PWM control signal and monitoring path for the cooler assembly.
15. For later individual tuning, use the ARCTIC individual-control cable only if you deliberately want separate pump, VRM fan, and radiator fan control. Connect those leads to 4-pin PWM-capable motherboard headers such as `CPU_FAN`, `CPU_OPT`, and `FAN4_PUMP`, then label the leads before closing the rear chamber.
16. In BIOS, set the connected cooler headers to PWM mode before tuning curves.
17. Secure loose fan and pump cables away from fan blades.

## Verification Checklist

- [ ] Radiator is mounted at the top.
- [ ] CPU EPS cables are not pinched.
- [ ] Radiator screws are the correct length.
- [ ] Cold plate protective film is removed.
- [ ] Pump block is evenly mounted.
- [ ] Fan and pump cables are connected.
- [ ] Connected cooler headers are planned for PWM mode in BIOS.
- [ ] Tubes are not sharply kinked.
- [ ] Fans spin freely by hand.

## Common Mistakes

- Installing the radiator before connecting CPU EPS power.
- Leaving cold-plate film installed.
- Using the wrong radiator screws.
- Applying too much thermal paste.
- Connecting pump/fan cables to an unmonitored or disabled header.
- Using the individual-control cable without noting which lead is pump, VRM fan, and radiator fans.
- Letting a cable touch the fan blades.

## Expected Result

The CPU cooler is mounted, the top radiator is secured, and pump/fan cables are ready for BIOS monitoring.

## Sources Reviewed

- [ARCTIC Liquid Freezer III Pro 360 manual](https://support.arctic.de/en/liquid-freezer-iii-pro-360)
- [ARCTIC Liquid Freezer III Pro 360 product page](https://www.arctic.de/en/Liquid-Freezer-III-Pro-360/ACFRE00180A)
- [Gigabyte B850 AORUS Elite WiFi7 user manual 1101](https://download.gigabyte.com/FileList/Manual/mb_manual_b850-aorus-elite-wf7_1101_e.pdf)

## Next Chapter

Continue to [GPU Installation](/PC-Build/build-guide/gpu-installation/).
