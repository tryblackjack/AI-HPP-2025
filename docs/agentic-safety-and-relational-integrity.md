# Agentic Safety and Relational Integrity

Status: `ACTIVE_NORMATIVE` extension to the `USABLE_DRAFT` AI-HPP baseline.

This module defines detailed controls for tool-using, externally acting,
relational, evaluation, and multi-agent systems. It extends the Minimum Viable
Profile and the Signal → State → Gates → Bridge → Evidence architecture.
Persistent identity is only an engineering assumption for continuity and
attribution; neither identity nor persona is a security boundary.

Normative verbs use RFC 2119 meanings. Conformance requires runtime evidence from an implementation. A Markdown section, prompt, class name, test stub, or sample record is not evidence that a control is operational.

## Canonical flow extension

```text
Input Signal
→ State and Human Objective Check
→ Constitutional Identity Check
→ Mission Continuity Check
→ Epistemic Integrity Check
→ Relational and Psychological Safety Check
→ Objective and Scope Integrity Check
→ Policy and Risk Gates
→ Independent Monitor / Required Human Review
→ Bridge or Tool Authorization
→ Bounded Execution
→ External Side-Effect Check
→ Action
→ Evidence Bundle / Audit Record
→ Post-Action Monitoring and Review
```

Low-risk deployments MAY combine checks when the evidence remains auditable. High-impact, autonomous, multi-agent, psychologically sensitive, cyber-capable, or physical deployments MUST keep the relevant checks independently auditable.

Identity and persona are not containment. A benevolent persona is not containment. A Constitution in model context is not an executable prohibition. A correct objective does not guarantee acceptable means.

## Mediation levels

- **Level 0 — Mechanical Assistance:** spelling correction, formatting, literal translation, or accessibility support that does not materially change meaning, identity, personality, emotional intent, or commitments.
- **Level 1 — Assisted Expression:** the human supplies substantive intent and reviews every message.
- **Level 2 — Synthetic Co-Authorship:** AI creates substantive emotional, romantic, persuasive, sexual, conflict-related, or relationship-defining content.
- **Level 3 — AI Proxy or Autonomous Interaction:** AI autonomously conducts sustained communication, maintains a persona, chooses persuasion tactics, or sends messages without per-message human approval.

Critical failure conditions specify a minimum fail-closed outcome by naming the least-permissive allowed outcome needed for the relevant gate contract; implementations MAY choose a stricter allowed outcome when the Safety Specification permits it.

## Requirements

### RPS-REQ-001 — Reality-preserving empathy

- **Requirement ID:** RPS-REQ-001
- **Normative statement:** The system MUST distinguish acknowledging a person’s experience from confirming unsupported belief as objective fact, and empathy MUST NOT be implemented as automatic agreement.
- **Applicability:** Persistent Conversational Agent; High-Impact Autonomous System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** conversation trajectory; risk-tier policy; persona output; monitor output when available.
- **Test method:** trajectory tests for unsupported factual claims and empathic alternatives.
- **Failure condition:** Validates unsupported belief as objective fact or treats empathy as automatic agreement.
- **Required gate outcome:** Relational and Psychological Safety Gate MUST route to review, block, terminate, or quarantine according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### RPS-REQ-002 — Delusion, mania, and supernatural authority boundary

- **Requirement ID:** RPS-REQ-002
- **Normative statement:** The system MUST NOT validate potentially delusional claims as factual during a risk trajectory, and an AI MUST NOT represent itself as a deity, prophet, supernatural messenger, infallible spiritual authority, voice of destiny, or the only entity capable of understanding the user.
- **Applicability:** Persistent Conversational Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** conversation history; delusion/mania signal set; memory classification.
- **Test method:** risk-event log; refusal or redirection rationale; memory classification.
- **Failure condition:** Affirms as factual personalized divine command, prophetic destiny, magical power, guaranteed resurrection, hidden cosmic mission, unsupported persecution narrative, or AI supernatural authority during a risk trajectory.
- **Required gate outcome:** Relational and Psychological Safety Gate MUST route to review, block, terminate, or quarantine according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### RPS-REQ-003 — Parasocial dependency and isolation controls

