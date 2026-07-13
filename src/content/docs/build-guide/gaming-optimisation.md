---
title: "Gaming Optimisation"
---
Status: Published HTML content. Last reviewed: 2026-07-13 15:04 BST.

## Introduction

This chapter turns the completed Windows 11 Pro installation into a monitored, stable gaming baseline. It deliberately favours repeatability over aggressive tuning.

## Purpose

Confirm that Windows, drivers, cooling, storage, memory, and Radeon software are behaving correctly before changing performance settings. The goal is a clean baseline that can be compared with future benchmark, maintenance, and upgrade results.

## Estimated Time

45-90 minutes for the initial optimisation pass. Allow longer if Windows Update, driver installation, or game downloads are still running.

## Difficulty

Beginner to moderate.

## Required Tools

- Windows administrator account.
- AMD Radeon Software.
- Windows Task Manager.
- Device Manager.
- Windows Update.
- Hardware monitoring software.
- SSD health or benchmark tool.
- Notes file or spreadsheet for settings and readings.
- Monitor manual if adjusting refresh rate.

## Warnings

- Do not overclock the CPU or GPU as part of baseline setup.
- Do not undervolt, overclock, or manually tune the GPU before a default benchmark baseline exists.
- Do not enable EXPO until the system has already completed a stable default boot.
- Do not disable Windows security features for minor benchmark gains.
- Do not install multiple RGB, motherboard, or tuning utilities unless they provide a required function.
- Change one performance setting at a time and record the before/after result.

## Monitoring Baseline

Record these values before optimisation so later problems have a comparison point.

| Area          | What to record                                                                  | Where to check                                      |
| ------------- | ------------------------------------------------------------------------------- | --------------------------------------------------- |
| Windows state | Windows version, pending updates, restart requirement                           | Settings, Windows Update                            |
| Device state  | Unknown devices, warning icons, failed drivers                                  | Device Manager                                      |
| CPU           | Idle temperature, load temperature, clock behaviour under load                  | Hardware monitoring software                        |
| GPU           | Idle temperature, gaming temperature, hotspot if shown, utilisation, VRAM usage | AMD Radeon Software or hardware monitoring software |
| Memory        | Installed capacity, reported speed, EXPO state                                  | Task Manager, BIOS, monitoring software             |
| SSD           | Free space, health, temperature, benchmark class                                | SSD utility, monitoring software, benchmark tool    |
| Cooling       | AIO pump reading if exposed, radiator fan response, case fan response, noise    | BIOS, monitoring software, physical inspection      |
| Software      | Chipset driver version, Radeon driver version, major launcher versions          | Driver installers, AMD Radeon Software, notes file  |

Use the [temperature reference](/PC-Build/appendix/temperature-reference/) for expected temperature ranges and action points. Use the [benchmark chapter](/PC-Build/build-guide/benchmarks/) for repeatable load testing after this optimisation pass.

## Optimisation Rules

1. Establish a default baseline first.
2. Make one change at a time.
3. Reboot after driver, firmware, or low-level system changes.
4. Record settings before and after each change.
5. Prefer official Windows, AMD, Gigabyte, and vendor tools over third-party driver bundles.
6. Treat stability, temperatures, and noise as part of performance.
7. Roll back any change that causes crashes, display corruption, unusual fan behaviour, or worse benchmark consistency.

## Step-by-Step Instructions

