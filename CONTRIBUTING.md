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
- Do not install documentation dependencies into the system Python environment.
- Install dependencies with `python -m pip install -r requirements.txt` after activating `.venv`.

## Documentation Drift

- Update project documentation when new durable information is discovered.
- Keep tooling versions, build assumptions, compatibility notes, workflow decisions, and accepted alternatives in tracked files.
- Do not leave important project knowledge only in chat history.

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
