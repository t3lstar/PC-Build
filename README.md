# Custom Gaming PC Build Manual

This repository contains a professional build manual for a custom gaming PC based on the hardware specification in `AGENTS.md`.

The documentation is built with MkDocs Material and is designed to evolve as components, firmware, drivers, and build decisions change.

The intended public site URL is `https://t3lstar.github.io/PC-Build/`.

## Current Milestone

The project is split into staged milestones:

1. Repository scaffolding
2. Core content
3. Technical diagrams
4. Polish
5. Professional Engineering Edition
6. Interactive Digital Twin Edition

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

Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
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

Milestone 5 will focus on professional engineering documentation, validation automation, verification tracking, printable/PDF output, and long-term maintenance records.

Milestone 6 will focus on an accessible, static-site-compatible digital twin after an architecture decision record and verified data model are in place.

## Local Preview

```bash
source .venv/bin/activate
mkdocs serve
```
