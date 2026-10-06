// Потоковый ответ (stream: true) через Heli.
//   HELI_API_KEY=sk-heli-... node stream.mjs "Расскажи коротко про SSE"
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.HELI_API_KEY,
  baseURL: process.env.HELI_BASE_URL ?? "https://getheli.ru/v1",
});

const prompt = process.argv[2] ?? "Посчитай от 1 до 5 словами.";

const stream = await client.chat.completions.create({
  model: process.env.HELI_MODEL ?? "deepseek/deepseek-v4-flash",
  messages: [{ role: "user", content: prompt }],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
process.stdout.write("\n");
