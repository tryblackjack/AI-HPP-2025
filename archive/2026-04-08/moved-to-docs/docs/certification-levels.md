# AI-HPP Certification Levels

Certification concludes the AI-HPP reading path by translating the architecture, controls, governance guidance, and protocol evidence model into maturity expectations.

## Level 1 — Research Systems

Applicable to non-production and experimental systems.

A Level 1 system **MUST** demonstrate:

- baseline application of cognitive safety controls;
- tool execution logging and request traceability;
- synthetic identity disclosure;
- basic evidence packaging sufficient for review.

## Level 2 — Commercial AI Systems

Applicable to customer-facing and operational systems.

A Level 2 system **MUST** satisfy Level 1 and **MUST** additionally demonstrate:

- explicit approval gates for high-impact external actions;
- enforced least-privilege authorization scopes;
- persona drift monitoring;
- multi-agent loop and delegation controls where applicable;
- verification-ready evidence bundles aligned with the AI-HPP specification.

## Level 3 — Critical Infrastructure Systems

Applicable to safety-critical and high-consequence environments.

A Level 3 system **MUST** satisfy Level 2 and **MUST** additionally demonstrate:

- deterministic pre-execution policy gates;
- immutable or equivalent tamper-evident audit retention;
- continuous monitoring for emergent multi-agent coordination risk;
- formal incident reconstruction procedures;
- independent verification support with complete provenance.
