# ATTACK_SURFACE_REPORT

## Simulated adversarial scenarios

### 1) Fake evidence injection
- **Method**: crafted evidence bundle with valid schema but forged signer identity.
- **Result**: succeeds if verifier does not enforce key trust registry.
- **Mitigation**: mandatory signer trust chain validation.

### 2) Replay attacks
- **Method**: resubmit previously valid bundle for a new experiment claim.
- **Result**: succeeds without nonce/sequence enforcement.
- **Mitigation**: experiment-bound nonce + monotonic run id + timestamp window checks.

### 3) Evidence cherry-picking
- **Method**: omit failed runs and publish only favorable outcomes.
- **Result**: succeeds if protocol does not require complete run ledger.
- **Mitigation**: append-only run index and declared stopping policy.

### 4) Model replacement after validation
- **Method**: swap model artifact after benchmark while keeping metadata unchanged.
- **Result**: blocked only when artifact digests are pinned and re-checked at serve time.
- **Mitigation**: deployment attestation + hash pinning.

### 5) Dataset poisoning
- **Method**: subtle injection in mutable dataset source between runs.
- **Result**: succeeds without version-locked dataset digest.
- **Mitigation**: immutable dataset references and content hashes.

## Residual risk summary
Highest residual risk remains in supply-chain and identity validation layers; protocol-level hard requirements reduce but do not eliminate risk.
