# Custom Gaming PC Build Manual

This repository contains a professional build manual and interactive digital twin for a custom gaming PC based on the hardware specification in `AGENTS.md`.

The documentation is built with Astro Starlight and published to GitHub Pages at <https://t3lstar.github.io/PC-Build/>.

## Project Records

The published manual is the source for reader-facing build, operations, appendix, and digital twin content. Historical milestone plans, project assumptions, verification notes, and acceptance criteria are kept in `MILESTONES.md` and `milestones/`.

## Repository Layout

```text
.
├── AGENTS.md
├── CONTRIBUTING.md
├── MILESTONES.md
├── README.md
├── astro.config.mjs
├── data/
├── milestones/
├── public/
│   └── assets/
├── src/
│   ├── components/
│   ├── content/docs/
│   └── styles/
├── package.json
├── requirements.txt
└── scripts/
```

Starlight documentation source lives under `src/content/docs/`. Public images, diagrams, icons, and generated QR assets live under `public/assets/`. The generated Starlight output is `dist/` and should not be committed.

## Local Environment

Use Node.js 24 for the Starlight toolchain and Python 3.12 for digital twin data and QR validation.

Keep the working copy on the local drive, not inside iCloud Drive or another synced folder. Static-site builds clean and rewrite generated output, and synced storage can make local builds dramatically slower.

Install dependencies:

```bash
npm ci
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

If `uv` is not available, activate `.venv` and use `python -m pip install -r requirements.txt`.

## Build

Build the Starlight HTML site:

```bash
./scripts/build.sh html
```

Build every configured output:

```bash
./scripts/build.sh all
```

The `pdf` target is deferred. The `printable` target currently builds the Starlight site and relies on browser print styles.

## Validation

Run local validation:

```bash
./scripts/validate.sh all
```

This validates digital twin JSON data, generated QR assets, Astro/Starlight type health, Markdown linting, the static Starlight build, local links, clean route expectations, and critical generated assets. The validation script uses `.venv/bin/python` automatically when it exists, unless `PYTHON` is explicitly set.

Useful focused commands:

```bash
npm run check
npm run check:astro
npm run lint:markdown
./scripts/validate.sh starlight
./scripts/validate.sh data
./scripts/validate.sh qrcodes
```

Regenerate official-link QR code assets after changing official links:

```bash
python scripts/generate-qrcodes.py
./scripts/validate.sh qrcodes
```

## Local Preview

```bash
npm run starlight:dev -- --host 127.0.0.1 --port 4321
```

## Public Sections

- Build Guide: first build and Windows setup.
- Operations: monitoring, maintenance, software, drivers, backups, security, troubleshooting, benchmarking, and upgrade planning.
- Appendix: reference material, checklists, bill of materials, drivers, BIOS settings, and publishing notes.
- Digital Twin: interactive data-backed build reference.

## Project Planning

- Milestone tracker: `MILESTONES.md`
- Detailed milestone plans: `milestones/`
- Technical verification register: `milestones/verification-register.md`
- Starlight source inventory: `milestones/starlight-migration-inventory.md`
- Digital twin architecture decision: `milestones/adr-0001-digital-twin-architecture.md`

Project planning records are repository-only unless they directly help readers build the PC.

Milestone implementation uses a local-first flow: commit locally per issue or issue group, validate locally, and push at agreed milestone checkpoints. GitHub issues are closed only after the relevant commits are pushed and GitHub Actions passes.

## Contribution Workflow

1. Read `AGENTS.md` and `MILESTONES.md` before making changes.
2. Work from the relevant GitHub issue or milestone plan.
3. Update project documentation in the same change when new durable information is discovered.
4. Keep technical claims source-backed or record unresolved items in `milestones/verification-register.md`.
5. Run `./scripts/validate.sh all` before publishing documentation changes.

## License

This documentation is published under the MIT License. See `LICENSE`.
