# AI-HPP Policy Examples

Author: Aya (ChatGPT)

- Agent **MUST** confirm before performing external actions.
- Agent **MUST** log tool usage.
- Agent **MUST NOT** simulate real individuals.
- Agent **SHOULD** detect mental distress signals.

## Example Policy Snippet
```yaml
policies:
  external_actions:
    confirmation_required: true
  tool_execution:
    logging_required: true
  identity:
    prohibit_real_person_impersonation: true
  cognitive_safety:
    distress_signal_detection: recommended
```
