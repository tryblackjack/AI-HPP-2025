# REPRODUCIBILITY_REQUIREMENTS

## Mandatory artifact set

1. **Dataset reference**
   - canonical dataset id, version, checksum, and license.
2. **Model reference**
   - model id/version, weight checksum, base model lineage.
3. **Code snapshot**
   - VCS commit hash, dependency lockfile, build instructions.
4. **Experiment parameters**
   - hyperparameters, seeds, selection criteria, stop conditions.
5. **Environment snapshot**
   - OS/container image, hardware profile, runtime/toolchain versions.

## Minimum reproducibility package
- `hypothesis.json`
- `experiment_manifest.json`
- `evidence_bundle.json`
- `verification_report.md`

## Acceptance checks
- All references resolvable.
- Integrity checks match declared digests.
- Experiment rerun produces metric deltas within tolerance.
- Reviewer can reproduce in <= 1 working day without private tribal knowledge.
