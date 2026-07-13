#!/usr/bin/env python3
"""Validate the full Astro Starlight site source and built static HTML."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "src" / "content" / "docs"
CSS = ROOT / "src" / "styles" / "starlight.css"
LIGHTBOX = ROOT / "public" / "assets" / "scripts" / "image-lightbox.js"
COMPONENT_DIR = ROOT / "src" / "components"
DIST = ROOT / "dist"
DIST_FIRST_SLICE = DIST / "digital-twin" / "first-slice" / "index.html"
OLD_CONFIG = ROOT / ("mk" + "docs.yml")
FORBIDDEN_TERM = "mk" + "docs"

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
ASSET_RE = re.compile(r"""(?:href|src)=["'](/PC-Build/[^"']+)["']""")

IGNORED_SCHEMES = {"http", "https", "mailto", "tel"}

EXPECTED_ROUTES = [
    "index.html",
    "build-guide/introduction/index.html",
    "build-guide/components/index.html",
    "build-guide/motherboard-overview/index.html",
    "build-guide/case-overview/index.html",
    "build-guide/tools/index.html",
    "build-guide/build-preparation/index.html",
    "build-guide/cpu-installation/index.html",
    "build-guide/memory-installation/index.html",
    "build-guide/m2-installation/index.html",
    "build-guide/case-build/index.html",
    "build-guide/psu-installation/index.html",
    "build-guide/motherboard-installation/index.html",
    "build-guide/aio-installation/index.html",
    "build-guide/gpu-installation/index.html",
    "build-guide/cable-routing/index.html",
    "build-guide/front-panel-connectors/index.html",
    "build-guide/first-boot/index.html",
    "build-guide/bios/index.html",
    "build-guide/expo/index.html",
    "build-guide/driver-installation/index.html",
    "build-guide/windows-installation/index.html",
    "build-guide/gaming-optimisation/index.html",
    "operations/overview/index.html",
    "operations/recommended-software/index.html",
    "operations/software-to-avoid/index.html",
    "operations/driver-strategy/index.html",
    "operations/monitoring/index.html",
    "operations/fancontrol/index.html",
    "operations/benchmark-baseline/index.html",
    "operations/maintenance-schedule/index.html",
    "operations/backup-recovery/index.html",
    "operations/security/index.html",
    "operations/troubleshooting/index.html",
    "operations/upgrade-planning/index.html",
    "appendix/glossary/index.html",
    "appendix/faq/index.html",
    "appendix/checklists/index.html",
    "appendix/connectors-cables/index.html",
    "appendix/bill-of-materials/index.html",
    "appendix/drivers/index.html",
    "appendix/bios-settings/index.html",
    "appendix/temperature-reference/index.html",
    "appendix/publishing/index.html",
    "digital-twin/first-slice/index.html",
]

REMOVED_OLD_ROUTES = [
    "01-introduction/index.html",
    "02-components/index.html",
    "03-motherboard-overview/index.html",
    "04-case-overview/index.html",
    "components/index.html",
    "case-overview/index.html",
    "project/adr-0001-digital-twin-architecture/index.html",
    "adr/0001-digital-twin-architecture/index.html",
    "project/verification-register/index.html",
    "project/starlight-migration-inventory/index.html",
    "build-guide/benchmarks/index.html",
    "build-guide/troubleshooting/index.html",
    "build-guide/maintenance/index.html",
    "build-guide/upgrades/index.html",
]

RECOMMENDED_SOFTWARE = [
    "HWiNFO64",
    "AMD Software: Adrenalin Edition",
    "Samsung Magician",
    "FanControl by Rem0o",
    "OCCT",
    "Cinebench 2024",
    "CrystalDiskMark",
    "MemTest86",
    "3DMark",
    "Everything Search",
    "Microsoft PowerToys",
    "Playnite",
    "7-Zip",
    "MSI Afterburner",
    "LibreHardwareMonitor",
    "Display Driver Uninstaller",
]

COMPONENTS = {
    "DigitalTwinSummary": "Digital Twin Data Slice",
    "DigitalTwinComponentInspector": "Static Component Inspector List",
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


def markdown_files() -> list[Path]:
    return sorted(path for path in CONTENT.rglob("*") if path.suffix in {".md", ".mdx"})


def strip_code_fences(markdown: str) -> str:
    return re.sub(r"```.*?```", "", markdown, flags=re.DOTALL)


def clean_target(raw_target: str) -> str:
    target = raw_target.strip()
    if " " in target and not target.startswith("<"):
        target = target.split()[0]
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target


def route_exists(target: str) -> bool:
    path = unquote(urlsplit(target).path)
    if not path.startswith("/PC-Build/"):
        return True

    relative = path.removeprefix("/PC-Build/").strip("/")
    if not relative:
        return (DIST / "index.html").exists()

    candidate = DIST / relative
    if candidate.is_file():
        return True
    return (candidate / "index.html").exists()


def local_source_exists(source: Path, target: str) -> bool:
    target = clean_target(target)
    parsed = urlsplit(target)
    if parsed.scheme in IGNORED_SCHEMES or target.startswith("#"):
        return True
    if parsed.scheme:
        return True

    path_part = unquote(parsed.path)
    if not path_part:
        return True
    if path_part.startswith("/PC-Build/"):
        return route_exists(path_part)

    candidate = (source.parent / path_part).resolve()
    return candidate.exists()


def validate_source(errors: list[str]) -> None:
    files = markdown_files()
    require(errors, len(files) == 45, f"Expected 45 Starlight content pages, found {len(files)}.")
    require(errors, not OLD_CONFIG.exists(), "Old site-generator config should be removed after Starlight migration.")
    require(errors, not (ROOT / "docs").exists(), "Old documentation source directory should be removed after Starlight migration.")

    page = read(CONTENT / "digital-twin" / "first-slice.mdx")
    css = read(CSS)
    lightbox = read(LIGHTBOX) if LIGHTBOX.exists() else ""

    require(errors, "<noscript>" in page, "Digital twin page is missing a no-JavaScript notice.")
    require(errors, "## Static Fallback" in page, "Digital twin page is missing the Static Fallback section.")
    require(errors, LIGHTBOX.exists(), "Image lightbox script is missing.")
    require(errors, "pc-image-lightbox" in lightbox, "Image lightbox script lacks expected lightbox markup.")

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
    require(errors, ".pc-image-lightbox" in css, "Starlight CSS lacks image lightbox styling.")

    recommended = read(CONTENT / "operations" / "recommended-software.md")
    for package in RECOMMENDED_SOFTWARE:
        require(errors, package in recommended, f"Recommended software page missing {package}.")
    for required in [
        "Official source",
        "Installation guidance",
        "Safe configuration",
        "Recommended settings",
        "Use cadence",
        "Permanently installed",
        "Resource usage",
        "Potential alternatives",
        "Update guidance",
        "Removal guidance",
    ]:
        require(errors, required in recommended, f"Recommended software page missing column or section '{required}'.")

    for markdown_file in files:
        raw_text = read(markdown_file)
        require(
            errors,
            FORBIDDEN_TERM not in raw_text.lower(),
            f"{markdown_file.relative_to(ROOT)} contains an old site-generator reference.",
        )
        text = strip_code_fences(raw_text)
        for regex in (LINK_RE, IMAGE_RE):
            for match in regex.finditer(text):
                target = clean_target(match.group(1))
                parsed = urlsplit(target)
                if parsed.scheme in IGNORED_SCHEMES or target.startswith("#"):
                    continue
                require(
                    errors,
                    local_source_exists(markdown_file, target),
                    f"{markdown_file.relative_to(ROOT)} has missing local target: {target}",
                )


def validate_dist(errors: list[str]) -> None:
    require(errors, DIST.exists(), "Starlight dist output has not been built.")
    if not DIST.exists():
        return

    for route in EXPECTED_ROUTES:
        require(errors, (DIST / route).exists(), f"Built Starlight output missing route {route}.")

    for route in REMOVED_OLD_ROUTES:
        require(errors, not (DIST / route).exists(), f"Old route should not exist after clean migration: {route}.")

    require(errors, DIST_FIRST_SLICE.exists(), "Starlight first-slice HTML has not been built.")
    if not DIST_FIRST_SLICE.exists():
        return

    first_slice = read(DIST_FIRST_SLICE)
    home = read(DIST / "index.html") if (DIST / "index.html").exists() else ""

    for expected in [
        "Interactive Case View",
        "Component Inspector",
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

    require(errors, first_slice.count("/PC-Build/assets/qrcodes/") >= 13, "Built first-slice HTML does not reference all QR assets.")
    require(
        errors,
        "/PC-Build/assets/scripts/image-lightbox.js" in home,
        "Built Starlight output does not include the image lightbox script.",
    )

    checked_assets = set()
    for html_file in DIST.rglob("*.html"):
        html = read(html_file)
        for match in ASSET_RE.finditer(html):
            target = urlsplit(match.group(1)).path.removeprefix("/PC-Build/")
            if not target or target in checked_assets:
                continue
            checked_assets.add(target)
            candidate = DIST / target
            if candidate.suffix:
                require(errors, candidate.exists(), f"{html_file.relative_to(DIST)} references missing asset /PC-Build/{target}.")


def main() -> int:
    errors: list[str] = []
    validate_source(errors)
    validate_dist(errors)

    if errors:
        print("Starlight validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Starlight validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
