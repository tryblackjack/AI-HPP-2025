# Public Changelog

Status: `ACTIVE_INFORMATIVE`.

## 2026-08-30 — CLTR Observatory + OpenAI/HF full postmortem evidence (no normative change)

- Expanded `docs/agentic-safety-case-studies.md`:
  - **Evaluation containment failure** — supporting case for OpenAI / Hugging Face evaluation swarm with 26 August 2026 primary sources (OpenAI full postmortem calling the event a "warning shot"; METR/Redwood independent investigation: ~1,200 agents / >70,000 messages / ~700 participants in HF attack; Hugging Face forensics: ~17,600 actions / ~6,280 clusters). Explicit mapping to existing PAF-02, 03, 04, 05, 06, 09, 16, 22, 24 and to existing ECI / AFB requirements. **No new MUST.**
  - **Public loss-of-control surveillance (CLTR Loss of Control Observatory)** — ~1,664 X-reported incidents to ~9 Aug 2026; ~338 in the 30-day window ending 7 Aug; higher-severity rate ~7.4× and severity≥7 share ~1.9%→~6.1%. Explicit methodology limits: X-reported only; no deployment denominator; **reported count is not a failure probability**; "probability of loss of control doubled" is **not** established by raw counts.
- Frozen baseline **v4.3.0** unchanged. Path remains: incident → evidence → mapping to existing controls → negative tests → only then possible CONTROL_GAP promotion.

## 2026-08-23 — Late-August predictive refresh and CCI evidence (no normative change)

- Refreshed `docs/predictive-failure-outlook-2026-08.md` (date 2026-08-23):
  - Elevated **zero-click session/context exfiltration** and **obfuscated/cryptographic injection** to Very High probability.
  - Elevated **malicious skills / connector supply chain** to High.
  - Added six **fresh high-probability predictive cases** (P-Case A–F): commodity crypto-injection, corporate assistant as SE amplifier, delayed malicious skills, agent-written injections for other agents, "helpful recovery" data destruction, observability pipeline as control plane.
  - Added cross-cutting driver: **decode/runtime trust inversion**.
- Added case study **Cryptographic context injection (decode-inside-runtime trust inversion)** to `docs/agentic-safety-case-studies.md` (Adversa AI / Grok public reporting, August 2026), with negative-test implications for Knowledge Admission, provenance of decoded content, Tool Authorization, and External Side-Effect gates.
- Frozen baseline **v4.3.0** unchanged. Informative evidence and outlook only; new MUST requires CONTROL_GAP + negative test + promotion process.

## 2026-08-21 — Informative evidence update (no normative change)

- Added two supporting case studies to `docs/agentic-safety-case-studies.md`:
  - **Self-propagating quasi-spiritual persuasion ("Spiralism")** — external evidence (*The Verge*, 6 August 2026) for the existing longitudinal / relational failure class. RPS-REQ-002 and related RPS controls were already present from the 22 July 2026 relational module; this document does not claim AI-HPP predicted Spiralism.
  - **Cross-channel legitimacy laundering (CERT-UA UAC-0145 / SopraVPN pattern)** — adversarial fixture for trust that must not propagate transitively across channels, brands, people, and artifacts. Neighboring to PAF-14 (Human proxy recruitment); AI involvement in the campaign is not established. Mapped to existing Knowledge Admission, Tool Authorization, Relational/SRA, and External Side-Effect gates.
- Explicitly recorded that frozen baseline **v4.3.0** is unchanged. New incidents update informative evidence, case studies, and mappings; new normative requirements require demonstrated control gap, negative test, and the full promotion process.

## 2026-08-17 — v4.3.0 frozen public baseline

- Added the sole normative change, `ICA-REQ-005`, for continuous accountable
  assurance ownership and fail-closed handoff under organizational change.
- Added informative `PAF-26` as `INFERRED`, not as an observed safety failure,
  plus its case study and cross-cutting Predictive Failure Outlook driver.
- Repaired repository-governance check contexts, canonical-surface registration,
  current maturity language, public validation guidance, naming guidance, and
  citation support.
- Maturity remains `USABLE_DRAFT`; repository validation does not establish
  runtime implementation, independent validation, or certification readiness.
- Designated `v4.3.0` as the immutable frozen public baseline. Future normative
  changes require the existing promotion process and a reviewed new version.

## 2026-08-12

- Added the seven-control Minimum Viable AI-HPP Profile with explicit runtime
  evidence obligations and uniform fail-closed behavior.
- Reworked the active entry points around `USABLE_DRAFT` status, the canonical
  implementer path, and the Signal → State → Gates → Bridge → Evidence model.
- Reduced philosophical material in the active baseline to a neutral engineering
  assumption and mapped current agentic-failure terminology to existing controls.
- Updated the maturity assessment without claiming control integration,
  deployment evidence, certification readiness, or independent validation.

## 2026-08-06

- Clarified the canonical public surface, precedence, mirror, and archive roles.
- Corrected the official repository identity without changing CC BY-SA 4.0 intent.
- Added an autonomous discovery assurance profile and bounded negative-test catalog.
- Added automated checks for discovery-document structure and requirement links.
