# AI-HPP Threat Model (Root)
Version: 4.1.1

AI-HPP protects people and the environment from malicious AI behavior.
The threat model describes simple questions:

**1. What could go wrong?**
- the agent performs an action without verification
- the model produces false data
- plugins provide dangerous access
- the human loses control

**2. What can we do to prevent this?**
- each step is verified by another agent
- a human can always stop
- all actions are recorded
- cryptography confirms authorship

**3. Where can I find the details?**
See annex/A-THREAT-MODEL.md (extended version).

This is a minimal, understandable version, so it can be understood by an engineer, an AI agent, and a child.
