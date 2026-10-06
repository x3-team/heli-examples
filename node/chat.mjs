// Chat Completions через Heli (OpenAI-совместимый API, оплата в рублях).
//   npm install
//   HELI_API_KEY=sk-heli-... node chat.mjs "Напиши функцию на JavaScript"
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.HELI_API_KEY,
  baseURL: process.env.HELI_BASE_URL ?? "https://getheli.ru/v1",
});

const prompt = process.argv[2] ?? "Привет! Ответь одним предложением.";

const response = await client.chat.completions.create({
  // Любой слаг из https://getheli.ru/models
  model: process.env.HELI_MODEL ?? "anthropic/claude-sonnet-4.6",
  messages: [{ role: "user", content: prompt }],
});

console.log(response.choices[0].message.content);
