#!/bin/sh
set -eu
flake8 --version
flake8 .
mypy --version
mypy --ignore-missing-imports .
