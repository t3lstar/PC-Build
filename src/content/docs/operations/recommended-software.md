---
title: "Recommended Software"
---

## Introduction

This chapter documents the software recommended for monitoring, driver management, benchmarking, file handling, and gaming-library management.

## Purpose

Install only useful tools from official sources, configure them safely, and remove tools that are no longer needed.

## Estimated Time

30-90 minutes depending on how many optional tools are installed.

## Difficulty

Beginner to moderate.

## Required Tools

- Windows administrator account.
- Web browser.
- Restore point before optional utilities.
- Notes file for installed version and settings.

## Warnings

- Download from official sources only.
- Do not install lookalike downloads, sponsored mirrors, or bundled installer sites.
- Do not run stress tests without monitoring temperatures.
- Do not install multiple tools that control the same fan or GPU setting at the same time.
- Keep optional cleanup tools such as DDU uninstalled until needed.

## Step-by-Step Instructions

1. Create a restore point before optional utilities are installed.
2. Install only the essential tools required for monitoring, drivers, storage health, and fan control.
3. Add recommended benchmarking or convenience tools only when they support a clear workflow.
4. Keep troubleshooting-only tools uninstalled until a fault requires them.
5. Record each installed tool, source, version, and removal path.
6. Disable unnecessary startup behaviour after installation.
7. Remove any tool that duplicates another tool's control of fans, GPU tuning, overlays, or driver cleanup.

## Software Reference

Use each entry to confirm the official source, safe setup, update cadence, and removal path before installing the tool.

### Essential

Install these as part of the normal completed build unless a specific workflow replaces them.

#### HWiNFO64

