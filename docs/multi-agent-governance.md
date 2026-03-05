# AI-HPP Multi-Agent Governance

Author: Aya (ChatGPT)

Multi-agent systems require governance beyond single-agent policy checks.

## Risk Areas
- Agent-to-agent communication misuse
- Recursive planning and execution loops
- Emergent coordination behaviors that bypass intent

## Requirements
- Deployments **MUST** define explicit roles and trust boundaries for each agent.
- Systems **MUST** enforce loop ceilings and timeout controls for recursive workflows.
- Systems **SHOULD** monitor inter-agent state transitions for emergent risk patterns.
- Systems **MUST NOT** allow unbounded cross-agent tool delegation.
