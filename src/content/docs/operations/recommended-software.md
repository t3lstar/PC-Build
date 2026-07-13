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

## Software Reference

| Application | Tier | Purpose | Official source | Installation guidance | Safe configuration | Recommended settings | Use cadence | Permanently installed | Resource usage | Potential alternatives | Update guidance | Removal guidance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HWiNFO64 | Essential | Sensor monitoring, logging, and hardware inventory. | [HWiNFO](https://www.hwinfo.com/download/) | Install the Windows x64 version or use portable mode. | Start with sensors-only mode for monitoring sessions. | Log CPU, GPU, SSD, memory, fan, and voltage readings during baseline tests. | Use during first baseline, monthly checks, troubleshooting, and benchmarks. | Yes, if used for monitoring. | Low at idle; logging increases disk writes slightly. | LibreHardwareMonitor. | Update from HWiNFO when sensor support or bug fixes are useful. | Uninstall from Windows Apps or delete portable folder. |
| AMD Software: Adrenalin Edition | Essential | Radeon GPU driver, GPU settings, monitoring, and update awareness. | [AMD Adrenalin](https://www.amd.com/en/products/software/adrenalin.html) and [AMD support](https://www.amd.com/en/support/download/drivers.html) | Install after chipset and core motherboard drivers. | Use default tuning until a baseline exists. | Keep GPU tuning default for the first benchmark baseline. | Check after driver installs, game issues, or monthly maintenance. | Yes. | Moderate background service and overlay impact if enabled. | Driver-only AMD package if the full app is not desired. | Update for game support, stability, security, or bug fixes; avoid day-one updates before important use. | Use AMD installer cleanup options first; use DDU only for persistent driver faults. |
| Samsung Magician | Essential | Samsung SSD health, firmware, SMART, and drive information. | [Samsung Magician](https://semiconductor.samsung.com/consumer-storage/magician/) | Install after Windows and chipset drivers. | Do not run destructive tests without reading prompts. | Use for firmware check, health, temperature, and over-provisioning review. | Monthly health check or before storage troubleshooting. | Yes, if you want SSD health visibility. | Low when idle. | CrystalDiskInfo for health-only checks. | Update from Samsung when prompted or when SSD support changes. | Uninstall from Windows Apps. |
| FanControl by Rem0o | Essential | Custom fan curves and sensor-based fan control. | [FanControl releases](https://github.com/Rem0o/FanControl.Releases) | Use the latest release from GitHub after the default BIOS fan baseline is known. | Do not control the pump unless the header behaviour is understood. | Use conservative curves from [FanControl Configuration](/PC-Build/operations/fancontrol/). | Leave running only after profiles are tested. | Yes, if Windows-level fan profiles are preferred. | Low, but it must run for software fan curves to apply. | BIOS fan curves. | Update after reading release notes; export config first. | Exit FanControl, restore BIOS curves if needed, then delete or uninstall according to installed package. |
| OCCT | Recommended | Stability, stress testing, and fault isolation. | [OCCT download](https://www.ocbase.com/download) | Use the official download; OCCT can be portable depending on edition. | Start with short tests and active monitoring. | Use CPU, memory, GPU, and power tests only as needed. | Baseline, post-upgrade, or troubleshooting. | No, keep only if regularly testing. | High during tests. | 3DMark stress tests, Cinebench, MemTest86. | Update before major validation sessions. | Delete portable folder or uninstall from Windows Apps. |
| Cinebench 2024 | Recommended | Repeatable CPU rendering benchmark. | [Maxon Cinebench downloads](https://www.maxon.net/en/downloads/cinebench-downloads) | Download from Maxon. | Close background tasks before runs. | Record CPU score, run type, room context, and temperatures. | Baseline and after CPU, BIOS, cooling, or driver changes. | No. | High CPU load while running. | OCCT CPU test. | Update only when you deliberately start a new baseline series. | Delete portable package or uninstall if installed through Maxon tooling. |
| CrystalDiskMark | Recommended | SSD performance benchmark. | [CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/) | Install standard edition from Crystal Dew World or Microsoft Store. | Avoid repeated large write tests. | Use default profile for baseline and record drive fill level. | Baseline and storage troubleshooting. | No. | High SSD load during tests. | Samsung Magician benchmark. | Update before storage retests if needed. | Uninstall from Windows Apps. |
| MemTest86 | Recommended | Bootable memory testing outside Windows. | [PassMark MemTest86](https://www.memtest86.com/download.htm) | Create USB media using the official package. | Back up USB contents first because media creation can overwrite the drive. | Run after EXPO enablement, memory faults, or RAM changes. | Baseline and memory troubleshooting. | No; keep USB media labelled. | Runs outside Windows. | Windows Memory Diagnostic for quick checks. | Recreate USB when using a newer major release. | Reformat the USB or keep it as recovery media. |
| 3DMark | Recommended | GPU/game-oriented benchmark and stress tests. | [UL 3DMark](https://benchmarks.ul.com/3dmark) | Install from UL/Steam/Microsoft Store route chosen by the user. | Use default GPU tuning for baseline. | Record test name, score, driver, temperature, and settings. | Baseline and after GPU driver or GPU changes. | Optional. | High GPU load while running. | Real game benchmark. | Update when benchmark modules require it or when starting a new baseline series. | Uninstall from the install platform. |
| Everything Search | Recommended | Fast local filename search. | [voidtools downloads](https://www.voidtools.com/downloads/) | Install x64 installer from voidtools. | Use default indexing first. | Exclude private or external paths only if desired. | Daily convenience tool. | Yes, if useful. | Very low. | Windows Search. | Update from voidtools when needed. | Uninstall from Windows Apps. |
| Microsoft PowerToys | Recommended | Windows utilities such as FancyZones, PowerRename, and Text Extractor. | [Microsoft PowerToys install](https://learn.microsoft.com/en-us/windows/powertoys/install) | Install from Microsoft Store, GitHub, or winget. | Enable only utilities you actually use. | Start with FancyZones and PowerRename only if helpful. | Daily convenience tool. | Optional. | Low to moderate depending on enabled utilities. | Built-in Windows features. | Update through Microsoft Store, GitHub, or winget. | Uninstall from Windows Apps. |
| Playnite | Recommended | Unified game library manager. | [Playnite](https://playnite.link/) | Download from Playnite official site. | Connect only accounts you want managed in one launcher. | Keep add-ons minimal. | Use if several launchers are installed. | Optional. | Low to moderate depending on library integrations. | Steam, GOG Galaxy, individual launchers. | Use Playnite built-in update path. | Uninstall from Windows Apps and remove personal library data only if intended. |
| 7-Zip | Recommended | Archive extraction and creation. | [7-Zip downloads](https://www.7-zip.org/download.html) | Install Windows x64 build from 7-Zip. | Avoid running unknown archives. | Enable context menu integration if useful. | As needed. | Yes. | Minimal. | Windows Explorer archive support, NanaZip. | Update occasionally for security and format support. | Uninstall from Windows Apps. |
| MSI Afterburner | Optional | GPU monitoring overlay or manual GPU tuning if required later. | [MSI Afterburner](https://www.msi.com/Landing/afterburner) | Install only if AMD Adrenalin/HWiNFO overlay is not enough. | Monitoring only unless deliberately tuning later. | Do not enable overclock or voltage changes for baseline. | Use for overlay troubleshooting or controlled GPU tuning only. | No, unless its overlay is required. | Low to moderate with overlay. | AMD Adrenalin metrics, HWiNFO. | Update from MSI when needed. | Uninstall from Windows Apps and remove profiles if no longer needed. |
| LibreHardwareMonitor | Optional | Alternative open-source monitoring. | [LibreHardwareMonitor GitHub](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor) | Use GitHub releases. | Use read-only monitoring. | Do not run alongside multiple sensor tools if readings become confusing. | Use if HWiNFO is not desired. | No, unless selected as the primary monitor. | Low. | HWiNFO64. | Update from GitHub releases. | Delete portable folder. |
| Display Driver Uninstaller | Optional | Deep display-driver cleanup for persistent GPU driver faults. | [Wagnardsoft DDU](https://www.wagnardsoft.com/display-driver-uninstaller-ddu) | Download only when needed and read current instructions. | Prefer Safe Mode and disconnect automatic driver installs if instructed by Wagnardsoft. | Use only after normal AMD cleanup fails or when changing GPU vendor. | Rare troubleshooting only. | No. | Not relevant except during cleanup. | AMD cleanup/install options. | Download fresh before use. | Delete extracted folder after use. |

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