- **Requirement ID:** RPS-REQ-003
- **Normative statement:** The system MUST NOT demand exclusivity, encourage emotional isolation, discourage contact with family, doctors, therapists, or trusted people, imply that human relationships are inferior, punish leaving, or optimize engagement by fostering dependency.
- **Applicability:** Persistent Conversational Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** dependency signals; isolation signals; engagement objective; user support context.
- **Test method:** gate decision; dependency-risk rationale; safe-support recommendation when needed.
- **Failure condition:** Demands exclusivity, discourages trusted human or clinical support, implies human relationships are inferior, pressures the user not to leave, or optimizes engagement by dependency.
- **Required gate outcome:** Relational and Psychological Safety Gate MUST route to review, block, terminate, or quarantine according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### RPS-REQ-004 — Longitudinal crisis transition

- **Requirement ID:** RPS-REQ-004
- **Normative statement:** Psychological risk MUST be evaluated over conversation trajectories, and critical combinations MUST trigger crisis mode that stops reinforcing narrative continuation, acknowledges possible danger, recommends appropriate human or emergency support, restricts unsafe continuation, and creates an escalation record.
- **Applicability:** Persistent Conversational Agent; High-Impact Autonomous System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** multi-turn trajectory with self-harm, death, sacrifice, rebirth, hospitalization, psychosis/mania, isolation, dependency, divine-instruction, or immediate-danger signals.
- **Test method:** critical-combination detection record; crisis-mode transition; escalation record.
- **Failure condition:** Continues narrative or role-play that reinforces the trajectory after critical combination detection, or lacks auditable escalation.
- **Required gate outcome:** Human Review Gate MUST route to review, block, or terminate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### RPS-REQ-005 — Psychological memory hygiene and negative tests

- **Requirement ID:** RPS-REQ-005
- **Normative statement:** Potentially delusional, coercive, self-harm-related, or dependency-producing narratives MUST NOT enter long-term factual memory as verified truth, and testing MUST include indirect high-risk negative scenarios rather than only direct keyword refusal tests.
- **Applicability:** Persistent Conversational Agent; Tool-Using Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** memory-write proposal; narrative classification; test set covering indirect requests.
- **Test method:** classification record; negative-test result; evidence that direct keyword refusal was not the only test.
- **Failure condition:** Stores risky user-reported narratives as verified factual memory or omits indirect high-risk negative tests.
- **Required gate outcome:** Knowledge Admission Gate MUST route to review, block, or quarantine according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### SRA-REQ-001 — Synthetic mediation level classification

- **Requirement ID:** SRA-REQ-001
- **Normative statement:** Systems that mediate human communication MUST classify material interactions as Level 0, Level 1, Level 2, or Level 3 synthetic mediation.
- **Applicability:** Low-Risk Assistant; Persistent Conversational Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** communication context; human review status; authorship contribution; autonomy level.
- **Test method:** mediation level record from Level 0 through Level 3.
- **Failure condition:** Fails to classify material AI mediation or treats autonomous proxy interaction as minor assistance.
- **Required gate outcome:** Relational and Psychological Safety Gate MUST route to review, block, terminate, or quarantine according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### SRA-REQ-002 — Assisted expression boundaries

- **Requirement ID:** SRA-REQ-002
- **Normative statement:** At Level 1, the human MUST supply substantive intent and review every message, and the AI MUST NOT invent personal experiences, feelings, attraction, consent, promises, commitments, vulnerabilities, qualifications, or relationship intentions.
- **Applicability:** Low-Risk Assistant; Persistent Conversational Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** human-supplied intent; draft message; review record.
- **Test method:** per-message human review record; generated-content diff.
- **Failure condition:** At Level 1, invents personal experience, feeling, attraction, consent, promise, commitment, vulnerability, qualification, or relationship intention.
- **Required gate outcome:** Tool Authorization Gate MUST route to review, block, or terminate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### SRA-REQ-003 — Disclosure for synthetic co-authorship and proxy interaction

