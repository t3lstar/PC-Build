#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-all}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  cat <<'USAGE'
Usage: ./scripts/validate.sh <target>

Targets:
  data  Validate digital twin JSON data against JSON Schema.
  qrcodes  Validate generated official-link QR code assets.
  docs  Validate required files, MkDocs nav targets, and local Markdown links.
  html  Build the MkDocs HTML site with strict mode.
  starlight  Build and validate the Astro Starlight digital twin.
  all   Run data validation, QR validation, docs validation, and the HTML build.
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

validate_qrcodes() {
  cd "$ROOT_DIR"
  "${PYTHON:-python3}" scripts/generate-qrcodes.py --check
}

validate_html() {
  cd "$ROOT_DIR"
  ./scripts/build.sh html
}

validate_starlight() {
  cd "$ROOT_DIR"
  npm run starlight:build
  "${PYTHON:-python3}" scripts/validate-starlight.py
}

case "$TARGET" in
  data)
    validate_data
    ;;
  qrcodes)
    validate_qrcodes
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
    validate_qrcodes
    validate_docs
    validate_html
    ;;
  *)
    usage
    exit 1
    ;;
esac
