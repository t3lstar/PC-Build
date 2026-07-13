# Milestone 5 Final QA

Status: Published QA complete. Last verified: 2026-07-13 15:27 BST.

## Purpose

Summarise the local Milestone 5 release state before pushing the local checkpoint to GitHub.

## Release State

Milestone 5 implementation is pushed, GitHub Actions has passed, and the live GitHub Pages site has been verified.

## Local Commit Range

The milestone checkpoint was pushed to `main` and published through GitHub Pages.

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
| GitHub Actions run `29257976974` | Passed. Build job completed in 14 seconds; deploy job completed in 11 seconds. |
| Live home page | HTTP 200 at `https://t3lstar.github.io/PC-Build/`. |
| Live final QA page | HTTP 200 at `https://t3lstar.github.io/PC-Build/project/milestone-05-final-qa/`. |
| Live connector appendix | HTTP 200 at `https://t3lstar.github.io/PC-Build/appendix/connectors-cables/`. |
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
| `#10` | Published | Ready to close |
| `#11` | Published | Ready to close |
| `#12` | Published | Ready to close |
| `#13` | Published | Ready to close |
| `#14` | Complete and pushed | Closed |
| `#15` | Published | Ready to close |
| `#16` | Published with PDF deferred | Ready to close |
| `#17` | Published | Ready to close |
| `#18` | Published | Ready to close |

## Remaining Release Actions

1. Close issues `#10`, `#11`, `#12`, `#13`, `#15`, `#16`, `#17`, and `#18`.
2. Mark the GitHub Milestone 5 milestone complete after issue closure.

## Known Warnings

- MkDocs Material prints its upstream MkDocs 2.0 warning during builds.
- PDF generation is deferred and intentionally not part of this release.
- Exact connector coordinates remain deferred to future digital twin verification.
- Real benchmark values remain pending until the physical PC is assembled and tested.
