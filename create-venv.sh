#!/usr/bin/env bash

ORIG_DIR="$(pwd)"
cd "$(dirname "$0")"
BIN_DIR="$(pwd)"

python3 -m venv venv
. ./venv/bin/activate
python -m pip install -U pip
python -m pip install -U pylint
deactivate

cd "${ORIG_DIR}"
