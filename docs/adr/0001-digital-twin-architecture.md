# ADR 0001: Digital Twin Architecture

Status: Accepted. Last verified: 2026-07-13 15:35 BST.

## Context

Milestone 6 adds an interactive digital twin to the published PC build manual. The digital twin must supplement the written guide without weakening the static documentation, GitHub Pages deployment, accessibility, or technical verification standards established in Milestone 5.

The current production site is MkDocs Material. Astro Starlight is the target platform for Milestone 6 because it supports Markdown/MDX documentation, components, static builds, and GitHub Pages deployment. Official Starlight documentation states that Starlight supports Markdown and MDX content, and the official Astro documentation describes GitHub Pages deployment for static Astro sites.

The architecture must also preserve verified source-of-truth data. Component names, connector labels, cable routes, slot choices, airflow roles, and BIOS training states should come from structured data and verified documentation rather than from duplicated hand-written UI logic.

## Decision

Use Astro Starlight as the direct target platform for the Milestone 6 digital twin, with a framework-neutral, data-first source model.

Do not build the digital twin as a MkDocs-specific enhancement. Migrate the documentation site to Astro Starlight as part of Milestone 6, while preserving GitHub Pages publication, existing content quality, stable source data, and static fallbacks.

Milestone 6 should proceed in three tracks:

1. Define the digital twin data model, JSON Schema, validation rules, verification states, and static fallback requirements in repository source files.
2. Create an Astro Starlight first slice that migrates representative documentation and proves GitHub Pages deployment before moving all pages.
3. Implement the interactive digital twin using Starlight/MDX components generated from structured data.

The first Starlight slice must use representative content:

- Home or landing page.
- Component page.
- Connector and cable reference.
- One interactive case or component view.
- One diagram-heavy page.
- Static fallback content for the interactive view.

The production site should switch from MkDocs to Starlight only after the first slice passes the acceptance criteria below. After that point, Starlight becomes the primary published site and MkDocs-specific build/deploy paths should be retired or documented as legacy.

## Acceptance Criteria for Starlight First Slice

- Builds as a static site suitable for GitHub Pages.
- Supports the repository URL base path `/PC-Build/`.
- Preserves readable navigation for the existing manual structure.
- Supports Markdown or MDX content without losing core chapter content.
- Supports interactive components without requiring server-side state.
- Supports static fallbacks when JavaScript is unavailable.
- Supports keyboard navigation, visible focus, reduced-motion behavior, and screen-reader labels for the vertical slice.
- Keeps digital twin data in structured source files rather than embedding build facts only in components.
- Does not make local validation or GitHub Actions materially slower than the current workflow without a documented benefit.

## Data Architecture

Store digital twin source data under `data/` using JSON files validated by JSON Schema.

Initial data domains:

| Domain | Purpose |
| --- | --- |
| Components | CPU, cooler, motherboard, memory, SSD, GPU, case, PSU, Windows USB installer. |
| Locations | Case regions, motherboard zones, slot groups, airflow zones. |
| Connectors | Motherboard headers, PSU connectors, front-panel leads, fan/pump headers, USB/audio headers. |
| Cables | Cable identity, endpoints, route segments, dependency notes, verification state. |
| Airflow | Intake/exhaust roles, fan groups, radiator direction, static fallback text. |
| Build sequence | Ordered steps mapped to chapters, components, tools, and verification checks. |
| BIOS training | Educational state machine for defaults, EXPO, boot order, and rollback paths. |
| Links | Official manufacturer URLs, support pages, manuals, and QR-code source URLs. |

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

The digital twin may support local-only maintenance or upgrade history later in Milestone 6. Any persistence must use browser-local storage only unless a future ADR explicitly approves server-side accounts or cloud state.

Do not store serial numbers, licence keys, invoice data, account names, or private benchmark logs in public repository data.

## Consequences

Positive:

- Commits Milestone 6 to the platform better suited to data-backed interactive documentation.
- Allows the data model and verification rules to proceed before UI implementation.
- Keeps digital twin facts framework-neutral even though the renderer target is Starlight.
- Preserves static GitHub Pages deployment.

Negative:

- Adds a controlled platform migration before full interactive implementation.
- Requires maintaining careful boundaries between data, renderer, and written documentation.
- Requires updating build scripts, validation commands, GitHub Actions, navigation, and source layout during Milestone 6.
- Some existing MkDocs-specific Markdown extensions, styling, and scripts will need conversion.

## Alternatives Considered

### Build the digital twin directly in MkDocs

Rejected. This is the lowest immediate migration cost, but risks building long-term interactive behavior around MkDocs-specific theme scripts and Markdown conventions.

### Migrate the whole site to Astro Starlight immediately

Accepted with sequencing constraints. Astro Starlight is the direct target, but the migration must start with a first slice that proves content conversion, GitHub Pages deployment, navigation, diagrams, validation, and one interactive component before the whole site is switched.

### Use a full 3D engine first

This is out of scope for the first digital twin slice. The manual needs accurate, accessible inspection and routing views before it needs a heavy 3D scene.

## Follow-Up Work

- Issue `#20`: define framework-neutral build data and JSON Schema.
- Issue `#21`: create the verified component and connector dataset.
- Add or repurpose an early Milestone 6 task for the Astro Starlight first slice and migration scaffold.
- Update build scripts, validation commands, GitHub Actions, and publishing documentation when the Starlight site becomes the production target.

## References

- [Astro Starlight Markdown authoring](https://starlight.astro.build/guides/authoring-content/)
- [Astro Starlight pages](https://starlight.astro.build/guides/pages/)
- [Astro Starlight components](https://starlight.astro.build/components/using-components/)
- [Astro GitHub Pages deployment](https://docs.astro.build/en/guides/deploy/github/)
