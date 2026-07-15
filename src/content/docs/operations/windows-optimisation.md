---
title: "Windows 11 Pro Optimisation"
---

## Introduction

This chapter applies conservative Windows 11 Pro settings after the hardware, drivers, and baseline checks are stable.

Optimisation means reducing avoidable background load, confirming gaming-related settings, and keeping the system repeatable. It does not mean running debloat scripts, disabling security, or applying registry tweaks from generic gaming guides.

## Purpose

Configure Windows 11 Pro for stable gaming and daily use while keeping changes reversible and easy to troubleshoot.

## Estimated Time

45-90 minutes.

## Difficulty

Beginner to moderate.

## Required Tools

- Windows administrator account.
- Windows Settings.
- Task Manager.
- Device Manager.
- AMD Software: Adrenalin Edition.
- HWiNFO64 or another monitoring tool.
- Restore point or backup plan.

## Warnings

- Do not disable Windows Security for benchmark gains.
- Do not run debloat scripts or registry cleaners.
- Do not disable Windows services from internet tweak lists.
- Do not change many settings before recording a stable baseline.
- Do not use third-party game booster tools.
- Do not tune the GPU, fan curves, EXPO, and Windows settings at the same time.

## Step-by-Step Instructions

Use this order so each change has a clear reason:

1. Complete Windows Update and driver installation.
2. Confirm Device Manager has no unknown devices.
3. Create a restore point.
4. Record idle readings.
5. Configure display and gaming settings.
6. Review startup apps.
7. Review storage, backup, and BitLocker decisions.
8. Run the benchmark baseline.

## Windows Update

Keep Windows current before performance testing.

1. Open **Settings**.
2. Go to **Windows Update**.
3. Select **Check for updates**.
4. Install available important updates.
5. Restart when prompted.
6. Repeat until no required restart remains.

Avoid optional driver updates unless:

- A current device has a fault.
- The update comes from a known vendor source.
- You can roll back if the update causes problems.

## Startup Apps

Startup apps can slow boot and add background load. Disable only apps that do not need to run automatically.

Use Settings:

1. Open **Settings**.
2. Go to **Apps > Startup**.
3. Sort by startup impact if the option is available.
4. Turn off launch-at-login for apps you do not need immediately after sign-in.
5. Leave security, audio, GPU, backup, and required peripheral apps enabled.
6. Restart and confirm normal behaviour.

Use Task Manager if you prefer the detailed list:

1. Press `Ctrl` + `Shift` + `Esc`.
2. Select **Startup apps**.
3. Review the **Status** and **Startup impact** columns.
4. Right-click an unnecessary app.
5. Select **Disable**.
6. Reboot and check that required devices, backup, audio, and Radeon software still work.

Good candidates to disable:

- Chat clients you open manually.
- Game launchers you do not use every session.
- Updaters for optional utilities.
- Capture tools that are not used daily.

Do not disable blindly:

- Windows Security.
- AMD Software or required Radeon services.
- Audio driver components if they provide needed audio functions.
- Backup or cloud sync tools that protect important files.
- Mouse, keyboard, headset, or controller utilities required for basic device behaviour.

## Display and Refresh Rate

Confirm display settings before benchmarking.

1. Open **Settings**.
2. Go to **System > Display**.
3. Confirm the monitor uses its native resolution.
4. Select **Advanced display**.
5. Choose the intended refresh rate for the gaming monitor.
6. Confirm the display cable is connected to the Radeon graphics card, not the motherboard.

If using HDR:

1. Open **Settings > System > Display**.
2. Select the HDR-capable display.
3. Select **HDR**.
4. Enable HDR only if the monitor supports it well and desktop appearance remains acceptable.
5. Record the HDR state before benchmark comparisons.

Leave HDR off if it causes washed-out desktop colour, inconsistent screenshots, or game-specific issues.

## Game Mode and Graphics Settings

Enable Game Mode as the default Windows gaming setting.

1. Open **Settings**.
2. Go to **Gaming > Game Mode**.
3. Turn **Game Mode** on.

Review per-game graphics settings only when a game needs a specific preference:

1. Open **Settings**.
2. Go to **System > Display > Graphics**.
3. Select the game or add it to the list.
4. Select **Options**.
5. Choose the intended graphics preference.
6. Test the game and record the result.

Do not change per-game graphics settings for every game without a reason. Use AMD Software for Radeon-specific features and keep GPU tuning at default until the baseline is recorded.

## Power Settings

Start with the standard Windows power behaviour. For this desktop build, the practical goal is stable boost behaviour without unnecessary noise or heat.

1. Open **Settings**.
2. Go to **System > Power** or **System > Power & battery**.
3. Review **Power mode** if available.
4. Start with **Balanced** or the default Windows mode.
5. Use a higher-performance mode only as a recorded test if a workload shows a repeatable benefit.
6. Set screen and sleep timers to match how the PC will be used.

