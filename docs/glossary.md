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
