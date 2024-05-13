#!/bin/bash

export PYTHONPATH="$(pwd):$PYTHONPATH"


SERVE_ARGS=$((python3 parse_utils/entry.py "$@") 2>&1)


python3  -m vllm.entrypoints.openai.api_server "$SERVE_ARGS"

