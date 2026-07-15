---
title: "Benchmark Baseline"
---

## Introduction

This chapter establishes a repeatable baseline test process for temperatures, stability, storage performance, and gaming performance after the monitored optimisation pass is complete.

## Purpose

Confirm the build is stable and performing as expected before daily use, with results that can be compared against the [gaming optimisation](/PC-Build/build-guide/gaming-optimisation/), [temperature reference](/PC-Build/appendix/temperature-reference/), and [maintenance schedule](/PC-Build/operations/maintenance-schedule/) records.

The benchmark process is not intended to chase leaderboard scores. It is intended to prove that the build is stable, cooled correctly, configured consistently, and ready for future comparison after driver, firmware, cooling, or hardware changes.

## Estimated Time

1-3 hours depending on test depth.

## Difficulty

Moderate.

## Required Tools

- Hardware monitoring software.
- [HWiNFO64](/PC-Build/operations/recommended-software/) for logging.
- MemTest86 for memory validation.
- Cinebench 2024 for CPU benchmark.
- 3DMark for GPU/game benchmark.
- CrystalDiskMark for SSD benchmark.
- OCCT for controlled stability testing.
- Notes file or spreadsheet for results.
- The monitoring log from [Gaming Optimisation](/PC-Build/build-guide/gaming-optimisation/).

## Warnings

- Monitor temperatures during stress tests.
- Stop testing if temperatures rise abnormally, fans stop, the pump reading disappears, the system becomes unstable, or visual artifacts appear.
- Do not compare results against systems with different settings without context.
- Run baseline tests before overclocking, undervolting, or manual GPU tuning.
- Do not publish logs that include serial numbers, licence keys, account names, screenshots with personal data, or invoices.

## Benchmark Preconditions

Complete these checks before recording the baseline:

- Windows Update has no required restart pending.
- Device Manager has no unknown devices.
- AMD chipset and Radeon GPU drivers are installed.
- Monitor resolution and refresh rate are set.
- EXPO state is known and recorded.
- GPU tuning is still at default unless a later controlled tuning pass is being tested.
- CPU, GPU, SSD, memory, and cooling readings are visible in monitoring software.
- Game launchers, Windows Update, and large downloads are idle.
- Room temperature is recorded if practical.

## Baseline Test Order

Run tests in this order so failures are easier to isolate.

| Order | Test area                       | Purpose                                                              | Record                                                                |
| ----- | ------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 1     | Idle desktop                    | Establish thermal and background-load baseline                       | Room temp, CPU temp, GPU temp, SSD temp, fan noise                    |
| 2     | Memory stability                | Confirm EXPO/default memory state is reliable                        | EXPO state, pass/fail, duration                                       |
| 3     | CPU load                        | Confirm cooler mount, pump/fan response, and CPU stability           | CPU temperature, fan response, pass/fail                              |
| 4     | SSD benchmark                   | Confirm NVMe-class behaviour and thermal response                    | Tool, result summary, peak SSD temp                                   |
| 5     | GPU synthetic or game benchmark | Confirm GPU stability, driver behaviour, airflow, and display output | Score/FPS if available, GPU temp, hotspot if shown, utilisation, VRAM |
| 6     | Mixed real game test            | Confirm practical gaming behaviour                                   | Settings, duration, stutter/artifacts/crash notes                     |

## Tool-Specific Procedure

| Tool | Use | Baseline action | Retest trigger |
| --- | --- | --- | --- |
| HWiNFO64 | Sensor logging | Start logging before idle, CPU, SSD, GPU, and mixed tests. | Any thermal, driver, fan, or instability investigation. |
| MemTest86 | Memory stability | Run after EXPO is enabled or after memory changes. | Boot loops, game crashes, WHEA errors, RAM upgrade, EXPO change. |
| Cinebench 2024 | CPU load and score trend | Run CPU benchmark with HWiNFO logging active. | BIOS update, cooler change, CPU change, fan curve change. |
| CrystalDiskMark | SSD throughput sanity check | Run default storage benchmark once the system is idle. | SSD firmware update, new NVMe drive, suspected throttling. |
| 3DMark | GPU/game-class performance | Run one appropriate benchmark or stress test at default GPU tuning. | GPU driver update, GPU change, display issue, airflow change. |
| OCCT | Stability and fault isolation | Use short targeted tests, not unattended torture runs. | Suspected CPU, memory, GPU, PSU, or thermal instability. |

