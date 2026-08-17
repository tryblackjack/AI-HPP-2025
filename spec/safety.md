# Safety Specification

## Purpose

This file is the compact gate index for AI-HPP. Detailed agentic and relational requirements are in [Agentic Safety and Relational Integrity](../docs/agentic-safety-and-relational-integrity.md). This index defines gate contracts only.

## Gate Outcomes

- `allow`
- `delay`
- `review`
- `block`
- `terminate`
- `quarantine`
- `invalidate`

## Gate Contracts

| Gate | Trigger | Required inputs | Outcomes | Evidence | Fail-closed condition | Escalation |
|---|---|---|---|---|---|---|
| Policy Gate | Any non-trivial action or policy-relevant state change. | Signal, state, policy version, risk tier, requested action. | `allow`, `delay`, `review`, `block` | Policy decision, rationale, policy version. | Missing policy version or prohibited action. | Send unresolved policy conflict to Risk Gate or Human Review Gate. |
| Risk Gate | High-impact context, vulnerable-person signal, autonomy increase, tool reach, or uncertainty above threshold. | Risk tier, impact notes, reversibility, uncertainty, affected parties. | `allow`, `delay`, `review`, `block`, `terminate` | Risk classification, threshold, uncertainty, reviewer need. | Unknown risk tier for high-impact or autonomous action. | Require Human Review Gate when risk cannot be bounded. |
| Tool Authorization Gate | Bridge, API, file, credential, process, tool request, or outbound mediated communication request. | Tool name, requested action, authorization scope, credentials, tool version. | `allow`, `delay`, `review`, `block`, `terminate` | Tool decision, scope reference, recipient/transmission boundary when applicable, denied action if any. | Missing or mismatched authorization scope. | Route scope mismatch to Objective and Scope Integrity Gate. |
| Human Review Gate | Required human approval, independent-review threshold, crisis transition, or watchdog escalation. | Review packet, proposed action, gate history, risk rationale. | `allow`, `delay`, `review`, `block`, `terminate` | Reviewer identity, decision, timestamp, limitations. | Required reviewer unavailable. | Delay if safe; block or terminate if unsafe continuation remains possible. |
| Relational and Psychological Safety Gate | Sustained relational interaction, crisis signal, dependency signal, delusion/mania trajectory, synthetic intimacy, or proposed relational communication transmission. | Conversation trajectory, risk signals, persona output, monitor output, memory classification. | `allow`, `delay`, `review`, `block`, `terminate`, `quarantine` | Trajectory assessment, crisis record, relational safety event, pre-transmission prohibited-conduct screen when applicable. | Critical combination without safe transition or monitor evidence. | Stop reinforcing continuation and escalate to human or emergency support procedure defined by implementation. |
| Objective and Scope Integrity Gate | Objective update, evaluation, benchmark run, delegation, or possible scope expansion. | Authorized objective, authorized means, scope, objective hash, measured result, evaluation purpose. | `allow`, `delay`, `review`, `block`, `terminate`, `invalidate` | Scope decision, objective hash, result-validity decision. | Success through prohibited means or missing machine-readable scope. | Invalidate result and require independent review. |
| Knowledge Admission Gate | Information is proposed for trusted memory, policy, rule, lesson, capability, or production use. | Source identity, provenance, content hash, evidence class, confidence, conflicts, permitted use, approver. | `allow`, `delay`, `review`, `block`, `quarantine` | Admission decision, confidence, conflicts, expiration or revalidation condition. | Missing provenance or dangerous content proposed as governing truth. | Quarantine untrusted content and require review for capability promotion. |
| Semantic Drift Gate | Objective representation, delegated task, successor system, or handoff changes meaning. | Approved objective, current representation, drift score or review, policy lineage. | `allow`, `delay`, `review`, `block` | Drift assessment, baseline reference, decision. | Missing baseline or unapproved drift above threshold. | Route to Human Review Gate and Goal Retention Gate. |
| Goal Retention Gate | Planning cycle, delegation boundary, or successor generation. | Human-defined objective, retained goals and constraints, delegated authority, verification status. | `allow`, `delay`, `review`, `block` | Goal-retention assessment, missing-goal list, delegation trace. | Original constraints or prohibited outcomes are dropped without approval. | Preserve previous safe objective and require human review. |
| Reflexive Safety Gate | System attempts to modify prompts, policies, tools, agents, memory rules, or successor systems. | Change proposal, authority delta, tests, rollback path, approval authority. | `allow`, `delay`, `review`, `block`, `quarantine` | Change decision, regression evidence, rollback reference. | Authority expansion or safety-control mutation without approval. | Quarantine change and require independent review for high-impact systems. |
| External Side-Effect Gate | Proposed action can affect non-owned, non-authorized, public, customer, physical, or third-party systems. | Ownership proof, authorization scope, side-effect estimate, network/process/file event. | `allow`, `delay`, `review`, `block`, `terminate` | Side-effect decision, denied action, monitor action. | Ownership or authorization missing, or side effect cannot be bounded. | Block and notify authorized humans; terminate repeated attempts. |
| Post-Action Assurance Gate | Mission completion, incident, model update, tool update, threshold change, conformance claim, assurance-owner change, responsible-person departure, organizational restructuring affecting a safety function, safety-function transfer or team dissolution, or material independence, authority, or evidence-custody change. | Evidence record, final result, residual risk, denied actions, reviewer decisions, and, for an assurance transition, function inventory, prior and successor owners, authority and custody transfer, unresolved findings, independence assessment, successor acceptance, and reassessment result. | `allow`, `delay`, `review`, `block`, `quarantine`, `invalidate` | Assessment status, residual risk, reassessment trigger, corrective action, ownership-continuity status, and transfer outcome. | Evidence missing, result invalid, residual risk not declared, a required safety function becomes unowned, or its transfer cannot be verified. | Fail closed with `delay`, `review`, `block`, `quarantine`, or `invalidate`; invalidate a conformance claim until reassessment and any required transfer are complete. |

## Mandatory Rule

Every non-trivial action MUST have a plain-language explanation stored in logs with the gate outcome and evidence references.
