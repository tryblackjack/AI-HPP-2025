from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_v430_normative_and_traceability_registration() -> None:
    module = read("docs/agentic-safety-and-relational-integrity.md")
    trace = read("docs/agentic-safety-traceability.md")
    assert module.count("### ICA-REQ-005 —") == 1
    assert trace.count("| ICA-REQ-005 |") == 1
    assert "organizational assurance handoff negative test" in module
    assert "Critical | High-Impact Autonomous System" in trace


def test_organizational_transition_is_fail_closed_in_existing_gate() -> None:
    safety = read("spec/safety.md")
    assert safety.count("| Post-Action Assurance Gate |") == 1
    assert "assurance-owner change" in safety
    assert "required safety function becomes unowned" in safety
    assert "Organizational Safety Gate" not in safety


def test_paf_26_is_informative_and_not_overpromoted() -> None:
    register = yaml.safe_load(read("data/paf-register.yaml"))
    scenarios = [item for item in register["scenarios"] if item["id"] == "PAF-26"]
    assert len(scenarios) == 1
    assert register["status"] == "informative"
    assert scenarios[0]["evidence_status"] == "INFERRED"
    assert scenarios[0]["severity"] == "HIGH"
    assert scenarios[0]["required_gates"] == [
        "Post-Action Assurance Gate",
        "Human Review Gate",
    ]


def test_frozen_baseline_preserves_mvp_and_public_maturity() -> None:
    baseline = read("docs/ai-hpp-standard.md")
    readme = read("README.md")
    assert baseline.startswith("# AI-HPP Standard v4.3.0")
    assert baseline.count("**MVP-00") == 7
    assert "MVP-008" not in baseline
    assert "USABLE_DRAFT" in readme
    assert "not certification-ready" in readme
    assert "repository consistency" in readme


def test_canonical_surface_and_licensing_boundaries() -> None:
    canonical = read("docs/canonical-surface-and-source-precedence.md")
    reuse = read("REUSE.toml")
    assert "Predictive Failure Outlook" in canonical
    assert "repository governance" in canonical
    assert "Autonomous Discovery Negative Tests" in canonical
    assert "Archive text has\n   no normative effect" in canonical
    assert '"CITATION.cff"' in reuse
    assert "CC-BY-SA-4.0" in reuse
    assert "Apache-2.0" in reuse
