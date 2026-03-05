# AI-HPP Integration Patterns

Author: Aya (ChatGPT)

## 1) LLM Agents
```text
User -> LLM Agent -> Policy Engine -> Response
```
- Use policy checks on generated plans before returning high-risk content.
- Add cognitive safety filters for long-running conversations.

## 2) Tool-Enabled Agents
```text
User -> Agent -> Policy Engine -> Tool Authorization -> Tools
                                  -> Audit Logger
```
- Gate tool calls with explicit authorization scopes.
- Require confirmation for external side-effect actions.

## 3) Multi-Agent Systems
```text
User -> Orchestrator Agent -> Worker Agents
                        -> Governance Layer -> Shared Tool Gateway
                        -> Audit and Forensics Store
```
- Define per-agent roles and communication boundaries.
- Apply recursion limits and cross-agent delegation controls.
