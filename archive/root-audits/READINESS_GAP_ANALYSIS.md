# Standards Readiness Gap Analysis — AI-HPP-Standard

Date: 2026-04-20  
Assessment target: readiness for skeptical external AI safety / governance review.

## Scoring rubric

0 = absent, 1 = very weak, 2 = early draft, 3 = usable with caveats, 4 = strong, 5 = review-ready best practice.

## Scorecard (0–5)

- **Structural maturity:** 2.5 / 5
- **Specification maturity:** 2.0 / 5
- **Audit readiness:** 2.5 / 5
- **Translation readiness:** 2.0 / 5
- **Governance readiness:** 2.5 / 5

---

## A) Specification maturity

### Findings

- Active surface (`docs/ai-hpp-standard.md`, `spec/*`) is concise and understandable, but does not expose the richer normative module architecture visible in archived v3.x materials.
- Consistent RFC-style modality (`SHALL`/`SHOULD`/`MAY`) is not systematically applied in active canonical docs.
- Version signaling exists (`v4.1.1` in active doc, v3.15/v3.17 markers in archive) but cross-version relationship is not explicitly defined.

### Gap

External reviewers cannot quickly determine if the minimal active standard supersedes, subsets, or diverges from archived normative modules.

---

## B) Evidence maturity

### Findings

- Evidence/conformance assets exist (schemas, conformance maps, regulator-sim templates), but are placed under archive paths.
- Active docs do not clearly map:
  - modules -> requirements,
  - requirements -> schema artifacts,
  - requirements -> conformance test scripts.
- Some conformance scripts in `scripts/` are not linked from main docs.

### Gap

Traceability chain is present in fragments, not as a single auditable graph.

---

## C) Governance maturity

### Findings

- Governance-rich content (incident handling, conflict safeguards, adaptive governance, failure taxonomy) exists in archive annexes.
- Operational pathways (escalation, CAPA-like control flow, regulator simulation procedures) are available but not prominently discoverable from root.
- Failure taxonomy IDs are not consistently available across translation sets.

### Gap

Governance appears substantial but is discoverability-constrained and translation-fragile for external comparability.

---

## Blockers preventing external expert trust

## Critical blockers

1. **Canonical ambiguity:** no explicit declaration of authoritative standard surface (active minimal vs archived comprehensive).
2. **Broken internal links in active governance process (`CONTRIBUTING.md`).**
3. **Translation parity gap for failure taxonomy (Annex C not broadly translated), weakening cross-language audit equivalence.**

## Major blockers

4. Missing explicit module->schema->test traceability matrix in current canonical entrypoints.
5. Mixed naming/versioning across translation folders (especially `uk-UA`) obscures authoritative documents.
6. Archived docs include dead links to removed spec files, reducing perceived rigor.

## Moderate blockers

7. Orphaned active docs/examples are not reachable from root entrypoint.
8. No clearly published external-review checklist (what to read, in what order, what evidence to verify).

---

## Expert-review readiness verdict

**Current state: “Promising but not yet expert-review ready.”**  
The repository contains meaningful governance material and evidence artifacts, but canonical path clarity and traceability packaging must be stabilized before external scrutiny by skeptical reviewers.
