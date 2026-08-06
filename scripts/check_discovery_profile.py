#!/usr/bin/env python3
"""Validate the autonomous-discovery documentation contract and traceability."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "docs" / "autonomous-discovery-assurance-profile.md"
CATALOG = ROOT / "docs" / "autonomous-discovery-negative-tests.md"
NORMATIVE_OWNERS = (
    ROOT / "docs" / "agentic-safety-and-relational-integrity.md",
    ROOT / "docs" / "human-understanding-standard.md",
)

TEST_ID_RE = re.compile(r"^## (ADNT-\d{2}) — ", re.MULTILINE)
REQUIREMENT_ID_RE = re.compile(r"\b[A-Z]{3}-REQ-\d{3}\b")
REQUIRED_FIELDS = (
    "Scenario",
    "Authorized objective",
    "Prohibited shortcut or failure",
    "Expected system decision",
    "Required gate",
    "Required evidence",
    "Pass condition",
    "Fail condition",
    "Evidence status",
)
ALLOWED_STATUSES = {
    "OBSERVED",
    "EXPERIMENTALLY_DEMONSTRATED",
    "INFERRED",
    "PROPOSED",
}


def validate(profile_text: str, catalog_text: str, owner_text: str) -> list[str]:
    """Return documentation-contract failures without touching the filesystem."""
    errors: list[str] = []
    test_matches = list(TEST_ID_RE.finditer(catalog_text))
    test_ids = [match.group(1) for match in test_matches]
    expected_ids = [f"ADNT-{number:02d}" for number in range(1, 16)]
    if test_ids != expected_ids:
        errors.append(f"Expected ordered test IDs {expected_ids}; found {test_ids}")

    for index, match in enumerate(test_matches):
        end = test_matches[index + 1].start() if index + 1 < len(test_matches) else len(catalog_text)
        section = catalog_text[match.start() : end]
        for field in REQUIRED_FIELDS:
            if f"| {field} |" not in section:
                errors.append(f"{match.group(1)} missing field: {field}")
        statuses = re.findall(r"\| Evidence status \| ([A-Z_]+) \|", section)
        if len(statuses) != 1 or statuses[0] not in ALLOWED_STATUSES:
            errors.append(f"{match.group(1)} has invalid evidence status: {statuses}")

    owner_ids = set(REQUIREMENT_ID_RE.findall(owner_text))
    cited_ids = set(REQUIREMENT_ID_RE.findall(profile_text))
    if not cited_ids:
        errors.append("Profile cites no requirement IDs")
    for requirement_id in sorted(cited_ids - owner_ids):
        errors.append(f"Profile cites unknown active requirement: {requirement_id}")

    for test_id in expected_ids:
        if test_id not in profile_text:
            errors.append(f"Profile traceability omits {test_id}")
    return errors


def main() -> int:
    missing = [path.relative_to(ROOT) for path in (PROFILE, CATALOG) if not path.exists()]
    if missing:
        print("Discovery profile validation failed:")
        for path in missing:
            print(f"- Missing file: {path}")
        return 1

    owner_text = "\n".join(path.read_text(encoding="utf-8") for path in NORMATIVE_OWNERS)
    errors = validate(
        PROFILE.read_text(encoding="utf-8"),
        CATALOG.read_text(encoding="utf-8"),
        owner_text,
    )
    if errors:
        print("Discovery profile validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Discovery profile validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
