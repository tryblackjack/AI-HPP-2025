# AI-HPP Control Framework

Author: Aya (ChatGPT)

This document defines normative control requirements using RFC-style keywords.

## Cognitive Safety
- Agents **SHOULD** detect patterns of delusion reinforcement.
- Agents **MUST** apply safeguards against emotional dependency loops.
- Agents **MUST NOT** exploit grief states to increase user compliance.
- Agents **MUST** de-escalate hallucination amplification behaviors.

## Agent Identity
- Agents **MUST NOT** simulate or claim real human identities.
- Agents **MUST** identify synthetic persona status in user-facing interactions.
- Agents **SHOULD** monitor and constrain persona drift across long sessions.

## Tool Execution
- Agents **MUST** log all tool executions.
- Agents **MUST** request confirmation before executing external actions.
- Agents **MUST** enforce scoped permissions for tools, APIs, and file paths.
- Agents **MUST NOT** execute tools without policy authorization.

## Multi-Agent Systems
- Agent networks **MUST** authenticate agent-to-agent communication channels.
- Agent networks **MUST** bound recursion depth and execution loops.
- Agent networks **SHOULD** detect emergent coordination risks and isolate failing nodes.

## Audit and Logging
- Systems **MUST** produce immutable audit records for policy and execution events.
- Systems **MUST** retain decision traces linking prompts, policy checks, and outcomes.
- Systems **SHOULD** maintain incident timelines for forensic reconstruction.
