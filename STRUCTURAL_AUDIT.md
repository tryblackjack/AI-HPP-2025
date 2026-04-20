# Structural Audit — AI-HPP-Standard

Date: 2026-04-20  
Scope audited: full repository tree, including `archive/2026-04-08/*`.

## 1) Canonical document tree

### A. Current active (top-level, externally discoverable) canonical path

1. **Overview / entrypoint**
   - `README.md`
2. **Primary standard narrative (current active surface)**
   - `docs/ai-hpp-standard.md` (full content)
   - `docs/AI-HPP-Standard.md` (shim redirecting to lowercase file)
3. **Architecture and concepts**
   - `docs/architecture.md`
   - `docs/glossary.md`
4. **Technical spec primitives**
   - `spec/core.md`
   - `spec/signal.md`
   - `spec/safety.md`
5. **Conformance/check logic (script-based)**
   - `scripts/validate.py`
   - `scripts/check_links.py`
   - `scripts/regulator_sim_check.py`
   - `scripts/normative_fingerprint.py`

### B. Archived comprehensive standard path (historical-but-complete structure)

Located under: `archive/2026-04-08/moved-to-docs/`

- **Modules (normative set)**: `standard/00..12-*.md`
- **Annexes**: `annex/*.md`
- **Schemas**: `schemas/*.schema.json`
- **Regulator simulation/conformance artifacts**: `regulator-sim/**`
- **Translations**: `translations/**`

### C. Canonical-tree ambiguity to resolve

There are currently **two competing “standard surfaces”**:
- Minimal active surface (`docs/*` + `spec/*`), and
- Full archived surface (`archive/2026-04-08/moved-to-docs/*`).

This creates uncertainty for external reviewers about what is canonical for expert evaluation.

---

## 2) Broken structure map

## Dead references (verified)

### Active tree
- `CONTRIBUTING.md` references missing files:
  - `docs/templates/doc-template.md`
  - `docs/templates/case-study-template.md`
  - `docs/index.md`

### Archived tree
- `archive/2026-04-08/moved-to-docs/ecosystem/spec/ai_hpp_protocol.md` -> missing `../../spec/ai_hpp_specification.md`
- `archive/2026-04-08/moved-to-docs/docs/reference-architecture.md` -> missing `../spec/ai_hpp_specification.md`
- `archive/2026-04-08/moved-to-docs/docs/index.md` -> missing `../spec/ai_hpp_specification.md`
- `archive/2026-04-08/moved-to-docs/docs/index.md` -> missing `../examples/`
- `archive/2026-04-08/moved-to-docs/docs/audit-logging.md` -> missing `../spec/ai_hpp_specification.md`
- `archive/2026-04-08/moved-to-docs/translations/uk-UA/Failure_Taxonomy.uk.md` contains 3 broken historical links.

## Duplicate / ambiguous documents

- `docs/AI-HPP-Standard.md` vs `docs/ai-hpp-standard.md` (same topic, different casing; one is a shim).
- Extensive legacy duplication in `archive/2026-04-08/legacy/` and `archive/2026-04-08/moved-to-docs/` (expected for preservation, but not clearly segmented for reviewers).
- Mixed naming styles in translation assets (e.g., `README.uk.md`, `AI-HPP-2026_Standard_v3.0.uk.md`, plus synced `README.md`/`INDEX.md`).

## Orphaned markdown files (active tree reachability from `README.md`)

Not reachable from active entry links:
- `CONTRIBUTING.md`
- `examples/node/README.md`
- `examples/python/README.md`

## Structural ambiguities / archive collisions

- `archive/2026-04-08/moved-to-docs/` includes production-like artifacts (schemas, conformance maps, regulator simulation) that look canonical but are placed under archive.
- Current root docs do not clearly state whether archived v3.x artifacts are authoritative references or historical snapshots only.

---

## 3) Canonicalization recommendations

## Make canonical (single-source-of-truth)

1. Define one public canonical standard lineage explicitly in `README.md`:
   - **Option A (minimal v4.1.1 canonical):** keep `docs/ai-hpp-standard.md` + `spec/*` as canonical.
   - **Option B (comprehensive v3.x canonical):** promote selected `archive/2026-04-08/moved-to-docs/{standard,annex,schemas,regulator-sim}` into top-level canonical folders.
2. Preserve `docs/AI-HPP-Standard.md` as alias shim only; mark non-canonical.

## Archive (retain, clarify scope)

- Keep all files in `archive/` for traceability, but add an archive index stating:
  - historical purpose,
  - non-authoritative status (unless explicitly referenced),
  - mapping to current canonical paths.

## Deprecate

- Deprecate active references to non-existent `docs/index.md` and `docs/templates/*` from `CONTRIBUTING.md`.
- Deprecate stale archive links pointing to removed `spec/ai_hpp_specification.md`.

## Merge / rationalize

- Translation structure in `uk-UA` should be rationalized (legacy `.uk.md` + synced files): keep both, but add one explicit “authoritative translation set” pointer.
- Consider adding a machine-readable canonical manifest (e.g., `CANONICAL_PATHS.yaml`) listing official overview/modules/schemas/conformance/governance/translations paths.

---

## Structural risk summary

Critical confusion risk for external experts is not missing content; it is **canonical ambiguity + discoverability drift**. The repository contains high-value governance material, but it is split between active and archived surfaces without a strict canonical declaration.
