# Python: OpenAI SDK + Heli

Официальный пакет `openai` работает с Heli без изменений — меняются только `base_url` и ключ.

```bash
pip install -r requirements.txt
export HELI_API_KEY=sk-heli-ВАШ_КЛЮЧ
```

| Файл | Что делает | Endpoint |
|------|------------|----------|
| [chat.py](chat.py) | обычный запрос к модели | `POST /v1/chat/completions` |
| [stream.py](stream.py) | потоковый ответ (`stream=True`) | `POST /v1/chat/completions` |
| [embeddings.py](embeddings.py) | векторы для поиска и RAG | `POST /v1/embeddings` |
| [transcribe.py](transcribe.py) | расшифровка аудио (Whisper) | `POST /v1/audio/transcriptions` |
| [list_models.py](list_models.py) | список моделей по ключу | `GET /v1/models` |
| [errors.py](errors.py) | обработка 401 и 402 | — |

Модель меняется переменной `HELI_MODEL`, например `HELI_MODEL=anthropic/claude-sonnet-4.6 python chat.py`.
Слаги и цены в рублях — на [getheli.ru/models](https://getheli.ru/models).

Если ваш код уже читает `OPENAI_API_KEY` и `OPENAI_BASE_URL`, можно ничего не менять в коде:

```bash
export OPENAI_API_KEY=sk-heli-ВАШ_КЛЮЧ
export OPENAI_BASE_URL=https://getheli.ru/v1
```