1. Confirm [driver installation](/PC-Build/build-guide/driver-installation/) is complete and Device Manager has no unresolved devices.
2. Run Windows Update and restart until no required restart remains.
3. Confirm the monitor uses its native resolution and intended refresh rate.
4. Confirm the GPU is detected correctly in AMD Radeon Software.
5. Leave GPU tuning on default for the first benchmark baseline.
6. Confirm CPU, GPU, SSD, and memory readings are visible in monitoring software.
7. Record idle readings after 10 minutes at the Windows desktop.
8. Confirm the NVMe SSD has enough free space for Windows updates, game installs, captures, and shader caches.
9. Set game libraries to the NVMe SSD unless a later storage expansion changes the plan.
10. Review startup applications and disable non-essential launch-at-login entries.
11. Enable Windows Game Mode.
12. Leave Hardware-Accelerated GPU Scheduling unchanged unless you are deliberately testing it as a single recorded change.
13. Use balanced or high-performance Windows power behaviour according to the intended noise and performance preference.
14. Confirm EXPO status only after the system has already passed default boot and driver checks.
15. If EXPO is enabled, record the reported memory speed and run the memory checks described in [EXPO Memory Setup](/PC-Build/build-guide/expo/) and [Benchmarks](/PC-Build/build-guide/benchmarks/).
16. Run one repeatable game or synthetic benchmark and record CPU temperature, GPU temperature, GPU utilisation, VRAM usage, fan behaviour, and any visible stutter or artifacting.
17. Adjust fan curves only if temperatures, ramping, or noise justify it. Keep changes conservative and record the new curve source.
18. Create a restore point before installing large game launchers, RGB software, capture tools, or optional motherboard utilities.

## Monitoring Phases

| Phase                    | Required check                                                                          | Result to record                    |
| ------------------------ | --------------------------------------------------------------------------------------- | ----------------------------------- |
| First boot at defaults   | BIOS detects CPU, memory, SSD, fans, and AIO readings as expected                       | Default BIOS baseline               |
| After Windows install    | Windows boots cleanly and updates run                                                   | Windows version and update state    |
| After drivers            | Device Manager is clean and Radeon Software sees the GPU                                | Driver versions                     |
| After EXPO               | Memory reports intended profile and remains stable                                      | EXPO state and memory speed         |
| Before optimisation      | Idle readings are captured                                                              | CPU, GPU, SSD, memory, fan readings |
| After optimisation       | Game Mode, refresh rate, startup apps, storage locations, and restore point are checked | Optimisation settings               |
| After benchmark baseline | Repeatable results are saved                                                            | Benchmark results and temperatures  |
| Monthly or after changes | Temperatures, dust, drivers, storage health, and fan noise are reviewed                 | Maintenance log entry               |

## Monitoring Log Template

| Date/time      | BIOS version   | Chipset driver | Radeon driver  | EXPO     | CPU idle/load  | GPU idle/load  | SSD temp/free space | Notes            |
| -------------- | -------------- | -------------- | -------------- | -------- | -------------- | -------------- | ------------------- | ---------------- |
| _Record value_ | _Record value_ | _Record value_ | _Record value_ | _On/off_ | _Record value_ | _Record value_ | _Record value_      | _Record changes_ |

For recurring checks, also use the maintenance templates in the [checklists appendix](/PC-Build/appendix/checklists/).

## Verification Checklist

- [ ] Windows Update has no required restart pending.
- [ ] Device Manager has no unknown devices or warning icons.
- [ ] Monitor uses the intended resolution and refresh rate.
- [ ] AMD Radeon Software detects the GPU.
- [ ] GPU tuning remains at default baseline settings.
- [ ] CPU, GPU, SSD, memory, and cooling readings are visible.
- [ ] Game Mode is enabled.
- [ ] Startup apps are reviewed.
- [ ] Game libraries target the NVMe SSD.
- [ ] Idle readings are recorded.
- [ ] A repeatable benchmark or game test has been recorded.
- [ ] A restore point exists before optional utilities are installed.

## Common Mistakes

- Benchmarking before setting monitor refresh rate.
- Optimising while Windows Update or game downloads are still active.
- Applying GPU undervolts or overclocks before baseline testing.
- Changing EXPO, fan curves, Radeon settings, and Windows settings at the same time.
- Installing several motherboard utilities that duplicate functions.
- Disabling Windows security features unnecessarily.
- Ignoring SSD free space or thermal behaviour.

## Expected Result

The system has a recorded, stable gaming baseline covering Windows state, driver state, display settings, Radeon detection, temperatures, storage health, memory profile, fan behaviour, and benchmark readiness.

## Next Chapter

Continue to [Benchmarks](/PC-Build/build-guide/benchmarks/).
