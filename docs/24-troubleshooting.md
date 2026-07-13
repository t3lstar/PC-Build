# Troubleshooting

Status: Verified Milestone 5 troubleshooting content. Last verified: 2026-07-13 14:09 BST.

## Introduction

This chapter gives structured checks for common build, boot, BIOS, Windows, driver, temperature, and performance problems.

## Purpose

Diagnose one fault at a time without randomly changing settings or disassembling working parts.

## Estimated Time

15 minutes to several hours depending on the fault.

## Difficulty

Moderate.

## Required Tools

- Motherboard manual.
- Flashlight.
- Spare USB drive if BIOS recovery is needed.
- Phone or laptop for support pages.
- Notes file for recording symptoms and changes.

## Warnings

- Change one variable at a time.
- Switch off and unplug the PSU before reseating hardware.
- Do not clear CMOS repeatedly without recording what changed.
- Do not keep power-cycling if there is a burning smell, smoke, liquid, or visible damage.
- Do not assume a failed boot is a failed component until basic power and seating checks are complete.

## Step-by-Step Instructions

1. Record the exact symptom.
2. Record what changed immediately before the symptom appeared.
3. Check motherboard debug LEDs or codes if available.
4. Check external basics: wall power, PSU switch, monitor input, display cable, keyboard, and USB installer.
5. Check internal power:
    - 24-pin ATX seated.
    - CPU EPS seated.
    - GPU PCIe power seated.
    - Front-panel power switch connected.
6. Check seating:
    - RAM fully latched in `A2` and `B2`.
    - GPU fully latched in primary PCIe slot.
    - SSD secured in M.2 slot.
7. Return BIOS to optimized defaults if the fault began after settings changes.
8. Disable EXPO if the fault is memory-training or boot-loop related.
9. Boot with minimum required hardware if needed: CPU, cooler, one RAM module, GPU, SSD, keyboard, and display.
10. Reintroduce hardware or settings one at a time.

## Decision Trees

Use these decision trees to isolate common faults. They are intentionally conservative: power down and unplug the PSU before reseating internal hardware.

### No Power

```mermaid
flowchart TD
    A["No power when case button is pressed"] --> B{"Any PSU or motherboard signs of power?"}
    B -->|No| C["Check wall socket, power strip, PSU switch, and IEC cable"]
    C --> D{"Power available at PSU?"}
    D -->|No| E["Change socket or cable before continuing"]
    D -->|Yes| F["Switch off and unplug PSU"]
    B -->|Yes| F
    F --> G["Check 24-pin ATX and CPU EPS seating"]
    G --> H["Check F_PANEL power switch on PW pins"]
    H --> I{"Starts from case button?"}
    I -->|Yes| J["Record fix and continue first boot"]
    I -->|No| K["Test onboard power button if available"]
    K --> L{"Starts from onboard button?"}
    L -->|Yes| M["Recheck case switch cable and F_PANEL placement"]
    L -->|No| N["Stop and inspect PSU, motherboard, or short risk"]
```

Source: [troubleshooting-no-power.mmd](assets/diagrams/mermaid/troubleshooting-no-power.mmd)

### Powers On, No Display

```mermaid
flowchart TD
    A["System powers on but no display"] --> B["Wait for DDR5 memory training"]
    B --> C{"Display appears after training?"}
    C -->|Yes| D["Enter BIOS and record first boot status"]
    C -->|No| E["Confirm monitor input and cable"]
    E --> F["Move display cable to GPU output"]
    F --> G["Check GPU seating and PCIe 8-pin power"]
    G --> H{"VGA debug LED active?"}
    H -->|Yes| I["Reseat GPU after powering down and unplugging PSU"]
    H -->|No| J["Check DRAM debug LED and memory seating"]
    J --> K["Boot with one DIMM in DDR5_A2 if needed"]
    K --> L{"Display appears?"}
    L -->|Yes| M["Reinstall second DIMM in DDR5_B2 and retest"]
    L -->|No| N["Return BIOS to defaults or clear CMOS once, then retest"]
```

Source: [troubleshooting-no-display.mmd](assets/diagrams/mermaid/troubleshooting-no-display.mmd)

### High Temperature

