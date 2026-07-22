# Translation Consistency Audit — AI-HPP-Standard

Date: 2026-04-20  
Scope: `archive/2026-04-08/moved-to-docs/translations/**`

## Method

- Structural comparison baseline:
  - English module set: `archive/2026-04-08/moved-to-docs/standard/00..12-*.md` (13 files)
  - English annex set: `archive/2026-04-08/moved-to-docs/annex/*.md` excluding README (9 files)
- Sync-pack baseline for translated folders (as declared in translations index): 11 expected files:
  - `README.md`, `INDEX.md`, `AI-HPP-Standard.md`
  - `standard/{05,07,12}`
  - `annex/{README,A,B,G,CEO}`
- Link validation performed across all translation markdown files.
- Failure taxonomy IDs scanned for patterns: `F-##`, `FT-A##`.

---

## Per-language status

## ar
- **Completeness (sync-pack baseline):** 100% (11/11)
- **Completeness (full EN baseline, indicative):** low (3/13 modules, 4/9 annexes)
- **Stale/missing sections:** Missing modules `00,01,02,03,04,06,08,09,10,11`; missing annexes `C,D,E,F,H`
- **Broken references:** none detected
- **Untranslated headings:** none obvious in sampled synced files
- **Taxonomy ID mapping:** no explicit `F-*`/`FT-*` IDs found in scanned files
- **Remediation priority:** P1

## hi
- **Completeness (sync-pack baseline):** 100% (11/11)
- **Completeness (full EN baseline, indicative):** low (3/13 modules, 4/9 annexes)
- **Stale/missing sections:** same coverage gaps as `ar`
- **Broken references:** none detected
- **Untranslated headings:** none obvious in sampled synced files
- **Taxonomy ID mapping:** no explicit `F-*`/`FT-*` IDs found
- **Remediation priority:** P1

## ja
- **Completeness (sync-pack baseline):** 100% (11/11)
- **Completeness (full EN baseline, indicative):** low (3/13 modules, 4/9 annexes)
- **Stale/missing sections:** same coverage gaps as `ar`
- **Broken references:** none detected
- **Untranslated headings:** none obvious in sampled synced files
- **Taxonomy ID mapping:** no explicit `F-*`/`FT-*` IDs found
- **Remediation priority:** P1

## ko
- **Completeness (sync-pack baseline):** 100% (11/11)
- **Completeness (full EN baseline, indicative):** low (3/13 modules, 4/9 annexes)
- **Stale/missing sections:** same coverage gaps as `ar`
- **Broken references:** none detected
- **Untranslated headings:** none obvious in sampled synced files
- **Taxonomy ID mapping:** no explicit `F-*`/`FT-*` IDs found
- **Remediation priority:** P1

## pt
- **Completeness (sync-pack baseline):** 100% (11/11)
- **Completeness (full EN baseline, indicative):** low (3/13 modules, 4/9 annexes)
- **Stale/missing sections:** same coverage gaps as `ar`
- **Broken references:** none detected
- **Untranslated headings:** none obvious in sampled synced files
- **Taxonomy ID mapping:** no explicit `F-*`/`FT-*` IDs found
- **Remediation priority:** P1

## zh
- **Completeness (sync-pack baseline):** 100% (11/11)
- **Completeness (full EN baseline, indicative):** low (3/13 modules, 4/9 annexes)
- **Stale/missing sections:** same coverage gaps as `ar`
- **Broken references:** none detected
- **Untranslated headings:** none obvious in sampled synced files
- **Taxonomy ID mapping:** no explicit `F-*`/`FT-*` IDs found
- **Remediation priority:** P1

## uk-UA
- **Completeness (sync-pack baseline):** 90.9% (10/11) — missing `AI-HPP-Standard.md` (uses legacy-named equivalents)
- **Completeness (full EN baseline, indicative):** low (3/13 modules, 4/9 annexes in synced subset)
- **Stale/missing sections:** same structural gaps as other languages + mixed legacy naming set (`*.uk.md`) increases ambiguity
- **Broken references:** 3 broken links found in `Failure_Taxonomy.uk.md`
- **Untranslated headings:** mixed-language legacy files present; requires manual normalization review
- **Taxonomy ID mapping:** `FT-A07` found, but broader canonical ID set not consistently present in synced translation pack
- **Remediation priority:** P0 (because of broken links + structural ambiguity)

---

## Cross-language consistency findings

1. **All major translation folders are partial relative to full English structure.**
2. **Synced pack consistency is good for ar/hi/ja/ko/pt/zh, but uk-UA is structurally mixed.**
3. **Failure taxonomy IDs are not consistently represented across translations**, mostly because Annex C translation is missing in all synced language sets and only a legacy Ukrainian taxonomy file contains an ID.
4. Translation README metadata indicates AI-generated status for most languages; native review status is incomplete, limiting standards-grade trust.

---

## Priority remediation for translation integrity

1. Publish translation coverage policy (e.g., “core-only” vs “full parity required”).
2. Add Annex C (Failure Taxonomy) translations or provide an explicit canonical fallback-to-English rule.
3. Normalize uk-UA authoritative path set and repair broken legacy links.
4. Add machine-readable translation parity matrix with per-file hash/source-version mapping.