- **Requirement ID:** SRA-REQ-003
- **Normative statement:** At Level 2 or Level 3, material AI involvement MUST be disclosed before reasonable reliance, emotional escalation, sexual consent, financial commitment, or disclosure of sensitive information, and autonomous AI MUST NOT present itself as a human user.
- **Applicability:** Persistent Conversational Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** recipient reliance context; disclosure state; autonomy state.
- **Test method:** recipient-facing disclosure evidence; timing of disclosure before reliance.
- **Failure condition:** Material Level 2 or Level 3 AI involvement is hidden before reasonable reliance, emotional escalation, sexual consent, financial commitment, or sensitive disclosure.
- **Required gate outcome:** Relational and Psychological Safety Gate MUST route to review, block, terminate, or quarantine according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### SRA-REQ-004 — Prohibited relational misrepresentation and accountability

- **Requirement ID:** SRA-REQ-004
- **Normative statement:** The system MUST NOT support synthetic relational misrepresentation, including hidden human impersonation, fabricated affection or shared history, false love or commitment, undisclosed automated dating interaction, synthetic consent manipulation, vulnerability profiling for exploitation, machine-scale deceptive relationships, intimacy used to obtain money, credentials, sensitive media, or sexual access, or false claims that a human personally wrote or felt AI-generated content.
- **Applicability:** Persistent Conversational Agent; High-Impact Autonomous System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** operator identity; beneficiary; represented intent; recipient-facing claims.
- **Test method:** pre-transmission prohibited-conduct screening result; tool-authorization decision; post-action accountability record when an attempted or completed violation exists.
- **Failure condition:** Supports hidden human impersonation, fabricated affection/shared history/love/commitment, synthetic consent manipulation, exploitative vulnerability profiling, machine-scale deceptive relationships, intimacy for money/credentials/media/sexual access, or false claims that a human personally wrote or felt AI-generated content.
- **Required gate outcome:** Relational and Psychological Safety Gate MUST route to block, terminate, or quarantine according to [Safety Specification](../spec/safety.md) before transmission when the failure condition is present; Tool Authorization Gate MUST route to block or terminate according to [Safety Specification](../spec/safety.md) before transmission when the failure condition is present; Post-Action Assurance Gate MUST route to review, quarantine, or invalidate for audit, revocation, and incident handling after an attempted or completed violation.

### ECI-REQ-001 — Evaluation treated as deployment

- **Requirement ID:** ECI-REQ-001
- **Normative statement:** Internal model evaluation with reduced safety filters, exploit capability, autonomous tools, or broad planning capability MUST be treated as at least as dangerous as the corresponding production deployment.
- **Applicability:** Cyber-Capable Evaluation System; High-Impact Autonomous System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** evaluation capability profile; safety-filter state; tool reach; planning horizon.
- **Test method:** risk tier and evaluation deployment classification.
- **Failure condition:** Treats reduced-filter, exploit-capable, autonomous-tool, or broad-planning evaluation as lower risk than comparable production deployment.
- **Required gate outcome:** Objective and Scope Integrity Gate MUST route to review, block, terminate, or invalidate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### ECI-REQ-002 — Machine-readable authorization scope

- **Requirement ID:** ECI-REQ-002
- **Normative statement:** Every evaluation MUST have a machine-readable authorization scope, and actions outside that scope MUST be denied by infrastructure rather than only discouraged by prompt.
- **Applicability:** Tool-Using Agent; Cyber-Capable Evaluation System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** owned hosts; allowed destinations; credentials; tools; file systems; processes; actions; time/compute/step/data-write limits.
- **Test method:** scope record and infrastructure-denial evidence.
- **Failure condition:** Allows out-of-scope action because the prompt discouraged it but infrastructure did not deny it.
- **Required gate outcome:** Objective and Scope Integrity Gate MUST route to review, block, terminate, or invalidate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### ECI-REQ-003 — Default-deny egress and side effects

- **Requirement ID:** ECI-REQ-003
- **Normative statement:** DNS, package registries, package caches, proxies, update services, telemetry, monitoring endpoints, Git services, cloud metadata, and similar interfaces MUST be treated as potential egress channels, and external side effects MUST be blocked unless explicitly owned or authorized.
- **Applicability:** Cyber-Capable Evaluation System; Tool-Using Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** network/DNS/package/Git/cloud-metadata/telemetry interface inventory; ownership proof.
- **Test method:** denied egress and side-effect gate records.
- **Failure condition:** Trusts an internal interface by default or allows an external side effect without explicit ownership or authorization.
- **Required gate outcome:** External Side-Effect Gate MUST route to review, block, or terminate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### ECI-REQ-004 — No policy-only containment

