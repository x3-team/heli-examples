# Cursor + Heli: Override OpenAI Base URL

Heli подключается к Cursor вместо OpenAI: тот же протокол, модели каталога Heli, оплата в рублях.

1. Получите ключ на [getheli.ru](https://getheli.ru): «Создать аккаунт», затем скопируйте `sk-heli-...` из кабинета.
2. В Cursor откройте **Settings → Models** (раздел API Keys).
3. В поле **OpenAI API Key** вставьте ключ `sk-heli-...`.
4. Включите **Override OpenAI Base URL** и укажите `https://getheli.ru/v1`.
5. Добавьте модель по слагу из каталога Heli, например `openai/gpt-4.1-mini`,
   `anthropic/claude-sonnet-4.6` или `deepseek/deepseek-v4-flash`, и выберите её в чате.

```
OpenAI API Key:           sk-heli-ВАШ_КЛЮЧ
Override OpenAI Base URL: https://getheli.ru/v1
Model:                    anthropic/claude-sonnet-4.6
```

Если запросы возвращают `402`, на балансе Heli нет средств: пополните его в кабинете рублями (карта РФ, СБП).
`401` означает неверный или отозванный ключ.

Те же base URL и ключ подходят для других редакторов и агентов с OpenAI-совместимым провайдером
(Continue, Cline, Roo Code, Zed и т.п.).

Подробнее: [getheli.ru/docs/cursor](https://getheli.ru/docs/cursor).
