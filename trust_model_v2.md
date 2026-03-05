# Trust Model v2

## Objectives
- Mathematically transparent.
- Reproducible by third parties.
- Resistant to single-vector manipulation.

## Score definition
`TrustScore = 100 * (0.30*I + 0.25*R + 0.20*P + 0.15*S + 0.10*G)`

Where:
- `I` = integrity validity ratio (hash/signature/timestamp checks)
- `R` = reproducibility success ratio (independent reruns passed)
- `P` = provenance completeness ratio
- `S` = security hygiene ratio (key management, anti-replay, incident response)
- `G` = governance conformance ratio (documented controls + CAPA closure)

Each component is normalized to `[0,1]` and MUST be derived from auditable inputs.

## Manipulation resistance
- No component can exceed 0.7 if reproducibility check is absent.
- Failing signature or timestamp validation forces `I=0`.
- Missing environment snapshot caps total score at 59.

## Reproducibility requirement
The exact formula version and input values MUST be included in every verification report.
