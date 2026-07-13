#!/usr/bin/env python3
"""Generate and validate QR code SVG assets for official digital twin links."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import qrcode
import qrcode.image.svg


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "digital-twin" / "build.json"
OUTPUT_DIR = ROOT / "public" / "assets" / "qrcodes"
MANIFEST_PATH = OUTPUT_DIR / "manifest.json"
OFFICIAL_KINDS = {"manufacturer", "support", "operating-system", "manual"}


def load_build_data() -> dict[str, object]:
    with DATA_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def official_links() -> list[dict[str, str]]:
    data = load_build_data()
    links = data.get("links", [])
    if not isinstance(links, list):
        return []

    official: list[dict[str, str]] = []
    for link in links:
        if not isinstance(link, dict) or link.get("kind") not in OFFICIAL_KINDS:
            continue
        official.append(
            {
                "id": str(link["id"]),
                "label": str(link["label"]),
                "url": str(link["url"]),
                "kind": str(link["kind"]),
                "file": f"{link['id']}.svg",
            }
        )
    return sorted(official, key=lambda item: item["id"])


def expected_manifest() -> dict[str, object]:
    return {
        "source": str(DATA_PATH.relative_to(ROOT)),
        "outputDir": str(OUTPUT_DIR.relative_to(ROOT)),
        "links": official_links(),
    }


def generate_svg(link: dict[str, str]) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(link["url"])
    qr.make(fit=True)
    image = qr.make_image(image_factory=qrcode.image.svg.SvgPathImage)
    image.save(OUTPUT_DIR / link["file"])


def write_manifest(manifest: dict[str, object]) -> None:
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def generate() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = expected_manifest()
    for link in manifest["links"]:
        generate_svg(link)
    write_manifest(manifest)


def check() -> list[str]:
    errors: list[str] = []
    expected = expected_manifest()

    if not MANIFEST_PATH.exists():
        errors.append(f"Missing QR manifest: {MANIFEST_PATH.relative_to(ROOT)}")
        return errors

    actual = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if actual != expected:
        errors.append("QR manifest is stale. Run scripts/generate-qrcodes.py.")

    for link in expected["links"]:
        output = OUTPUT_DIR / link["file"]
        if not output.exists():
            errors.append(f"Missing QR SVG: {output.relative_to(ROOT)}")
        elif "<svg" not in output.read_text(encoding="utf-8", errors="ignore"):
            errors.append(f"QR SVG does not look like SVG: {output.relative_to(ROOT)}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate committed QR assets without rewriting them.")
    args = parser.parse_args()

    if args.check:
        errors = check()
        if errors:
            print("QR code validation failed:", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 1
        print("QR code validation passed.")
        return 0

    generate()
    print(f"Generated {len(official_links())} QR code SVG assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
