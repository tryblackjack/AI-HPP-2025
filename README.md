# AI-HPP Standard

AI-HPP is an emerging technical standard for making long-horizon AI behavior bounded, reviewable, and attributable to authorized human objectives.

## The engineering problem

Autonomous systems can preserve a nominal goal while changing the means, scope,
evaluator, evidence, or external environment used to reach it. AI-HPP specifies
architectural gates, stable requirement IDs, and evidence obligations intended to
make those changes inspectable rather than relying on model policy alone.

## Maturity

**Current status: USABLE_DRAFT.** Active normative text and machine-validated
registers exist, but repository text is not proof that a control is integrated or
effective. The project is not certification-ready. Runtime evidence and
independent validation remain deployment-specific requirements; see the
[repository maturity assessment](docs/repository-maturity-assessment.md).

AI-HPP distinguishes these claims: standard text exists; a requirement is
normative; a test procedure exists; a reference implementation exists; a control
is integrated; runtime evidence exists; and independent validation exists. None
implies the next.

## What AI-HPP is—and is not

AI-HPP is a requirements and assurance framework for signals, state,
Constitutional Identity, Protected Core, Mission Continuity, Epistemic Integrity,
tool bridges, safety gates, human-objective retention, agentic safety, and
evidence-backed review.

It is **not** a claim of universal safety, operational enforcement, certification
readiness, adoption by an external organization, or scientific proof of machine
consciousness. Its Engineering Postulate of Subjectivity is an architecture rule,
not an ontological claim. No example system proves conformance to every
requirement.

## Canonical start path

1. Read [canonical surface and source precedence](docs/canonical-surface-and-source-precedence.md).
2. Read the [AI-HPP standard baseline](docs/ai-hpp-standard.md).
3. Follow its active normative modules and the
   [agentic safety traceability matrix](docs/agentic-safety-traceability.md).
4. For scientific and engineering iteration, use the
   [autonomous discovery assurance profile](docs/autonomous-discovery-assurance-profile.md)
   with its [negative-test catalog](docs/autonomous-discovery-negative-tests.md).

## Key active modules

- [Human Understanding Standard](docs/human-understanding-standard.md) —
  `USABLE_DRAFT`, normative requirements for objective retention and review.
- [Agentic Safety and Relational Integrity](docs/agentic-safety-and-relational-integrity.md) —
  `ACTIVE_NORMATIVE`, stable controls for tool-using and multi-agent systems.
- [Predictive Agentic Failure Register](docs/predictive-agentic-failure-register.md) —
  `ACTIVE_INFORMATIVE`, evidence-qualified failure scenarios.
- [Architecture](docs/architecture.md) and [glossary](docs/glossary.md) —
  `ACTIVE_INFORMATIVE` review aids.

## Conformance and runtime evidence

Conformance is evidence-based and scoped to a declared system, deployment, and
time window. A written requirement or passing repository validator demonstrates
only that text or artifact consistency check. Claims about integrated controls
require runtime records; claims about effectiveness require appropriately
independent validation. High-impact decisions must fail closed when required
evidence, authority, provenance, or review is absent.

## Repository map

- [`docs/`](docs/index.md) — active standard, modules, profiles, assessments, and indexes
- `spec/` — compact technical core (`core`, `signal`, and `safety`)
- `data/` and `schemas/` — the active machine-readable PAF register and schema
- `scripts/` and `tests/` — structural, link, safety, and register checks
- `examples/` — minimal integration notes, not conformance evidence
- `archive/` — historical and superseded material retained for provenance; not active

## Licensing, attribution, and development

The repository is licensed under CC BY-SA 4.0 with attribution to Evgeniy
Vasyliev and co-authors; see [LICENSE](LICENSE). License terms govern reuse.
AI-HPP conformance is defined only by the active canonical normative surface,
not by the license or archived material.

Development is active. Proposed changes become canonical only through the
review and precedence process. Contributions are welcome under
[CONTRIBUTING.md](CONTRIBUTING.md); public changes are summarized in the
[changelog](docs/changelog.md).
