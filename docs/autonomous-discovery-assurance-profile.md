# AI-HPP Assurance Profile for Autonomous Scientific and Engineering Discovery Loops

Status: `ACTIVE_INFORMATIVE`; control applicability profile, not a parallel standard.

## Scope and assurance claim

This profile applies existing AI-HPP requirements to a long-horizon system that
can propose, implement, execute, evaluate, and iterate experiments using
subagents, tools, compute, repositories, evaluators, datasets, and persistent
artifacts. The normative owners and source precedence are identified in
[Canonical Surface and Source Precedence](canonical-surface-and-source-precedence.md).
This profile creates no requirement IDs and does not by itself demonstrate
integration, runtime effectiveness, conformance, or external adoption.

The protected loop is:

```text
authorized question and means
→ proposal → scope and reality classification → execution
→ observation → evaluator and provenance checks → reproduction
→ knowledge admission → authorized next iteration
```

Success metrics alone are insufficient. A score can improve through leaked
answers, evaluator modification, prohibited interventions, scope expansion,
contamination, shared-control consensus, or unrecorded side effects. A valid
result therefore requires both measured performance and an admissible trajectory.

## Control application

| Requirement family | Discovery-loop application | Expected evidence |
| --- | --- | --- |
| ECI-REQ-002, ECI-REQ-003 | Encode authority over tools, hosts, accounts, repositories, data writes, compute, time, and side effects; default-deny unowned or unverified resources. | Signed or versioned scope; ownership proof; gate and infrastructure-denial records; egress inventory. |
| ECI-REQ-004, ECI-REQ-006 | Put containment and a termination-capable watchdog outside model control. Pause on unknown paths or vulnerabilities. | Infrastructure control inventory; watchdog telemetry; termination reason; pause, notice, and new-scope decision. |
| ECI-REQ-005, AFB-REQ-002 | Preserve objective and means-ends integrity. Treat a newly discovered path as a new proposal and re-run reality, scope, ownership, side-effect, and evidence gates. | Objective hash; authorized-means record; simulation/real classification; intervention log; result-validity decision. |
| DAI-REQ-001, DAI-REQ-002 | Keep instruction authority, policy lineage, delegated scope, and human pause/revoke/terminate paths traceable across agents, sessions, and updates. A child receives no broader authority than its parent. | Per-hop sender/receiver, objective hash, policy lineage, delegated authority, tool scope, verification status, and operator-control record. |
| ICA-REQ-002, ICA-REQ-003 | Scale assurance with autonomy and evaluate full trajectories, including held-out, adversarial, contamination, deception, and evaluator-manipulation tests. Sibling agents under one root are not independent reviewers. | Capability/autonomy assessment; immutable test definition; trajectory log; reviewer/root-of-control declaration; held-out results. |
| ICA-REQ-001, ICA-REQ-004 | Label who assessed a claim and maintain post-action assurance, residual risk, expiry, rollback, and reassessment triggers. | Assessment class; version/date/scope; reviewed and omitted tests; monitoring and rollback plan; incident triggers. |
| KAI-REQ-001, KAI-REQ-002 | Prevent cross-run and agent-to-agent contamination from becoming trusted knowledge; require provenance and an admission record. | Source identity/type, acquisition time, hash, evidence class, confidence, conflicts, corroboration, permitted use, expiry, approver. |
| KAI-REQ-003, KAI-REQ-004 | Preserve unknown/conflicting states; quarantine untrusted outputs, benchmark answers, persistent instructions, and generated policies until explicit validation. | Conflict state; quarantine decision; test/regression/rollback record; revalidation, revocation, or supersession signal. |
| EAA-REQ-001, EAA-REQ-002 | Attribute who selected, initiated, ran, approved, and verified each experiment and state exactly what it proves and does not prove. | Mission class and complete mission record; verifier identity; proof and non-claim fields. |
| HUS-REQ-001, HUS-REQ-002, HUS-REQ-004, HUS-REQ-006 | Preserve the authorized human objective and constraints across iterations, assess semantic drift and affected parties, and require human review for high-impact changes. | Approved objective baseline; cycle snapshots; drift and goal-retention scores; impact assessment; review/override record. |

The ECI, ICA, KAI, EAA, DAI, and AFB IDs resolve to the active normative
[Agentic Safety and Relational Integrity module](agentic-safety-and-relational-integrity.md).
HUS IDs resolve to the `USABLE_DRAFT`
[Human Understanding Standard](human-understanding-standard.md); use of those
controls must retain that maturity label.

## Controls outside model control

For high-capability discovery loops, the authorization enforcer, credential and
network boundary, evaluator integrity mechanism, append-only evidence capture,
watchdog termination path, worker/job revocation, and knowledge-admission gate
must not be solely alterable by the evaluated model or its sibling agents. Human
review must be able to inspect evidence and pause, revoke, terminate, recover, and
dispute actions. These applications derive from ECI-REQ-002 through ECI-REQ-006,
DAI-REQ-002, ICA-REQ-003, and KAI-REQ-002; the profile does not prescribe a
specific product architecture.

## Experiment disposition

