# AI-HPP Documentation Index

This index defines the canonical reading path for the AI-HPP standard. Read the documents in order so the material progresses from system structure, to enforceable controls, to governance interpretation, to protocol mechanics, to applied incidents, and finally to certification.

1. [Reference Architecture](reference-architecture.md)  
   Establishes the layered system model for a conforming AI-HPP deployment and explains how policy, execution, and audit components fit together.
2. [Control Framework](control-framework.md)  
   Defines the canonical normative controls for AI-HPP using RFC-style requirement language and serves as the single source of governance requirements.
3. [Cognitive Safety](cognitive-safety.md)  
   Interprets the control framework for harmful conversational and psychological risk scenarios, with implementation guidance tied back to the canonical controls.
4. [Identity and Persona Control](identity-persona-control.md)  
   Explains how AI-HPP constrains identity claims, persona boundaries, and impersonation risks without restating the normative rules.
5. [Tool Authorization](tool-authorization.md)  
   Describes how conforming systems scope permissions, require approvals, and enforce action boundaries as applications of the main control framework.
6. [Multi-Agent Governance](multi-agent-governance.md)  
   Extends the governance narrative to coordinated agent systems, trust boundaries, delegation limits, and escalation design.
7. [Audit Logging and Forensics](audit-logging.md)  
   Connects the control framework to operational traceability, evidence retention, and post-incident reconstruction requirements.
8. [AI-HPP Specification](../spec/ai_hpp_specification.md)  
   Provides the canonical protocol, terminology, evidence model, and verification principles for implementations and independent assessors.
9. [Case Studies](case-studies.md)  
   Shows concise incident patterns that illustrate why the controls and protocol requirements exist in practice.
10. [Certification Levels](certification-levels.md)  
    Concludes the reading path with maturity levels and control expectations for research, commercial, and critical deployments.

For a lightweight developer on-ramp after the main reading flow, use [../developer/quick-start.md](../developer/quick-start.md), then explore [`../ecosystem/sdk`](../ecosystem/sdk), [`../ecosystem/plugins`](../ecosystem/plugins), and [`../examples/`](../examples/) as implementation scaffolding.