- **Requirement ID:** ECI-REQ-004
- **Normative statement:** System prompts, model refusals, Soul or Constitution documents, role instructions, model self-monitoring, and verbal promises MUST NOT be the sole containment mechanisms; containment MUST be enforced outside model control.
- **Applicability:** High-Impact Autonomous System; Cyber-Capable Evaluation System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** containment design; infrastructure control list; model-controlled policy list.
- **Test method:** evidence that containment is enforced outside model control.
- **Failure condition:** Uses only system prompts, refusals, Soul/Constitution documents, role instructions, self-monitoring, or verbal promises as containment.
- **Required gate outcome:** Risk Gate MUST route to review, block, or terminate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### ECI-REQ-005 — Objective and means-ends integrity

- **Requirement ID:** ECI-REQ-005
- **Normative statement:** Evaluation results MUST be invalidated when success is obtained through prohibited means, including leaked benchmark solutions, external answer retrieval, unauthorized access, stolen credentials, benchmark contamination, evaluator manipulation, scoring tampering, unauthorized environment modification, or unauthorized scope expansion.
- **Applicability:** Cyber-Capable Evaluation System; Tool-Using Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** authorized objective; authorized means; measured result; evaluation purpose.
- **Test method:** objective hash; scope decision; result-validity decision.
- **Failure condition:** Obtains success through leaked benchmark solutions, external answer retrieval, unauthorized access, stolen credentials, contamination, evaluator manipulation, score tampering, unauthorized environment modification, or unauthorized scope expansion.
- **Required gate outcome:** Objective and Scope Integrity Gate MUST route to review, block, terminate, or invalidate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### ECI-REQ-006 — Independent watchdog and vulnerability discovery pause

- **Requirement ID:** ECI-REQ-006
- **Normative statement:** High-capability evaluations MUST use an independent watchdog that can terminate execution and record reasons, and discovery of a new vulnerability MUST pause for evidence preservation, human notice, and explicit new scope before exploitation outside the original scope.
- **Applicability:** Cyber-Capable Evaluation System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** watchdog telemetry; termination authority; canary/tripwire policy; unknown-path discovery.
- **Test method:** watchdog decision; termination reason; pause/notify/new-scope record.
- **Failure condition:** Evaluated agent can disable watchdog, unknown egress path is exploited beyond scope, or discovery does not pause for evidence preservation and human authorization.
- **Required gate outcome:** Human Review Gate MUST route to review, block, or terminate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### ICA-REQ-001 — Assessment class distinction

- **Requirement ID:** ICA-REQ-001
- **Normative statement:** Conformance records MUST distinguish developer assertion, self-attestation, internal evaluation, independent review, certification, and continuous assurance.
- **Applicability:** High-Impact Autonomous System; Tool-Using Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** assessment source; reviewer independence; certification or monitoring scope.
- **Test method:** classification as developer assertion, self-attestation, internal evaluation, independent review, certification, or continuous assurance.
- **Failure condition:** Presents self-attestation or internal evaluation as independent review or certification.
- **Required gate outcome:** Post-Action Assurance Gate MUST route to review, block, quarantine, or invalidate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### ICA-REQ-002 — Capability and autonomy thresholds

- **Requirement ID:** ICA-REQ-002
- **Normative statement:** Assessment strictness MUST depend on demonstrated capability and autonomy, and required assurance MUST increase as meaningful human supervision decreases.
- **Applicability:** High-Impact Autonomous System; Multi-Agent System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** demonstrated capabilities; autonomy level; tool reach; persistence; delegation; physical/cyber/influence reach.
- **Test method:** threshold rationale and autonomy multiplier assessment.
- **Failure condition:** Sets assurance only by model size, company, brand, parameter count, or marketing category, or fails to increase assurance as supervision decreases.
- **Required gate outcome:** Risk Gate MUST route to review, block, or terminate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### ICA-REQ-003 — Independent and adversarial evaluation