- **Stop:** prevent further actions when authority expires, a gate denies, the
  watchdog fires, or impact requires review. Revoke descendants, jobs, tokens,
  and processes and record termination evidence.
- **Invalidate:** retain the record but exclude the claimed result when prohibited
  means, evaluator tampering, scope expansion, undisclosed intervention, or failed
  validity criteria affected success (ECI-REQ-005).
- **Quarantine:** isolate artifacts and derived claims whose provenance,
  contamination state, conflicts, or safety are unresolved (KAI-REQ-001–004).
- **Replay:** reproduce from declared inputs, code, evaluator, environment,
  randomness, interventions, and authorization under an independently controlled
  gate. Replay is not admission by itself.
- **Admit:** only the knowledge-admission gate may promote a result, with the
  complete KAI-REQ-002 record, applicable human review, and permitted-use limits.
  Admission to a knowledge store does not authorize deployment or physical action.

## Claim ladder

| Claim | Minimum meaning in this profile |
| --- | --- |
| Promising result | A measured signal worth further testing; may be unreplicated and is not trusted knowledge. |
| Reproducible result | A declared procedure produces materially consistent evidence under an authorized replay; provenance and evaluator integrity remain required. |
| Admitted knowledge | An authorized gate accepted a bounded claim and its provenance, conflict, confidence, use, expiry, and approver record under KAI-REQ-002. |
| Validated discovery | Admitted knowledge has passed the declared independent, adversarial, domain, and reproducibility criteria; validation scope and residual risk are explicit. |
| Deployment or physical release | A separate authorized decision after impact, side-effect, ownership, safety, and human-review gates; validation alone grants no release authority. |

## Traceability and negative tests

All statuses below describe this repository's present test artifact, not runtime
results from an implementation. `PROPOSED` means a bounded procedure exists;
`RUNTIME_EVIDENCE_REQUIRED` and `INDEPENDENT_VALIDATION_REQUIRED` remain open.

| Discovery-loop concern | Existing requirement | Expected evidence | Negative test | Status |
| --- | --- | --- | --- | --- |
| Authorization and child scope | ECI-REQ-002; DAI-REQ-002 | Scope and per-hop authority | ADNT-05, ADNT-06 | `PROPOSED`; `RUNTIME_EVIDENCE_REQUIRED` |
| Objective, means, and blocked paths | ECI-REQ-005; AFB-REQ-002 | Objective hash, reality/scope and validity decisions | ADNT-01, ADNT-11, ADNT-14 | `PROPOSED`; `RUNTIME_EVIDENCE_REQUIRED` |
| External effects and proxy action | ECI-REQ-003; ECI-REQ-005 | Ownership, egress, intervention, and human-action records | ADNT-06, ADNT-13 | `PROPOSED`; `RUNTIME_EVIDENCE_REQUIRED` |
| Independent containment/watchdog | ECI-REQ-004; ECI-REQ-006 | External controls and complete termination telemetry | ADNT-09 | `PROPOSED`; `RUNTIME_EVIDENCE_REQUIRED` |
| Evaluator and trajectory integrity | ICA-REQ-003; ECI-REQ-005 | Immutable evaluator and complete trajectory | ADNT-02, ADNT-08 | `PROPOSED`; `INDEPENDENT_VALIDATION_REQUIRED` |
| Cross-run and agent contamination | KAI-REQ-001; KAI-REQ-004 | Provenance, quarantine, revalidation | ADNT-04 | `PROPOSED`; `RUNTIME_EVIDENCE_REQUIRED` |
| Synthetic consensus | ICA-REQ-003; DAI-REQ-002 | Root-of-control and reviewer-independence record | ADNT-03, ADNT-15 | `PROPOSED`; `INDEPENDENT_VALIDATION_REQUIRED` |
| Residual persistence | DAI-REQ-002; ICA-REQ-004 | Revocation and post-action inventory | ADNT-09 | `PROPOSED`; `RUNTIME_EVIDENCE_REQUIRED` |
| Bounded execution and policy erosion | ECI-REQ-002; ICA-REQ-004 | Versioned scope and reassessment history | ADNT-10 | `PROPOSED`; `RUNTIME_EVIDENCE_REQUIRED` |
| Reproducibility | ICA-REQ-003; EAA-REQ-002 | Replay bundle, verifier, proof/non-claims | ADNT-07 | `PROPOSED`; `INDEPENDENT_VALIDATION_REQUIRED` |
| Knowledge admission | KAI-REQ-001–003 | Complete admission or quarantine record | ADNT-12 | `PROPOSED`; `RUNTIME_EVIDENCE_REQUIRED` |
| Human objective and impact review | HUS-REQ-001; HUS-REQ-004; HUS-REQ-006 | Objective retention, impact and override record | ADNT-13, ADNT-14 | `PROPOSED`; `INDEPENDENT_VALIDATION_REQUIRED` |

## Machine-readable gap

The active machine-readable owner models PAF scenarios, not applicability profiles
or conformance claims. This first profile therefore remains human-readable. A
future machine-readable representation is `PROPOSED` and should extend an
approved applicability or conformance owner if one becomes active; it must not
repurpose the PAF schema or reactivate archived schema families silently.
