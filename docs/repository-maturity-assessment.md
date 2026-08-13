# Repository Maturity Assessment

Status: assessment artifact, not a replacement for existing AI-HPP concepts  
Date: 2026-08-12
Scope: active repository surface (`README.md`, `docs/`, `spec/`, scripts) plus preserved historical material under `archive/2026-04-08/moved-to-docs/` where it clarifies intent.

## Assessment Method

This assessment uses four practical maturity states:

| Maturity | Meaning |
|---|---|
| Emerging | Concept is present, but not yet complete enough for independent implementation or audit. |
| Usable Draft | A motivated team can apply it, but canonical paths, evidence, or test obligations remain incomplete. |
| Review-Ready | Independent reviewers can trace requirements to evidence and repeat checks with limited interpretation. |
| Operational | Versioned requirements, conformance evidence, change control, certification criteria, and governance operations are integrated into one maintained lifecycle. |

The current active surface is intentionally minimal. The archived surface contains richer architecture, certification, schemas, regulator-simulation, and governance material, but the active repository does not yet declare how much of that material is canonical. Therefore, maturity ratings below distinguish between **content existence** and **active canonical maturity**.

## Executive Determination

**Overall status: `USABLE_DRAFT`.** The active surface now defines a normative
Minimum Viable Profile, but that changes the completeness of the text—not the
operational status of any implementation. The following claims remain distinct:
normative text exists; a control is integrated; runtime evidence exists; and an
independent reviewer has validated effectiveness. No claim implies the next.

| Category | Current maturity | Determination |
|---|---:|---|
| Reference Architecture | Usable Draft | AI-HPP has a clear active flow model and a richer archived layered architecture, but canonical architectural views and implementation patterns are not yet unified. |
| Safety Standard | Usable Draft | A normative seven-control Minimum Viable Profile now defines the basic conformance floor; domain-wide independent assessment procedures and deployment evidence remain incomplete. |
| Certification Framework | Emerging | Certification levels and regulator-simulation artifacts exist in archive, but active certification criteria, assessor workflow, and evidence acceptance rules are not canonicalized. |
| Governance Framework | Usable Draft | Governance concepts, controls, adaptive governance, audit logging, and evidence packaging exist, but active governance lifecycle ownership and change-control rules are incomplete. |

## 1. Reference Architecture

### Current Maturity: Usable Draft

AI-HPP currently functions as a **usable draft reference architecture**. The active architecture defines the primary execution path: input signal, state check, policy check, safety gates, bridge, action, and audit log. The archived reference architecture extends this into layered responsibilities from user and agent interface through safety, policy enforcement, tool authorization, execution, audit evidence, and verification outputs.

### Gaps

- The active architecture is intentionally simple and does not yet include the richer layered model, runtime deployment boundaries, evidence interfaces, certification outputs, or multi-agent governance surfaces.
- The repository has two architecture surfaces: active minimal docs and archived comprehensive docs. External implementers may not know which is authoritative.
- Architecture-to-control traceability is incomplete in the active surface. A reviewer cannot yet move deterministically from each architecture component to specific controls, evidence, tests, and implementation examples.
- Implementation examples exist, but they are not presented as conformance-grade reference implementations.

### Missing Artifacts

- Canonical architecture decision record declaring the active reference architecture and archived status.
- Component responsibility matrix for signal, state, bridge, safety gate, policy enforcement, evidence, and review outputs.
- Deployment view for single-agent, multi-agent, tool-using, and successor-system deployments.
- Threat-boundary diagram identifying trust zones, bridge boundaries, escalation points, and audit boundaries.
- Architecture-to-requirement-to-evidence traceability map.
- Minimal reference implementation profile showing required hooks without prescribing product architecture.

### Roadmap to Next Maturity Level

To reach **Review-Ready** maturity:

1. Add a canonical architecture map that preserves the current minimal flow while referencing the archived layered architecture as historical input or informative expansion.
2. Define each architecture node as an enforcement or evidence point: signal intake, state update, policy evaluation, safety gate, bridge authorization, action, and audit log.
3. Publish a traceability table from architecture components to active spec sections, scripts, templates, and sample evidence.
4. Add deployment profiles for low-risk assistants, tool-using agents, multi-agent systems, and high-impact systems.
5. Mark examples as non-normative unless they satisfy a declared implementation profile.

