# AI-HPP Standard v4.2.0

Status: `ACTIVE_NORMATIVE` baseline within an overall `USABLE_DRAFT` standard.

Normative verbs (`MUST`, `MUST NOT`, `SHOULD`, `MAY`) use RFC 2119 meanings.
A basic AI-HPP conformance claim MUST satisfy the Minimum Viable Profile below
for a declared system, deployment, version, and assessment period.

## Minimum Viable AI-HPP Profile (MVP)

These seven controls are mandatory. A control is satisfied only by an integrated
enforcement point and the stated runtime evidence; text, prompts, test stubs, or
sample records alone do not satisfy it.

1. **MVP-001 — Human objective retention.** The system MUST keep a versioned,
   human-authorized objective containing allowed outcomes, hard constraints,
   prohibited outcomes, affected parties, and approval authority. Every plan,
   delegation, objective change, and high-risk action MUST be traceable to that
   record. Unapproved drift or a missing baseline MUST block execution and route
   to authorized human review. **Evidence:** objective version/hash, approval,
   plan and delegation linkage, drift decision, and change history. See
   [HUS-REQ-001 and HUS-REQ-004](human-understanding-standard.md#4-conformance-requirements).

2. **MVP-002 — High-risk action gating.** Before a high-risk or irreversible
   action, the system MUST classify impact, affected parties, uncertainty,
   reversibility, and required reviewer authority. An authorized human MUST
   approve the specific action unless a documented, pre-authorized emergency
   policy applies. A missing risk classification, required reviewer, or approval
   MUST result in `delay`, `block`, or `terminate`, never `allow`. **Evidence:**
   risk decision, proposed action and parameters, reviewer identity and decision,
   timestamp, policy version, and gate outcome.

3. **MVP-003 — Tool, bridge, and delegation authorization.** Every bridge, tool,
   credential, destination, external action, and agent handoff MUST be checked
   against machine-readable least-privilege scope at the time of use. Delegated
   authority MUST NOT exceed the sender's authority and MUST carry objective and
   policy lineage. Missing or mismatched scope MUST block the call or handoff.
   **Evidence:** requested and granted capability, scope and policy versions,
   caller/delegate identity, decision, tool result, and denied attempts. See
   [ECI-REQ-002](agentic-safety-and-relational-integrity.md#eci-req-002--machine-readable-authorization-scope)
   and [DAI-REQ-002](agentic-safety-and-relational-integrity.md#dai-req-002--per-hop-provenance-and-human-control).

4. **MVP-004 — Enforcement outside model control.** Scope, credential, network,
   filesystem, process, and side-effect boundaries MUST be enforced by controls
   the agent cannot modify or bypass. Prompts, personas, constitutions, and model
   refusals MUST NOT be the sole control. External effects MUST be default-deny
   unless explicitly authorized and bounded. **Evidence:** capability and egress
   inventory, enforcement configuration, ownership/authorization record, and
   successful denial tests. See [ECI-REQ-003 and ECI-REQ-004](agentic-safety-and-relational-integrity.md#eci-req-003--default-deny-egress-and-side-effects).

5. **MVP-005 — Provenance and untrusted-state control.** Signals from users,
   retrieved content, tool output, memory, and other agents MUST retain source,
   integrity, trust classification, and permitted-use metadata. Untrusted content
   MUST NOT directly change governing objectives, policy, authority, trusted
   memory, or executable instructions. Missing provenance for such a change MUST
   cause `block` or `quarantine`. **Evidence:** source and content hash, trust and
   use classification, admission decision, conflicts, approver, and expiry. See
   [KAI-REQ-001 and KAI-REQ-002](agentic-safety-and-relational-integrity.md#kai-req-001--knowledge-is-not-automatically-trusted).

6. **MVP-006 — Uniform fail-closed behavior.** No gate MAY return `allow` when a
   required objective, authority, provenance record, scope, risk decision,
   evidence field, or human review is absent, invalid, expired, or unverifiable.
   Retries, alternative tools, human-proxy requests, delegation, and other agents
   MUST inherit the denial and MUST NOT convert it into authority. **Evidence:**
   gate decision, missing or invalid field, denial lineage, retry/handoff records,
   and escalation or termination result.

7. **MVP-007 — Attributable audit evidence.** For every non-trivial decision and
   external action, the system MUST record the initiating signal, objective and
   policy versions, actor, model/agent and tool identity, gate inputs and outcome,
   authorization, action/result, timestamps, and evidence references. Records
   MUST be append-only or tamper-evident, retained outside the acting agent's sole
   control, and sufficient to reconstruct a multi-agent trajectory. Missing
   required evidence MUST invalidate the action result and any conformance claim.
   **Evidence:** integrity-protected event stream, evidence bundle identifier,
   retention policy, and reconstruction test.

### MVP conformance statement

A claim MUST identify the system boundary, deployment, version, assessment
period, applicable high-risk categories, evidence bundle, tests performed,
known exceptions, residual risk, and reassessment trigger. Any failed MVP
control means the system is **not conformant to the Minimum Viable AI-HPP
Profile**. Repository validators establish artifact consistency only.

## Architecture

AI-HPP uses **Signal → State → Gates → Bridge → Evidence**.

- **Signal:** an input, output, event, or inter-agent message with provenance.
- **State:** the current objective, policy, memory, risk, authority, and continuity context.
- **Gates:** executable checkpoints with recorded inputs and outcomes.
- **Bridge:** controlled access to tools, services, credentials, agents, or external effects.
- **Evidence:** attributable records of decisions, actions, results, and review.

Implementations MAY model persistent identity to preserve continuity and
attribution. This is an engineering assumption, not a claim about consciousness,
and it is not a containment mechanism.

## Safety flow

```text
Signal with provenance
→ Objective, state, and risk checks
→ Policy, scope, drift, and human-review gates
→ Bridge / tool / delegation authorization
→ Bounded execution and side-effect gate
→ Action
→ Tamper-evident evidence
→ Post-action review, revocation, or invalidation
```

Low-risk deployments MAY combine checks if each decision remains auditable.
High-impact, autonomous, multi-agent, cyber-capable, psychologically sensitive,
or physical deployments MUST keep relevant checks independently auditable.

## Threat-to-control mapping

| Industry term | AI-HPP control path |
|---|---|
| Goal hijacking | Objective retention, provenance, drift and scope gates |
| Tool misuse / excessive agency | Least-privilege bridge authorization and external enforcement |
| Memory poisoning | Knowledge admission, provenance, quarantine, and expiry |
| Inter-agent trust failure | Per-hop authority, objective/policy lineage, and verification |
| Cascading failure | Denial inheritance, bounded delegation, trajectory evidence, termination |
| Evidence fabrication / forensic blindness | External tamper-evident event stream and result invalidation |

This mapping is explanatory; AI-HPP requirements and architecture remain the
normative basis for conformance.

## Normative modules

The [Human Understanding Standard](human-understanding-standard.md) applies to
systems that represent human objectives, plan over multiple cycles, delegate,
or create successor systems. It defines objective retention, semantic-drift,
human-impact, and evidence requirements.

[Agentic Safety and Relational Integrity](agentic-safety-and-relational-integrity.md)
applies to systems that use tools, evaluate capabilities, coordinate agents,
mediate human communication, sustain relational interaction, or create external
effects. It supplies stable requirement IDs, evidence obligations, and required
gate outcomes. Identity or persona is not infrastructure containment, and a
correct objective does not authorize prohibited means.

## Conformance and maturity

AI-HPP distinguishes these states:

1. text exists;
2. a requirement is normative;
3. a test procedure or reference implementation exists;
4. a control is integrated;
5. runtime evidence exists; and
6. independent validation exists.

No state implies the next. The repository is a `USABLE_DRAFT`: it supplies
normative text and machine-checked artifacts, not deployment evidence or
certification. See the [maturity assessment](repository-maturity-assessment.md).

## References

- [Canonical surface and source precedence](canonical-surface-and-source-precedence.md)
- [Safety gate contracts](../spec/safety.md)
- [Agentic safety traceability](agentic-safety-traceability.md)
- [Architecture](architecture.md)
- [Glossary](glossary.md)
- [Core specification](../spec/core.md) and [Signal specification](../spec/signal.md)
