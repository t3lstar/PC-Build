# Custom Gaming PC Build Manual

This repository contains a professional build manual for a custom gaming PC based on the hardware specification in `AGENTS.md`.

The documentation is built with MkDocs Material and is designed to evolve as components, firmware, drivers, and build decisions change.

The intended public site URL is `https://t3lstar.github.io/PC-Build/`.

## Current Roadmap Status

The project is split into staged milestones. Milestones 1-4 are complete for the published GitHub Pages HTML site. Milestone 5 is in progress.

| Milestone | Status | Tracker |
| --- | --- | --- |
| 1. Repository scaffolding | Complete | [Issue #4](https://github.com/t3lstar/PC-Build/issues/4) |
| 2. Core content | Complete | [Issue #1](https://github.com/t3lstar/PC-Build/issues/1) |
| 3. Technical diagrams | Complete | [Issue #2](https://github.com/t3lstar/PC-Build/issues/2) |
| 4. Polish | Complete for GitHub Pages HTML | [Issue #3](https://github.com/t3lstar/PC-Build/issues/3) |
| 5. Professional Engineering Edition | In progress | [GitHub milestone](https://github.com/t3lstar/PC-Build/milestone/1) |
| 6. Interactive Digital Twin Edition | Planned | [GitHub milestone](https://github.com/t3lstar/PC-Build/milestone/2) |

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

## Project Planning

- Milestone tracker: `MILESTONES.md`
- Detailed milestone plans: `milestones/`
- Repository audit and verification planning: `docs/project/`
- Live site structure guide: `docs/project/documentation-structure.md`
- Technical verification register: `docs/project/verification-register.md`
- Validation report: `docs/project/milestone-05-06-validation-report.md`

Milestone 5 will focus on professional engineering documentation, validation automation, verification tracking, printable/PDF output, and long-term maintenance records.

Milestone 6 will focus on an accessible, static-site-compatible digital twin after an architecture decision record and verified data model are in place.

## Contribution Workflow

1. Read `AGENTS.md` and `MILESTONES.md` before making changes.
2. Work from the relevant GitHub issue or milestone plan.
3. Update project documentation in the same change when new durable information is discovered.
4. Keep technical claims source-backed or record unresolved items in `docs/project/verification-register.md`.
5. Run `./scripts/build.sh html` before publishing documentation changes.

## Local Preview

```bash
source .venv/bin/activate
mkdocs serve
```
