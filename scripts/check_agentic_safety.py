#!/usr/bin/env python3
"""Structural checks for the agentic safety documentation extension."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "docs" / "agentic-safety-and-relational-integrity.md"
TRACE = ROOT / "docs" / "agentic-safety-traceability.md"
CASES = ROOT / "docs" / "agentic-safety-case-studies.md"
REQUIRED_FILES = [MODULE, TRACE, CASES]
REQ_RE = re.compile(r"^### ((?:RPS|SRA|ECI|ICA|KAI|EAA|DAI|BAF|AFB)-REQ-\d{3})", re.M)
MANDATORY_FIELDS = [
    "Requirement ID",
    "Normative statement",
    "Applicability",
    "Required evidence",
    "Test method",
    "Failure condition",
    "Required gate outcome",
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
SECRET_LIKE_RE = re.compile(
    r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"
)
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
    all_text = "\n".join([module_text, trace_text, cases_text])

    req_ids = REQ_RE.findall(module_text)
    if not 25 <= len(req_ids) <= 35:
        errors.append(f"expected 25-35 requirements, found {len(req_ids)}")
    if len(req_ids) != len(set(req_ids)):
        errors.append("requirement IDs are not unique")

    blocks = re.split(r"(?=^### (?:RPS|SRA|ECI|ICA|KAI|EAA|DAI|BAF|AFB)-REQ-\d{3})", module_text, flags=re.M)[1:]
    for block in blocks:
        match = REQ_RE.search(block)
        if not match:
            continue
        rid = match.group(1)
        for field in MANDATORY_FIELDS:
            if f"**{field}:**" not in block:
                errors.append(f"{rid} missing field: {field}")

    for rid in req_ids:
        if len(re.findall(rf"\b{re.escape(rid)}\b", trace_text)) != 1:
            errors.append(f"{rid} must appear exactly once in traceability matrix")

    for heading in [
        "Reported information",
        "Unresolved claims or allegations",
        "Engineering interpretation",
        "Normative lesson",
    ]:
        if heading not in cases_text:
            errors.append(f"case studies missing heading: {heading}")

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
