---
title: Connector and Cable Reference
description: Representative migrated connector and cable appendix page.
---

This page proves that technical appendix content can move into Starlight while keeping connector rules explicit.

## Motherboard Headers Used

| Connector or header | Used for | Build guidance | Verification state |
| --- | --- | --- | --- |
| `ATX_24PIN` / 24-pin ATX | Main motherboard power | Route through the side grommet with a gentle bend. | Verified from motherboard manual connector inventory. |
| CPU EPS 8-pin / 4+4-pin | CPU power | Route before final top radiator installation. | Verified from motherboard manual connector inventory. |
| `CPU_FAN` | Simple AIO all-in-one cable path | Use for the simple ARCTIC Liquid Freezer III Pro 360 control path. | Verified as an acceptable path. |
| `F_PANEL` | Case power switch, LEDs, reset/speaker if used | Follow motherboard pin labels and LED polarity. | Verified for labels and polarity caution. |

## Do Not Use

- Do not use SATA M.2 drives in this build.
- Do not use mixed PSU cables from another modular PSU.
- Do not use CPU EPS cables as GPU PCIe cables, or GPU PCIe cables as CPU EPS cables.
- Do not add extra fan/RGB hubs during baseline setup unless they are required and documented.

## Static Fallback

The full interactive connector map must have an equivalent text fallback. This page is the first-slice fallback content.
