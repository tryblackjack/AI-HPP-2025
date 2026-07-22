#!/usr/bin/env python3
"""Validate the informative Predictive Agentic Failure Register data file."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "paf-register.yaml"
TRACE = ROOT / "docs" / "agentic-safety-traceability.md"

STATUS = {"OBSERVED", "EXPERIMENTAL", "INFERRED", "SPECULATIVE"}
COMPLETENESS = {"COMPLETE", "PARTIAL"}
CONFIDENCE = {"HIGH", "MEDIUM", "LOW"}
SEVERITY = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}
PRIORITY = {"P0", "P1", "P2", "P3"}
PAF_RE = re.compile(r"^PAF-\d{2}$")
SRC_RE = re.compile(r"^PAF-SRC-\d{3}$")
REQ_RE = re.compile(r"^[A-Z]{3}-REQ-\d{3}$")


def strip_value(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    return value


def parse_register(path: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    sources: list[dict[str, object]] = []
    scenarios: list[dict[str, object]] = []
    section = None
    current: dict[str, object] | None = None
    list_key: str | None = None

    for raw in path.read_text().splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if not raw.startswith(" ") and raw.endswith(":") and raw in {"sources:", "scenarios:"}:
            section = raw[:-1]
            current = None
            list_key = None
            continue
        if not raw.startswith(" ") and ":" in raw:
            continue
        if raw.startswith("  - "):
            if section not in {"sources", "scenarios"}:
                raise ValueError(f"item outside known section: {raw}")
            key, value = raw[4:].split(":", 1)
            current = {key: strip_value(value)}
            (sources if section == "sources" else scenarios).append(current)
            list_key = None
            continue
        if raw.startswith("    ") and current is not None:
            content = raw[4:]
            if content.lstrip().startswith("- "):
                if not list_key:
                    raise ValueError(f"list item without list key: {raw}")
                item = content.lstrip()[2:]
                current.setdefault(list_key, []).append(strip_value(item))
                continue
            key, value = content.split(":", 1)
            if value.strip():
                current[key] = strip_value(value)
                list_key = None
            else:
                current[key] = []
                list_key = key
            continue
        raise ValueError(f"unrecognized YAML subset line: {raw}")
    return sources, scenarios


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def visit(pid: str, variants: dict[str, str], stack: tuple[str, ...], errors: list[str]) -> None:
    if pid in stack:
        fail(errors, "cyclic variant_of relationship: " + " -> ".join((*stack, pid)))
        return
    parent = variants.get(pid)
    if parent:
        visit(parent, variants, (*stack, pid), errors)


def main() -> int:
    errors: list[str] = []
    sources, scenarios = parse_register(DATA)
    source_ids = {str(source.get("id")) for source in sources}
    scenario_ids = {str(scenario.get("id")) for scenario in scenarios}
    trace_text = TRACE.read_text()
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
        for key, allowed in (("evidence_status", STATUS), ("evidence_completeness", COMPLETENESS), ("evidence_confidence", CONFIDENCE), ("severity", SEVERITY), ("test_priority", PRIORITY)):
            value = scenario.get(key)
            if value not in allowed:
                fail(errors, f"{pid} has invalid {key}: {value}")
        for key in ("last_evidence_date", "review_date", "owner", "negative_test", "promotion_criteria"):
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
        for field in ("variant_of",):
            if scenario.get(field):
                ref = str(scenario[field])
                if ref not in scenario_ids:
                    fail(errors, f"{pid} {field} references unknown scenario {ref}")
                variants[pid] = ref
        for field in ("related_to", "compounds_with"):
            for ref in scenario.get(field, []):
                if ref not in scenario_ids:
                    fail(errors, f"{pid} {field} references unknown scenario {ref}")
    for pid in variants:
        visit(pid, variants, (), errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PAF register OK: {len(scenarios)} scenarios, {len(sources)} sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
