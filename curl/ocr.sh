#!/usr/bin/env bash
# OCR, совместимый с Mistral OCR: на выходе страницы в markdown.
# Использование: ./ocr.sh https://example.com/scan.pdf
set -euo pipefail
curl -sS https://getheli.ru/v1/ocr \
  -H "Authorization: Bearer ${HELI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"mistral-ocr-latest\",
    \"document_url\": \"${1:-https://example.com/scan.pdf}\"
  }"
echo
