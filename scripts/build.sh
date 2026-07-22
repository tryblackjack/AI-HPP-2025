#!/usr/bin/env bash
set -euo pipefail
python3 scripts/validate.py
python3 scripts/check_agentic_safety.py
echo "Build checks completed."
