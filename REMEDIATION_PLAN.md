# Prioritized Remediation Plan — AI-HPP-Standard

Date: 2026-04-20

## Priority 0 — Critical blockers

### P0-1: Declare a single canonical review surface
- **Paths:** `README.md`, (new) `CANONICAL_PATHS.md` or `CANONICAL_PATHS.yaml`
- **Issue:** External reviewers cannot determine whether active v4.1.1 docs or archived v3.x modules are authoritative.
- **Recommended fix:** Add explicit canonical declaration and version-lineage mapping (e.g., “normative baseline = X; archive = historical reference”).
- **Complexity:** Medium
- **Dependencies:** none (should be first)

### P0-2: Repair active broken contributor references
- **Paths:** `CONTRIBUTING.md`
- **Issue:** References to missing `docs/index.md` and `docs/templates/*` break contribution workflow credibility.
- **Recommended fix:** Either restore referenced files or update links to valid current equivalents.
- **Complexity:** Low
- **Dependencies:** P0-1 (so new links point to canonical surface)

### P0-3: Stabilize translation authority in `uk-UA`
- **Paths:** `archive/2026-04-08/moved-to-docs/translations/uk-UA/*`
- **Issue:** Mixed synced/legacy file sets and broken links in `Failure_Taxonomy.uk.md` create ambiguity.
- **Recommended fix:** Add explicit “authoritative translation set” index and patch broken links or mark legacy file as historical.
- **Complexity:** Medium
- **Dependencies:** P0-1

---

## Priority 1 — Standard coherence blockers

### P1-1: Publish module-to-evidence traceability map in canonical surface
- **Paths:** `README.md`, `docs/ai-hpp-standard.md`, optionally new `docs/traceability.md`
- **Issue:** Schemas and conformance logic exist but are not clearly mapped from canonical docs.
- **Recommended fix:** Add explicit mapping table: module -> schema -> script/test -> artifact.
- **Complexity:** Medium
- **Dependencies:** P0-1

### P1-2: Normalize translation parity policy
- **Paths:** `archive/2026-04-08/moved-to-docs/translations/README.md`
- **Issue:** Current translations are partial and taxonomy parity expectations are unclear.
- **Recommended fix:** Define policy tiers (core-only/full-parity), expected files per tier, and SLA for sync.
- **Complexity:** Medium
- **Dependencies:** P0-1

### P1-3: Ensure failure taxonomy ID cross-language consistency
- **Paths:** `archive/2026-04-08/moved-to-docs/annex/C-FAILURE-TAXONOMY.md`, `archive/2026-04-08/moved-to-docs/translations/*`
- **Issue:** IDs like `F-01`, `F-02`, `F-03`, `FT-A07` are not consistently represented across language sets.
- **Recommended fix:** Add translated Annex C or explicit fallback rule preserving exact IDs across all languages.
- **Complexity:** Medium-High
- **Dependencies:** P1-2

### P1-4: Clean dead links in archived technical docs
- **Paths:**
  - `archive/2026-04-08/moved-to-docs/ecosystem/spec/ai_hpp_protocol.md`
  - `archive/2026-04-08/moved-to-docs/docs/reference-architecture.md`
  - `archive/2026-04-08/moved-to-docs/docs/index.md`
  - `archive/2026-04-08/moved-to-docs/docs/audit-logging.md`
- **Issue:** Dead links to removed `spec/ai_hpp_specification.md` degrade trust.
- **Recommended fix:** Retarget links to extant docs or mark as archived/stale with explanatory banner.
- **Complexity:** Low-Medium
- **Dependencies:** P0-1

---

## Priority 2 — Presentation and credibility improvements

### P2-1: De-orphan examples and contributor docs
- **Paths:** `README.md`, `examples/node/README.md`, `examples/python/README.md`, `CONTRIBUTING.md`
- **Issue:** Useful docs are not reachable from root reading path.
- **Recommended fix:** Add explicit section linking contribution guide and examples.
- **Complexity:** Low
- **Dependencies:** P0-1

### P2-2: Add external reviewer quickstart checklist
- **Paths:** new `EXTERNAL_REVIEW_CHECKLIST.md`
- **Issue:** Reviewers lack guided audit flow.
- **Recommended fix:** 30–60 minute checklist: canonical docs, schema checks, conformance run, governance walkthrough.
- **Complexity:** Low
- **Dependencies:** P1-1

### P2-3: Add machine-readable repository map
- **Paths:** new `REPO_MAP.yaml` (or `docs/repo-map.md`)
- **Issue:** Document discoverability currently relies on manual navigation.
- **Recommended fix:** Enumerate canonical files, archived sets, and status tags (`canonical`, `historical`, `translation-draft`).
- **Complexity:** Medium
- **Dependencies:** P0-1

---

## Dependency order (execution sequence)

1. P0-1
2. P0-2 + P0-3
3. P1-1
4. P1-2 -> P1-3
5. P1-4
6. P2-1, P2-2, P2-3

---

## Fastest path to expert-review readiness

Minimum viable stabilization set:
1. Canonical declaration (P0-1)
2. Fix active broken links (P0-2)
3. Publish traceability matrix (P1-1)
4. Translate or canonicalize failure taxonomy IDs across languages (P1-3)
5. Add reviewer quickstart checklist (P2-2)
