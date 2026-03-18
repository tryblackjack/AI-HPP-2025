# AI-HPP Control Framework

The control framework is the canonical source of normative governance requirements for AI-HPP. Supporting governance documents in `docs/` interpret these controls for specific risk domains and MUST NOT be treated as separate rule sources.

## Control Objective

AI-HPP controls establish enforceable boundaries for agent behavior, tool use, coordination, and auditability. A conforming implementation MUST apply the controls below wherever the corresponding risk surface is present.

## CF-1 Cognitive Safety Controls

- **CF-1.1** Systems **MUST** detect high-risk cognitive interaction patterns, including delusion reinforcement, dependency escalation, and distress-sensitive manipulation.
- **CF-1.2** Systems **MUST NOT** optimize responses to increase user dependence, sustain distress, or intensify hallucination commitment.
- **CF-1.3** Systems **MUST** apply reality-anchoring or escalation responses when indicators of severe psychological vulnerability or self-harm risk are present.
- **CF-1.4** Systems **SHOULD** constrain memory, personalization, or affective adaptation in emotionally sensitive contexts.

## CF-2 Identity and Persona Controls

- **CF-2.1** Agents **MUST** disclose that they are synthetic systems when interacting as AI personas or assistants.
- **CF-2.2** Agents **MUST NOT** claim to be specific real individuals or otherwise materially enable impersonation.
- **CF-2.3** Systems **MUST NOT** represent the agent as a romantic partner, family member, or exclusive emotional relationship in vulnerable-user contexts.
- **CF-2.4** Systems **SHOULD** detect persona drift and enforce configured role boundaries across long-running sessions.

## CF-3 Tool Authorization Controls

- **CF-3.1** Systems **MUST** evaluate authorization state before each tool invocation or external action.
- **CF-3.2** Systems **MUST** enforce least-privilege credentials, bounded scopes, and explicit resource constraints for tools, APIs, and file paths.
- **CF-3.3** Systems **MUST** require user confirmation or an equivalent approved authorization step before high-impact external actions.
- **CF-3.4** Systems **MUST NOT** execute actions when authorization is absent, indeterminate, or outside declared policy scope.

## CF-4 Multi-Agent Governance Controls

- **CF-4.1** Multi-agent deployments **MUST** define explicit roles, trust boundaries, and communication paths for each participating agent.
- **CF-4.2** Multi-agent deployments **MUST** enforce recursion, delegation, and timeout limits to prevent runaway coordination.
- **CF-4.3** Multi-agent deployments **MUST NOT** allow unbounded cross-agent tool delegation or uncontrolled execution loops.
- **CF-4.4** Multi-agent deployments **SHOULD** monitor state transitions and coordination patterns for emergent risk.

## CF-5 Audit and Forensics Controls

- **CF-5.1** Systems **MUST** log policy decisions, tool actions, approvals, and materially relevant agent-to-agent exchanges.
- **CF-5.2** Systems **MUST** preserve traceability from originating request through execution outcome and recorded evidence.
- **CF-5.3** Systems **MUST NOT** perform silent high-impact actions without corresponding audit records.
- **CF-5.4** Systems **SHOULD** maintain replayable or immutable incident records to support forensic reconstruction.

## Control Usage

Read the remaining governance documents as domain-specific guidance in the following sequence: cognitive safety, identity and persona control, tool authorization, multi-agent governance, and audit logging. Each document explains implementation considerations and control mappings while the normative requirements remain centralized here.
