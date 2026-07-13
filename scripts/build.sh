#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  cat <<'USAGE'
Usage: ./scripts/build.sh <target>

Targets:
  html       Build the MkDocs HTML site.
  pdf        Deferred; PDF generation is not part of the current release.
  printable  Build printable HTML into build/printable/.
  all        Build HTML and printable outputs.
USAGE
}

build_html() {
  cd "$ROOT_DIR"
  mkdocs build --strict
}

build_pdf() {
  cd "$ROOT_DIR"
  echo "PDF generation is deferred. Use ./scripts/build.sh html or ./scripts/build.sh printable for the current release."
}

build_printable() {
  cd "$ROOT_DIR"
  mkdocs build --strict --site-dir build/printable
}

case "$TARGET" in
  html)
    build_html
    ;;
  pdf)
    build_pdf
    ;;
  printable)
    build_printable
    ;;
  all)
    build_html
    build_printable
    ;;
  *)
    usage
    exit 1
    ;;
esac
