#!/usr/bin/env bash
# Расшифровка аудио (Whisper). Использование: ./transcribe.sh meeting.mp3
set -euo pipefail
curl -sS https://getheli.ru/v1/audio/transcriptions \
  -H "Authorization: Bearer ${HELI_API_KEY}" \
  -F model=whisper-1 \
  -F file=@"${1:-audio.mp3}"
echo
