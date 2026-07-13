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
  html       Build the Astro Starlight HTML site.
  starlight  Check, lint, build, and validate the Astro Starlight site.
  all        Run data validation, QR validation, and Starlight validation.
USAGE
}

validate_data() {
  cd "$ROOT_DIR"
  "${PYTHON:-python3}" scripts/validate-data.py
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
  npm run check
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
  html)
    validate_html
    ;;
  starlight)
    validate_starlight
    ;;
  all)
    validate_data
    validate_qrcodes
    validate_starlight
    ;;
  *)
    usage
    exit 1
    ;;
esac