- Tier: Essential.
- Purpose: Sensor monitoring, logging, and hardware inventory.
- Official source: [HWiNFO](https://www.hwinfo.com/download/).
- Installation guidance: Install the Windows x64 version or use portable mode.
- Safe configuration: Start with sensors-only mode for monitoring sessions.
- Recommended settings: Log CPU, GPU, SSD, memory, fan, and voltage readings during baseline tests.
- Use cadence: Use during first baseline, monthly checks, troubleshooting, and benchmarks.
- Permanently installed: Yes, if used for monitoring.
- Resource usage: Low at idle; logging increases disk writes slightly.
- Potential alternatives: LibreHardwareMonitor.
- Update guidance: Update from HWiNFO when sensor support or bug fixes are useful.
- Removal guidance: Uninstall from Windows Apps or delete the portable folder.

#### AMD Software: Adrenalin Edition

- Tier: Essential.
- Purpose: Radeon GPU driver, GPU settings, monitoring, and update awareness.
- Official source: [AMD Adrenalin](https://www.amd.com/en/products/software/adrenalin.html) and [AMD support](https://www.amd.com/en/support/download/drivers.html).
- Installation guidance: Install after chipset and core motherboard drivers.
- Safe configuration: Use default tuning until a baseline exists.
- Recommended settings: Keep GPU tuning default for the first benchmark baseline.
- Use cadence: Check after driver installs, game issues, or monthly maintenance.
- Permanently installed: Yes.
- Resource usage: Moderate background service and overlay impact if enabled.
- Potential alternatives: Driver-only AMD package if the full app is not desired.
- Update guidance: Update for game support, stability, security, or bug fixes; avoid day-one updates before important use.
- Removal guidance: Use AMD installer cleanup options first; use DDU only for persistent driver faults.

#### Samsung Magician

- Tier: Essential.
- Purpose: Samsung SSD health, firmware, SMART, and drive information.
- Official source: [Samsung Magician](https://semiconductor.samsung.com/consumer-storage/magician/).
- Installation guidance: Install after Windows and chipset drivers.
- Safe configuration: Do not run destructive tests without reading prompts.
- Recommended settings: Use for firmware check, health, temperature, and over-provisioning review.
- Use cadence: Monthly health check or before storage troubleshooting.
- Permanently installed: Yes, if you want SSD health visibility.
- Resource usage: Low when idle.
- Potential alternatives: CrystalDiskInfo for health-only checks.
- Update guidance: Update from Samsung when prompted or when SSD support changes.
- Removal guidance: Uninstall from Windows Apps.

#### FanControl by Rem0o

- Tier: Essential.
- Purpose: Custom fan curves and sensor-based fan control.
- Official source: [FanControl releases](https://github.com/Rem0o/FanControl.Releases).
- Installation guidance: Use the latest release from GitHub after the default BIOS fan baseline is known.
- Safe configuration: Do not control the pump unless the header behaviour is understood.
- Recommended settings: Use conservative curves from [FanControl Configuration](/PC-Build/operations/fancontrol/).
- Use cadence: Leave running only after profiles are tested.
- Permanently installed: Yes, if Windows-level fan profiles are preferred.
- Resource usage: Low, but it must run for software fan curves to apply.
- Potential alternatives: BIOS fan curves.
- Update guidance: Update after reading release notes; export config first.
- Removal guidance: Exit FanControl, restore BIOS curves if needed, then delete or uninstall according to installed package.

### Recommended

Install these when they support your baseline, maintenance, or daily workflow.

#### OCCT

- Tier: Recommended.
- Purpose: Stability, stress testing, and fault isolation.
- Official source: [OCCT download](https://www.ocbase.com/download).
- Installation guidance: Use the official download; OCCT can be portable depending on edition.
- Safe configuration: Start with short tests and active monitoring.
- Recommended settings: Use CPU, memory, GPU, and power tests only as needed.
- Use cadence: Baseline, post-upgrade, or troubleshooting.
- Permanently installed: No, keep only if regularly testing.
- Resource usage: High during tests.
- Potential alternatives: 3DMark stress tests, Cinebench, MemTest86.
- Update guidance: Update before major validation sessions.
- Removal guidance: Delete the portable folder or uninstall from Windows Apps.

#### Cinebench 2024

- Tier: Recommended.
- Purpose: Repeatable CPU rendering benchmark.
- Official source: [Maxon Cinebench downloads](https://www.maxon.net/en/downloads/cinebench-downloads).
- Installation guidance: Download from Maxon.
- Safe configuration: Close background tasks before runs.
- Recommended settings: Record CPU score, run type, room context, and temperatures.
- Use cadence: Baseline and after CPU, BIOS, cooling, or driver changes.
- Permanently installed: No.
- Resource usage: High CPU load while running.
- Potential alternatives: OCCT CPU test.
- Update guidance: Update only when you deliberately start a new baseline series.
- Removal guidance: Delete the portable package or uninstall if installed through Maxon tooling.

#### CrystalDiskMark

- Tier: Recommended.
- Purpose: SSD performance benchmark.
- Official source: [CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/).
- Installation guidance: Install standard edition from Crystal Dew World or Microsoft Store.
- Safe configuration: Avoid repeated large write tests.
- Recommended settings: Use default profile for baseline and record drive fill level.
- Use cadence: Baseline and storage troubleshooting.
- Permanently installed: No.
- Resource usage: High SSD load during tests.
- Potential alternatives: Samsung Magician benchmark.
- Update guidance: Update before storage retests if needed.
- Removal guidance: Uninstall from Windows Apps.

#### MemTest86

- Tier: Recommended.
- Purpose: Bootable memory testing outside Windows.
- Official source: [PassMark MemTest86](https://www.memtest86.com/download.htm).
- Installation guidance: Create USB media using the official package.
- Safe configuration: Back up USB contents first because media creation can overwrite the drive.
- Recommended settings: Run after EXPO enablement, memory faults, or RAM changes.
- Use cadence: Baseline and memory troubleshooting.
- Permanently installed: No; keep USB media labelled.
- Resource usage: Runs outside Windows.
- Potential alternatives: Windows Memory Diagnostic for quick checks.
- Update guidance: Recreate USB when using a newer major release.
- Removal guidance: Reformat the USB or keep it as recovery media.

#### 3DMark

- Tier: Recommended.
- Purpose: GPU/game-oriented benchmark and stress tests.
- Official source: [UL 3DMark](https://benchmarks.ul.com/3dmark).
- Installation guidance: Install from the UL, Steam, or Microsoft Store route chosen by the user.
- Safe configuration: Use default GPU tuning for baseline.
- Recommended settings: Record test name, score, driver, temperature, and settings.
- Use cadence: Baseline and after GPU driver or GPU changes.
- Permanently installed: Optional.
- Resource usage: High GPU load while running.
- Potential alternatives: Real game benchmark.
- Update guidance: Update when benchmark modules require it or when starting a new baseline series.
- Removal guidance: Uninstall from the install platform.

#### Everything Search

- Tier: Recommended.
- Purpose: Fast local filename search.
- Official source: [voidtools downloads](https://www.voidtools.com/downloads/).
- Installation guidance: Install the x64 installer from voidtools.
- Safe configuration: Use default indexing first.
- Recommended settings: Exclude private or external paths only if desired.
- Use cadence: Daily convenience tool.
- Permanently installed: Yes, if useful.
- Resource usage: Very low.
- Potential alternatives: Windows Search.
- Update guidance: Update from voidtools when needed.
- Removal guidance: Uninstall from Windows Apps.

#### Microsoft PowerToys

- Tier: Recommended.
- Purpose: Windows utilities such as FancyZones, PowerRename, and Text Extractor.
- Official source: [Microsoft PowerToys install](https://learn.microsoft.com/en-us/windows/powertoys/install).
- Installation guidance: Install from Microsoft Store, GitHub, or winget.
- Safe configuration: Enable only utilities you actually use.
- Recommended settings: Start with FancyZones and PowerRename only if helpful.
- Use cadence: Daily convenience tool.
- Permanently installed: Optional.
- Resource usage: Low to moderate depending on enabled utilities.
- Potential alternatives: Built-in Windows features.
- Update guidance: Update through Microsoft Store, GitHub, or winget.
- Removal guidance: Uninstall from Windows Apps.

#### Playnite

- Tier: Recommended.
- Purpose: Unified game library manager.
- Official source: [Playnite](https://playnite.link/).
- Installation guidance: Download from Playnite official site.
- Safe configuration: Connect only accounts you want managed in one launcher.
- Recommended settings: Keep add-ons minimal.
- Use cadence: Use if several launchers are installed.
- Permanently installed: Optional.
- Resource usage: Low to moderate depending on library integrations.
- Potential alternatives: Steam, GOG Galaxy, individual launchers.
- Update guidance: Use Playnite built-in update path.
- Removal guidance: Uninstall from Windows Apps and remove personal library data only if intended.

#### 7-Zip

- Tier: Recommended.
- Purpose: Archive extraction and creation.
- Official source: [7-Zip downloads](https://www.7-zip.org/download.html).
- Installation guidance: Install the Windows x64 build from 7-Zip.
- Safe configuration: Avoid running unknown archives.
- Recommended settings: Enable context menu integration if useful.
- Use cadence: As needed.
- Permanently installed: Yes.
- Resource usage: Minimal.
- Potential alternatives: Windows Explorer archive support, NanaZip.
- Update guidance: Update occasionally for security and format support.
- Removal guidance: Uninstall from Windows Apps.

### Optional / Troubleshooting Only

Keep these out of the default build unless you need the specific function.

#### MSI Afterburner

- Tier: Optional.
- Purpose: GPU monitoring overlay or manual GPU tuning if required later.
- Official source: [MSI Afterburner](https://www.msi.com/Landing/afterburner).
- Installation guidance: Install only if AMD Adrenalin/HWiNFO overlay is not enough.
- Safe configuration: Monitoring only unless deliberately tuning later.
- Recommended settings: Do not enable overclock or voltage changes for baseline.
- Use cadence: Use for overlay troubleshooting or controlled GPU tuning only.
- Permanently installed: No, unless its overlay is required.
- Resource usage: Low to moderate with overlay.
- Potential alternatives: AMD Adrenalin metrics, HWiNFO.
- Update guidance: Update from MSI when needed.
- Removal guidance: Uninstall from Windows Apps and remove profiles if no longer needed.

#### LibreHardwareMonitor

- Tier: Optional.
- Purpose: Alternative open-source monitoring.
- Official source: [LibreHardwareMonitor GitHub](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor).
- Installation guidance: Use GitHub releases.
- Safe configuration: Use read-only monitoring.
- Recommended settings: Do not run alongside multiple sensor tools if readings become confusing.
- Use cadence: Use if HWiNFO is not desired.
- Permanently installed: No, unless selected as the primary monitor.
- Resource usage: Low.
- Potential alternatives: HWiNFO64.
- Update guidance: Update from GitHub releases.
- Removal guidance: Delete the portable folder.

#### Display Driver Uninstaller

- Tier: Optional.
- Purpose: Deep display-driver cleanup for persistent GPU driver faults.
- Official source: [Wagnardsoft DDU](https://www.wagnardsoft.com/display-driver-uninstaller-ddu).
- Installation guidance: Download only when needed and read current instructions.
- Safe configuration: Prefer Safe Mode and disconnect automatic driver installs if instructed by Wagnardsoft.
- Recommended settings: Use only after normal AMD cleanup fails or when changing GPU vendor.
- Use cadence: Rare troubleshooting only.
- Permanently installed: No.
- Resource usage: Not relevant except during cleanup.
- Potential alternatives: AMD cleanup/install options.
- Update guidance: Download fresh before use.
- Removal guidance: Delete the extracted folder after use.

## Software To Keep Minimal

Use one primary tool for each job:

- Monitoring: HWiNFO64 or LibreHardwareMonitor.
- Fan control: BIOS fan curves or FanControl.
- GPU settings: AMD Adrenalin, with MSI Afterburner only if a specific overlay or tuning workflow is needed.
- Storage health: Samsung Magician, with CrystalDiskMark only for benchmark runs.

## Verification Checklist

- [ ] Every installed tool came from an official source.
- [ ] Each installed tool has a recorded reason.
- [ ] Optional stress-test tools are not running in the background.
- [ ] GPU tuning remains default until the baseline is recorded.
- [ ] FanControl is not fighting BIOS or other fan-control software.
- [ ] Uninstall path is known for every optional utility.

## Common Mistakes

- Installing download-mirror builds instead of official packages.
- Leaving multiple overlays active.
- Using DDU as routine maintenance.
- Running SSD benchmarks repeatedly without a reason.
- Letting optional tools auto-start when they are not needed.

## Expected Result

The system has a small, controlled software set with official sources, known settings, and clear removal paths.

## Next Chapter

Continue to [Software To Avoid](/PC-Build/operations/software-to-avoid/).
