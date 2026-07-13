---
title: "Front Panel Connectors"
---

## Introduction

This chapter connects the case power switch, front USB, USB-C, and front audio cables to the Gigabyte B850 AORUS Elite WiFi7 motherboard.

## Purpose

Make the case controls and front I/O work correctly before first boot.

Use the [connector and cable reference](/PC-Build/appendix/connectors-cables/) for front-panel polarity rules and related internal USB/audio header guidance.

## Estimated Time

20-35 minutes.

## Difficulty

Moderate because front-panel header pins are small.

## Required Tools

- Gigabyte B850 AORUS Elite WiFi7 user manual.
- Case manual.
- Flashlight.
- Precision screwdriver or tweezers if needed for positioning small plugs.

## Warnings

- Do not force USB 3.x or USB-C headers; bent pins are difficult to repair.
- Do not guess front-panel pins. Use the `F_PANEL` labels below and confirm against the motherboard manual diagram before applying pressure.
- Do not connect front audio to the wrong header.
- Do not pull front-panel cables tight.

## Step-by-Step Instructions

![Front panel connector map](/PC-Build/assets/diagrams/svg/front-panel-connectors.svg)

1. Locate the motherboard `F_PANEL` header at the bottom edge of the board.
2. Connect the case power switch plug to the `PW` pins. Switch polarity does not matter.
3. Connect reset switch, power LED, or HDD LED plugs only if the case provides them.
4. For LED plugs, align positive and negative polarity with the motherboard labels before pressing the connector down.
5. Use these verified motherboard header labels:

| Label                   | Function                 | Polarity note                                 |
| ----------------------- | ------------------------ | --------------------------------------------- |
| `PW+` / `PW-`           | Power switch             | Polarity does not matter for a simple switch. |
| `RES+` / `RES-`         | Reset switch             | Polarity does not matter for a simple switch. |
| `PLED+` / `PLED-`       | Power LED                | Polarity matters.                             |
| `PWR_LED+` / `PWR_LED-` | Alternate power LED pins | Polarity matters.                             |
| `HD+` / `HD-`           | Drive activity LED       | Polarity matters.                             |
| `SPEAK+` / `SPEAK-`     | Case speaker             | Only used if a speaker is supplied.           |
| `CI+` / `CI-`           | Chassis intrusion        | Not used unless the case provides this cable. |
| `NC`                    | No connection            | Leave unused.                                 |

1. Leave speaker and chassis-intrusion pins unused unless the case accessory bundle includes those cables.
2. Connect the front USB-A cable to the motherboard USB 3.x header.
3. Connect the front USB-C cable to the motherboard USB-C front-panel header.
4. Connect the HD audio cable to the front audio header at the lower-left area of the motherboard.
5. Check that each keyed connector is aligned before applying pressure.
6. Leave a small service loop so connectors are not under tension.

## Verification Checklist

- [ ] Power switch is connected to the correct pins.
- [ ] LED polarity is correct where LEDs are connected.
- [ ] Front USB-A connector is fully seated.
- [ ] Front USB-C connector is fully seated.
- [ ] HD audio connector is fully seated.
- [ ] No header pins are bent.
- [ ] Cables are not pulling on the headers.

## Common Mistakes

- Reversing LED polarity and assuming the system is broken.
- Misplacing the power switch plug by one pin.
- Forcing the USB-C connector at an angle.
- Routing HD audio too tightly.
- Forgetting front-panel connectors before first boot.

## Expected Result

The case power button and front I/O are connected and ready for first boot testing.

## Sources Reviewed

- [Gigabyte B850 AORUS Elite WiFi7 user manual 1101](https://download.gigabyte.com/FileList/Manual/mb_manual_b850-aorus-elite-wf7_1101_e.pdf)
- [Lian Li O11 Dynamic Mini V2 product page](https://lian-li.com/product/o11-dynamic-mini-v2/)

## Next Chapter

Continue to [First Boot](/PC-Build/build-guide/first-boot/).
