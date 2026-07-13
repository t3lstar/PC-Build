---
title: ADR 0001 Digital Twin Architecture
description: Accepted architecture decision for the Starlight digital twin migration.
---

ADR 0001 accepts Astro Starlight as the direct target platform for Milestone 6.

## Decision

Use Astro Starlight as the direct target platform for the Milestone 6 digital twin, with a framework-neutral, data-first source model.

Do not build the digital twin as a MkDocs-specific enhancement. Migrate the documentation site to Astro Starlight as part of Milestone 6, while preserving GitHub Pages publication, existing content quality, stable source data, and static fallbacks.

## First Slice Requirements

- Builds as a static site suitable for GitHub Pages.
- Supports the repository URL base path `/PC-Build/`.
- Preserves readable navigation for the existing manual structure.
- Supports Markdown or MDX content without losing core chapter content.
- Supports interactive components without requiring server-side state.
- Supports static fallbacks when JavaScript is unavailable.
- Keeps digital twin data in structured source files rather than embedding build facts only in components.

The source ADR remains at `docs/adr/0001-digital-twin-architecture.md` until the full migration plan retires MkDocs paths.
