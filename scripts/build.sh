#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  cat <<'USAGE'
Usage: ./scripts/build.sh <target>

Targets:
  html       Build the MkDocs HTML site.
  pdf        Build the PDF output when PDF tooling is configured.
  printable  Build the printable manual output when print tooling is configured.
  all        Run html, pdf, and printable targets.
USAGE
}

build_html() {
  cd "$ROOT_DIR"
  mkdocs build --strict
}

build_pdf() {
  cd "$ROOT_DIR"
  echo "PDF generation is reserved for Milestone 4 polish."
  echo "The HTML documentation is the source build target for Milestone 1."
}

build_printable() {
  cd "$ROOT_DIR"
  echo "Printable manual generation is reserved for Milestone 4 polish."
  echo "The HTML documentation is the source build target for Milestone 1."
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
    build_pdf
    build_printable
    ;;
  *)
    usage
    exit 1
    ;;
esac

