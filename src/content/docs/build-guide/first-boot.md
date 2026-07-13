---
title: "First Boot"
---
Status: Published HTML content. Last reviewed: 2026-07-13 13:53 BST.

## Introduction

This chapter performs the first controlled power-on test before Windows installation.

## Purpose

Confirm that the system powers on, reaches BIOS, detects CPU, memory, SSD, fans, pump, and GPU, and shows no obvious assembly fault.

## Estimated Time

20-45 minutes.

## Difficulty

Moderate.

## Required Tools

- Monitor connected to the graphics card.
- Keyboard.
- Power cable.
- Windows 11 Pro USB installer.
- Flashlight.

## Warnings

- Do not close the case panels before the first successful boot.
- Do not enable EXPO during the first power-on attempt.
- First DDR5 memory training can take several minutes.
- If you smell burning or see smoke, switch off the PSU immediately.
- Plug the display cable into the GPU, not the motherboard rear I/O.

## Step-by-Step Instructions

![Boot process diagram](/PC-Build/assets/diagrams/svg/boot-process.svg)

![Boot flow diagram](/PC-Build/assets/diagrams/svg/boot-flow.svg)

Diagram sources: [boot-process.mmd](/PC-Build/assets/diagrams/mermaid/boot-process.mmd), [boot-flow.puml](/PC-Build/assets/diagrams/plantuml/boot-flow.puml)

1. Confirm the PSU switch is off.
2. Connect the monitor to the graphics card.
3. Connect keyboard and mouse.
4. Insert the Windows 11 Pro USB installer only after BIOS access is confirmed, unless you intend to boot directly into setup.
5. Connect wall power.
6. Switch the PSU on.
7. Press the case power button.
8. Watch for fan spin, pump activity, motherboard LEDs, and display output.
9. Wait through DDR5 memory training if the screen stays blank for a short period.
10. Enter BIOS using the motherboard setup key when prompted.
11. Confirm the CPU is detected as Ryzen 7 7800X3D.
12. Confirm both memory modules are detected at default speed.
13. Confirm the Samsung 990 EVO Plus is detected.
14. Confirm CPU temperature is reasonable in BIOS.
15. Shut down if any fan or pump is not detected.

## Verification Checklist

- [ ] System powers on from the case button.
- [ ] Display output appears from the GPU.
- [ ] BIOS is accessible.
- [ ] CPU is detected.
- [ ] 32GB memory is detected.
- [ ] SSD is detected.
- [ ] CPU fan or pump monitoring shows activity.
- [ ] No abnormal noise, smell, or warning LED remains.

## Common Mistakes

- Connecting the monitor to the motherboard instead of the GPU.
- Interrupting the first memory training too quickly.
- Forgetting CPU EPS power.
- Forgetting GPU PCIe power.
- Assuming EXPO must be enabled before the first successful default boot.

## Expected Result

The system reaches BIOS at default settings and all core hardware is detected.

## Next Chapter

Continue to [BIOS Configuration](/PC-Build/build-guide/bios/).
