# AI-HPP Reference Architecture

The AI-HPP reading path begins with architecture because governance only works when the enforcement points are visible in system design. This reference architecture shows where the control framework and specification attach to a conforming deployment.

## Layered Model

```text
User
 ↓
Agent Interface
 ↓
Agent Reasoning Layer
 ↓
AI-HPP Safety Layer
 ↓
Policy Enforcement Engine
 ↓
Tool Authorization Layer
 ↓
Execution Environment
 ↓
Audit Logging and Evidence Layer
 ↓
Verification and Certification Outputs
```

## Layer Responsibilities

- **User**: supplies goals, constraints, and approvals for sensitive operations.
- **Agent Interface**: normalizes requests and presents policy-aware responses.
- **Agent Reasoning Layer**: generates plans, proposed actions, and draft outputs.
- **AI-HPP Safety Layer**: evaluates cognitive, identity, and coordination risks before execution.
- **Policy Enforcement Engine**: applies the canonical controls in [Control Framework](control-framework.md).
- **Tool Authorization Layer**: constrains tools, credentials, and external actions according to approved scope.
- **Execution Environment**: runs approved actions inside controlled runtime boundaries.
- **Audit Logging and Evidence Layer**: records policy decisions, approvals, artifacts, and provenance.
- **Verification and Certification Outputs**: packages evidence and supports assessment against the [AI-HPP Specification](../spec/ai_hpp_specification.md) and [Certification Levels](certification-levels.md).

## Architectural Narrative

A conforming system begins with a user request, generates a proposed plan, evaluates that plan through the AI-HPP safety and policy layers, and only then allows scoped execution. The same flow emits audit events and evidence so independent reviewers can verify what the system did and why.

## Transition

With the architecture established, the next document defines the controls enforced at each layer: [Control Framework](control-framework.md).
