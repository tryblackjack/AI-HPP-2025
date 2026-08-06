#!/usr/bin/env python3
"""Validate the informative Predictive Agentic Failure Register data file."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "paf-register.yaml"
SCHEMA = ROOT / "schemas" / "paf-register.schema.json"
TRACE = ROOT / "docs" / "agentic-safety-traceability.md"

STATUS = {"OBSERVED", "EXPERIMENTAL", "INFERRED", "SPECULATIVE"}
COMPLETENESS = {"COMPLETE", "PARTIAL"}
CONFIDENCE = {"HIGH", "MEDIUM", "LOW"}
SEVERITY = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}
PRIORITY = {"P0", "P1", "P2", "P3"}
PAF_RE = re.compile(r"^PAF-\d{2}$")
SRC_RE = re.compile(r"^PAF-SRC-\d{3}$")
REQ_RE = re.compile(r"^[A-Z]{3}-REQ-\d{3}$")
TIMESTAMP_TAG = "tag:yaml.org,2002:timestamp"


class StringDatesSafeLoader(yaml.SafeLoader):
    """Load YAML safely without coercing ISO-like timestamps to date objects."""


StringDatesSafeLoader.yaml_implicit_resolvers = {
    key: [
        (tag, regexp)
        for tag, regexp in resolvers
        if tag != TIMESTAMP_TAG
    ]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}



def load_register(data_path: Path, schema_path: Path) -> dict[str, object]:
    """Load YAML register data and validate it against the JSON Schema."""
    with data_path.open(encoding="utf-8") as data_file:
        register = yaml.load(data_file, Loader=StringDatesSafeLoader)
    with schema_path.open(encoding="utf-8") as schema_file:
        schema = json.load(schema_file)

    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    errors = sorted(
        validator.iter_errors(register), key=lambda error: list(error.path)
    )
    if errors:
        details = []
        for error in errors:
            location = "/".join(str(part) for part in error.path) or "<root>"
            details.append(f"schema violation at {location}: {error.message}")
        raise ValueError("\n".join(details))

    if not isinstance(register, dict):
        raise ValueError("register root must be a mapping")
    return register


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def visit(pid: str, variants: dict[str, str], stack: tuple[str, ...], errors: list[str]) -> None:
    if pid in stack:
        fail(errors, "cyclic variant_of relationship: " + " -> ".join((*stack, pid)))
        return
    parent = variants.get(pid)
    if parent:
        visit(parent, variants, (*stack, pid), errors)



def validate_semantics(register: dict[str, object], trace_text: str) -> list[str]:
    """Validate repository-specific PAF IDs and relationships."""
    errors: list[str] = []
    sources = register.get("sources", [])
    scenarios = register.get("scenarios", [])
    source_ids = {str(source.get("id")) for source in sources}
    scenario_ids = {str(scenario.get("id")) for scenario in scenarios}
    known_requirements = set(re.findall(r"\b[A-Z]{3}-REQ-\d{3}\b", trace_text))

    if len(source_ids) != len(sources):
        fail(errors, "duplicate source id")
    for source in sources:
        sid = str(source.get("id"))
        if not SRC_RE.match(sid):
            fail(errors, f"invalid source id: {sid}")
        for key in ("publisher", "title", "publication_date", "url"):
            if not source.get(key):
                fail(errors, f"{sid} missing {key}")

    if len(scenario_ids) != len(scenarios):
        fail(errors, "duplicate scenario id")
    variants: dict[str, str] = {}
    for scenario in scenarios:
        pid = str(scenario.get("id"))
        if not PAF_RE.match(pid):
            fail(errors, f"invalid scenario id: {pid}")
        status_fields = (
            ("evidence_status", STATUS),
            ("evidence_completeness", COMPLETENESS),
            ("evidence_confidence", CONFIDENCE),
            ("severity", SEVERITY),
            ("test_priority", PRIORITY),
        )
        for key, allowed in status_fields:
            value = scenario.get(key)
            if value not in allowed:
                fail(errors, f"{pid} has invalid {key}: {value}")
        required_text_fields = (
            "last_evidence_date",
            "review_date",
            "owner",
            "negative_test",
            "promotion_criteria",
        )
        for key in required_text_fields:
            if not scenario.get(key):
                fail(errors, f"{pid} missing {key}")
        for sid in scenario.get("evidence_sources", []):
            if sid not in source_ids:
                fail(errors, f"{pid} references unknown source {sid}")
        for req in scenario.get("existing_controls", []):
            if not REQ_RE.match(str(req)):
                fail(errors, f"{pid} has malformed requirement {req}")
            elif req not in known_requirements:
                fail(errors, f"{pid} references unknown requirement {req}")
        if scenario.get("variant_of"):
            ref = str(scenario["variant_of"])
            if ref not in scenario_ids:
                fail(errors, f"{pid} variant_of references unknown scenario {ref}")
            variants[pid] = ref
        for field in ("related_to", "compounds_with"):
            for ref in scenario.get(field, []):
                if ref not in scenario_ids:
                    fail(errors, f"{pid} {field} references unknown scenario {ref}")
    for pid in variants:
        visit(pid, variants, (), errors)
    return errors


def main() -> int:
    try:
        register = load_register(DATA, SCHEMA)
    except (OSError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    errors = validate_semantics(register, TRACE.read_text())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    scenarios = register.get("scenarios", [])
    sources = register.get("sources", [])
    print(f"PAF register OK: {len(scenarios)} scenarios, {len(sources)} sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
