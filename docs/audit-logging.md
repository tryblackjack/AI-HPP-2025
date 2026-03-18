# AI-HPP Audit Logging and Forensics

This document interprets the canonical audit and forensics controls in [Control Framework](control-framework.md#cf-5-audit-and-forensics-controls). It explains the operational evidence required for traceability and incident reconstruction without duplicating the normative control text.

## Log Domains

A conforming implementation should treat the following as core audit domains:

- policy evaluations;
- tool invocation attempts and outcomes;
- user approvals and overrides;
- agent-to-agent exchanges that materially affect execution;
- evidence packaging and verification events.

## Implementation Guidance

A conforming implementation should map the following practices to the canonical controls:

- **Structured event logging** with actor, time, decision, and outcome fields. See **CF-5.1**.
- **Request-to-outcome correlation** across prompts, policy checks, tools, and evidence bundles. See **CF-5.2**.
- **No-silent-action guarantees** for high-impact operations. See **CF-5.3**.
- **Immutable or replayable storage patterns** for incident response and independent review. See **CF-5.4**.

## Transition

With architecture, controls, and governance covered, the next document in the canonical reading path is the [AI-HPP Specification](../spec/ai_hpp_specification.md), which defines the protocol objects, evidence model, and verification principles that make those controls auditable.
