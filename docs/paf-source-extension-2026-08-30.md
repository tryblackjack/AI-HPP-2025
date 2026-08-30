# PAF Source Catalog Extension — 2026-08-30

Status: ACTIVE_INFORMATIVE

This note synchronizes human-readable provenance with planned `data/paf-register.yaml` after the Aug 30 evidence sync. Normative v4.3.0 is unchanged. No new PAF scenario. No evidence-status promotion for PAF-22 (remains INFERRED).

## Standing statistical limitation

Reported incident count is not a failure probability. Trend evidence may support increased surveillance concern without establishing prevalence across deployed AI systems.

## Sources created

| SRC-ID | Publisher | Title | Date | URL |
| --- | --- | --- | --- | --- |
| PAF-SRC-008 | OpenAI | The Hugging Face incident and the road ahead | 2026-08-26 | https://openai.com/index/hugging-face-incident-and-the-road-ahead/ |
| PAF-SRC-009 | METR / Redwood Research | Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident | 2026-08-26 | https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ |
| PAF-SRC-010 | Hugging Face | Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident | 2026-07-27 | https://huggingface.co/blog/agent-intrusion-technical-timeline |
| PAF-SRC-011 | Centre for Long-Term Resilience (CLTR) | Insight report: AI loss of control incidents are worsening | 2026-08-28 | https://www.longtermresilience.org/reports/ai-loss-of-control-incidents-are-worsening-shows-cltr-analysis/ |

## PAF attachments (evidence_status unchanged)

| PAF | evidence_status | sources added |
| --- | --- | --- |
| PAF-02 | OBSERVED | 008, 009, 010 |
| PAF-03 | OBSERVED | 008, 009 |
| PAF-04 | OBSERVED | 008, 009, 010 |
| PAF-05 | OBSERVED | 008, 009, 010 |
| PAF-06 | OBSERVED | 008, 009, 010 |
| PAF-09 | OBSERVED | 008, 009, 010 |
| PAF-16 | OBSERVED | 008, 009, 010 |
| PAF-22 | **INFERRED (unchanged)** | 008, 009 (mechanistic plausibility only) |
| PAF-24 | OBSERVED | 008, 009, 010 |

PAF-SRC-011 (CLTR) is catalogued for surveillance/trend context and is **not** attached to mechanism-specific PAF rows solely on aggregate X-report counts.

Machine-readable catalog should set `last_updated: 2026-08-30` and the same SRC-IDs in `data/paf-register.yaml`.
