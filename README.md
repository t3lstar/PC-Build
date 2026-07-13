# Custom Gaming PC Build Manual

This repository contains a professional build manual for a custom gaming PC based on the hardware specification in `AGENTS.md`.

The documentation is built with MkDocs Material and is designed to evolve as components, firmware, drivers, and build decisions change.

The intended public site URL is `https://t3lstar.github.io/PC-Build/`.

## Current Roadmap Status

The project is split into staged milestones. Milestones 1-5 are complete for the published GitHub Pages HTML site. Milestone 6 is in progress locally.

| Milestone | Status | Tracker |
| --- | --- | --- |
| 1. Repository scaffolding | Complete | [Issue #4](https://github.com/t3lstar/PC-Build/issues/4) |
| 2. Core content | Complete | [Issue #1](https://github.com/t3lstar/PC-Build/issues/1) |
| 3. Technical diagrams | Complete | [Issue #2](https://github.com/t3lstar/PC-Build/issues/2) |
| 4. Polish | Complete for GitHub Pages HTML | [Issue #3](https://github.com/t3lstar/PC-Build/issues/3) |
| 5. Professional Engineering Edition | Complete and published | [GitHub milestone](https://github.com/t3lstar/PC-Build/milestone/1) |
| 6. Interactive Digital Twin Edition | In progress locally | [GitHub milestone](https://github.com/t3lstar/PC-Build/milestone/2) |

See `MILESTONES.md` for the current roadmap, assumptions, and acceptance criteria.

## License

This documentation is published under the MIT License. See `LICENSE`.

## Repository Layout

```text
.
├── AGENTS.md
├── CONTRIBUTING.md
├── MILESTONES.md
├── README.md
├── docs/
│   ├── index.md
│   ├── 01-introduction.md
│   ├── ...
│   ├── 26-upgrades.md
│   ├── appendix/
│   ├── project/
│   └── assets/
├── milestones/
├── mkdocs.yml
├── requirements.txt
└── scripts/
    └── build.sh
```

Rendered documentation content lives under `docs/` so MkDocs can build the site cleanly. The appendix and assets are also stored under `docs/` for reliable internal links.

## Build

Use Python 3.12 for local documentation builds. Node.js 24 is the expected local JavaScript runtime if Node-based tooling is added or used.

Keep the working copy on the local drive, not inside iCloud Drive or another synced folder. MkDocs cleans and rewrites `site/` on each build, and synced storage can make local builds dramatically slower.

Install dependencies:

```bash
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Build the HTML site:

```bash
./scripts/build.sh html
```

Build every configured output:

```bash
./scripts/build.sh all
```

The `pdf` and `printable` script targets are reserved for later work. The current published output is the GitHub Pages HTML site.

Run local validation:

```bash
./scripts/validate.sh all
```

This checks digital twin JSON data and cross-references, required repository files, MkDocs navigation targets, local Markdown links, and the strict HTML build.

Regenerate official-link QR code assets after changing official links:

```bash
python scripts/generate-qrcodes.py
./scripts/validate.sh qrcodes
```

Build the Astro Starlight first slice:

```bash
npm install
./scripts/validate.sh starlight
```

The Starlight first slice builds to `dist/` and then runs source/built-output checks for the digital twin's interaction structure, accessibility markers, static fallbacks, and QR asset references. MkDocs remains the production GitHub Pages path until the Starlight migration slice is approved and the deployment workflow is switched.

The first slice currently uses Astro `7.0.7`, Starlight `0.41.3`, and MDX `7.0.2`. Local Node tooling should remain compatible with the repository Node.js 24 target.

## Project Planning

- Milestone tracker: `MILESTONES.md`
- Detailed milestone plans: `milestones/`
- Repository audit and verification planning: `docs/project/`
- Live site structure guide: `docs/project/documentation-structure.md`
- Technical verification register: `docs/project/verification-register.md`
- Validation report: `docs/project/milestone-05-06-validation-report.md`

Milestone 5 added professional engineering documentation, validation automation, verification tracking, printable output, and long-term maintenance records. PDF generation remains deferred.

Milestone 6 focuses on an accessible, static-site-compatible Astro Starlight digital twin backed by framework-neutral verified build data.

## Contribution Workflow

1. Read `AGENTS.md` and `MILESTONES.md` before making changes.
2. Work from the relevant GitHub issue or milestone plan.
3. Update project documentation in the same change when new durable information is discovered.
4. Keep technical claims source-backed or record unresolved items in `docs/project/verification-register.md`.
5. Run `./scripts/validate.sh all` before publishing documentation changes.

Milestone implementation uses a local-first flow: commit locally per issue or issue group, validate locally, and push at agreed milestone checkpoints. GitHub issues are closed only after the relevant commits are pushed and GitHub Actions passes.

## Local Preview

```bash
source .venv/bin/activate
mkdocs serve
```
