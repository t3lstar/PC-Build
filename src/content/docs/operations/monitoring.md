---
title: "Monitoring"
---

## Introduction

This chapter defines what to monitor, what abnormal readings may indicate, and how to investigate without inventing exact limits.

## Purpose

Use monitoring to identify cooling, power, driver, memory, storage, and airflow problems early.

## Estimated Time

20-40 minutes for setup; 5-10 minutes for routine checks.

## Difficulty

Moderate.

## Required Tools

- HWiNFO64 or equivalent monitoring software.
- AMD Adrenalin for GPU telemetry.
- Samsung Magician for SSD health.
- Baseline log from [Benchmark Baseline](/PC-Build/operations/benchmark-baseline/).

## Warnings

- Do not treat one spike as a failure without workload context.
- Do not compare readings from different tools unless sensor names match.
- Do not run stress tests unattended.
- Do not use unverified internet temperature targets as hard limits.

## Monitored Values

| Value | Normal use expectation | Warning threshold | What abnormal values may indicate | Investigation sequence |
| --- | --- | --- | --- | --- |
| CPU temperature | Idle and gaming readings should be consistent with the original baseline and [temperature reference](/PC-Build/appendix/temperature-reference/). | Investigate sustained readings materially above baseline in similar room conditions, rapid temperature rise, or thermal throttling. | Cooler mount, pump/fan reading, radiator airflow, dust, background load, BIOS fan curve. | Check workload, pump/fan readings, radiator fans, dust, then cooler mount. |
| GPU temperature | Gaming readings should be stable for the same game/settings. | Investigate sustained rise versus baseline, driver timeouts, artifacts, or fan behaviour changes. | Blocked bottom/side intake, GPU fan curve, driver issue, dust, cable obstruction. | Check fans, airflow, driver version, game settings, and case filters. |
| SSD temperature | Idle/light use should be stable; sustained transfers run warmer. | Investigate high idle temperature, thermal throttling, or large temperature rise during normal use. | Heatsink contact, poor airflow, heavy background writes, low free space. | Check Samsung Magician, drive free space, background activity, heatsink seating. |
| Motherboard temperature | Should remain stable relative to baseline. | Investigate if it rises with no workload or after airflow changes. | Case airflow, cable obstruction, fan failure, sensor mismatch. | Check case fan operation and recent fan curve changes. |
| CPU package power | Should scale with workload. | Investigate high power at idle or unexpectedly low power under load. | Background process, power plan, BIOS setting, thermal limit. | Check Task Manager, power plan, CPU clocks, temperatures. |
| GPU power | Should scale with game or benchmark load. | Investigate if high at idle or unstable under load. | Driver setting, high-refresh desktop behaviour, overlay, power cable issue. | Check refresh rate, Radeon settings, background GPU use, PCIe power seating. |
| Clock speeds | Should boost and idle according to load. | Investigate clocks stuck low under load or stuck high at idle with high power. | Thermal throttling, power limits, background load, driver setting. | Check temperatures, utilisation, power, Windows power plan. |
| Memory speed | Should match default or EXPO state recorded in BIOS/Windows. | Investigate if speed changes unexpectedly or instability appears after EXPO. | BIOS reset, failed training, unstable EXPO, wrong slots. | Check BIOS EXPO state, Task Manager speed, MemTest86 if unstable. |
| Fan speeds | Should follow BIOS or FanControl curves. | Investigate missing fan reading, unexpected 0 RPM under load, or new noise. | Header issue, fan stop mode, cable obstruction, fan curve conflict. | Check BIOS/FanControl, physical fan movement, cables. |
| Voltages | Should be reviewed mainly for changes from baseline or obvious sensor faults. | Investigate sudden abnormal readings, instability, or values flagged by monitoring software. | Sensor misread, PSU issue, motherboard reading difference, overclock setting. | Cross-check tool readings, restore defaults, inspect power cabling. |

## Step-by-Step Instructions

1. Open HWiNFO64 sensors-only mode.
2. Confirm CPU, GPU, SSD, motherboard, fan, and memory sensors are visible.
3. Wait 10 minutes at idle after startup.
4. Record idle readings.
5. Run a short controlled load from [Benchmark Baseline](/PC-Build/operations/benchmark-baseline/).
6. Record load readings and fan behaviour.
7. Save the baseline privately.
8. Compare future readings against the same workload, room context, driver version, and fan profile.

## Verification Checklist

- [ ] CPU temperature is visible.
- [ ] GPU temperature and utilisation are visible.
- [ ] SSD temperature and health are visible.
- [ ] Fan speeds are visible where headers expose them.
- [ ] Memory speed is recorded.
- [ ] Baseline includes idle and controlled load readings.
- [ ] Monitoring tool version is recorded.

## Common Mistakes

- Comparing idle after boot with idle after a game session.
- Using different fan profiles for baseline and retest.
- Ignoring room temperature.
- Treating every voltage sensor label as equally reliable.
- Running multiple sensor tools and confusing duplicate readings.

## Expected Result

Monitoring provides a repeatable view of thermal, power, clock, fan, storage, and memory behaviour.

## Next Chapter

Continue to [FanControl Configuration](/PC-Build/operations/fancontrol/).
