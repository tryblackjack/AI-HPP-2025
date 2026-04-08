# Core Terms and Principles

## Core Terms

- Signal
- State
- Bridge
- Safety gate

## Safety Flow

Input signal -> state check -> policy check -> safety gate -> bridge/tool -> auditable output.

## Signal Model (Simplified)

`decision = f(signal, state, policy, risk)`

## Doom-Proofing Principles

1. Fail safe by default.
2. Ask for review on high-risk actions.
3. Keep reversible actions where possible.
4. Always leave an auditable trail.

## Carmack Minimalism Rules

1. Prefer the simplest working design.
2. Remove extra layers that do not improve safety.
3. Keep components small and readable.

## Kawasaki Simplicity Rules

1. Use plain words.
2. One idea per sentence.
3. If a child cannot explain it, rewrite it.
