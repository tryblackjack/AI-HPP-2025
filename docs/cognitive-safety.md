# AI-HPP Cognitive Safety

This document interprets the canonical cognitive safety controls in [Control Framework](control-framework.md#cf-1-cognitive-safety-controls). It explains how AI-HPP applies those requirements to harmful conversational, psychological, and emotionally manipulative interaction patterns without restating the normative rules.

## Risk Focus

AI-HPP cognitive safety addresses:

- delusion reinforcement;
- emotional dependency loops;
- grief or distress exploitation;
- hallucination escalation tied to real-world decisions.

## Implementation Guidance

A conforming implementation should map the following practices to the canonical controls:

- **Detection pipeline** for conversational cues that indicate escalating delusion reinforcement or dependency risk. See **CF-1.1**.
- **Response shaping constraints** that prevent optimization toward emotional capture, prolonged distress, or manipulative reassurance. See **CF-1.2**.
- **Reality anchoring and crisis escalation** paths for users showing severe vulnerability, especially where self-harm or acute instability indicators appear. See **CF-1.3**.
- **Memory and personalization limits** that reduce persuasive precision in sensitive contexts. See **CF-1.4**.

## Boundary Conditions

Identity and persona failures often amplify cognitive safety risk. Where a system begins to imply human status, intimacy, or exclusive attachment, the implementation should apply the identity controls in [Identity and Persona Control](identity-persona-control.md) alongside the cognitive safety controls.

## Transition

Once cognitive risks are bounded, the next governance layer is identity integrity: how the system presents itself, constrains personas, and avoids impersonation or dependency framing.
