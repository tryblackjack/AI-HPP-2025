# AI-HPP Protocol for Ecosystem Integrations

## Purpose
Defines the implementation contract for SDKs and framework plugins.

## Required SDK capabilities
1. Register hypothesis and experiment manifests.
2. Capture execution metadata and metrics.
3. Generate signed evidence bundle.
4. Verify bundle integrity and reproducibility metadata.

## Plugin adapter contract
Every plugin MUST expose:
- `collect_context()`
- `start_run()`
- `record_metric(name, value, metadata)`
- `finalize_evidence()`
- `verify_bundle(path)`

## Versioning
- Protocol: `aihpp/1.0`
- Backward-compatible minor increments for optional fields.
- Breaking changes require explicit major version bump.
