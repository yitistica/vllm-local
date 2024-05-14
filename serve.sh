#!/bin/bash

export PYTHONPATH="$(pwd):$PYTHONPATH"

python3 parse_utils/entry.py "$@"

#python3 -m vllm.entrypoints.openai.api_server --port 8000  --model unsloth/llama-3-8b --enable-lora --lora-modules review-lora=$(pwd)/downloaded_model/

