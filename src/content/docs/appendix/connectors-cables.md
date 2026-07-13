---
title: "Connector and Cable Reference"
---
Status: Verified Milestone 5 content. Last verified: 2026-07-13 15:21 BST.

## Purpose

Provide a single reference for the motherboard headers, PSU cables, front-panel connectors, cooling leads, and routing dependencies used by this build.

This appendix identifies connector names and safe routing rules. It does not provide exact physical coordinates for an interactive board map; those remain future digital twin work.

## Motherboard Headers Used

| Connector or header      | Used for                                       | Build guidance                                                                                    | Verification state                                                     |
| ------------------------ | ---------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `ATX_24PIN` / 24-pin ATX | Main motherboard power                         | Route through the side grommet with a gentle bend. Seat fully at the motherboard and PSU.         | Verified from motherboard manual connector inventory.                  |
| CPU EPS 8-pin / 4+4-pin  | CPU power                                      | Route before final top radiator installation. Do not confuse with PCIe 8-pin GPU power.           | Verified from motherboard manual connector inventory.                  |
| `CPU_FAN`                | Simple AIO all-in-one cable path               | Use for the simple ARCTIC Liquid Freezer III Pro 360 control path. Set the header to PWM in BIOS. | Verified as an acceptable path from ARCTIC and Gigabyte documentation. |
| `CPU_OPT`                | Optional radiator fan or cooler lead           | Use only if choosing the individual-control cooler path and documenting the cable map.            | Verified as a 4-pin fan-capable header.                                |
| `FAN4_PUMP`              | Optional pump-capable header                   | Use only if deliberately separating pump control from the all-in-one cable path.                  | Verified as fan/water-cooling pump capable.                            |
| `F_PANEL`                | Case power switch, LEDs, reset/speaker if used | Follow the motherboard pin labels and LED polarity.                                               | Verified for labels and polarity caution.                              |
| Internal USB 3.x header  | Front USB-A ports                              | Align carefully before applying pressure. Do not bend header pins.                                | Verified from motherboard connector inventory.                         |
| Internal USB-C header    | Front USB-C port                               | Align straight and avoid side load.                                                               | Verified from motherboard connector inventory.                         |
| HD audio header          | Front audio jack                               | Route away from fans and high-tension power cable bundles.                                        | Verified from motherboard connector inventory.                         |
| `M2A_CPU`                | Boot NVMe SSD                                  | Preferred slot for the Samsung 990 EVO Plus boot drive. Use the motherboard heatsink.             | Verified as CPU-connected M.2 slot.                                    |
| Primary PCIe x16 slot    | Graphics card                                  | Install GPU in the primary slot and connect monitor to GPU outputs.                               | Verified from motherboard connector inventory.                         |

## PSU Cable Reference

| Cable                | Connects to               | Rules                                                                                                          |
| -------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 24-pin ATX           | PSU to motherboard 24-pin | Use the PSU-supplied modular cable. Do not force the latch.                                                    |
| CPU EPS 4+4-pin      | PSU to CPU power header   | Route before the radiator blocks access. Keep separate from PCIe GPU cables.                                   |
| PCIe 8-pin GPU power | PSU to graphics card      | Use the correct PCIe cable for the GPU. Avoid sharp bends at the GPU connector.                                |
| SATA power           | Optional accessories only | Leave unused unless a future accessory requires it. Do not add unnecessary powered hubs during baseline setup. |
| AC mains cable       | Wall power to PSU         | Connect only after the internal build inspection is complete.                                                  |

## Front-Panel Connector Rules

- Power switch is not polarity-sensitive.
- LED connectors are polarity-sensitive; match positive and negative markings.
- Do not connect front-panel leads by colour alone. Use the case label and motherboard `F_PANEL` labels.
- If the power button does not work, re-check `PW`/power switch placement before suspecting the PSU.
- If only an LED does not work, re-check polarity before moving other connectors.

## Cooling Cable Rules

- For the simple build path, use the ARCTIC all-in-one cable to `CPU_FAN`.
- For individual control, label each pump, VRM fan, and radiator fan lead before connecting it.
- Keep radiator fan cables clear of blades before powering on.
- Set connected cooling headers to PWM mode before tuning fan curves.
- Do not run the system if the pump/fan reading is missing and CPU temperature rises rapidly.

## Routing Dependencies

| Dependency                                   | Reason                                                                   |
| -------------------------------------------- | ------------------------------------------------------------------------ |
| CPU EPS before radiator                      | Top radiator access can make the EPS connector difficult to reach.       |
| Motherboard 24-pin before rear-panel closure | Side pressure can loosen or strain the connector if cable slack is poor. |
| Front USB-C before final cable tie-down      | The connector is sensitive to angle and side pressure.                   |
| GPU power after GPU is fully latched         | The cable should not pull the card out of alignment.                     |
| Fan clearance before first boot              | A tied cable can move into a blade when panels are closed.               |

## Do Not Use

- Do not use SATA M.2 drives in this build; the motherboard M.2 guidance is for PCIe NVMe SSDs.
- Do not use mixed PSU cables from another modular PSU.
- Do not use CPU EPS cables as GPU PCIe cables, or GPU PCIe cables as CPU EPS cables.
- Do not add extra fan/RGB hubs during baseline setup unless they are required and documented.

## Related Chapters

- [Motherboard Overview](/PC-Build/build-guide/motherboard-overview/)
- [PSU Installation](/PC-Build/build-guide/psu-installation/)
- [AIO Installation](/PC-Build/build-guide/aio-installation/)
- [Cable Routing](/PC-Build/build-guide/cable-routing/)
- [Front Panel Connectors](/PC-Build/build-guide/front-panel-connectors/)
- [Troubleshooting](/PC-Build/build-guide/troubleshooting/)