Avoid:

- Enabling hidden power plans because a benchmark guide recommends them.
- Disabling sleep globally without a reason.
- Changing many power settings before baseline testing.

## Storage Settings

Follow the [SSD Storage Plan](/PC-Build/operations/storage-plan/).

1. Keep Windows and active game libraries on the Samsung 990 PRO.
2. Keep one main `C:` volume unless the storage plan is deliberately changed.
3. Keep 15-20% free space where practical.
4. Move old captures, installers, and exports off the SSD when they are no longer active.
5. Let Windows handle SSD optimisation automatically.
6. Do not install SSD defragmentation tools.

Use Storage Sense cautiously:

1. Open **Settings**.
2. Go to **System > Storage**.
3. Review **Storage Sense** settings before enabling automatic cleanup.
4. Do not let cleanup remove Downloads or temporary files you still need.

## Privacy, Notifications, and Focus

Reduce noise without turning off security visibility.

1. Open **Settings > System > Notifications**.
2. Turn off notifications from apps that do not require attention.
3. Keep Windows Security notifications enabled.
4. Open **Settings > Privacy & security**.
5. Review app permissions such as camera, microphone, location, and background app access.
6. Disable permissions that are not needed for installed apps.

Keep changes practical. Privacy settings should reduce unnecessary access, not break game launchers, audio chat, capture tools, or controller software.

## Accessibility and Visual Comfort

Make the PC comfortable to use before benchmark work.

1. Open **Settings > Accessibility**.
2. Adjust text size only if normal scaling is not readable.
3. Use colour filters, captions, keyboard, mouse, or pointer settings if they improve usability.
4. Open **Settings > System > Display** and confirm scaling is comfortable.
5. Use Night Light only if desired for evening use.

Do not treat accessibility settings as performance tweaks. They are usability settings.

## Restore Point

Create a restore point before optional utilities, launchers, capture software, RGB utilities, or deeper tuning.

1. Open Start.
2. Type `restore point`.
3. Open **Create a restore point**.
4. Select the Windows drive.
5. Select **Configure** if System Protection is off.
6. Turn on System Protection.
7. Select **Create**.
8. Name the restore point with the date and reason.

## What Not To Optimise

Do not do these as part of normal setup:

- Disable Windows Security.
- Disable TPM or Secure Boot.
- Disable services without a fault-specific reason.
- Run registry cleaners.
- Run debloat scripts.
- Force hidden power plans.
- Disable Windows Update.
- Remove Microsoft Store components needed by Xbox, Game Bar, or app updates.
- Use game booster utilities.
- Apply GPU tuning before the baseline.

## Verification Checklist

- [ ] Windows Update has no required restart.
- [ ] Device Manager has no unknown devices.
- [ ] Restore point exists.
- [ ] Monitor resolution and refresh rate are correct.
- [ ] Game Mode is enabled.
- [ ] Startup apps are reviewed.
- [ ] Required security, audio, GPU, backup, and peripheral tools still start correctly.
- [ ] Storage free-space target is understood.
- [ ] Windows Security remains enabled.
- [ ] Any power, HDR, graphics, or notification changes are recorded.

## Common Mistakes

- Disabling every startup app without checking what the app does.
- Benchmarking while Windows Update, game downloads, or indexing are active.
- Using game boosters instead of Windows Game Mode and clean driver setup.
- Applying hidden power plans before measuring default behaviour.
- Turning off Windows Security for small benchmark gains.
- Changing HDR, refresh rate, Radeon settings, and Windows power mode at the same time.

## Expected Result

Windows 11 Pro is updated, stable, quiet at idle, configured for the intended display and game use, and ready for a repeatable benchmark baseline.

## Sources Reviewed

- [Microsoft Configure Startup applications in Windows](https://support.microsoft.com/en-us/windows/experience/startup-boot/configure-startup-applications-in-windows)
- [Microsoft Tips to improve PC performance in Windows](https://support.microsoft.com/en-us/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows)
- [Microsoft Power settings in Windows 11](https://support.microsoft.com/en-us/windows/experience/power-battery/power-settings-in-windows-11)
- [Microsoft Optimizations for windowed games in Windows 11](https://support.microsoft.com/en-us/windows/hardware/display-graphics/optimizations-for-windowed-games-in-windows-11)
- [Microsoft HDR settings in Windows](https://support.microsoft.com/en-us/windows/hardware/display-graphics/hdr-settings-in-windows)
- [Microsoft Windows Settings accessibility guide](https://support.microsoft.com/en-us/accessibility/windows/understand-and-explore-windows-settings)

## Next Chapter

Continue to [Benchmark Baseline](/PC-Build/operations/benchmark-baseline/).
