# AI-HPP Tool Authorization

This document interprets the canonical tool authorization controls in [Control Framework](control-framework.md#cf-3-tool-authorization-controls). It explains how AI-HPP governs permissions, execution gates, and user approvals without introducing duplicate normative rules.

## Risk Focus

Tool authorization addresses:

- API access;
- file-system access;
- messaging, purchasing, or configuration actions;
- ambiguous or stale authorization state.

## Implementation Guidance

A conforming implementation should map the following practices to the canonical controls:

- **Per-action authorization checks** before each tool use or external effect. See **CF-3.1**.
- **Least-privilege credentialing and resource scoping** for tools, APIs, and paths. See **CF-3.2**.
- **Approval workflows** for high-impact actions that can materially affect users, systems, or third parties. See **CF-3.3**.
- **Hard execution denials** whenever authorization is missing, ambiguous, or outside policy scope. See **CF-3.4**.

## Boundary Conditions

Tool failures become more serious in coordinated agent systems. When one agent delegates actions to another, these controls should be enforced together with [Multi-Agent Governance](multi-agent-governance.md).

## Transition

With single-agent action boundaries defined, AI-HPP next addresses the additional failure modes created by coordinated agent systems.
