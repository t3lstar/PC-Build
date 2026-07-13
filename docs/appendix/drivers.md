# Drivers

Status: Initial Milestone 2 content. Last verified: 2026-07-13 10:53 BST.

## Purpose

Track required chipset, motherboard, network, audio, GPU, and utility drivers.

Driver pages change over time. Use the official links below and record the actual installed version during the build.

## Official Sources

| Area | Source | Use |
| --- | --- | --- |
| Motherboard BIOS and drivers | [Gigabyte B850 AORUS Elite WiFi7 support](https://www.gigabyte.com/Motherboard/B850-AORUS-ELITE-WIFI7-rev-1x/support) | BIOS, chipset package, LAN, WLAN, Bluetooth, audio, utilities, manuals. |
| AMD chipset drivers | [AMD drivers and support](https://www.amd.com/en/support/download/drivers.html) | AMD AM5/B850 chipset driver if choosing AMD direct source. |
| AMD Radeon graphics driver | [AMD drivers and support](https://www.amd.com/en/support/download/drivers.html) | Radeon driver for the RX 9060 XT. |
| Windows updates | Windows Settings > Windows Update | OS, security, framework, and some device drivers. |
| Samsung SSD software | [Samsung Magician](https://semiconductor.samsung.com/consumer-storage/support/tools/) | Optional SSD health and firmware utility. |

## Recommended Installation Order

1. Windows Update.
2. AMD chipset driver.
3. LAN or Wi-Fi driver if network is not fully working.
4. Bluetooth driver if needed.
5. Audio driver if Windows default audio is incomplete.
6. AMD Radeon GPU driver.
7. Samsung Magician if SSD monitoring or firmware checking is required.
8. Optional motherboard utilities only when needed.

## Version Record

| Driver or firmware | Installed version | Install date | Source | Notes |
| --- | --- | --- | --- | --- |
| BIOS | _Record during build_ | _Record during build_ | Gigabyte support | Update only for a documented reason. |
| AMD chipset | _Record during build_ | _Record during build_ | Gigabyte or AMD | Install before GPU tuning or benchmarks. |
| LAN | _Record during build_ | _Record during build_ | Gigabyte support | Required if Windows does not provide working network. |
| Wi-Fi/Bluetooth | _Record during build_ | _Record during build_ | Gigabyte support | Required for wireless networking and Bluetooth devices. |
| Audio | _Record during build_ | _Record during build_ | Gigabyte support | Install if default audio lacks required function. |
| AMD Radeon | _Record during build_ | _Record during build_ | AMD support | Use official Radeon driver package. |
| Samsung Magician | _Optional_ | _Optional_ | Samsung | Optional utility, not required for Windows installation. |

## Verification

- Device Manager has no unknown devices.
- Network works after reboot.
- Audio output and microphone input work if used.
- AMD Radeon Software opens and identifies the GPU.
- Windows Update reports no required restart.
