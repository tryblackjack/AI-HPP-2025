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
