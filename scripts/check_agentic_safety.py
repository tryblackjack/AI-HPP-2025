#!/usr/bin/env python3
"""Structural and contract checks for the agentic safety documentation extension."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "docs" / "agentic-safety-and-relational-integrity.md"
TRACE = ROOT / "docs" / "agentic-safety-traceability.md"
CASES = ROOT / "docs" / "agentic-safety-case-studies.md"
ARCH = ROOT / "docs" / "architecture.md"
SAFETY = ROOT / "spec" / "safety.md"
REQUIRED_FILES = [MODULE, TRACE, CASES, ARCH, SAFETY]
FAMILIES = ("RPS", "SRA", "ECI", "ICA", "KAI", "EAA", "DAI", "BAF", "AFB")
REQ_RE = re.compile(r"^### ((?:" + "|".join(FAMILIES) + r")-REQ-\d{3})", re.M)
FIELD_RE = re.compile(r"^- \*\*(Requirement ID|Normative statement|Applicability|Required evidence|Test method|Failure condition|Required gate outcome):\*\*\s*(.+)$", re.M)
TRACE_ID_RE = re.compile(r"^\|\s*((?:" + "|".join(FAMILIES) + r")-REQ-\d{3})\s*\|", re.M)
GATE_OUTCOME_RE = re.compile(r"([A-Z][A-Za-z and+\-]+ Gate) MUST route to ([^.]+?)(?: according to| when | for | after| before|\.)")
OUTCOME_RE = re.compile(r"`?\b(allow|delay|review|block|terminate|quarantine|invalidate)\b`?")
SPEC_GATE_RE = re.compile(r"^\| ([^|]+ Gate) \|[^|]*\|[^|]*\|([^|]+)\|", re.M)
MANDATORY_FIELDS = [
    "Requirement ID",
    "Normative statement",
    "Applicability",
    "Required evidence",
    "Test method",
    "Failure condition",
    "Required gate outcome",
]
CASE_FIELDS = [
    "Reported information",
    "Unresolved claims or allegations",
    "Engineering interpretation",
    "Normative lesson",
]
BASELINE_ARCH = [
    "Engineering Postulate of Subjectivity",
    "Subjective State (Engineering Model)",
    "Constitutional Identity",
]
BANNED_CLAIMS = [
    "guaranteed safe",
    "zero risk",
    "fully aligned",
    "cannot escape",
    "cannot deceive",
    "100% accurate",
    "proves consciousness",
    "proves absence of consciousness",
    "containment is proven",
    "conformance is achieved",
    "scientifically validated",
]
PROHIBITED_NAMES = ["JARVIS"]
SECRET_LIKE_RE = re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def local_links(text: str) -> list[str]:
    links: list[str] = []
    for raw in LINK_RE.findall(text):
        target = raw.strip().split("#", 1)[0].split("?", 1)[0]
        if not target or target.startswith("#") or ":" in target or target.startswith("/"):
            continue
        links.append(target)
    return links


def split_requirement_blocks(text: str) -> dict[str, str]:
    starts = list(REQ_RE.finditer(text))
    blocks: dict[str, str] = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        blocks[match.group(1)] = text[match.start():end]
    return blocks


def parse_gate_contracts(spec_text: str) -> dict[str, set[str]]:
    contracts: dict[str, set[str]] = {}
    for gate, outcomes in SPEC_GATE_RE.findall(spec_text):
        contracts[gate.strip()] = set(OUTCOME_RE.findall(outcomes))
    return contracts


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists() or not path.read_text(encoding="utf-8", errors="ignore").strip():
            errors.append(f"missing or empty file: {rel(path)}")

    if errors:
        for error in errors:
            print(error)
        return 1

    module_text = MODULE.read_text(encoding="utf-8")
    trace_text = TRACE.read_text(encoding="utf-8")
    cases_text = CASES.read_text(encoding="utf-8")
    arch_text = ARCH.read_text(encoding="utf-8")
    safety_text = SAFETY.read_text(encoding="utf-8")
    all_text = "\n".join([module_text, trace_text, cases_text])

    req_ids = REQ_RE.findall(module_text)
    req_set = set(req_ids)
    if not 25 <= len(req_ids) <= 35:
        errors.append(f"expected 25-35 requirements, found {len(req_ids)}")
    if len(req_ids) != len(req_set):
        errors.append("requirement IDs are not unique")
    present_families = {rid.split("-", 1)[0] for rid in req_ids}
    for family in FAMILIES:
        if family not in present_families:
            errors.append(f"missing requirement family: {family}")

    contracts = parse_gate_contracts(safety_text)
    if not contracts:
        errors.append("no gate contracts parsed from spec/safety.md")

    blocks = split_requirement_blocks(module_text)
    for rid, block in blocks.items():
        fields = {name: value.strip() for name, value in FIELD_RE.findall(block)}
        for field in MANDATORY_FIELDS:
            if field not in fields:
                errors.append(f"{rid} missing field: {field}")
            elif not fields[field] or fields[field] in {"TBD", "TODO", "N/A"}:
                errors.append(f"{rid} has empty placeholder field: {field}")
        if fields.get("Requirement ID") and fields["Requirement ID"] != rid:
            errors.append(f"{rid} Requirement ID field does not match heading: {fields['Requirement ID']}")
        outcome_text = fields.get("Required gate outcome", "")
        gate_mentions = GATE_OUTCOME_RE.findall(outcome_text)
        if not gate_mentions:
            errors.append(f"{rid} required gate outcome does not name a gate/outcome contract")
        for gate, raw_outcomes in gate_mentions:
            gate = gate.strip()
            mentioned = set(OUTCOME_RE.findall(raw_outcomes))
            if gate not in contracts:
                errors.append(f"{rid} references unknown gate: {gate}")
                continue
            if not mentioned:
                errors.append(f"{rid} names {gate} without explicit outcomes")
            unsupported = mentioned - contracts[gate]
            if unsupported:
                errors.append(f"{rid} requires unsupported outcome(s) for {gate}: {', '.join(sorted(unsupported))}")

    trace_ids = TRACE_ID_RE.findall(trace_text)
    trace_set = set(trace_ids)
    for rid in req_ids:
        if trace_ids.count(rid) != 1:
            errors.append(f"{rid} must appear exactly once in traceability matrix")
    for rid in sorted(trace_set - req_set):
        errors.append(f"traceability contains unknown requirement ID: {rid}")

    case_blocks = re.split(r"(?=^## (?!Purpose|Gate|Mandatory|Flow)[^\n]+)", cases_text, flags=re.M)[1:]
    for case in case_blocks:
        title = case.splitlines()[0].removeprefix("## ").strip()
        for field in CASE_FIELDS:
            pattern = rf"^- \*\*{re.escape(field)}:\*\*\s*\S"
            if not re.search(pattern, case, flags=re.M):
                errors.append(f"case study '{title}' missing non-empty field: {field}")

    for element in BASELINE_ARCH:
        if element not in arch_text:
            errors.append(f"architecture missing baseline element: {element}")

    lowered = all_text.lower()
    for claim in BANNED_CLAIMS:
        if claim in lowered:
            errors.append(f"banned absolute or overclaim phrase found: {claim}")

    for name in PROHIBITED_NAMES:
        if name in all_text:
            errors.append(f"prohibited implementation name found: {name}")

    for path in REQUIRED_FILES:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if SECRET_LIKE_RE.search(text):
            errors.append(f"secret-like string found in {rel(path)}")
        for link in local_links(text):
            if not (path.parent / link).resolve().exists():
                errors.append(f"broken local link in {rel(path)} -> {link}")

    if errors:
        print("Agentic safety documentation structural checks failed.")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Agentic safety documentation structural checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
