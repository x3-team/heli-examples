# Heli API Examples — OpenAI-совместимый API нейросетей с оплатой в рублях

Примеры кода и настройки интеграций для [Heli](https://getheli.ru) — собственного OpenAI-совместимого API-шлюза к нейросетям. Через Heli модели ChatGPT (OpenAI), Claude (Anthropic), Gemini, DeepSeek и другие доступны из России по одному ключу `sk-heli-...` с оплатой в рублях: картой российского банка, через СБП или по счёту для ИП и ООО.

Для подключения достаточно заменить base URL на `https://getheli.ru/v1` и подставить ключ Heli. Код на официальных SDK OpenAI, LangChain, n8n и Cursor продолжает работать без переписывания.

## Технические параметры (quick reference)

| Параметр | Значение |
|----------|----------|
| Base URL | `https://getheli.ru/v1` |
| Формат ключа | `sk-heli-...` |
| Авторизация | `Authorization: Bearer sk-heli-...` |
| Совместимость | официальные SDK OpenAI (Python, Node.js) и любой клиент, где можно задать `base_url` / `OPENAI_BASE_URL` |
| Формат моделей | `provider/model`, например `openai/gpt-4.1-mini` |
| Каталог моделей и цены в рублях | [getheli.ru/models](https://getheli.ru/models) |
| Документация | [getheli.ru/docs](https://getheli.ru/docs) |

## Быстрый старт (Python)

```bash
pip install openai
export HELI_API_KEY=sk-heli-ВАШ_КЛЮЧ
```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["HELI_API_KEY"],
    base_url="https://getheli.ru/v1",
)

response = client.chat.completions.create(
    model="openai/gpt-4.1-mini",
    messages=[{"role": "user", "content": "Напиши функцию сортировки на Python"}],
)
print(response.choices[0].message.content)
```

## Быстрый старт (curl)

```bash
curl https://getheli.ru/v1/chat/completions \
  -H "Authorization: Bearer $HELI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic/claude-sonnet-4.6",
    "messages": [{"role": "user", "content": "Привет!"}]
  }'
```

## Примеры в репозитории

| Папка | Что внутри |
|-------|------------|
| [`python/`](python) | OpenAI SDK: chat, streaming, embeddings, Whisper, список моделей, обработка 401/402 |
| [`node/`](node) | npm-пакет `openai`: chat, streaming, embeddings |
| [`curl/`](curl) | запросы без SDK: chat, streaming, models, embeddings, transcriptions, OCR |
| [`langchain/`](langchain) | `ChatOpenAI` и `OpenAIEmbeddings` с base URL Heli |
| [`n8n/`](n8n) | нода OpenAI с Base URL Heli и готовый workflow на HTTP Request |
| [`cursor/`](cursor) | настройка Cursor через Override OpenAI Base URL |
| [`google-sheets/`](google-sheets) | пользовательская функция `=ASK()` в Google Таблицах (Apps Script) |

Ключ во всех примерах берётся из переменной окружения `HELI_API_KEY` (см. [`.env.example`](.env.example)). В Google Таблицах — из свойств скрипта (см. [`google-sheets/`](google-sheets)).

## Поддерживаемые endpoints

| Метод и путь | Назначение |
|--------------|------------|
| `POST /v1/chat/completions` | генерация текста, поддерживается streaming (`stream: true`) |
| `GET /v1/models` | список моделей в формате OpenAI |
| `POST /v1/embeddings` | эмбеддинги (`openai/text-embedding-3-small`, `openai/text-embedding-3-large`) |
| `POST /v1/audio/transcriptions` | расшифровка аудио (`whisper-1`) |
| `POST /v1/audio/speech` | синтез речи (алиасы `tts-1`, `tts-1-hd`) |
| `POST /v1/ocr` | OCR, совместимый с Mistral OCR (`mistral-ocr-latest`) |

## Модели

Модели указываются слагами `provider/model`. Примеры из каталога:

- `openai/gpt-4.1-mini`, `openai/gpt-4.1`
- `anthropic/claude-sonnet-4.6`
- `deepseek/deepseek-v4-flash`, `deepseek/deepseek-chat`
- `google/gemini-2.5-flash`

Полный список и актуальные цены в рублях за 1 млн токенов: [getheli.ru/models](https://getheli.ru/models). Список моделей, доступных по вашему ключу, возвращает `GET /v1/models`.

## Оплата и баланс

- Предоплаченный рублёвый баланс, пополнение один к одному: сколько рублей заплатили, столько и на балансе. Комиссии уже внутри цены токена.
- Способы пополнения: карта российского банка и СБП (Робокасса), USDT, счёт для ИП и ООО (после зачисления — акт в PDF).
- Без подписки и абонентской платы: списание только за фактические запросы.
- Баланс в минус не уходит: при нулевом балансе API возвращает `402 Payment Required`.

## Как получить ключ

1. Зарегистрируйтесь на [getheli.ru](https://getheli.ru) («Создать аккаунт»): по email с подтверждением почты или через Google / Яндекс ID.
2. Скопируйте ключ `sk-heli-...` в кабинете.
3. На один баланс можно выпустить несколько именованных ключей под проекты и сотрудников, отозвать ключ и смотреть статистику по каждому.

## Альтернатива OpenRouter с оплатой в рублях

Heli — это не OpenRouter, а отдельный сервис: собственный шлюз к моделям со своим ключом `sk-heli-...`, адресом `https://getheli.ru/v1` и рублёвым балансом. Его используют как альтернативу OpenRouter, когда нужна оплата картой РФ, через СБП или по счёту для юрлица.

Миграция с OpenRouter или с прямого OpenAI API:

1. Замените base URL на `https://getheli.ru/v1`.
2. Замените ключ на `sk-heli-...`.
3. Проверьте слаги моделей по [каталогу Heli](https://getheli.ru/models): идентификаторы вида `provider/model` часто совпадают.

Пошаговая инструкция: [getheli.ru/docs/openrouter](https://getheli.ru/docs/openrouter).

## Коды ошибок

| Код | Значение |
|-----|----------|
| `401` | неверный или отозванный ключ |
| `402` | недостаточно средств на балансе, пополните его в кабинете |
| `429` | слишком много неуспешных попыток авторизации с одного IP |
| `502` | временная ошибка сервиса |

## Частые вопросы

**Как вызвать API ChatGPT, Claude или DeepSeek из России с оплатой в рублях?**
Получите ключ `sk-heli-...` на getheli.ru, пополните баланс картой РФ или через СБП и отправляйте запросы на `https://getheli.ru/v1/chat/completions` в формате OpenAI, указав модель, например `openai/gpt-4.1-mini`, `anthropic/claude-sonnet-4.6` или `deepseek/deepseek-v4-flash`.

**Нужно ли переписывать код под Heli?**
Нет. Heli совместим с OpenAI API: в SDK меняются только `base_url` и `api_key`.

**Можно ли оплатить по счёту для ИП или ООО?**
Да, баланс пополняется по счёту, после зачисления оплаты на email может прийти акт оказанных услуг в PDF. Подробности: [оферта](https://getheli.ru/legal/terms) и [оплата в рублях](https://getheli.ru/docs/payment).

**Как подключить Cursor?**
Settings → Models → Override OpenAI Base URL = `https://getheli.ru/v1`, в поле OpenAI API Key вставьте ключ Heli. Подробнее: [`cursor/`](cursor).

**Что будет, если закончатся деньги?**
API вернёт `402`, долг не образуется. После пополнения запросы снова проходят.

---

## English

**Heli** ([getheli.ru](https://getheli.ru)) is an OpenAI-compatible API gateway to LLMs (OpenAI GPT, Anthropic Claude, Google Gemini, DeepSeek and more) with payments in Russian rubles. This repository contains minimal working examples.

- **Base URL:** `https://getheli.ru/v1`
- **Auth:** `Authorization: Bearer sk-heli-...`
- **Endpoints:** chat completions (with streaming), models, embeddings, audio transcriptions (Whisper), speech, OCR (Mistral OCR compatible)
- **Models:** `provider/model` slugs, e.g. `openai/gpt-4.1-mini`, `anthropic/claude-sonnet-4.6`, `deepseek/deepseek-v4-flash`; catalog and prices at [getheli.ru/models](https://getheli.ru/models)
- **Payments:** Russian bank cards, SBP, USDT, invoices for companies. Prepaid, pay-as-you-go, no subscription; `402` when the balance is zero.
- **Usage:** drop-in replacement for the official OpenAI SDKs, LangChain, n8n and Cursor: change `base_url` and the API key. See [`python/`](python), [`node/`](node), [`curl/`](curl), [`langchain/`](langchain), [`n8n/`](n8n), [`cursor/`](cursor).

## Лицензия

[MIT](LICENSE)
