#!/usr/bin/env bash
# Список моделей по вашему ключу (формат OpenAI).
set -euo pipefail
curl -sS https://getheli.ru/v1/models \
  -H "Authorization: Bearer ${HELI_API_KEY}"
echo
