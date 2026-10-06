#!/usr/bin/env bash
set -euo pipefail
curl -sS https://getheli.ru/v1/embeddings \
  -H "Authorization: Bearer ${HELI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/text-embedding-3-small",
    "input": "Оплата API в рублях"
  }'
echo
