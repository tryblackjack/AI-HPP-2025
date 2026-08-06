# Repository Governance

Status: `ACTIVE_INFORMATIVE` repository-control document.

This document records the expected governance controls for changes to the public
AI-HPP repository. It does not add normative AI-HPP requirements and does not by
itself prove that GitHub applies the settings described below.

## Ownership

Repository-wide ownership is declared in [`.github/CODEOWNERS`](../.github/CODEOWNERS).
Changes to the active public surface are expected to receive approval from
`@tryblackjack` before merge.

## Recommended protection for `main`

The `main` branch should be configured to:

- require a pull request before merge;
- require at least one approval, including the applicable CODEOWNER;
- dismiss stale approvals when the proposed changes move;
- require all review conversations to be resolved;
- prohibit merge while required checks are pending or failing; and
- prevent ordinary direct pushes and force pushes.

The required pre-merge checks are exactly:

- `Repo Structure Validator`;
- `AI-HPP Standard Audit`; and
- `Spec Consistency Checker`.

`Auto-Archive Repository Clutter (AI-HPP v4.2 Rules)` is a post-merge repository
maintenance workflow. It is not a substitute for any pre-merge evidence gate.

## Pull-request lifecycle

A pull request that is replaced by another delivery path should be closed rather
than left as an apparently active competing change. The closing record should
name the superseding pull request and, after merge, the immutable merge commit.
A closed superseded pull request is retained as provenance and is not represented
as an independently accepted change.

## Public maturity description

The GitHub About description should remain consistent with the repository's
`USABLE_DRAFT` maturity. Recommended text:

> Emerging evidence-oriented standard for bounded, reviewable long-horizon AI
> behavior. USABLE_DRAFT; runtime effectiveness and certification are not
> claimed.

## Evidence boundary

Committed policy text and CODEOWNERS express the intended repository-control
model. They do not demonstrate that branch protection, required checks, review
rules, or About metadata are currently enforced by GitHub. Enforcement claims
require a direct settings inspection or equivalent GitHub API evidence tied to
the repository and observation time.