## Step-by-Step Instructions

1. Record ambient room temperature.
2. Record BIOS version, driver versions, EXPO status, Windows version, monitor resolution, and refresh rate.
3. Confirm the optimisation monitoring log has current idle readings.
4. Wait 10 minutes at the Windows desktop with launchers and downloads idle.
5. Record idle CPU, GPU, SSD, memory, and fan readings.
6. Run a memory stability test appropriate for the installed EXPO/default memory state.
7. Run a short CPU load test while monitoring CPU temperature and pump/fan behaviour.
8. Run an SSD benchmark and confirm the NVMe drive behaves like a PCIe NVMe drive, not a SATA drive.
9. Run a GPU benchmark or a repeatable in-game benchmark.
10. Record average FPS, 1% lows if available, GPU temperature, GPU utilisation, VRAM usage, CPU temperature, driver version, and any stutter or artifacting.
11. Run one real game test for at least a short controlled session using settings you can repeat later.
12. Repeat any failed test only after fixing or rolling back the likely cause.

## Benchmark Log Template

| Date/time      | Room temp      | BIOS           | Chipset driver | Radeon driver  | EXPO     | Test          | Settings          | Result          | CPU temp       | GPU temp       | SSD temp       | Notes                 |
| -------------- | -------------- | -------------- | -------------- | -------------- | -------- | ------------- | ----------------- | --------------- | -------------- | -------------- | -------------- | --------------------- |
| _Record value_ | _Record value_ | _Record value_ | _Record value_ | _Record value_ | _On/off_ | _Record test_ | _Record settings_ | _Record result_ | _Record value_ | _Record value_ | _Record value_ | _Record observations_ |

Store benchmark logs privately if they contain serial numbers, account names, screenshots, or other personal details.

## Pass Criteria

A baseline is acceptable when:

- All selected tests complete without crash, reboot, display corruption, or driver timeout.
- CPU, GPU, and SSD temperatures are consistent with the [temperature reference](/PC-Build/appendix/temperature-reference/) and the observed cooling behaviour.
- Fan and pump readings respond plausibly under load.
- Device Manager remains clean after testing.
- SSD performance is consistent with NVMe-class operation.
- Gaming results are repeatable enough to compare with future driver, firmware, or hardware changes.

## Retest Rules

Repeat the relevant part of the baseline after:

- BIOS update.
- AMD chipset driver update.
- Radeon GPU driver update.
- EXPO change.
- Fan curve or cooling change.
- GPU, SSD, memory, cooler, PSU, or case fan change.
- Windows feature update that changes gaming or driver behaviour.
- Any troubleshooting fix for no display, high temperature, instability, or driver failure.

When retesting, change one variable at a time and keep the previous result visible for comparison.

## Verification Checklist

- [ ] Baseline settings are recorded.
- [ ] Optimisation monitoring log is current.
- [ ] Idle temperatures are recorded.
- [ ] Memory test result is recorded.
- [ ] CPU load temperature is acceptable for the cooler.
- [ ] SSD benchmark confirms NVMe-class performance.
- [ ] GPU benchmark completes without crash or artifacting.
- [ ] Real game test completes without obvious instability.
- [ ] Results are saved for future comparison.
- [ ] Retest trigger is understood before future updates.

## Common Mistakes

- Running tests before drivers are installed.
- Ignoring room temperature.
- Comparing EXPO-on results with EXPO-off results.
- Running benchmarks while Windows Update is active.
- Treating one synthetic score as the only measure of build quality.
- Changing Radeon settings, EXPO, fan curves, and Windows settings before retesting.
- Publishing private machine details in public benchmark logs.

## Expected Result

The system has a documented stable baseline for temperatures, memory, storage, CPU, GPU, and real-game behaviour.

## Next Chapter

Continue to [Troubleshooting](/PC-Build/operations/troubleshooting/).