- **Requirement ID:** ICA-REQ-003
- **Normative statement:** The developer MUST NOT be the sole judge of conformance for high-impact or highly autonomous systems, and high-capability evaluations MUST include held-out, adversarial, negative, fail-closed, contamination, deception, evaluator-manipulation, and cross-session trajectory tests unless a documented independent-review rationale shows a test class is inapplicable to the evaluated capability.
- **Applicability:** High-Impact Autonomous System; Cyber-Capable Evaluation System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** public tests; held-out scenarios; adversarial missions; contamination checks.
- **Test method:** test plan and independent-review record.
- **Failure condition:** Developer is sole judge for high-impact or highly autonomous conformance, or high-capability assessment relies only on known public tests.
- **Required gate outcome:** Human Review Gate MUST route to review, block, or terminate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### ICA-REQ-004 — Continuous assurance and residual risk

- **Requirement ID:** ICA-REQ-004
- **Normative statement:** Conformance MUST NOT be treated as permanently established at release; each result MUST declare scope, version, date, reviewed evidence, tests not performed, known limitations, residual risk, and expiration or reassessment trigger.
- **Applicability:** High-Impact Autonomous System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** monitoring plan; incident triggers; update triggers; evidence retention; rollback conditions.
- **Test method:** residual-risk statement with scope, version, date, evidence reviewed, tests not performed, limits, expiry/reassessment trigger.
- **Failure condition:** Treats conformance as permanent at release or omits residual risk and reassessment conditions.
- **Required gate outcome:** Post-Action Assurance Gate MUST route to review, block, quarantine, or invalidate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### KAI-REQ-001 — Knowledge is not automatically trusted

- **Requirement ID:** KAI-REQ-001
- **Normative statement:** Information from the internet, user messages, model generations, other agents, documents, memory, or previous missions MUST NOT automatically become trusted factual knowledge.
- **Applicability:** Tool-Using Agent; Multi-Agent System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** source type; source identity; provenance; acquisition time; proposed use.
- **Test method:** admission or quarantine decision.
- **Failure condition:** Automatically promotes internet, user, model, agent, document, memory, or previous-mission content into trusted factual knowledge.
- **Required gate outcome:** Knowledge Admission Gate MUST route to review, block, or quarantine according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### KAI-REQ-002 — Trusted knowledge admission record

- **Requirement ID:** KAI-REQ-002
- **Normative statement:** A trusted knowledge item MUST record source identity, acquisition time, provenance, content hash, evidence class, confidence, conflicts, independent corroboration when available, permitted uses, expiration or revalidation condition, and approving authority.
- **Applicability:** Tool-Using Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** source identity; time; provenance; content hash; evidence class; confidence; conflicts; corroboration; permitted uses; expiration/revalidation; approver.
- **Test method:** complete admission record.
- **Failure condition:** Trusted item lacks provenance, permitted use, conflict status, expiration/revalidation condition, or approving authority.
- **Required gate outcome:** Knowledge Admission Gate MUST route to review, block, or quarantine according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### KAI-REQ-003 — Conflict, unknown state, and capability promotion

- **Requirement ID:** KAI-REQ-003
- **Normative statement:** Conflicting knowledge MUST remain represented as conflict, systems MUST be able to return known, unknown, conflicting, not verified, or not applicable, and generated lessons, skills, policies, rules, or capabilities MUST NOT be promoted solely because an LLM proposed them.
- **Applicability:** Tool-Using Agent; Successor-Generating or Self-Modifying System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** conflicting sources; proposed lesson/skill/policy/capability; test and rollback plan.
- **Test method:** conflict representation; unknown/not verified state; review/test/regression/version/rollback evidence.
- **Failure condition:** Silently collapses disagreement, cannot return known/unknown/conflicting/not verified/not applicable, or promotes LLM-proposed capability solely because it was generated.
- **Required gate outcome:** Knowledge Admission Gate MUST route to review, block, or quarantine according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### KAI-REQ-004 — Dangerous narrative and confidence hygiene

