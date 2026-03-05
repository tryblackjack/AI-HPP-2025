# AI-HPP Quickstart (5-minute integration)

## 1) Initialize project
```bash
aihpp init
```

## 2) Register hypothesis
```bash
aihpp register-hypothesis --id H-001 --title "Model X improves F1 by 5%" --metric f1 --target ">=0.75"
```

## 3) Run experiment
```bash
aihpp run-experiment --hypothesis H-001 --config experiment.yaml
```

## 4) Generate evidence
```bash
aihpp generate-evidence --run-id RUN-001 --out evidence_bundle.json
```

## 5) Verify results
```bash
aihpp verify --bundle evidence_bundle.json
```

## Output
- Verified bundle
- Reproducibility checklist
- Trust score summary
