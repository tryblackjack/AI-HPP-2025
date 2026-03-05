# AI-HPP Tool Authorization

Author: Aya (ChatGPT)

Tool authorization governs whether an agent can perform actions beyond text generation.

## Control Scope
- API access
- File system access
- External actions (messages, purchases, configuration changes)

## Requirements
- Agents **MUST** evaluate authorization before each tool invocation.
- Agents **MUST** use least-privilege credentials and bounded file scopes.
- Agents **MUST** request user confirmation for high-impact external actions.
- Agents **MUST NOT** execute actions when authorization state is indeterminate.
