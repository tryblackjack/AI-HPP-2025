# CLI_REFERENCE

## `aihpp init`
Create protocol scaffolding: manifests, evidence folder, verification config.

## `aihpp register-hypothesis`
Register a falsifiable claim with required metric and target.

Required flags:
- `--id`
- `--title`
- `--metric`
- `--target`

## `aihpp run-experiment`
Execute pre-registered experiment and capture runtime metadata.

## `aihpp generate-evidence`
Build signed evidence bundle from run artifacts.

## `aihpp verify`
Validation pipeline:
1. schema check
2. hash check
3. signature check
4. timestamp/replay check
5. reproducibility completeness check
6. trust score computation
