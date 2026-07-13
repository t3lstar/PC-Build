# Documentation Structure

Status: Active Milestone 5 structure guide. Last verified: 2026-07-13 15:14 BST.

## Purpose

Define how this documentation site is organised so future changes extend the existing manual instead of duplicating pages or losing project state.

## Navigation Groups

| Group | Purpose | Source location |
| --- | --- | --- |
| Home | Public landing page for the manual. | `docs/index.md` |
| Build Guide | First-time builder instructions in build order. | `docs/01-introduction.md` through `docs/26-upgrades.md` |
| Appendix | Reference material, buying guide, checklists, drivers, BIOS settings, publishing, and other reusable support pages. | `docs/appendix/` |
| Project | Repository planning, verification, validation, and milestone status for maintainers. | `docs/project/` |

## Page Status Convention

Use the first lines of each Markdown page for lightweight maintenance status.

| Status wording | Meaning |
| --- | --- |
| `Published HTML content` | The page is part of the published GitHub Pages manual and has passed the HTML build, but was not fully source-reverified in the current issue. |
| `Verified Milestone 5 content` | The page was updated with explicit source-backed technical verification during Milestone 5. |
| `Active Milestone 5 ...` | The page is an active project-control document for Milestone 5 planning, verification, or validation. |
| `Publication-ready HTML site` | The home page reflects the current public site state. |

Use date and time in the format `YYYY-MM-DD HH:MM TZ`.

## Link Rules

- Link from chapter to chapter through the existing `Next Chapter` section.
- Preserve the current post-BIOS reading order: BIOS, Windows Installation, Driver Installation, then EXPO. This follows the build workflow even though the historical filenames are `18-bios.md`, `19-expo.md`, `20-driver-installation.md`, and `21-windows-installation.md`.
- Keep technical evidence in the affected chapter, appendix, or `docs/project/verification-register.md`.
- Keep GitHub milestone and issue links in `MILESTONES.md`, `milestones/`, and project pages.
- Do not create a duplicate chapter when an existing page can be extended.
- Do not commit generated `site/` output.

## Local-First Milestone Workflow

Use `/Users/simondawson/Herd/PC-Build` as the active local checkout.

For milestone implementation:

- Make local commits per issue or coherent issue group.
- Run the local HTML build before each local commit.
- Run `./scripts/validate.sh all` for Milestone 5 validation checkpoints.
- Keep GitHub issues open while their commits are local-only.
- Push at agreed milestone checkpoints instead of after every issue.
- Close GitHub issues only after the relevant commits are pushed and GitHub Actions passes.
- Push earlier when a change needs live GitHub Pages review, CI-only validation, or remote backup.

## Current Live Site

The public site is published through GitHub Pages at:

https://t3lstar.github.io/PC-Build/
