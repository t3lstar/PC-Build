#!/usr/bin/env python3
"""Validate the Starlight digital twin source and built static HTML."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIRST_SLICE = ROOT / "src" / "content" / "docs" / "digital-twin" / "first-slice.mdx"
CSS = ROOT / "src" / "styles" / "starlight.css"
COMPONENT_DIR = ROOT / "src" / "components"
DIST_FIRST_SLICE = ROOT / "dist" / "digital-twin" / "first-slice" / "index.html"
DIST_ACCESSIBILITY = ROOT / "dist" / "project" / "digital-twin-accessibility" / "index.html"

COMPONENTS = {
    "DigitalTwinSummary": "Digital Twin Data Slice",
    "DigitalTwinCaseView": "Static Zone List",
    "DigitalTwinConnectorMap": "Static Connector List",
    "DigitalTwinCableRouting": "Static Cable Route List",
    "DigitalTwinBuildSequence": "Static Build Sequence",
    "DigitalTwinAirflow": "Static Airflow List",
    "DigitalTwinExplodedView": "Static Assembly Layers",
    "DigitalTwinBiosSimulator": "Static BIOS Training Flow",
    "DigitalTwinDriverDashboard": "Static Driver Source List",
    "DigitalTwinQrCodes": "Static QR Link List",
    "DigitalTwinMaintenanceHistory": "Printable History Template",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def validate_source(errors: list[str]) -> None:
    page = read(FIRST_SLICE)
    css = read(CSS)

    require(errors, "<noscript>" in page, "Digital twin page is missing a no-JavaScript notice.")
    require(errors, "## Static Fallback" in page, "Digital twin page is missing the Static Fallback section.")

    for component, fallback in COMPONENTS.items():
        component_path = COMPONENT_DIR / f"{component}.astro"
        require(errors, component_path.exists(), f"Missing component {component_path.relative_to(ROOT)}.")
        require(errors, f"import {component}" in page, f"Digital twin page does not import {component}.")
        require(errors, f"<{component}" in page, f"Digital twin page does not render {component}.")

        source = read(component_path)
        require(errors, "aria-labelledby" in source or "aria-label" in source, f"{component} lacks an accessible label.")
        if component != "DigitalTwinSummary":
            require(errors, fallback in source, f"{component} lacks expected fallback '{fallback}'.")

    require(errors, ":focus-visible" in css, "Starlight CSS lacks visible focus styles.")
    require(errors, "prefers-reduced-motion" in css, "Starlight CSS lacks reduced-motion handling.")


def validate_dist(errors: list[str]) -> None:
    require(errors, DIST_FIRST_SLICE.exists(), "Starlight first-slice HTML has not been built.")
    require(errors, DIST_ACCESSIBILITY.exists(), "Starlight accessibility audit HTML has not been built.")
    if not DIST_FIRST_SLICE.exists() or not DIST_ACCESSIBILITY.exists():
        return

    first_slice = read(DIST_FIRST_SLICE)
    accessibility = read(DIST_ACCESSIBILITY)

    for expected in [
        "Interactive Case View",
        "Motherboard Connector Map",
        "Cable-Routing Mode",
        "Guided Build Sequence",
        "Airflow Visualisation",
        "Exploded Assembly View",
        "Educational BIOS Simulator",
        "Driver and Firmware Source Dashboard",
        "Official-Link QR Codes",
        "Maintenance and Upgrade History",
        "JavaScript is disabled",
        "aria-live",
        "aria-pressed",
    ]:
        require(errors, expected in first_slice, f"Built first-slice HTML missing '{expected}'.")

    for expected in ["Digital Twin Accessibility", "Static Fallback Inventory", "Keyboard operation", "No-JavaScript behavior"]:
        require(errors, expected in accessibility, f"Built accessibility audit HTML missing '{expected}'.")

    require(errors, first_slice.count("/PC-Build/assets/qrcodes/") >= 13, "Built first-slice HTML does not reference all QR assets.")


def main() -> int:
    errors: list[str] = []
    validate_source(errors)
    validate_dist(errors)

    if errors:
        print("Starlight digital twin validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Starlight digital twin validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
