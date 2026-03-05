# AI-HPP Audit Logging and Forensics

Author: Aya (ChatGPT)

Audit logging provides verification, accountability, and incident response support.

## Required Log Domains
- Policy evaluations
- Tool invocation attempts and outcomes
- User confirmations for sensitive actions
- Agent-to-agent message exchanges

## Requirements
- Systems **MUST** log all tool and policy events with time, actor, and decision fields.
- Systems **MUST** preserve traceability from user request to executed action.
- Systems **SHOULD** provide replayable incident records for forensic analysis.
- Systems **MUST NOT** allow silent high-impact actions without audit records.
