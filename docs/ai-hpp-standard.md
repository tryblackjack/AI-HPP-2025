# AI-HPP Standard v4.1.1

## Table of Contents

1. [Purpose](#purpose)
2. [Core model](#core-model)
3. [Safety flow](#safety-flow)
4. [Cross-links](#cross-links)

## Purpose

AI-HPP helps teams build AI systems that are safe and understandable.

## Core model

- **Signal**: what the system receives or sends.
- **State**: what the system currently knows.
- **Bridge**: a controlled connection to tools or external services.
- **Safety gates**: checkpoints that can allow, delay, or block actions.

## Safety flow

1. Read input signal.
2. Check state and policy.
3. Pass through safety gates.
4. Use bridge if allowed.
5. Log action with reason.

## Cross-links

- [Architecture](architecture.md)
- [Glossary](glossary.md)
- [Core spec](../spec/core.md)
- [Signal spec](../spec/signal.md)
- [Safety spec](../spec/safety.md)
