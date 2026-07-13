#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-all}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  cat <<'USAGE'
Usage: ./scripts/validate.sh <target>

Targets:
  data  Validate digital twin JSON data against JSON Schema.
  docs  Validate required files, MkDocs nav targets, and local Markdown links.
  html  Build the MkDocs HTML site with strict mode.
  starlight  Build the Astro Starlight first slice.
  all   Run data validation, docs validation, and the HTML build.
USAGE
}

validate_data() {
  cd "$ROOT_DIR"
  "${PYTHON:-python3}" scripts/validate-data.py
}

validate_docs() {
  cd "$ROOT_DIR"
  "${PYTHON:-python3}" scripts/validate-docs.py
}

validate_html() {
  cd "$ROOT_DIR"
  ./scripts/build.sh html
}

validate_starlight() {
  cd "$ROOT_DIR"
  npm run starlight:build
}

case "$TARGET" in
  data)
    validate_data
    ;;
  docs)
    validate_docs
    ;;
  html)
    validate_html
    ;;
  starlight)
    validate_starlight
    ;;
  all)
    validate_data
    validate_docs
    validate_html
    ;;
  *)
    usage
    exit 1
    ;;
esac
