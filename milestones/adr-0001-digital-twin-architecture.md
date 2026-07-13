---
title: "ADR 0001: Digital Twin Architecture"
---
Status: Accepted. Last verified: 2026-07-13 18:08 BST.

## Context

The PC build manual includes an interactive digital twin that supplements the written guide without weakening static documentation, GitHub Pages deployment, accessibility, or technical verification standards.

The site uses Astro Starlight because it supports Markdown, MDX, Astro components, static builds, and GitHub Pages deployment.

The architecture must preserve verified source-of-truth data. Component names, connector labels, cable routes, slot choices, airflow roles, and BIOS training states should come from structured data and verified documentation rather than duplicated hand-written UI logic.

## Decision

Use Astro Starlight with a framework-neutral, data-first source model.

Digital twin implementation proceeds in three tracks:

1. Define the data model, JSON Schema, validation rules, verification states, and static fallback requirements in repository source files.
2. Render documentation through Astro Starlight Markdown and MDX pages.
3. Implement interactive views using Astro components generated from structured data.

## Data Architecture

Store digital twin source data under `data/` using JSON files validated by JSON Schema.

Initial data domains:

| Domain         | Purpose                                                                                      |
| -------------- | -------------------------------------------------------------------------------------------- |
| Components     | CPU, cooler, motherboard, memory, SSD, GPU, case, PSU, Windows USB installer.                |
| Locations      | Case regions, motherboard zones, slot groups, airflow zones.                                 |
| Connectors     | Motherboard headers, PSU connectors, front-panel leads, fan/pump headers, USB/audio headers. |
| Cables         | Cable identity, endpoints, route segments, dependency notes, verification state.             |
| Airflow        | Intake/exhaust roles, fan groups, radiator direction, static fallback text.                  |
| Build sequence | Ordered steps mapped to chapters, components, tools, and verification checks.                |
| BIOS training  | Educational state machine for defaults, EXPO, boot order, and rollback paths.                |
| Links          | Official manufacturer URLs, support pages, manuals, and QR-code source URLs.                 |

Every data item must carry a verification state:

- `verified`: backed by official documentation or completed build verification.
- `partially_verified`: backed for identity or labels, but missing exact physical position or route verification.
- `pending`: known requirement, not yet verified.
- `deferred`: deliberately outside the current issue or milestone slice.

## Rendering Architecture

Interactive views should be Starlight/MDX components generated from structured data.

Preferred rendering order:

1. Static text fallback in Markdown.
2. Accessible Astro, SVG, or HTML component generated from data.
3. Lightweight client-side JavaScript only where needed for selection, highlighting, filtering, and guided sequence behavior.
4. Heavier 3D or canvas rendering only if a later ADR proves a strong user benefit.

Do not use photorealistic or AI-generated technical diagrams as authoritative digital twin views. Generated or reference imagery may remain visual context only.

## Accessibility Requirements

Each interactive view must include:

- Keyboard-operable controls.
- Visible focus indicators.
- Screen-reader names for controls and selected regions.
- Reduced-motion behavior.
- Text alternative or static fallback with equivalent instructional value.
- Touch-friendly target sizing for tablet use.
- No critical information communicated by colour alone.

## Persistence

The digital twin may support local-only maintenance or upgrade history. Any persistence must use browser-local storage only unless a future ADR explicitly approves server-side accounts or cloud state.

Do not store serial numbers, licence keys, invoice data, account names, or private benchmark logs in public repository data.

## Consequences

Positive:

- Keeps the interactive documentation static-site compatible.
- Keeps digital twin facts framework-neutral.
- Allows validation to check data, routes, assets, accessibility markers, and static fallbacks.
- Preserves GitHub Pages deployment.

Negative:

- Requires strong validation so structured data and rendered documentation do not drift.
- Requires clear boundaries between data, renderer, and written documentation.

## Alternatives Considered

### Data-Backed Astro Components

Accepted. This gives the documentation enough interactivity while keeping deployment static and validation straightforward.

### Full 3D Engine First

Rejected for the first digital twin slice. The manual needs accurate, accessible inspection and routing views before it needs a heavy 3D scene.

## References

- [Astro Starlight Markdown authoring](https://starlight.astro.build/guides/authoring-content/)
- [Astro Starlight pages](https://starlight.astro.build/guides/pages/)
- [Astro Starlight components](https://starlight.astro.build/components/using-components/)
- [Astro GitHub Pages deployment](https://docs.astro.build/en/guides/deploy/github/)
