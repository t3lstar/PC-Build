#!/usr/bin/env python3
"""Validate digital twin JSON data against JSON Schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "data" / "schemas" / "digital-twin.schema.json"
DATA_FILES = [ROOT / "data" / "digital-twin" / "build.json"]


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def item_ids(instance: dict[str, object], collection: str) -> set[str]:
    items = instance.get(collection, [])
    if not isinstance(items, list):
        return set()
    return {item["id"] for item in items if isinstance(item, dict) and isinstance(item.get("id"), str)}


def add_reference_error(
    errors: list[str],
    data_file: Path,
    path: str,
    value: object,
    valid_ids: set[str],
    label: str,
) -> None:
    if isinstance(value, str) and value not in valid_ids:
        rel_file = data_file.relative_to(ROOT)
        errors.append(f"{rel_file}:{path}: unknown {label} reference '{value}'")


def validate_references(instance: object, data_file: Path, errors: list[str]) -> None:
    if not isinstance(instance, dict):
        return

    component_ids = item_ids(instance, "components")
    location_ids = item_ids(instance, "locations")
    connector_ids = item_ids(instance, "connectors")
    airflow_ids = item_ids(instance, "airflow")
    bios_ids = item_ids(instance, "biosTraining")

    cable_endpoint_ids = connector_ids | location_ids
    cable_route_ids = location_ids

    for index, location in enumerate(instance.get("locations", [])):
        if isinstance(location, dict) and "parentId" in location:
            add_reference_error(
                errors,
                data_file,
                f"locations/{index}/parentId",
                location["parentId"],
                component_ids | location_ids,
                "component or location",
            )

    for index, connector in enumerate(instance.get("connectors", [])):
        if not isinstance(connector, dict):
            continue
        add_reference_error(errors, data_file, f"connectors/{index}/componentId", connector.get("componentId"), component_ids, "component")
        add_reference_error(errors, data_file, f"connectors/{index}/locationId", connector.get("locationId"), location_ids, "location")

    for index, cable in enumerate(instance.get("cables", [])):
        if not isinstance(cable, dict):
            continue
        add_reference_error(errors, data_file, f"cables/{index}/from", cable.get("from"), cable_endpoint_ids, "connector or location")
        add_reference_error(errors, data_file, f"cables/{index}/to", cable.get("to"), cable_endpoint_ids, "connector or location")
        route = cable.get("route", [])
        if isinstance(route, list):
            for route_index, route_id in enumerate(route):
                add_reference_error(errors, data_file, f"cables/{index}/route/{route_index}", route_id, cable_route_ids, "location")

    for index, airflow_zone in enumerate(instance.get("airflow", [])):
        if isinstance(airflow_zone, dict):
            add_reference_error(
                errors,
                data_file,
                f"airflow/{index}/locationId",
                airflow_zone.get("locationId"),
                location_ids,
                "location",
            )

    for index, build_step in enumerate(instance.get("buildSequence", [])):
        if not isinstance(build_step, dict):
            continue
        component_refs = build_step.get("componentIds", [])
        if isinstance(component_refs, list):
            for component_index, component_id in enumerate(component_refs):
                add_reference_error(
                    errors,
                    data_file,
                    f"buildSequence/{index}/componentIds/{component_index}",
                    component_id,
                    component_ids,
                    "component",
                )

    for index, bios_state in enumerate(instance.get("biosTraining", [])):
        if not isinstance(bios_state, dict):
            continue
        next_states = bios_state.get("nextStateIds", [])
        if isinstance(next_states, list):
            for state_index, state_id in enumerate(next_states):
                add_reference_error(
                    errors,
                    data_file,
                    f"biosTraining/{index}/nextStateIds/{state_index}",
                    state_id,
                    bios_ids,
                    "BIOS state",
                )

    for index, link in enumerate(instance.get("links", [])):
        if isinstance(link, dict) and "componentId" in link:
            add_reference_error(
                errors,
                data_file,
                f"links/{index}/componentId",
                link["componentId"],
                component_ids,
                "component",
            )


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    errors: list[str] = []
    for data_file in DATA_FILES:
        instance = load_json(data_file)
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
            path = "/".join(str(part) for part in error.path) or "<root>"
            rel_file = data_file.relative_to(ROOT)
            errors.append(f"{rel_file}:{path}: {error.message}")
        validate_references(instance, data_file, errors)

    if errors:
        print("Digital twin data validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Digital twin data validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
