# Custom Gaming PC Build Manual

This repository contains a professional build manual for a custom gaming PC based on the hardware specification in `AGENTS.md`.

The documentation is built with MkDocs Material and is designed to evolve as components, firmware, drivers, and build decisions change.

The intended public site URL is `https://t3lstar.github.io/PC-Build/`.

## Current Milestone

The project is split into four milestones:

1. Repository scaffolding
2. Core content
3. Technical diagrams
4. Polish

See `MILESTONES.md` for the current roadmap, assumptions, and acceptance criteria.

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
│   └── assets/
├── mkdocs.yml
├── requirements.txt
└── scripts/
    └── build.sh
```

Rendered documentation content lives under `docs/` so MkDocs can build the site cleanly. The appendix and assets are also stored under `docs/` for reliable internal links.

## Build

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

## Local Preview

```bash
mkdocs serve
```