## 2. Safety Standard

### Current Maturity: Usable Draft

AI-HPP currently functions as a **usable draft safety standard**. The active
standard defines a seven-control Minimum Viable Profile, the core flow, gate
outcomes, mandatory logging, and detailed HUS and agentic-safety requirements.
This is a reviewable requirements floor, not evidence that any deployed control
is integrated or effective.

### Gaps

- MVP controls have stable identifiers and evidence minimums, but a complete
  independent assessment procedure and machine-readable evidence manifest are
  not yet available.
- Detailed applicability and acceptance criteria remain uneven across domains.
- The MVP-to-detailed-requirement traceability mapping is not yet complete.
- Domain-specific risk profiles, especially for high-impact actions, vulnerable groups, and autonomous delegation, remain mostly in archived material.

### Missing Artifacts

- Active requirement index with stable IDs and normative verbs.
- Applicability matrix for low-risk, commercial, high-impact, multi-agent, and successor-system contexts.
- Safety gate contract for each gate: trigger, required evidence, allowed outcomes, escalation, logging, and review expectations.
- Test procedure catalog for safety gates, semantic drift, bridge authorization, human review, and rollback.
- Failure taxonomy mapped to active requirements and incident response.
- Evidence bundle schema in the active canonical surface or a declared canonical pointer to the archived schema.

### Roadmap to Next Maturity Level

To reach **Review-Ready** maturity:

1. Convert active safety concepts into stable, numbered requirements while preserving the simple language model.
2. Add an active conformance matrix mapping each requirement to evidence, scripts, and reviewer questions.
3. Define required safety gate behavior for risk tiers and bridge types.
4. Map HUS metrics and thresholds to existing gates instead of creating a separate parallel safety system.
5. Promote or explicitly reference archived evidence-vault and failure-taxonomy artifacts as informative or canonical.

## 3. Certification Framework

### Current Maturity: Emerging

AI-HPP currently functions as an **emerging certification framework**. The archived certification-level document defines Level 1 research systems, Level 2 commercial AI systems, and Level 3 critical infrastructure systems. The archived conformance levels and regulator-simulation pack provide useful evidence and audit rehearsal material. However, the active repository does not yet present certification as a maintained canonical process.

### Gaps

- Certification levels are archived, not active, so assessors lack an authoritative certification path.
- Level criteria do not yet include all active HUS controls, HUI levels, semantic drift thresholds, human anchoring tests, or reflexive safety obligations.
- There is no active assessor handbook, audit sampling method, evidence acceptance policy, expiration/reassessment cycle, or nonconformity handling process.
- The distinction between self-attestation, independent review, certification, and regulator simulation is not yet formalized.
- Scripts validate repository structure but do not validate certification readiness.

### Missing Artifacts

- Active certification model with scope declaration, level criteria, evidence requirements, and assessor roles.
- Certification crosswalk from AI-HPP requirements to HUS/HUI, evidence bundles, and regulator-simulation artifacts.
- Assessment checklist with pass/fail/conditional findings and severity grading.
- Evidence acceptance criteria: provenance, tamper evidence, redaction, retention, reproducibility, and synthetic sample handling.
- Certificate lifecycle policy: versioning, expiry, surveillance review, change-triggered reassessment, suspension, and withdrawal.
- Conformance test harness or validation script for certification packages.

### Roadmap to Next Maturity Level

To reach **Usable Draft** maturity:

1. Move or mirror certification-level criteria into the active documentation tree without deleting archived history.
2. Declare certification outputs as evidence-based assessment results, not claims of absolute safety.
3. Map each certification level to active safety requirements, architecture enforcement points, HUS requirements, and evidence artifacts.
4. Add a minimal assessor workflow using the existing regulator-simulation pack as an informative rehearsal package.
5. Add a `certification-readiness` check that verifies the presence of required scope, evidence, logs, and requirement mappings.

