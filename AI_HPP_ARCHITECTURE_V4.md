# AI_HPP_ARCHITECTURE_V4

## System design
AI-HPP v4 is structured as a protocol stack with normative specification, implementation interfaces, and verification tooling contracts.

## Evidence flow
1. Register hypothesis.
2. Register experiment with locked references.
3. Execute run and collect telemetry.
4. Produce signed evidence bundle.
5. Verify integrity and reproducibility.
6. Emit trust assessment.

## Trust model
Trust Model v2 combines integrity, reproducibility, provenance, security hygiene, and governance conformance using a transparent weighted formula.

## Reproducibility pipeline
The pipeline requires dataset/model/code/environment references and independent rerun validation before high-confidence claims are granted.

## Credibility claim
AI-HPP can credibly claim to be a reproducibility and provenance protocol **when** implementations enforce mandatory evidence, signature/timestamp checks, and independent verification.

## 4. Cryptographic Security Primitives (v4.1)

### 4.1 Zero-Trust Agentic Handoffs (ZTAH)
Every inter-agent handoff SHALL be treated as untrusted until cryptographically verified. Each handoff packet (prompt, retrieved context, constraints, tool-intent metadata) is serialized into a canonical payload and signed with agent-scoped Ed25519 (preferred) or ECDSA keys.

**Control flow:**
1. Orchestrator issues short-lived signing credentials to each agent identity with explicit scope and expiry.
2. Sender agent signs `(payload_hash || parent_policy_hash || nonce || timestamp || delegate_scope)`.
3. Receiver verifies signature, key validity, policy lineage, and nonce monotonicity before parsing payload contents.
4. Verification failure forces deny-by-default execution and mandatory Evidence Vault emission.

**Security objective:** Prevent instruction override, policy laundering, and unauthorized authority inheritance during delegated execution.

### 4.2 Cryptographic Circuit Breakers (CCB)
Classical monitoring is observational; CCB introduces mathematically enforced action control. Runtime orchestration maintains an approved Markov Decision Process (MDP) safe graph `G_safe = (S, A, P, C)`, where `S` is state, `A` actions, `P` transition probabilities, and `C` hard constraints.

**Trigger logic (normative):**
- Let observed transition be `T_obs = (s_i, a_j, s_k, p_obs)`.
- If `T_obs ∉ G_safe` **or** `|p_obs - p_ref| > epsilon_risk(s_i, a_j)` **or** recursion depth exceeds bounded chain threshold, breaker SHALL trigger.
- On trigger, the action-authorization key for the current chain is cryptographically revoked, pending human re-authorization.

**Result:** Unsafe chains are stopped at the cryptographic capability layer, not merely flagged post-facto.

### 4.3 Semantic Isolation Layers (SIL)
SIL extends VDM-style isolation from process boundaries into memory semantics.

**Required separation domains:**
- `D_policy`: immutable system and governance prompts.
- `D_state`: mutable agent state and execution memory.
- `D_user`: untrusted user/task content.
- `D_tool`: tool outputs and external artifacts.

**Enforcement model:**
- Distinct memory regions and access control labels per domain.
- One-way typed mediation channels between domains (no raw concatenation of `D_user -> D_policy`).
- Boundary hashing and attestation at each context assembly step.

**Security objective:** Block prompt leaking, context poisoning, and latent cross-contamination in multi-agent runtime stacks.

### 4.4 Integration with HITL and Evidence Vault
These primitives do not replace core AI-HPP principles; they harden them.

- **Cryptographic HITL evolution:** Human approvals now bind to specific payload hashes and action keys, preventing post-approval substitution.
- **Evidence Vault upgrade:** Vault records include signatures, key IDs, transition attestations, breaker events, and isolation boundary proofs.
- **Operational effect:** HITL remains the governance authority while cryptographic controls provide pre-execution enforcement and non-repudiable forensic traceability.
