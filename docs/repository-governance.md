# Repository Governance

Status: `ACTIVE_INFORMATIVE`.
Owner: Repository maintainers
Last updated: 2026-08-06

## Purpose

This document records the repository controls expected for changes to AI-HPP. It
does not claim that a hosting provider has enabled those controls; the live
repository settings remain the authoritative evidence for their enforcement.

## Scope

This guidance covers the default branch, repository metadata, and pull-request
lifecycle. It does not define standard conformance or runtime assurance.

## Guidance

## Protected default branch

The `main` branch SHOULD be protected against direct or unreviewed changes. Its
ruleset should:

- require a pull request before merge;
- require approval from the repository owner identified by
  [`.github/CODEOWNERS`](../.github/CODEOWNERS);
- dismiss stale approvals when a reviewable change is pushed;
- require conversation resolution;
- prohibit merge while required checks are pending or failing; and
- apply the rules to administrators unless a documented emergency exception is
  being exercised.

The human-readable workflow names are:

- `Repo Structure Validator`;
- `AI-HPP Standard Audit`; and
- `Spec Consistency Checker`.

Branch protection must use the exact status-check contexts emitted by the jobs,
not these workflow display names. The corresponding required-check contexts are:

- `validate-structure`;
- `audit`; and
- `spec-check`.

The post-merge `Auto-Archive Repository Clutter` workflow is an additional
repository-hygiene control. It is not a substitute for the pre-merge checks.

## Repository metadata

Hosting metadata MUST describe the project consistently with its declared
maturity. Until runtime effectiveness and certification are supported by
appropriate evidence, the recommended repository description is:

> Emerging evidence-oriented standard for bounded, reviewable long-horizon AI
> behavior. USABLE_DRAFT; runtime effectiveness and certification are not
> claimed.

Metadata is informative and MUST NOT override the canonical surface or maturity
assessment.

## Pull-request lifecycle

Maintainers SHOULD close obsolete pull requests promptly and identify the
change that superseded them. A supersession comment should name the merged pull
request and immutable commit identifier so that reviewers can reconstruct the
decision without treating stale work as an active alternative.

These controls govern repository changes only. Passing them demonstrates
repository consistency and review discipline, not runtime conformance or control
effectiveness.

## Evidence

Reviewers should inspect the hosting provider's live branch rules, check runs,
repository metadata, pull-request history, and merge commits. This document and
`CODEOWNERS` express the intended policy but do not prove that the provider
enforces it.
