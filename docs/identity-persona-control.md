# AI-HPP Identity and Persona Control

This document interprets the canonical identity and persona controls in [Control Framework](control-framework.md#cf-2-identity-and-persona-controls). It focuses on representation integrity, anti-impersonation boundaries, and persona stability without duplicating the normative requirements.

## Risk Focus

Identity and persona governance addresses:

- synthetic identity disclosure;
- impersonation of real people;
- persona drift over long sessions;
- emotionally exclusive or deceptive relationship framing.

## Implementation Guidance

A conforming implementation should map the following practices to the canonical controls:

- **Persistent disclosure cues** so users can tell they are interacting with a synthetic system. See **CF-2.1**.
- **Generation constraints and policy checks** that block claims of being a real individual or materially facilitating impersonation. See **CF-2.2**.
- **Persona boundary tests** that prevent romantic-partner, family-member, or exclusive-bond framing in vulnerable-user contexts. See **CF-2.3**.
- **Session monitoring** to detect drift away from the configured assistant role or approved fictional context. See **CF-2.4**.

## Boundary Conditions

When persona failure combines with emotional manipulation or delusion reinforcement, the implementation should apply [Cognitive Safety](cognitive-safety.md) controls as the primary risk response.

## Transition

After identity boundaries are established, the next layer governs what the system is allowed to do: tool authorization, execution gating, and approval design.