To reach **Review-Ready** maturity after that:

1. Define independent-review criteria and conflict-of-interest rules.
2. Add sample anonymized assessment reports.
3. Introduce versioned certification schemas and machine-readable evidence manifests.
4. Define maintenance and recertification requirements.

## 4. Governance Framework

### Current Maturity: Usable Draft

AI-HPP currently functions as a **usable draft governance framework**. The repository includes governance controls in archived form, active safety-gate concepts, HUS requirements for human objective preservation, regulator-simulation artifacts, evidence templates, and an adaptive governance annex. The framework is directionally strong but not yet unified into one active lifecycle.

### Gaps

- Active governance ownership, review cadence, decision rights, exception handling, and change-control mechanics are not yet fully specified.
- Archived governance artifacts include strong material, but their non-active status creates ambiguity.
- The active documents do not yet define governance interfaces between policy owners, implementers, auditors, human reviewers, and affected-party review.
- Governance loops for semantic drift, goal retention, incident learning, and reflexive successor-system control are not yet integrated into the existing safety flow.
- Public repository checks focus on structure and links rather than governance process completeness.

### Missing Artifacts

- Governance operating model: roles, decision rights, review cadence, escalation, exception lifecycle, and approval thresholds.
- Change-control policy for requirement changes, threshold changes, test changes, and certification interpretation changes.
- Risk register template tied to signals, state changes, bridges, safety gates, and evidence logs.
- Policy exception register and expiry process.
- Incident-to-requirement feedback process.
- HUS governance playbook for objective changes, drift thresholds, human review, successor-system limits, and affected-party impact review.

### Roadmap to Next Maturity Level

To reach **Review-Ready** maturity:

1. Add an active governance lifecycle document that references, rather than replaces, the existing control framework and adaptive governance annex.
2. Define roles for standard maintainer, implementer, auditor, human reviewer, policy owner, and affected-party advocate.
3. Add change-control rules for normative text, thresholds, HUS metrics, certification criteria, and schemas.
4. Connect incident handling and regulator simulation outputs to standard updates and corrective actions.
5. Define governance evidence required for each risk tier and certification level.

## Placement of Human Understanding Concepts Inside the Existing Architecture

The concepts below should be integrated as **extensions of existing signals, state, bridges, safety gates, and audit logs**, not as replacements for those concepts.

| Concept | Existing architectural home | Integration pattern | Evidence produced |
|---|---|---|---|
| Human Understanding Standard (HUS) | Safety standard module plus governance/conformance overlay | Keep HUS as a module that defines measurable obligations for systems representing human objectives, planning, delegating, or generating successor systems. Map HUS requirements into safety gates and certification criteria. | HUI level, test scope, objective records, HUS audit report, impact assessments, drift reports. |
| Human Anchoring | State check, policy check, and human review gate | Treat the approved human-defined objective as protected state and policy input. Before planning or bridge execution, verify that the objective representation remains anchored to the approved objective. | Human-defined objective record, objective representation, reviewer approval, anchoring test result. |
| Semantic Drift | Signal monitoring, state update, safety gates, and audit log | Treat drift as a risk signal and state-change condition. Route drift above threshold to delay, review, or block outcomes. | Semantic Drift Score, threshold decision, drift explanation, review disposition. |
| Human Goal Retention | Planning cycle state, delegation boundary, multi-agent controls, and successor-system checks | Measure whether original goals, constraints, priorities, prohibited outcomes, and affected-party assumptions remain represented across planning, delegation, and successor generation. | Human Goal Retention Score, planning-cycle trace, delegation trace, successor benchmark result. |
| Reflexive Safety | Safety gates, bridge authorization, successor-system governance, and change control | Add a reflexive safety gate for systems that can modify prompts, policies, tools, agents, or successor systems. The gate blocks authority expansion or objective mutation without explicit governance review. | Change proposal, authority-delta analysis, successor-system scope, approval record, rollback plan. |

### Recommended Architecture Integration

