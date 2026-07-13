#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  cat <<'USAGE'
Usage: ./scripts/build.sh <target>

Targets:
  html       Build the Astro Starlight HTML site.
  pdf        Deferred; PDF generation is not part of the current release.
  printable  Build the Astro Starlight HTML site; browser print styles are used for printing.
  all        Build the Astro Starlight HTML site.
USAGE
}

build_html() {
  cd "$ROOT_DIR"
  npm run starlight:build
}

build_pdf() {
  cd "$ROOT_DIR"
  echo "PDF generation is deferred. Use ./scripts/build.sh html or ./scripts/build.sh printable for the current release."
}

build_printable() {
  cd "$ROOT_DIR"
  npm run starlight:build
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
