#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

echo "Start training YouTube Algorithm"
source .venv/bin/activate
python educating-youtube-for-me.py
