#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  cat <<'USAGE'
Usage: ./scripts/build.sh <target>

Targets:
  html       Build the MkDocs HTML site.
  pdf        Deferred; PDF generation is not part of the current GitHub Pages release.
  printable  Deferred; printable manual generation is not part of the current GitHub Pages release.
  all        Build the GitHub Pages HTML site.
USAGE
}

build_html() {
  cd "$ROOT_DIR"
  mkdocs build --strict
}

build_pdf() {
  cd "$ROOT_DIR"
  echo "PDF generation is deferred. Use ./scripts/build.sh html for the current GitHub Pages site."
}

build_printable() {
  cd "$ROOT_DIR"
  echo "Printable manual generation is deferred. Use ./scripts/build.sh html for the current GitHub Pages site."
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
    ;;
  *)
    usage
    exit 1
    ;;
esac
