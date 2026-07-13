# Contributing

Follow these rules when adding or changing documentation.

## Writing Style

- Use direct instructional language.
- Assume the reader is building their first PC.
- Keep every step verifiable.
- Avoid unnecessary verbosity.
- Use technically accurate component names.

## Local Environment

- Use Python 3.12 for the local documentation environment.
- Use Node.js 24 if Node-based tooling is added or used locally.
- Use a local Python virtual environment named `.venv`.
- Keep the repository checkout on the local drive, not inside iCloud Drive or another synced folder.
- Prefer `uv venv --python 3.12 .venv` and `uv pip install -r requirements.txt` when `uv` is available.
- Do not install documentation dependencies into the system Python environment.
- Install dependencies with `python -m pip install -r requirements.txt` after activating `.venv`.
- Install Node dependencies with `npm install` before working on the Astro Starlight first slice.

## Documentation Drift

- Update project documentation when new durable information is discovered.
- Keep tooling versions, build assumptions, compatibility notes, workflow decisions, and accepted alternatives in tracked files.
- Do not leave important project knowledge only in chat history.
- Update `docs/project/milestone-05-06-validation-report.md` when validation commands, outcomes, warnings, or blockers change.
- Update `docs/project/verification-register.md` when a technical claim is verified, remains pending, or is deliberately deferred.

## Issue Workflow

- Read `AGENTS.md` and `MILESTONES.md` before starting an issue.
- Use the matching GitHub issue as the work boundary.
- Preserve completed Milestones 1-4 unless the user explicitly changes direction.
- Extend existing chapters, appendices, project pages, scripts, or workflows before creating parallel duplicates.
- Close an issue only after its acceptance criteria and validation notes are satisfied.
- Keep `milestones/` and `MILESTONES.md` current when milestone scope or issue status changes.

## Local-First Milestone Flow

Use local commits for milestone implementation work and push only at deliberate milestone checkpoints.

- Commit locally after each completed issue or coherent issue group.
- Run `./scripts/build.sh html` locally before each local commit.
- Keep GitHub issues open while their commits are local-only.
- Do not close GitHub issues until the relevant commits have been pushed and GitHub Actions has passed.
- Push once per milestone, or at an agreed checkpoint, instead of pushing after every issue.
- Push earlier if a change needs GitHub Pages review, GitHub Actions validation, or remote backup before continuing.
- Keep `docs/project/milestone-05-06-validation-report.md` current while working locally so the eventual push has a complete validation trail.

## Technical Verification

- Prefer official manufacturer documentation for component specifications, connector labels, compatibility, BIOS behavior, and clearance claims.
- Do not invent screenshots, benchmark scores, URLs, connector coordinates, BIOS menu names, or compatibility claims.
- Treat retailer links as convenience links, not authoritative technical evidence.
- Keep product images as visual aids only; model numbers and official documentation remain the source of truth.

## Chapter Structure

Every main chapter must include:

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

- Keep exact component identification and purchase links in `docs/appendix/bill-of-materials.md`.
- Prefer manufacturer product pages for stable references.
- Prefer amazon.co.uk for retailer links.
- Treat retailer links as convenience links because price, stock, and listing details can change.
- Do not scatter retailer links through installation chapters unless there is a specific reason.

## Diagrams and Images

- Use technically accurate diagrams.
- Use SVG for vector diagrams where possible.
- Keep Mermaid and PlantUML source files when diagrams are added.
- Do not use AI-generated artwork for technical diagrams.
- Use the final-build reference image only as a visual target where appropriate.

## Validation

Run local validation before committing documentation changes:

```bash
source .venv/bin/activate
./scripts/validate.sh all
```

Use `./scripts/build.sh html` when you only need to rebuild the MkDocs site. Use `./scripts/validate.sh docs` when you only need the repository structure and local Markdown link checks. Use `./scripts/validate.sh data` when you only need digital twin JSON Schema and cross-reference validation. Use `./scripts/validate.sh qrcodes` after changing official links or QR assets.

QR code SVG assets under `public/assets/qrcodes/` are generated from `data/digital-twin/build.json` by `scripts/generate-qrcodes.py`. Regenerate them with:

```bash
python scripts/generate-qrcodes.py
```

Use this command when validating the Astro Starlight first slice:

```bash
./scripts/validate.sh starlight
```

The Starlight validation target builds the static site and then checks the digital twin source and generated HTML for required interactive sections, accessibility markers, static fallbacks, reduced-motion styling, and QR asset references.

If a change introduces new tooling, document the command and expected result in `docs/project/milestone-05-06-validation-report.md`.

Do not commit generated `site/` output.
