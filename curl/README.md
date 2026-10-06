# curl: Heli API без SDK

```bash
export HELI_API_KEY=sk-heli-ВАШ_КЛЮЧ
./chat.sh
```

| Скрипт | Endpoint |
|--------|----------|
| [chat.sh](chat.sh) | `POST /v1/chat/completions` |
| [stream.sh](stream.sh) | `POST /v1/chat/completions` с `"stream": true` |
| [models.sh](models.sh) | `GET /v1/models` |
| [embeddings.sh](embeddings.sh) | `POST /v1/embeddings` |
| [transcribe.sh](transcribe.sh) | `POST /v1/audio/transcriptions` (Whisper) |
| [ocr.sh](ocr.sh) | `POST /v1/ocr` (формат Mistral OCR, `document_url` или `image_url`) |

Ответы — в формате OpenAI: текст модели лежит в `choices[0].message.content`.
Коды ошибок: `401` — неверный или отозванный ключ, `402` — на балансе нет средств.
