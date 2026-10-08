#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m ruff check --select E9,F --ignore-noqa scripts .github/workflow-tests
python3 scripts/validate-source.py
python3 scripts/workflow_contracts.py
python3 -m unittest discover -s .github/workflow-tests -p 'test_*.py' -v
