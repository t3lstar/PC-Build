---
title: "Publishing"
---

## Purpose

Document how the public GitHub Pages site is built and deployed.

## Publication Model

- Repository owner: `t3lstar`.
- Repository: `PC-Build`.
- Public site URL: `https://t3lstar.github.io/PC-Build/`.
- Pull requests validate and build the Starlight site, but do not deploy it.
- Pushes to `main` validate, build, and deploy the Starlight site to GitHub Pages.
- The deployment workflow adds `.nojekyll` to the published output.

## Local Build

Use the single parameterized build script:

```bash
./scripts/build.sh html
```

Supported targets:

```bash
./scripts/build.sh html
./scripts/build.sh pdf
./scripts/build.sh printable
./scripts/build.sh all
```

The `pdf` target is deferred by project decision. The `printable` target builds the Starlight site and relies on browser print styles.

## Environment Expectations

| Tool               | Target                                      |
| ------------------ | ------------------------------------------- |
| Node.js            | 24                                          |
| Python             | 3.12                                        |
| Python environment | Local `.venv`                               |
| Starlight output   | `dist/`                                     |
| Published route    | `https://t3lstar.github.io/PC-Build/`       |
| Digital twin route | `/digital-twin/first-slice/`                |
| Public assets      | `public/assets/` copied into `dist/assets/` |

`dist/`, `site/`, and `build/` are generated outputs and should not be committed.

## GitHub Actions Flow

1. Pull request or push to `main` starts the workflow.
2. GitHub Actions checks out the repository.
3. Python 3.12 dependencies are installed from `requirements.txt`.
4. Node.js 24 dependencies are installed from `package-lock.json`.
5. `./scripts/validate.sh all` validates data, QR assets, Markdown, Astro/Starlight types, static output, routes, links, and critical assets.
6. `.nojekyll` is added to `dist/`.
7. Pull request workflow stops after validation.
8. Push to `main` uploads `dist/` as the GitHub Pages artifact.
9. GitHub Pages serves the deployed site at the public URL.

## Verification

- Local `./scripts/validate.sh all` succeeds.
- Local `./scripts/build.sh html` succeeds.
- GitHub Actions validation succeeds.
- The deployed site returns HTTP 200.
- The deployed digital twin returns HTTP 200 at `https://t3lstar.github.io/PC-Build/digital-twin/first-slice/`.
- Navigation includes all chapter and appendix pages.
- `.nojekyll` is included in the deployed output.