```mermaid
flowchart TD
    A["CPU or GPU temperature is higher than expected"] --> B["Stop load test and record temperature, workload, and fan speeds"]
    B --> C{"CPU temperature issue?"}
    C -->|Yes| D["Check AIO pump and radiator fan readings in BIOS or HWInfo"]
    D --> E["Confirm cold-plate film was removed and block is evenly mounted"]
    E --> F["Confirm top radiator fans exhaust and cables clear blades"]
    C -->|No| G["Check GPU fan speed, bottom intake fans, and GPU power cable clearance"]
    G --> H["Confirm case panels and filters are not blocking airflow"]
    F --> I{"Temperature returns to expected range?"}
    H --> I
    I -->|Yes| J["Record fix and new baseline"]
    I -->|No| K["Recheck fan curves, dust, ambient temperature, and mount quality"]
```

Source: [troubleshooting-high-temperature.mmd](assets/diagrams/mermaid/troubleshooting-high-temperature.mmd)

### Windows, Driver, Or Game Fault

```mermaid
flowchart TD
    A["Windows, device, driver, or game stability fault"] --> B["Record symptom, error text, and last change"]
    B --> C{"Device Manager shows unknown or failed device?"}
    C -->|Yes| D["Install or reinstall chipset, network, audio, then GPU driver from official sources"]
    C -->|No| E{"Fault started after driver update?"}
    E -->|Yes| F["Roll back or clean reinstall the affected driver"]
    E -->|No| G{"Fault started after EXPO or BIOS change?"}
    G -->|Yes| H["Return BIOS to defaults and retest before re-enabling EXPO"]
    G -->|No| I["Check Windows Update, game files, temperatures, and event logs"]
    D --> J["Reboot and retest one change at a time"]
    F --> J
    H --> J
    I --> J
    J --> K{"Fault resolved?"}
    K -->|Yes| L["Record driver or setting version"]
    K -->|No| M["Escalate with recorded symptoms and versions"]
```

Source: [troubleshooting-windows-driver.mmd](assets/diagrams/mermaid/troubleshooting-windows-driver.mmd)

## Common Faults

| Symptom | Likely area | First checks |
| --- | --- | --- |
| No power | PSU, front-panel connector, wall power | PSU switch, wall socket, 24-pin, front-panel power switch pins. |
| Powers on, no display | GPU, memory training, monitor path | Display cable in GPU, GPU power, wait for DDR5 training, RAM seating. |
| Boot loop after EXPO | Memory profile | Clear CMOS, boot defaults, confirm approved kit and slots. |
| SSD missing | M.2 installation | Slot seating, M.2 latch/screw, BIOS storage page. |
| High CPU temperature | Cooler | Pump/fan header, cold-plate film, mounting pressure, radiator fans. |
| Front USB not working | Front-panel cable | USB header seating, bent pins, Windows driver status. |
| GPU driver crash | GPU driver or power | AMD driver version, PCIe power cable, Windows Update, default GPU tuning. |
| Random restart under load | Power, temperature, driver, or memory stability | Check temperatures, PSU/GPU power seating, Event Viewer, and EXPO stability. |
| Front audio missing | Header or Windows audio device | Confirm `F_AUDIO` seating, Realtek driver state, and selected output device. |
| Network missing after Windows install | Driver or adapter state | Install official motherboard network driver, then Windows Update. |

## Verification Checklist

- [ ] Symptom and last change are recorded.
- [ ] Power cables are checked.
- [ ] RAM and GPU seating are checked.
- [ ] BIOS defaults are tested if settings changed.
- [ ] EXPO is disabled during memory fault isolation.
- [ ] Only one change is tested at a time.
- [ ] Final fix is recorded.

## Common Mistakes

- Changing BIOS, drivers, and cables at the same time.
- Reseating the CPU before checking power cables.
- Forgetting that first DDR5 training can take time.
- Blaming Windows before checking Device Manager.
- Leaving the successful fix undocumented.

## Expected Result

Faults are isolated methodically, corrected, and documented without introducing additional uncertainty.

## Sources Reviewed

- [Gigabyte B850 AORUS Elite WiFi7 user manual 1101](https://download.gigabyte.com/FileList/Manual/mb_manual_b850-aorus-elite-wf7_1101_e.pdf)
- [Microsoft Windows 11 recovery options](https://support.microsoft.com/windows/recovery-options-in-windows-31ce2444-7de3-818c-d626-e3b5a3024da5)
- [AMD drivers and support](https://www.amd.com/en/support/download/drivers.html)

## Next Chapter

Continue to [Maintenance](25-maintenance.md).
