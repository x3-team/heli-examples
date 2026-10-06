# n8n + Heli

Два способа подключить Heli к n8n: готовая нода OpenAI с другим Base URL или универсальная нода HTTP Request.

## Способ 1. Нода OpenAI / OpenAI Chat Model

1. **Credentials → Create credential → OpenAI API**.
2. **API Key**: ваш ключ `sk-heli-...`.
3. **Base URL**: `https://getheli.ru/v1` (вместо `https://api.openai.com/v1`). Organization ID оставьте пустым.
4. В ноде **OpenAI Chat Model** (AI Agent, Basic LLM Chain) или **OpenAI → Message a model** выберите этот credential.
5. Модель укажите по ID (режим *By ID*), например `openai/gpt-4.1-mini`, `anthropic/claude-sonnet-4.6`
   или `deepseek/deepseek-v4-flash`. Список — на [getheli.ru/models](https://getheli.ru/models).

Поле Base URL есть в OpenAI credential в актуальных версиях n8n. Если в вашей версии его нет, используйте способ 2.

## Способ 2. HTTP Request (готовый workflow)

Импортируйте [heli-chat-workflow.json](heli-chat-workflow.json): меню workflow → **Import from File**.

1. Создайте credential **Header Auth**: Name `Authorization`, Value `Bearer sk-heli-ВАШ_КЛЮЧ`.
2. Выберите его в ноде **Heli Chat Completion**.
3. Нажмите **Test workflow**. Ответ модели окажется в поле `answer`.

Нода отправляет `POST https://getheli.ru/v1/chat/completions` в формате OpenAI:

```json
{
  "model": "openai/gpt-4.1-mini",
  "messages": [{ "role": "user", "content": "{{ $json.prompt }}" }]
}
```

Храните ключ в credentials n8n, а не в тексте workflow.
При нулевом балансе Heli вернёт `402` — нода покажет ошибку, пополните баланс в кабинете.
