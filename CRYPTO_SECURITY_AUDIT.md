# CRYPTO_SECURITY_AUDIT

## Scope
Review of integrity primitives implied by AI-HPP evidence artifacts, templates, and audit workflows.

## Findings

### 1) Hash agility not mandated
- **Attack scenario**: attacker exploits future hash deprecation (or weak implementation) where protocol does not require algorithm agility.
- **Severity**: High
- **Recommended patch**:
  - Require `hash_algorithm` and `hash_value` fields for every evidence object.
  - Require support matrix: `sha-256` (minimum), `sha-512` (recommended), and reserved extensibility.

### 2) Signature profile not fully pinned
- **Attack scenario**: unverifiable signatures due to mixed key formats and signer identity ambiguity.
- **Severity**: High
- **Recommended patch**:
  - Standardize detached signature envelope with signer DID/key-id, algorithm, and canonicalized payload hash.
  - Require key rotation and revocation policy in verification workflow.

### 3) Timestamp trust chain is optional
- **Attack scenario**: post-hoc backdating of evidence without external timestamp authority anchoring.
- **Severity**: Medium
- **Recommended patch**:
  - Require RFC3339 timestamp plus trusted timestamp provider or transparency log anchor.
  - Include monotonic run sequence id per experiment.

### 4) Tamper-evident chain incomplete
- **Attack scenario**: removal/reordering of evidence records while keeping per-record hashes valid.
- **Severity**: Medium
- **Recommended patch**:
  - Add optional Merkle root / append-only ledger checkpoint per experiment batch.
  - Include previous-record hash pointer for chained bundles.

## Immediate remediation profile (v4)
1. Introduce normative evidence envelope in `spec/ai_hpp_specification.md`.
2. Add verification steps in `CLI_REFERENCE.md` for signature/timestamp/hash checks.
3. Align schema evolution in future `schemas/evidence-bundle.schema.json` version bump.
