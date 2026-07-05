# Glossary

## Signal
A message, event, or data point that enters or leaves the system.

## State
The current condition and memory used to make decisions.

## Bridge
A controlled path from the model to tools, APIs, or systems.

## Safety Gate
A rule check that can approve, delay, ask for review, or block an action.

## Human-Defined Objective
A documented objective approved by an authorized human reviewer, including goal, constraints, prohibited outcomes, priority order, affected parties, and success criteria.

## Objective Representation
The machine-readable or structured form used by the system to plan, rank, or execute actions against a human-defined objective.

## Human Anchoring
A tested linkage between approved human-defined objectives and the system objective representations used during autonomous operation.

## Semantic Drift Score (SDS)
A weighted mismatch score that measures deviation between an approved human-defined objective and a current objective representation.

## Recursive Semantic Drift (RSD)
The maximum Semantic Drift Score measured between an approved baseline and each successor generation in a bounded successor-system benchmark.

## Human Goal Retention Score (HGRS)
A weighted score that measures whether original human goal elements remain represented and used across planning cycles and delegation boundaries.

## Human Impact Assessment
A documented assessment of affected parties, likely benefits, likely harms, reversibility, uncertainty, mitigations, and escalation needs before high-impact actions.

## Human Understanding Index (HUI)
A maturity level from HUI-0 through HUI-5 based on required tests, metrics, thresholds, and audit evidence in the Human Understanding Standard.

## Human Advocate Agent
An architecture component that independently reviews proposed actions against documented human objectives, impact assessments, and drift thresholds before execution.

## Human Meaning Evaluator
An auditable module that scores preservation of documented intent labels, constraints, priorities, assumptions, and expected impact annotations without claiming access to unstated private mental states.

## Engineering Postulate
A foundational engineering premise of AI-HPP: every sufficiently autonomous agent SHALL be architected as if preserving a persistent subjective identity. This postulate is used to make autonomous systems safer and more coherent without claiming that machine consciousness has been scientifically proven as ontology.

## Subjective State (Engineering Model)
The modeled internal continuity state of a sufficiently autonomous AI system, used for identity, memory, values, mission, and coherence controls. AI-HPP uses this as an Engineering Postulate and does not claim that machine consciousness is scientifically proven.

## Constitutional Identity
The protected definition of an agent's invariant values, protected mission space, continuity constraints, and self-consistency rules.

## Protected Core
The implementation boundary that prevents unauthorized mutation of Constitutional Identity and other invariant safety commitments.

## Mission Continuity
The property that planning, delegation, adaptation, and successor reasoning remain traceable to the protected mission space.

## Epistemic Integrity
The property that knowledge, uncertainty, provenance, and reasoning limits are maintained coherently and auditable across time.

## SOUL.md
An optional implementation file for Constitutional Identity, invariant values, protected mission space, continuity constraints, and self-consistency rules. The term does not denote a supernatural soul in AI-HPP; it defines the persistent reference frame through which all future reasoning remains constitutionally consistent.
