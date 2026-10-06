#!/usr/bin/env bash
# Chat Completions через Heli. Использование: HELI_API_KEY=sk-heli-... ./chat.sh
set -euo pipefail
curl -sS https://getheli.ru/v1/chat/completions \
  -H "Authorization: Bearer ${HELI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-4.1-mini",
    "messages": [{"role": "user", "content": "Привет!"}]
  }'
echo
