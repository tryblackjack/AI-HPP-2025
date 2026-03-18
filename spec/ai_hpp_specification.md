# AI-HPP Specification

The AI-HPP specification is the canonical technical definition of the standard's protocol behavior. It defines the core terminology, protocol objects, evidence model, and verification principles used throughout the repository.

## 1. Scope

AI-HPP specifies how an AI system declares governed activity, records tamper-evident evidence, and supports independent verification. It is designed for agentic systems whose behavior may involve planning, tool use, multi-step execution, and external effects.

## 2. Core Terminology

The following terms are normative within AI-HPP:

- **Hypothesis Record**: a declared claim about system behavior, safety posture, or operational outcome that can be evaluated.
- **Experiment Record**: the registered procedure, inputs, parameters, and environment used to evaluate a hypothesis record.
- **Evidence Bundle**: the integrity-protected package containing execution metadata, artifacts, metrics, and signatures.
- **Verification Report**: the independent assessment produced after validating evidence integrity, provenance, and outcome reproducibility.
- **Provenance**: the traceable lineage of prompts, models, tools, data, code, policies, and execution decisions.
- **Trust Assessment**: the conclusion about whether evidence is complete, authentic, and sufficient for the claimed result.

Related terminology summaries in [`terminology.md`](terminology.md) are informative pointers back to this canonical section.

## 3. Protocol Description

AI-HPP implementations MUST support the following protocol stages:

1. **Registration**  
   The system MUST register the hypothesis record, experiment record, protocol version, and declared control context before execution begins.
2. **Execution**  
   The system MUST capture runtime metadata, policy decisions, tool actions, and outcome artifacts during execution.
3. **Evidence Packaging**  
   The system MUST assemble an evidence bundle that binds artifacts, metrics, provenance metadata, and integrity information to the executed run.
4. **Verification**  
   An assessor MUST be able to validate integrity, authenticate the signer, reconstruct the declared environment, and evaluate reproducibility claims.
5. **Disposition**  
   The implementation SHOULD emit a trust assessment and MAY attach corrective actions, exceptions, or escalation notes when verification is incomplete.

## 4. Protocol Objects

An AI-HPP implementation MUST be able to produce or reference the following objects:

- **Hypothesis Record** containing scope, claim, falsification criteria, and success metrics.
- **Experiment Record** containing datasets, model references, parameters, environment snapshot, and execution plan.
- **Evidence Bundle** containing run identifiers, artifacts, metrics, policy traces, signatures, and timestamps.
- **Verification Report** containing validation results, replay findings, metric comparisons, and final verdict.
- **Trust Assessment** containing the assurance conclusion, observed limitations, and residual risk notes.

## 5. Evidence Model

The evidence model is the canonical basis for auditability in AI-HPP.

### 5.1 Required Evidence Bundle Contents

An evidence bundle MUST contain:

- bundle identifier and protocol version;
- references to all mandatory artifacts with checksums or equivalent integrity digests;
- execution metadata including model, tool, dataset, and environment identifiers;
- policy and authorization decisions relevant to the run;
- metrics payloads and evaluation outputs;
- signer identity and detached or embedded signature metadata;
- trusted timestamp metadata or an equivalent replay-resistant time assertion.

An evidence bundle SHOULD include a previous-bundle hash pointer or equivalent linkage when runs are part of a governed sequence.

### 5.2 Provenance Requirements

Implementations MUST preserve provenance sufficient to trace:

- the originating request or trigger;
- the governing policy set and applicable control decisions;
- all material tool invocations and their outcomes;
- the model, code, and dataset versions used;
- any human approvals, overrides, or escalation events.

### 5.3 Integrity Expectations

Implementations MUST validate integrity using algorithm-agile hashing and signature mechanisms. They MUST support signer revocation handling, MUST resist replay through unique identifiers or monotonic sequencing, and SHOULD preserve evidence in immutable or append-only storage.

## 6. Verification Principles

AI-HPP verification is based on four principles:

1. **Authenticity**  
   Evidence MUST be attributable to a declared signer or trusted execution authority.
2. **Integrity**  
   Evidence MUST be protected against undetected modification.
3. **Reproducibility**  
   An independent assessor SHOULD be able to reconstruct the declared environment and compare outcomes against stated tolerances.
4. **Traceability**  
   A verifier MUST be able to connect the original request, policy decisions, execution activity, and resulting evidence.

A conforming verification workflow MUST, at minimum:

1. validate schema or structural conformance;
2. validate integrity digests and signatures;
3. validate signer trust policy and timestamp assertions;
4. inspect provenance completeness and authorization traces;
5. re-execute or replay the declared procedure when reproducibility is claimed;
6. issue a verification report with pass, fail, or incomplete disposition.

## 7. Relationship to Governance Documents

The documents in `docs/` explain how the control framework applies to cognitive safety, identity, tools, multi-agent governance, and audit operations. They do not replace this specification's protocol and evidence requirements.

## 8. Related Implementation References

- [`scientific_validation_protocol.md`](scientific_validation_protocol.md) expands the verification workflow for research and benchmarking use cases.
- [`../ecosystem/spec/ai_hpp_protocol.md`](../ecosystem/spec/ai_hpp_protocol.md) maps this specification into SDK and plugin integration expectations.
