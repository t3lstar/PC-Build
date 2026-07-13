# Milestone 5 Final QA

Status: Local QA complete pending checkpoint push. Last verified: 2026-07-13 15:24 BST.

## Purpose

Summarise the local Milestone 5 release state before pushing the local checkpoint to GitHub.

## Release State

Milestone 5 implementation is complete locally. The GitHub issues remain open for local-first workflow reasons and should be closed only after the local commits are pushed and GitHub Actions passes.

## Local Commit Range

The local branch is ahead of `origin/main` by eight commits:

| Commit | Summary |
| --- | --- |
| `62f685a` | Document local-first milestone workflow |
| `5b366ba` | Complete monitoring and optimisation guide |
| `12722c8` | Complete maintenance schedules and logs |
| `ec1eae8` | Establish benchmark baseline methodology |
| `68362e3` | Add documentation validation scripts |
| `0f85d91` | Improve site and print styling |
| `3853828` | Make printable builds reproducible |
| `45fe4b9` | Expand connector and cable references |

## Local Validation

| Check | Result |
| --- | --- |
| `./scripts/validate.sh all` | Passed. Documentation validation passed; MkDocs HTML build passed. |
| `./scripts/build.sh all` | Passed. HTML and printable outputs built successfully. |
| Generated output policy | `site/` and `build/` are ignored and should not be committed. |
| PDF generation | Deferred by project decision; `./scripts/build.sh pdf` reports the deferral. |
| Active checkout | `/Users/simondawson/Herd/PC-Build`. |
| Old iCloud checkout | Removed. |

## GitHub Issue State Before Push

| Issue | Local state | GitHub state |
| --- | --- | --- |
| `#5` | Complete and pushed | Closed |
| `#6` | Complete and pushed | Closed |
| `#7` | Complete and pushed | Closed |
| `#8` | Complete and pushed | Closed |
| `#9` | Complete and pushed | Closed |
| `#10` | Complete locally | Open |
| `#11` | Complete locally | Open |
| `#12` | Complete locally | Open |
| `#13` | Complete locally | Open |
| `#14` | Complete and pushed | Closed |
| `#15` | Complete locally | Open |
| `#16` | Complete locally with PDF deferred | Open |
| `#17` | Complete locally | Open |
| `#18` | Complete locally after this QA page | Open |

## Remaining Release Actions

1. Push the local commits when the milestone checkpoint is approved.
2. Wait for GitHub Actions to pass.
3. Verify the live GitHub Pages site.
4. Close issues `#10`, `#11`, `#12`, `#13`, `#15`, `#16`, `#17`, and `#18`.
5. Mark the GitHub Milestone 5 milestone complete.

## Known Warnings

- MkDocs Material prints its upstream MkDocs 2.0 warning during builds.
- PDF generation is deferred and intentionally not part of this release.
- Exact connector coordinates remain deferred to future digital twin verification.
- Real benchmark values remain pending until the physical PC is assembled and tested.
