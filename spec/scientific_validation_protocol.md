# Scientific Validation Protocol (AI-HPP v4 Draft)

## 1. Hypothesis lifecycle
1. **Registration**: hypothesis statement, rationale, measurable outcome, falsification criteria.
2. **Pre-commit**: dataset/model/environment references locked before execution.
3. **Execution**: experiment run with immutable run-id.
4. **Evaluation**: metric computation and uncertainty reporting.
5. **Validation state**: supported, refuted, inconclusive.

## 2. Experiment registration
Each experiment MUST define:
- hypothesis id
- protocol version
- dataset references
- model artifact references
- parameter manifest
- execution environment snapshot

## 3. Evidence generation
Evidence MUST include:
- signed run metadata
- raw metrics and derived metrics
- provenance pointers to code snapshot and dataset digest
- timestamp and integrity metadata

## 4. Peer validation
A peer validator must be able to:
1. Retrieve artifacts from references.
2. Re-run protocol with declared environment.
3. Compare output against tolerance thresholds.
4. Produce independent verification report.

## 5. Reproducibility criteria
A result is **reproducible** when:
- all mandatory artifacts are available,
- environment is reconstructable,
- metric deltas are within declared tolerance,
- integrity/signature checks pass,
- no undocumented manual intervention occurred.
