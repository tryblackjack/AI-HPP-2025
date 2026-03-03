# AI-HPP Standard Library

AI-HPP is an implementation-neutral Standard for verification, governance, and auditable operation of agentic AI systems.

## Language / Мова
- 🇬🇧 **English**: [AI-HPP Full Document (EN)](docs/AI-HPP-Standard-Full-Document-EN.md)
- 🇺🇦 **Українська**: [Повний документ AI-HPP (UA)](docs/AI-HPP-Standard-Full-Document-UA.md)

## 5-minute explanation
AI-HPP defines a verification Protocol for AI systems that can act, use tools, and affect high-impact decisions. Instead of relying on policy statements alone, it requires:

1. **Normative requirements** with stable identifiers.
2. **Verification criteria** that are measurable and testable.
3. **Audit Artifacts** that document conformance and incidents.
4. **Governance controls** for escalation, override accountability, and safe-state behavior.

In practical terms, AI-HPP helps institutions answer: *What was required, what was verified, what evidence exists, and who was accountable?*

## Core reading entry points
- Full academic document (EN): [`docs/AI-HPP-Standard-Full-Document-EN.md`](docs/AI-HPP-Standard-Full-Document-EN.md)
- Full academic document (UA): [`docs/AI-HPP-Standard-Full-Document-UA.md`](docs/AI-HPP-Standard-Full-Document-UA.md)
- Academic comparison and scope statement: [`docs/ACADEMIC_POSITIONING.md`](docs/ACADEMIC_POSITIONING.md)
- Baseline inspection entry point: [`BASELINE-v3.17.md`](BASELINE-v3.17.md)

## For Researchers
Use AI-HPP as a reproducible verification Framework for evaluating agentic AI controls. The Standard supports rigorous comparison across systems through requirement-level traceability, explicit verification checkpoints, and machine-readable evidence structures.

Recommended starting sequence:
1. [`docs/AI-HPP-Standard-Full-Document-EN.md`](docs/AI-HPP-Standard-Full-Document-EN.md)
2. [`docs/ACADEMIC_POSITIONING.md`](docs/ACADEMIC_POSITIONING.md)
3. [`standard/REQUIREMENTS-INDEX.md`](standard/REQUIREMENTS-INDEX.md)

## For Engineers
Use AI-HPP as a Protocol for implementing verifiable controls in production and pre-production systems. The Standard specifies how to connect runtime behavior, tool execution boundaries, incident handling, and evidence generation.

Recommended implementation path:
1. [`BASELINE-v3.17.md`](BASELINE-v3.17.md)
2. [`standard/README.md`](standard/README.md)
3. [`schemas/README.md`](schemas/README.md)
4. [`regulator-sim/README.md`](regulator-sim/README.md)

## For Regulators
Use AI-HPP as an inspection-ready Standard for conformance review of agentic AI operations. The Framework links normative requirements to verifiable evidence and supports structured audit workflows.

Recommended review path:
1. [`docs/AI-HPP-Standard-Full-Document-EN.md`](docs/AI-HPP-Standard-Full-Document-EN.md)
2. [`regulator-sim/AUDIT_WALKTHROUGH.md`](regulator-sim/AUDIT_WALKTHROUGH.md)
3. [`regulator-sim/CONFORMANCE/REQUIREMENT_TO_EVIDENCE_MAP.yaml`](regulator-sim/CONFORMANCE/REQUIREMENT_TO_EVIDENCE_MAP.yaml)

## Repository structure (reference)
- `standard/` — normative requirements (core Standard)
- `annex/` — supporting context (threat, incident, regulatory mappings)
- `schemas/` — machine-readable evidence and audit schemas
- `regulator-sim/` — inspection and conformance workflow materials
- `docs/` — academic and human-readable entry documents
- `translations/` — multilingual resources

## Safety and disclosure
- Responsible security reporting: [`SECURITY.md`](SECURITY.md)
- Post-merge maintainer controls: [`docs/POST_MERGE_OPERATOR_CHECKLIST.md`](docs/POST_MERGE_OPERATOR_CHECKLIST.md)
