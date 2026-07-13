# Front Panel Connectors

Status: Initial Milestone 2 content. Last verified: 2026-07-13.

## Introduction

This chapter connects the case power switch, front USB, USB-C, and front audio cables to the Gigabyte B850 AORUS Elite WiFi7 motherboard.

## Purpose

Make the case controls and front I/O work correctly before first boot.

## Estimated Time

20-35 minutes.

## Difficulty

Moderate because front-panel header pins are small.

## Required Tools

- Motherboard manual.
- Case manual.
- Flashlight.
- Precision screwdriver or tweezers if needed for positioning small plugs.

## Warnings

- Do not force USB 3.x or USB-C headers; bent pins are difficult to repair.
- Do not guess the power switch pins. Use the motherboard manual.
- Do not connect front audio to the wrong header.
- Do not pull front-panel cables tight.

## Step-by-Step Instructions

1. Locate the motherboard front-panel header in the manual.
2. Connect the case power switch plug to the correct `PWR_SW` pins.
3. Connect reset switch, power LED, or HDD LED plugs only if the case provides them and the manual confirms polarity.
4. Connect the front USB-A cable to the motherboard USB 3.x header.
5. Connect the front USB-C cable to the motherboard USB-C front-panel header.
6. Connect the HD audio cable to the front audio header at the lower-left area of the motherboard.
7. Check that each keyed connector is aligned before applying pressure.
8. Leave a small service loop so connectors are not under tension.

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

## Next Chapter

Continue to [First Boot](17-first-boot.md).
