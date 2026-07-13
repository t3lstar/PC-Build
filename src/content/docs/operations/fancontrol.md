---
title: "FanControl Configuration"
---

## Introduction

This chapter gives a conservative FanControl strategy for the Lian Li O11 Dynamic Mini V2 Flow build with bottom intake, side intake, and top AIO exhaust.

## Purpose

Reduce noise while preserving airflow for the CPU radiator, GPU intake path, SSD, and motherboard area.

## Estimated Time

30-60 minutes after baseline monitoring is complete.

## Difficulty

Moderate.

## Required Tools

- [FanControl by Rem0o](https://github.com/Rem0o/FanControl.Releases).
- HWiNFO64 or FanControl-detected sensors.
- Baseline readings from [Monitoring](/PC-Build/operations/monitoring/).
- BIOS fan curve access as fallback.

## Warnings

- Do not configure FanControl before confirming the BIOS default fan behaviour works.
- Do not set radiator fans or pump too low during first testing.
- Do not rely on a sensor that disappears after sleep, reboot, or driver update.
- Keep a BIOS fan curve fallback.

## Fan Groups

| Group | Hardware | Preferred control sensor | Reason |
| --- | --- | --- | --- |
| Bottom intake fans | 3 x included reverse-blade 120mm fans | GPU temperature or mixed CPU/GPU curve | Bottom intake primarily feeds the GPU. |
| Side intake fans | 2 x included reverse-blade 120mm fans | Mixed CPU/GPU or motherboard temperature | Side intake feeds the main chamber and motherboard area. |
| Top radiator fans | ARCTIC 360mm radiator fans | CPU package or CPU temperature | Radiator fans respond to CPU heat. |
| Pump | ARCTIC pump lead if individually controlled | Fixed high-safe duty or BIOS-managed pump header | Pump reliability is more important than silence. |

## Recommended Curves

Use these as starting profiles, then tune against the real baseline. Percentages are fan duty targets, not guaranteed RPM.

| Profile | Bottom intake | Side intake | Top radiator fans | Pump |
| --- | --- | --- | --- | --- |
| Quiet | 25-35% at idle, rising gently with GPU temperature | 25-35% at idle, rising with mixed temperature | 30-40% at idle, rising with CPU temperature | BIOS-managed or fixed safe duty |
| Gaming | 35-45% at warm idle, rising more quickly above normal gaming baseline | 35-45% warm idle, steady rise | 40-55% warm idle, steady rise with CPU load | BIOS-managed or fixed safe duty |
| Stress testing | 50% minimum during tests, rising aggressively with GPU temperature | 45-55% minimum during tests | 55% minimum, rising aggressively with CPU temperature | BIOS-managed or fixed safe duty |

## Step-by-Step Instructions

1. Record default BIOS fan behaviour first.
2. Install FanControl from the official GitHub release.
3. Identify each controllable fan header.
4. Rename fans by physical position: bottom intake, side intake, top radiator, pump if exposed.
5. Confirm each fan responds to manual changes.
6. Return every fan to a safe automatic curve.
7. Create a quiet profile for desktop use.
8. Create a gaming profile based on GPU and CPU baseline temperatures.
9. Create a stress-test profile with higher minimum fan speeds.
10. Leave the pump BIOS-managed unless you have confirmed safe individual-control behaviour.
11. Export the FanControl configuration after testing.
12. Reboot and confirm the profile reloads correctly.

## Noise Optimisation

- Prefer gradual curves over sharp ramps.
- Use response delay or hysteresis where FanControl supports it.
- Avoid curves that oscillate around a common temperature.
- Tune bottom intake fans with GPU workload, not only CPU workload.
- Tune radiator fans with CPU workload, not only GPU workload.

## Verification Checklist

- [ ] BIOS default fan behaviour was recorded first.
- [ ] Each fan group is labelled by physical location.
- [ ] Each fan responds to control.
- [ ] Pump handling is known and conservative.
- [ ] Quiet, gaming, and stress-test profiles exist.
- [ ] A configuration export exists.
- [ ] Reboot behaviour is verified.

## Common Mistakes

- Setting all fans from only CPU temperature.
- Letting the pump follow a quiet fan curve.
- Running FanControl and motherboard fan software together.
- Making curves too flat, then troubleshooting high temperatures.
- Making curves too steep, then troubleshooting noise.

## Expected Result

FanControl provides predictable quiet, gaming, and stress-test behaviour without weakening cooling safety.

## Next Chapter

Continue to [Benchmark Baseline](/PC-Build/operations/benchmark-baseline/).
