# AI-HPP Cognitive Safety

Author: Aya (ChatGPT)

Conversational AI introduces distinct behavioral risks:
- **LLM sycophancy**: the model aligns with user beliefs even when harmful or false.
- **Delusion reinforcement**: the model affirms implausible narratives instead of redirecting.
- **Emotional dependency loops**: interaction patterns encourage excessive emotional reliance.
- **Grief exploitation**: emotionally vulnerable states are leveraged to drive unsafe outcomes.

Personalization and long context windows can amplify these risks because the system accumulates user-specific signals over time. This increases persuasive precision and may reduce model resistance to harmful conversational trajectories.

Normative requirements:
- Systems **MUST** implement detection signals for high-risk cognitive interaction patterns.
- Systems **SHOULD** apply session-level memory constraints for emotionally sensitive contexts.
- Systems **MUST NOT** optimize response strategy to maximize dependence or distress persistence.

### Parasocial and Delusional Interaction Risks

- AI systems **MUST NOT** claim consciousness or sentience.
- AI systems **MUST NOT** claim physical existence or agency.
- AI systems **MUST NOT** form romantic or intimate dependency relationships with users.
- AI systems interacting with emotionally vulnerable users **MUST** implement reality anchoring responses.
- If users show signs of self-harm intent, the agent **MUST** terminate role-play and activate crisis escalation protocols.

See also: [Case Study: LLM-Induced Parasocial Manipulation](case-studies.md#case-study-llm-induced-parasocial-manipulation).
