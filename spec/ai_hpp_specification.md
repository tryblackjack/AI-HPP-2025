# AI-HPP Specification (v4 Draft)

## 1. Introduction
AI-HPP defines a protocol for registering hypotheses, executing experiments, producing tamper-evident evidence, and verifying reproducibility.

## 2. Terminology
Normative terms are defined in `spec/terminology.md`.

## 3. Threat model
Primary threats: fabricated evidence, replayed runs, model substitution, dataset poisoning, post-hoc cherry-picking, and identity spoofing.

## 4. System architecture
Layers:
1. Registration layer (hypothesis + experiment manifests)
2. Execution layer (runtime and telemetry capture)
3. Evidence layer (signed bundles + integrity metadata)
4. Verification layer (independent replay and policy checks)
5. Governance layer (audit, CAPA, and compliance mapping)

## 5. Data model
Core entities:
- HypothesisRecord
- ExperimentRecord
- EvidenceBundle
- VerificationReport
- TrustAssessment

## 6. Evidence format
An EvidenceBundle MUST contain:
- bundle id + protocol version
- artifact references + checksums
- metrics payload
- signer identity + detached signature
- trusted timestamp metadata
- optional previous-bundle hash pointer

## 7. Validation process
1. Validate schema.
2. Validate integrity hashes.
3. Validate signatures and signer trust policy.
4. Validate timestamp chain and replay protections.
5. Re-execute experiment and compare metrics.
6. Emit verification verdict.

## 8. Reproducibility protocol
Conform to `REPRODUCIBILITY_REQUIREMENTS.md` and `spec/scientific_validation_protocol.md`.

## 9. Security considerations
- algorithm agility for hashing/signatures,
- key rotation/revocation,
- anti-replay nonces and monotonic sequence ids,
- immutable audit logs,
- access control on sensitive evidence.

## 10. Compliance considerations
AI-HPP aligns with AI risk-management and auditability frameworks (e.g., NIST AI RMF mappings in `regulator-sim/CROSSWALK/`).
