# Checklists

Status: Verified Milestone 5 checklist content. Last verified: 2026-07-13 14:09 BST.

## Purpose

Provide preparation, installation, first boot, BIOS, Windows, driver, benchmark, handover, and maintenance checklists.

Use these checklists alongside the chapter instructions. Do not use them as a substitute for the step-by-step chapters when installing hardware for the first time.

## How To Use

- Work from top to bottom.
- Mark an item complete only when it has been physically checked.
- Write down any failed item before continuing.
- Stop and resolve power, cooling, connector, or firmware uncertainty before first boot.
- Keep benchmark and maintenance results outside the public repository if they include serial numbers, account names, or personal data.

## Pre-Purchase Checklist

- [ ] CPU model is AMD Ryzen 7 7800X3D.
- [ ] Motherboard model is Gigabyte B850 AORUS Elite WiFi7 rev. 1.x.
- [ ] Memory is an approved 2 x 16GB DDR5-6000 CL30 AMD EXPO kit from the bill of materials.
- [ ] SSD is a 2TB M.2 2280 NVMe drive, not SATA M.2.
- [ ] GPU listing is the Gigabyte Radeon RX 9060 XT Gaming OC 16GB model.
- [ ] Case is Lian Li O11 Dynamic Mini V2 Flow, black Flow SKU `O11DMIV2FX` if matching the documented build.
- [ ] PSU is ASUS TUF Gaming 1000W Gold or a documented compatible equivalent.
- [ ] Retailer listings match exact model numbers.
- [ ] Return windows and warranty terms are understood.
- [ ] Windows 11 Pro USB installer is already available.

## Workspace Checklist

- [ ] Large, flat, clean table available.
- [ ] Good lighting available.
- [ ] Drinks and loose metal objects removed.
- [ ] Anti-static wrist strap available.
- [ ] Screw tray or labelled containers available.
- [ ] Full-size Phillips #2 screwdriver available.
- [ ] Precision screwdriver available.
- [ ] Flashlight or head torch available.
- [ ] Component manuals available.
- [ ] Phone or camera available for reference photos.

## Parts Intake Checklist

- [ ] Outer shipping boxes inspected for damage.
- [ ] Component boxes inspected for damage.
- [ ] Exact component model numbers match the bill of materials.
- [ ] Motherboard socket cover is present and undamaged.
- [ ] Motherboard accessory pack is present.
- [ ] Case accessory box is present.
- [ ] PSU modular cable set is present.
- [ ] AIO AM5 mounting hardware is present.
- [ ] GPU power connector requirement is confirmed.
- [ ] Serial numbers and invoices are recorded privately.

## Motherboard Prep

- [ ] Motherboard is on its cardboard box or another safe non-conductive surface.
- [ ] AM5 socket is inspected before CPU installation.
- [ ] Ryzen 7 7800X3D is aligned and installed without force.
- [ ] Socket cover stored.
- [ ] DDR5 memory is installed in `A2` and `B2`.
- [ ] Samsung 990 EVO Plus is installed in `M2A_CPU`.
- [ ] M.2 thermal pad film removed.
- [ ] M.2 heatsink is reinstalled.
- [ ] No screws or loose parts are under the motherboard.

## Case Prep

- [ ] Panels removed and stored safely.
- [ ] ATX standoffs checked.
- [ ] No unused standoff under board area.
- [ ] PSU chamber accessible.
- [ ] Radiator area dry-fit planned.
- [ ] Front-panel cables identified.
- [ ] Included bottom and side fans are present.
- [ ] Top radiator bracket access is understood.
- [ ] Front I/O location is chosen for the final desk layout.

## Power and Cooling

- [ ] PSU mounted.
- [ ] 24-pin ATX connected.
- [ ] CPU EPS connected before radiator final install.
- [ ] AIO cold-plate film removed.
- [ ] Pump/fan cable connected.
- [ ] AIO all-in-one cable is connected to `CPU_FAN` for the simple build path, or individual-control leads are labelled.
- [ ] Radiator fans clear of cables.
- [ ] GPU PCIe power connected.
- [ ] PSU modular cables are fully seated at the PSU end and component end.
- [ ] No cable touches fan blades.

## Cable Routing Checklist

- [ ] 24-pin ATX cable has a gentle curve and no side-panel pressure.
- [ ] CPU EPS cable is routed before final radiator tightening.
- [ ] PCIe GPU power cable is not sharply bent at the GPU connector.
- [ ] Front-panel switch/LED cable reaches `F_PANEL` without tension.
- [ ] Front USB-A cable reaches the USB 3.x header without bending pins.
- [ ] Front USB-C cable is aligned before pressure is applied.
- [ ] HD audio cable is routed away from fan blades.
- [ ] Excess cable length is secured in the rear chamber.
- [ ] Rear panel closes without compressing cables aggressively.

## First Boot

- [ ] Monitor connected to GPU.
- [ ] Keyboard connected.
- [ ] PSU switch on.
- [ ] Case power button works.
- [ ] BIOS opens.
- [ ] CPU detected.
- [ ] 32GB memory detected.
- [ ] SSD detected.
- [ ] Pump/fan readings visible.
- [ ] Debug LEDs do not remain stuck after memory training.
- [ ] No burning smell, scraping fan noise, or liquid leak is present.

## BIOS

- [ ] Optimized defaults loaded if needed.
- [ ] UEFI boot mode confirmed.
- [ ] TPM/fTPM available.
- [ ] Secure Boot available for Windows 11.
- [ ] USB installer selected for Windows installation.
- [ ] EXPO left disabled until default boot is confirmed.
- [ ] Fan and pump headers are visible in monitoring.
- [ ] Connected cooler headers are set to PWM mode before fan tuning.

## Windows and Drivers

- [ ] Windows 11 Pro installed to NVMe SSD.
- [ ] Windows activated or activation state known.
- [ ] Windows Update completed.
- [ ] AMD chipset driver installed.
- [ ] Network driver working.
- [ ] Audio driver working.
- [ ] AMD Radeon driver installed.
- [ ] Device Manager has no unknown devices.
- [ ] Restore point or recovery plan exists before optional utilities.

## Benchmark and Handover

- [ ] EXPO enabled and confirmed.
- [ ] Idle temperatures recorded.
- [ ] CPU load temperatures recorded.
- [ ] Memory stability check passed.
- [ ] SSD benchmark recorded.
- [ ] GPU benchmark recorded.
- [ ] Driver and BIOS versions recorded.
- [ ] Any abnormal result is investigated before treating the build as complete.
- [ ] Final photos are taken for private maintenance reference.

## Maintenance

- [ ] Dust filters checked monthly.
- [ ] Temperatures compared with baseline.
- [ ] Fan noise checked for new vibration or scraping.
- [ ] SSD free space checked.
- [ ] Drivers reviewed when troubleshooting or before major games.
- [ ] BIOS updated only for a documented reason.
- [ ] Cable strain checked after moving the case.
- [ ] Maintenance action recorded.

## Monthly Maintenance Log Template

| Date | Dust/filter state | Idle CPU/GPU temps | Fan noise | SSD free space | Action taken |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Driver And Firmware Change Log Template

| Date | Item changed | Previous version | New version | Reason | Result |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Hardware Change Log Template

| Date | Change | Parts affected | Compatibility checked | Baseline repeated | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
