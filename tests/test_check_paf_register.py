from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml

from scripts.check_paf_register import load_register, validate_semantics


SCHEMA = Path(__file__).resolve().parents[1] / "schemas" / "paf-register.schema.json"
TRACE_TEXT = "ECI-REQ-001\nOGS-REQ-001\n"


def base_register() -> dict[str, object]:
    return {
        "version": "test",
        "status": "informative",
        "last_updated": "2026-07-22",
        "sources": [
            {
                "id": "PAF-SRC-001",
                "publisher": "Test Publisher",
                "title": "Test Source",
                "publication_date": "2026-07-22",
                "url": "https://example.com/source",
            }
        ],
        "scenarios": [
            {
                "id": "PAF-01",
                "name": "Test scenario",
                "evidence_status": "OBSERVED",
                "evidence_completeness": "COMPLETE",
                "evidence_confidence": "HIGH",
                "severity": "HIGH",
                "test_priority": "P1",
                "last_evidence_date": "2026-07-22",
                "review_date": "2026-10-31",
                "owner": "AI-HPP Maintainers",
                "evidence_sources": ["PAF-SRC-001"],
                "existing_controls": ["ECI-REQ-001"],
                "required_gates": ["containment design review"],
                "negative_test": "Test must fail closed.",
                "promotion_criteria": "Promote only with evidence.",
            }
        ],
    }


def write_register(tmp_path: Path, register: dict[str, object]) -> Path:
    data_path = tmp_path / "paf-register.yaml"
    data_path.write_text(yaml.safe_dump(register), encoding="utf-8")
    return data_path


def schema_errors(tmp_path: Path, register: dict[str, object]) -> str:
    with pytest.raises(ValueError) as excinfo:
        load_register(write_register(tmp_path, register), SCHEMA)
    return str(excinfo.value)


def test_unknown_field_fails_schema_validation(tmp_path: Path) -> None:
    register = base_register()
    register["unexpected"] = "not allowed"

    assert "Additional properties are not allowed" in schema_errors(tmp_path, register)


def test_invalid_enum_fails_schema_validation(tmp_path: Path) -> None:
    register = base_register()
    scenario = register["scenarios"][0]
    scenario["evidence_status"] = "RUMORED"

    assert "RUMORED" in schema_errors(tmp_path, register)


def test_format_checker_rejects_invalid_date(tmp_path: Path) -> None:
    register = base_register()
    register["last_updated"] = "not-a-date"

    assert "not-a-date" in schema_errors(tmp_path, register)


def test_missing_evidence_source_fails_semantic_validation() -> None:
    register = base_register()
    scenario = register["scenarios"][0]
    scenario["evidence_sources"] = ["PAF-SRC-999"]

    errors = validate_semantics(register, TRACE_TEXT)

    assert "PAF-01 references unknown source PAF-SRC-999" in errors


def test_unknown_requirement_id_fails_semantic_validation() -> None:
    register = base_register()
    scenario = register["scenarios"][0]
    scenario["existing_controls"] = ["ECI-REQ-999"]

    errors = validate_semantics(register, TRACE_TEXT)

    assert "PAF-01 references unknown requirement ECI-REQ-999" in errors


def test_cyclic_variant_of_fails_semantic_validation() -> None:
    register = base_register()
    first = register["scenarios"][0]
    second = copy.deepcopy(first)
    first["variant_of"] = "PAF-02"
    second["id"] = "PAF-02"
    second["variant_of"] = "PAF-01"
    register["scenarios"].append(second)

    errors = validate_semantics(register, TRACE_TEXT)

    assert "cyclic variant_of relationship: PAF-01 -> PAF-02 -> PAF-01" in errors


def test_schema_declares_draft_2020_12() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
