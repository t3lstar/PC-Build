# Publishing

Status: Published HTML content. Last verified: 2026-07-13 16:54 BST.

## Purpose

Document how the public GitHub Pages site is built and deployed.

## Publication Model

- Repository owner: `t3lstar`.
- Repository: `PC-Build`.
- Public site URL: `https://t3lstar.github.io/PC-Build/`.
- Pull requests build the MkDocs site, build the Starlight digital twin slice, merge the digital twin into the site artifact, and do not deploy it.
- Pushes to `main` build the same combined artifact and deploy it to GitHub Pages.
- The deployment workflow adds `.nojekyll` to the published output.

## Local Build

Use the local Python virtual environment and the single parameterized build script:

```bash
. .venv/bin/activate
./scripts/build.sh html
```

Supported targets:

```bash
./scripts/build.sh html
./scripts/build.sh pdf
./scripts/build.sh printable
./scripts/build.sh all
```

## Environment Expectations

| Tool | Target |
| --- | --- |
| Python | 3.12 |
| Node.js | 24 |
| Python environment | Local `.venv` |
| MkDocs output | `site/` |
| Starlight output | `dist/` |
| Published digital twin route | `site/digital-twin/first-slice/` |
| Printable HTML output | `build/printable/` |

Do not install MkDocs dependencies into system Python.

`site/`, `dist/`, and `build/` are generated outputs and should not be committed. GitHub Pages publishes the combined HTML site from `site/`; printable output is a local release artifact unless a future workflow publishes it deliberately.

The printable target builds the same documentation into `build/printable/` using the tracked print CSS in `docs/assets/stylesheets/theme.css`.

PDF generation is deferred by project decision. The script keeps the `pdf` target so the command surface remains stable, but it prints a deferred message instead of generating a PDF.

## GitHub Actions Flow

1. Pull request opened or updated.
2. GitHub Actions checks out the repository.
3. Python dependencies are installed from `requirements.txt`.
4. Node dependencies are installed from `package-lock.json`.
5. MkDocs builds the manual into `site/`.
6. Starlight builds the digital twin into `dist/`.
7. `./scripts/build-digital-twin-site.sh` merges `dist/digital-twin/`, `dist/_astro/`, `dist/pagefind/`, and QR assets into `site/`.
8. Pull request workflow stops after validation.
9. Push to `main` repeats the build.
10. Deployment workflow uploads the built site as a Pages artifact.
11. GitHub Pages serves the result at the public URL.

## Verification

- Local `./scripts/build.sh html` succeeds.
- Local `./scripts/build.sh printable` succeeds.
- Local `./scripts/build.sh all` succeeds.
- GitHub Actions build succeeds.
- The deployed site returns HTTP 200.
- The deployed digital twin returns HTTP 200 at `https://t3lstar.github.io/PC-Build/digital-twin/first-slice/`.
- Navigation includes all chapter and appendix pages.
- `.nojekyll` is included in the deployed output.
