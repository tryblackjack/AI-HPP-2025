# REPO_MAP

## Repository tree (functional)

```text
AI-HPP-Standard/
├── standard/                 # Normative standard text (v3.x control requirements)
├── annex/                    # Supporting threat, incident, taxonomy, and governance annexes
├── schemas/                  # JSON schema definitions for evidence and governance artifacts
├── regulator-sim/            # Audit simulation pack (requests, templates, conformance maps)
├── docs/                     # Explanatory documentation for humans/operators
├── developer/                # Integration-facing guides and architecture examples
├── scripts/                  # CI quality gates and conformance checks
├── translations/             # Multilingual copies of key standard documents
├── .github/                  # Workflow automation, issue templates, repository governance
├── spec/                     # v4 standardization artifacts (added in this upgrade)
├── ecosystem/                # SDK/plugin ecosystem skeleton (added in this upgrade)
└── examples/                 # End-to-end usage examples (added in this upgrade)
```

## Module purpose map

- **Normative layer**: `standard/`, `annex/`, `INDEX.md`, `GLOSSARY.md`.
- **Assurance layer**: `regulator-sim/`, `schemas/`, `scripts/`, `SECURITY.md`.
- **Adoption layer**: `docs/`, `developer/`, `translations/`, new `ecosystem/`, `examples/`.
- **Governance layer**: `.github/`, `CONTRIBUTING.md`, `CHANGELOG.md`, `AUTHORS.md`.

## Architecture layers

1. **Policy / specification**: control definitions, threat model, conformance levels.
2. **Evidence model**: JSON schemas and evidence bundle templates.
3. **Regulatory simulation**: adversarial inspector workflows and request catalogs.
4. **Developer implementation**: integration patterns and quick-start usage.
5. **Ecosystem extension (v4 target)**: SDKs, plugins, CLI contract, badges.

## Dependency graph (logical)

- `standard/*` requirements are referenced by:
  - `standard/REQUIREMENTS-INDEX.md`
  - `regulator-sim/CONFORMANCE/REQUIREMENT_TO_EVIDENCE_MAP.yaml`
- `schemas/*.schema.json` validate operational artifacts used by:
  - `regulator-sim/TEMPLATES/*`
  - `regulator-sim/SAMPLES/*`
- `scripts/*` provide repository integrity checks used in CI workflows.
- `translations/*` mirror selected core docs for international adoption.

## Public vs private artifacts

### Public-ready (current state)
- Normative standard docs (`standard/`, `annex/`, `docs/`, `developer/`).
- Public conformance scaffolding (`regulator-sim/*_PUBLIC.md`, templates, samples).
- Schemas and CI checks.

### Potentially private in downstream deployments
- Real evidence bundles and tool registry snapshots generated from templates.
- Incident records and CAPA records populated with operational details.

## Audit findings from structural review

### Dead/underutilized code paths
- No executable runtime system exists yet; repository is documentation-heavy.
- `scripts/` currently validates documentation integrity, not protocol execution.

### Duplicate/overlap areas
- Significant content overlap between `docs/`, `developer/`, and `standard/` onboarding narratives.
- Translations include mixed naming conventions (`README.md` and `README.uk.md` variants).

### Naming clarity issues
- Version naming is split across `BASELINE-*`, `AI-HPP-2025`, `AI-HPP-2026`, and `v3.17/v3.18` phrasing.
- `regulator-sim` and `docs` both contain audit walkthroughs, creating entry-point ambiguity.

### Architectural violations against standard-product pattern
- No single canonical protocol spec file for external implementers.
- No SDK/plugin contract directory for ecosystem contributors.
- No first-class CLI reference despite operational workflow requirements.
