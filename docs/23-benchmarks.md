# Benchmarks

Status: Published HTML content. Last reviewed: 2026-07-13 15:04 BST.

## Introduction

This chapter establishes a baseline test process for temperatures, stability, storage performance, and gaming performance after the monitored optimisation pass is complete.

## Purpose

Confirm the build is stable and performing as expected before daily use, with results that can be compared against the [gaming optimisation](22-gaming-optimisation.md), [temperature reference](appendix/temperature-reference.md), and [maintenance](25-maintenance.md) records.

## Estimated Time

1-3 hours depending on test depth.

## Difficulty

Moderate.

## Required Tools

- Hardware monitoring software.
- Memory test tool.
- CPU load test.
- GPU benchmark or game benchmark.
- SSD benchmark.
- Notes file or spreadsheet for results.

## Warnings

- Monitor temperatures during stress tests.
- Stop testing if temperatures rise abnormally, fans stop, or the system becomes unstable.
- Do not compare results against systems with different settings without context.
- Run baseline tests before overclocking or undervolting.

## Step-by-Step Instructions

1. Record ambient room temperature.
2. Record BIOS version, driver versions, EXPO status, and Windows version.
3. Confirm the optimisation monitoring log has current idle readings.
4. Record idle CPU and GPU temperatures after 10 minutes at the desktop.
5. Run a short CPU load test while monitoring CPU temperature and pump/fan behavior.
6. Run a memory stability test with EXPO enabled.
7. Run an SSD benchmark and confirm the NVMe drive behaves like a PCIe NVMe drive, not a SATA drive.
8. Run a GPU benchmark or a repeatable in-game benchmark.
9. Record average FPS, 1% lows if available, GPU temperature, GPU utilisation, VRAM usage, CPU temperature, and driver version.
10. Repeat any failed test after fixing the cause.

## Verification Checklist

- [ ] Baseline settings are recorded.
- [ ] Optimisation monitoring log is current.
- [ ] Idle temperatures are recorded.
- [ ] CPU load temperature is acceptable for the cooler.
- [ ] Memory test passes.
- [ ] SSD benchmark confirms NVMe-class performance.
- [ ] GPU benchmark completes without crash or artifacting.
- [ ] Results are saved for future comparison.

## Common Mistakes

- Running tests before drivers are installed.
- Ignoring room temperature.
- Comparing EXPO-on results with EXPO-off results.
- Running benchmarks while Windows Update is active.
- Treating one synthetic score as the only measure of build quality.

## Expected Result

The system has a documented stable baseline for temperatures, memory, storage, CPU, and GPU performance.

## Next Chapter

Continue to [Troubleshooting](24-troubleshooting.md).
