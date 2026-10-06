#!/usr/bin/env bash
# Потоковый ответ (SSE): строки "data: {...}", в конце "data: [DONE]".
set -euo pipefail
curl -sS -N https://getheli.ru/v1/chat/completions \
  -H "Authorization: Bearer ${HELI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek/deepseek-v4-flash",
    "stream": true,
    "messages": [{"role": "user", "content": "Посчитай от 1 до 5 словами."}]
  }'
