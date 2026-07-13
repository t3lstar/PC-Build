# Contributing

Follow these rules when adding or changing documentation.

## Writing Style

- Use direct instructional language.
- Assume the reader is building their first PC.
- Keep every step verifiable.
- Avoid unnecessary verbosity.
- Use technically accurate component names.

## Local Environment

- Use Node.js 24 for Astro Starlight.
- Use Python 3.12 for digital twin data and QR validation.
- Use a local Python virtual environment named `.venv`.
- Keep the repository checkout on the local drive, not inside iCloud Drive or another synced folder.
- Install Node dependencies with `npm ci`.
- Prefer `uv venv --python 3.12 .venv` and `uv pip install -r requirements.txt` when `uv` is available.
- Do not install Python dependencies into the system Python environment.

## Documentation Drift

- Update project documentation when new durable information is discovered.
- Keep tooling versions, build assumptions, compatibility notes, workflow decisions, and accepted alternatives in tracked files.
- Do not leave important project knowledge only in chat history.
- Update `milestones/starlight-migration-inventory.md` when Starlight source layout, route, asset, or validation coverage changes.
- Update `milestones/verification-register.md` when a technical claim is verified, remains pending, or is deliberately deferred.

## Issue Workflow

- Read `AGENTS.md` and `MILESTONES.md` before starting an issue.
- Use the matching GitHub issue as the work boundary.
- Preserve completed milestones unless the user explicitly changes direction.
- Extend existing chapters, appendices, project pages, scripts, or workflows before creating parallel duplicates.
- Close an issue only after its acceptance criteria and validation notes are satisfied.
- Keep `milestones/` and `MILESTONES.md` current when milestone scope or issue status changes.

## Local-First Milestone Flow

Use local commits for milestone implementation work and push only at deliberate milestone checkpoints.

- Commit locally after each completed issue or coherent issue group.
- Run `./scripts/validate.sh all` locally before each milestone checkpoint push.
- Keep GitHub issues open while their commits are local-only.
- Do not close GitHub issues until the relevant commits have been pushed and GitHub Actions has passed.
- Push once per milestone, or at an agreed checkpoint, instead of pushing after every issue.
- Push earlier if a change needs GitHub Pages review, GitHub Actions validation, or remote backup before continuing.

## Technical Verification

- Prefer official manufacturer documentation for component specifications, connector labels, compatibility, BIOS behavior, and clearance claims.
- Do not invent screenshots, benchmark scores, URLs, connector coordinates, BIOS menu names, or compatibility claims.
- Treat retailer links as convenience links, not authoritative technical evidence.
- Keep product images as visual aids only; model numbers and official documentation remain the source of truth.

## Chapter Structure

Every main chapter should include:

- Introduction
- Purpose
- Estimated time
- Difficulty
- Required tools
- Warnings
- Step-by-step instructions
- Verification checklist
- Common mistakes
- Expected result
- Next chapter

## Buying Links

- Keep exact component identification and purchase links in `src/content/docs/appendix/bill-of-materials.md`.
- Prefer manufacturer product pages for stable references.
- Prefer amazon.co.uk for retailer links.
- Treat retailer links as convenience links because price, stock, and listing details can change.
- Do not scatter retailer links through installation chapters unless there is a specific reason.

## Diagrams and Images

- Use technically accurate diagrams.
- Use SVG for vector diagrams where possible.
- Keep Mermaid and PlantUML source files when diagrams are added.
- Store reader-facing assets under `public/assets/`.
- Do not use AI-generated artwork for technical diagrams.
- Use the final-build reference image only as a visual target where appropriate.

## Validation

Run local validation before committing documentation changes:

```bash
npm ci
source .venv/bin/activate
./scripts/validate.sh all
```

The `all` target validates digital twin data, QR assets, Astro/Starlight type health, Markdown linting, static site generation, local links, clean route expectations, and critical generated assets.

Useful focused commands:

```bash
npm run check
npm run check:astro
npm run lint:markdown
./scripts/validate.sh starlight
./scripts/validate.sh data
./scripts/validate.sh qrcodes
```

QR code SVG assets under `public/assets/qrcodes/` are generated from `data/digital-twin/build.json` by `scripts/generate-qrcodes.py`. Regenerate them with:

```bash
python scripts/generate-qrcodes.py
```

Do not commit generated `dist/`, `dist/`, or `build/` output.
