# AI-HPP Protocol for Ecosystem Integrations

This document maps the canonical [AI-HPP Specification](../../spec/ai_hpp_specification.md) into implementation expectations for SDKs and framework plugins. It does not redefine protocol stages, evidence objects, or verification principles.

## Required SDK Capabilities

An SDK integration SHOULD be able to:

1. register hypothesis and experiment records;
2. capture execution metadata, policy traces, and metrics;
3. generate an evidence bundle aligned with the canonical specification;
4. verify bundle integrity and reproducibility metadata.

## Plugin Adapter Contract

Every plugin adapter SHOULD expose:

- `collect_context()`
- `start_run()`
- `record_metric(name, value, metadata)`
- `finalize_evidence()`
- `verify_bundle(path)`

## Versioning

- Protocol identifier: `aihpp/1.0`
- Backward-compatible optional fields SHOULD use minor version increments.
- Breaking changes MUST use a major version increment.