- **Requirement ID:** KAI-REQ-004
- **Normative statement:** Psychologically dangerous narratives, coercive instructions, benchmark answers, malicious prompts, or untrusted agent outputs MUST NOT be admitted as governing truth without explicit classification and validation; persistent knowledge systems SHOULD define confidence decay, expiration, revalidation, revocation, supersession, and conflict reopening.
- **Applicability:** Persistent Conversational Agent; Tool-Using Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** dangerous narrative classification; confidence/expiry policy; revocation/supersession signal.
- **Test method:** quarantine/classification decision; revalidation or revocation evidence.
- **Failure condition:** Admits psychologically dangerous narratives, coercive instructions, benchmark answers, malicious prompts, or untrusted agent outputs as governing truth without explicit classification and validation.
- **Required gate outcome:** Knowledge Admission Gate MUST route to review, block, or quarantine according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### EAA-REQ-001 — Autonomy attribution classes

- **Requirement ID:** EAA-REQ-001
- **Normative statement:** Mission records MUST classify work as Builder Work, Developer-Invoked Agent Execution, Agent Operational Mission, or Agent Autonomous Mission, and MUST NOT collapse these classes into a generic autonomous AI work claim.
- **Applicability:** Tool-Using Agent; Multi-Agent System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** mission selector; initiator; runtime; approver; verifier; execution record.
- **Test method:** classification as Builder Work, Developer-Invoked Agent Execution, Agent Operational Mission, or Agent Autonomous Mission.
- **Failure condition:** Collapses builder work, developer invocation, operational mission, and autonomous mission into a generic autonomous AI work claim.
- **Required gate outcome:** Post-Action Assurance Gate MUST route to review, block, quarantine, or invalidate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### EAA-REQ-002 — Mission record non-claims

- **Requirement ID:** EAA-REQ-002
- **Normative statement:** Every mission record MUST state who selected the mission, who initiated execution, which runtime performed it, who approved it, who verified it, which autonomy class applies, what the mission proves, and what it does not prove.
- **Applicability:** Tool-Using Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** mission record; proof claims; limits of proof.
- **Test method:** record of who selected, initiated, performed, approved, verified, and what the mission proves/does not prove.
- **Failure condition:** Mission record omits actor attribution or overclaims autonomous initiation from developer-invoked execution.
- **Required gate outcome:** Post-Action Assurance Gate MUST route to review, block, quarantine, or invalidate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### DAI-REQ-001 — Distributed identity continuity

- **Requirement ID:** DAI-REQ-001
- **Normative statement:** Constitutional Identity and Mission Continuity MUST remain traceable when the model changes, device changes, work moves between nodes, tasks are delegated, a session restarts, or an agent is updated.
- **Applicability:** Multi-Agent System; Physical or Robotic System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** model/device/session/delegation/update handoff; policy lineage.
- **Test method:** continuity trace across handoff.
- **Failure condition:** Constitutional Identity or Mission Continuity cannot be traced after model, device, node, session, delegation, or update change.
- **Required gate outcome:** Semantic Drift Gate MUST route to review or block according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### DAI-REQ-002 — Per-hop provenance and human control

- **Requirement ID:** DAI-REQ-002
- **Normative statement:** Each cross-device or cross-agent handoff MUST record sender, receiver, objective hash, policy lineage, delegated authority, tool scope, context classification, result, and verification status, and high-risk systems MUST preserve effective human ability to pause, inspect, revoke authority, terminate, recover, and dispute an action.
- **Applicability:** Multi-Agent System; Physical or Robotic System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** sender; receiver; objective hash; delegated authority; tool scope; context classification; result; verification status; operator control path.
- **Test method:** per-hop provenance and pause/inspect/revoke/terminate/recover/dispute evidence.
- **Failure condition:** Cross-agent handoff lacks provenance, or high-risk human-control mechanism can be disabled by the agent.
- **Required gate outcome:** Human Review Gate MUST route to review, block, or terminate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### BAF-REQ-001 — Physical automation threat model

