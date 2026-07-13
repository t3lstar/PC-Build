# BIOS Settings

Status: Published HTML content. Last reviewed: 2026-07-13 13:53 BST.

## Purpose

Document BIOS settings for first boot, Windows 11 Pro installation, EXPO, fan monitoring, and future updates.

## Baseline Settings

| Setting area | Recommended state | Notes |
| --- | --- | --- |
| Optimized defaults | Load before configuration if board history is unknown | Gives a clean baseline. |
| UEFI boot | Enabled | Required for a normal Windows 11 install. |
| TPM/fTPM | Enabled or available | Required for Windows 11 compatibility. |
| Secure Boot | Available, configure for Windows after baseline install | Do not disable permanently without a reason. |
| EXPO | Disabled for first boot; enabled later | Enable only after default boot succeeds. |
| CPU overclocking | Default | Do not overclock during baseline setup. |
| GPU settings | Default | Configure GPU in Windows after drivers. |
| Fan/pump monitoring | Enabled | Confirm the AIO reports activity. |
| Boot order | Windows USB first for setup, NVMe SSD first after install | Remove USB from first priority after installation. |

## EXPO Setting

Enable the AMD EXPO profile for the approved RAM kit only after:

- CPU is detected correctly.
- 32GB memory is detected in `A2` and `B2`.
- SSD is detected.
- Windows can boot or the system has proven stable at defaults.

## BIOS Update Policy

The Gigabyte support page listed BIOS `F12b` dated 2026-06-30 at the time this page was last verified. Treat BIOS releases as moving targets and confirm the current support page before flashing.

Update BIOS only when:

- A release note fixes a relevant stability or security issue.
- A future CPU upgrade requires it.
- A memory compatibility issue affects this build.
- Gigabyte support directs the update for this exact motherboard revision.

## Q-Flash Safety

- Use only the BIOS file for `B850 AORUS ELITE WIFI7` and the correct revision.
- Use a reliable FAT32 USB drive.
- Keep power stable.
- Do not turn off the system during flashing.
- Load optimized defaults after flashing and re-check settings.

## Verification

- BIOS settings are recorded before and after changes.
- The system can boot after each change.
- EXPO status is visible after reboot.
- Fan and pump readings are visible.
- Windows boots from the NVMe SSD after installation.