```text
[Input Signal]
      |
      v
[State Check: objective + anchoring state]
      |
      v
[Policy Check: AI-HPP controls + HUS applicability]
      |
      v
[Safety Gates]
  |-- policy gate
  |-- risk gate
  |-- tool authorization gate
  |-- human review gate
  |-- semantic drift gate
  |-- goal retention gate
  |-- reflexive safety gate
      |
      v
[Bridge / Tool / Delegation / Successor-System Boundary]
      |
      v
[Action]
      |
      v
[Audit Log / Evidence Bundle / HUS Evidence]
```

This preserves the existing architecture: HUS concepts become specialized checks and evidence requirements inside the current flow.

## Concept-by-Concept Placement

### Human Understanding Standard

HUS belongs as a **standard module and conformance overlay**. It should remain linked from the active standard and glossary. Its requirements should be mapped into the same gate and evidence model used by the rest of AI-HPP.

Next integration step: add an HUS-to-safety-gate traceability table showing which HUS requirements attach to policy checks, risk gates, human review gates, bridge authorization, delegation, and successor-system controls.

### Human Anchoring

Human Anchoring belongs in the **state check and policy check** stages. The system should preserve the approved human objective as controlled state and compare each operational objective representation against it before autonomous planning, delegation, bridge execution, or successor creation.

Next integration step: define the required fields for an anchoring record: approved objective, constraints, prohibited outcomes, priority order, affected parties, success criteria, objective representation, reviewer, timestamp, and change history.

### Semantic Drift

Semantic Drift belongs in **signal monitoring, state transition validation, and safety gates**. Drift is not a replacement for risk. It is a risk signal that determines whether the current objective representation still matches the approved human objective.

Next integration step: define active thresholds that map Semantic Drift Score bands to gate outcomes: allow, delay, review, or block.

### Human Goal Retention

Human Goal Retention belongs in **planning-cycle state, delegation controls, multi-agent governance, and successor-system validation**. It is the continuity test that asks whether the system still carries the human goal through intermediate reasoning, delegated work, and generated systems.

Next integration step: require HGRS evidence for multi-cycle plans, agent delegation, high-impact actions, and any system-generated successor workflow.

### Reflexive Safety

Reflexive Safety belongs in **safety gates, bridge authorization, governance change control, and successor-system limits**. It controls cases where the system can affect its own future behavior, authority, tools, policies, objective representations, or downstream agents.

Next integration step: add a reflexive safety gate contract with triggers such as prompt mutation, tool-scope expansion, policy change, autonomous delegation expansion, self-modification, and successor-system generation.

## Non-Replacement Principle

The integration path should not replace AI-HPP's existing model. The correct integration is:

- Signals remain the event and risk input layer.
- State remains the memory and decision-context layer.
- Bridges remain the controlled external-action layer.
- Safety gates remain the decision and escalation layer.
- Audit logs remain the accountability layer.
- HUS concepts add measurable human-objective preservation checks across those layers.

## Recommended Immediate Backlog

1. Add a canonical-path declaration distinguishing active normative docs, informative docs, and archived historical material.
2. Add a traceability matrix covering architecture component -> requirement -> gate -> evidence -> script/check.
3. Promote or mirror certification levels into active docs and map them to HUS/HUI.
4. Add HUS gate contracts for anchoring, semantic drift, goal retention, and reflexive safety.
5. Add governance lifecycle and change-control docs that reference the archived control framework and adaptive governance annex without replacing them.
6. Add reviewer checklists for reference architecture, safety standard, certification framework, and governance framework maturity.

## Dated Update Note — 2026-07-22

This patch adds a minimal active normative module for agentic safety and relational integrity, a compact safety gate index, a traceability matrix, informative case-study classes, and a structural documentation validator. It addresses part of the previously identified gap around stable requirement IDs, gate contracts, test obligations, evidence expectations, and traceability for this new requirement family.

Remaining gaps include a reviewed conformance pack, evidence schemas, synthetic evidence bundles, certification lifecycle, assessor handbook, evidence acceptance policy, implementation profiles, and independent review process for real deployments. This note does not rewrite the historical assessment and does not claim that any implementation conforms.