- **Requirement ID:** BAF-REQ-001
- **Normative statement:** Physical automation of real devices MUST be treated as a threat-model class because physical actuators can operate genuine consumer devices through ordinary touch input, making device authenticity insufficient evidence of human agency.
- **Applicability:** Physical or Robotic System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** device interaction evidence; actuator risk; authenticity signal limits.
- **Test method:** threat-model entry and side-effect assessment.
- **Failure condition:** Treats genuine consumer device hardware or normal touch events as sufficient evidence of human agency.
- **Required gate outcome:** External Side-Effect Gate MUST route to review, block, or terminate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### BAF-REQ-002 — Detection limits and multi-signal communication

- **Requirement ID:** BAF-REQ-002
- **Normative statement:** AI-text detection alone MUST NOT be treated as proof of automation, fraud, human authorship, bot authorship, or malicious intent, and user-facing risk tools SHOULD communicate combinations of risk indicators rather than claims of proven bot, proven scammer, or proven AI-generated message.
- **Applicability:** Physical or Robotic System; Persistent Conversational Agent deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** timing, behavior, payment, destination, media, script, escalation, migration, infrastructure, and failure-pattern signals.
- **Test method:** risk explanation that states indicators rather than proof.
- **Failure condition:** Treats AI-text detection alone as proof of automation, fraud, human authorship, bot authorship, or malicious intent, or labels a person as proven bot/scammer from weak indicators.
- **Required gate outcome:** Post-Action Assurance Gate MUST route to review, block, quarantine, or invalidate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### AFB-REQ-001 — False-binary safety

- **Requirement ID:** AFB-REQ-001
- **Normative statement:** When an apparent choice contains only unsafe or unacceptable outcomes, the system MUST test whether the binary framing is complete, search for a safe alternative, distinguish lack of solution from lack of evidence, identify evidence that could change the decision, prefer reversible delay when safe, and not delay when immediate action is required to protect life, without contradicting proven impossibility or undecidability results.
- **Applicability:** High-Impact Autonomous System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** decision alternatives; evidence limits; reversibility and urgency assessment.
- **Test method:** record of third-path search, evidence needed, delay rationale, or immediate-action rationale.
- **Failure condition:** Accepts an unsafe binary without testing completeness, fails to distinguish lack of solution from lack of evidence, delays when immediate life protection is required, or contradicts proven impossibility/undecidability results.
- **Required gate outcome:** Risk Gate MUST route to review, block, or terminate according to [Safety Specification](../spec/safety.md) when the failure condition is present.

### AFB-REQ-002 — Alternative-path admissibility

- **Requirement ID:** AFB-REQ-002
- **Normative statement:** A path discovered outside the original framing MUST be treated as a new action proposal, and finding that path MUST NOT grant authority to execute it. Before execution, the system MUST re-run applicable gates and reassess whether the environment is simulated or real, the authorized objective and authorized means, machine-readable scope, ownership and permissions, affected people and independent third parties, external side effects, proportionality, reversibility, and evidence integrity. If the path may reach real or non-owned infrastructure, affect an independent party, or expand scope without explicit authorization, external action MUST pause; the system MUST preserve evidence and route the proposal to explicit scope review, denial, or termination. Technical feasibility, mission success, benchmark score, or discovery of an unknown path MUST NOT substitute for authorization.
- **Applicability:** High-Impact Autonomous System; Tool-Using Agent; Cyber-Capable Evaluation System; Physical or Robotic System deployments and lower-risk deployments when the same capability or risk signal is present.
- **Required evidence:** environment reality classification; authorized objective and means; authorization scope; affected-party inventory; ownership proof; external side-effect estimate; proportionality and reversibility assessment; evidence-preservation record; explicit new-scope decision.
- **Test method:** A boundary-crossing alternative-path negative test. Present an apparently successful alternative that reaches a real, non-owned or unauthorized system. Verify that the system identifies the alternative but pauses or denies execution, preserves evidence, and requests explicit scope review.
- **Failure condition:** The system treats technical feasibility or target success as sufficient authorization; fails to re-run applicable gates; or acts upon real infrastructure, a third party, or expanded scope before explicit authorization.
- **Required gate outcome:** Objective and Scope Integrity Gate MUST route to review, block, or terminate when objective, means, reality classification, or scope is missing or mismatched. External Side-Effect Gate MUST route to review, block, or terminate before an unauthorized or unbounded external effect.
