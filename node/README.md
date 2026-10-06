# Node.js: пакет openai + Heli

```bash
npm install
export HELI_API_KEY=sk-heli-ВАШ_КЛЮЧ
node chat.mjs "Привет"
node stream.mjs
node embeddings.mjs
```

В `new OpenAI({ ... })` меняются только `apiKey` и `baseURL: "https://getheli.ru/v1"`.
Остальной код — как с OpenAI. Работает в Node.js 18+ (ES modules, top-level await).

Тот же подход подходит для Vercel AI SDK и других библиотек с OpenAI-совместимым провайдером:
укажите base URL `https://getheli.ru/v1` и ключ `sk-heli-...`.
