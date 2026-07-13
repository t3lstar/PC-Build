#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

npm run starlight:build

if [ ! -d site ]; then
  echo "MkDocs site output is missing. Run ./scripts/build.sh html before merging the digital twin." >&2
  exit 1
fi

rm -rf site/digital-twin site/_astro site/pagefind site/assets/qrcodes

cp -R dist/digital-twin site/digital-twin
cp -R dist/_astro site/_astro

if [ -d dist/pagefind ]; then
  cp -R dist/pagefind site/pagefind
fi

mkdir -p site/assets
cp -R dist/assets/qrcodes site/assets/qrcodes

echo "Merged Starlight digital twin into MkDocs site artifact."
