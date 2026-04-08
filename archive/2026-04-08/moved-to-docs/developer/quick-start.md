# AI-HPP Developer Quick Start

Author: Aya (ChatGPT)

Integrate AI-HPP as a thin governance layer around your existing agent runtime.

## Minimal Integration Path
Agent
 → Policy Layer
 → Tool Control
 → Logging

## Steps
1. Add policy checks before tool execution.
2. Enforce scoped tool permissions.
3. Log every policy decision and tool action.

## Minimal Pseudocode
```pseudo
response = agent.reason(user_input)
policy_decision = policy_engine.evaluate(response.plan)
if policy_decision == "deny":
    return safe_refusal()
if policy_decision == "confirm_required":
    require_user_confirmation()
result = tool_layer.execute(response.plan, scoped_permissions)
audit.log(user_input, response.plan, policy_decision, result)
return result
```
