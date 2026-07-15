---
title: "FAQ"
---

## Purpose

Answer common first-time builder questions for this hardware platform.

## Questions

### Can I use DDR4 memory?

No. The Gigabyte B850 AORUS Elite WiFi7 uses DDR5 memory. DDR4 is physically incompatible.

### Which RAM slots should I use?

Use `A2` and `B2` for two DIMMs.

### Should EXPO be enabled before first boot?

No. First boot at default settings. Enable EXPO only after BIOS detects the CPU, RAM, SSD, pump/fans, and GPU correctly.

### Is the ARCTIC 360mm AIO compatible with the case?

Yes, with a clearance note. The case supports a top 360mm radiator, and the ARCTIC cooler is a 360mm AIO, but the ARCTIC radiator is thick. Dry-fit the radiator and route CPU EPS cables before final radiator mounting.

### Should the monitor connect to the motherboard or graphics card?

Connect the monitor to the graphics card.

### Can I use another SSD?

Not for the locked build. Use the Samsung 990 PRO 2TB model listed in the bill of materials unless component selection is deliberately reopened and reverified.

### Should I split the SSD into OS and data partitions?

No. Use one main `C:` volume on the Samsung 990 PRO unless you have a specific recovery workflow that requires partition separation. A separate partition on the same SSD is not a backup. See [SSD Storage Plan](/PC-Build/operations/storage-plan/).

### Can I add another RAM kit later?

Avoid adding a separate kit. Replace the full memory kit with a verified matched kit if upgrading capacity.

### Do I need a BIOS update?

Only update BIOS when there is a relevant reason: CPU support, memory stability, security fix, or a documented issue affecting this build. Use the exact Gigabyte support page for the motherboard revision.

### Why does first boot take a long time?

DDR5 memory training can delay first display output. Wait several minutes before treating a blank screen as a fault.

### Should I install motherboard utilities?

Install drivers first. Add utilities only when they provide a function you need and cannot get from BIOS, Windows, or AMD Radeon Software.

### Where should I check cable and connector names?

Use the [connector and cable reference](/PC-Build/appendix/connectors-cables/). It consolidates the motherboard headers, PSU cable rules, front-panel polarity guidance, cooling cable paths, and routing dependencies used by this build.
