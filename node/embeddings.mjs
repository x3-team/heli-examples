// Эмбеддинги через Heli: POST /v1/embeddings.
//   HELI_API_KEY=sk-heli-... node embeddings.mjs
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.HELI_API_KEY,
  baseURL: process.env.HELI_BASE_URL ?? "https://getheli.ru/v1",
});

const result = await client.embeddings.create({
  model: "openai/text-embedding-3-small",
  input: ["Оплата API в рублях", "OpenAI-совместимый шлюз"],
});

for (const item of result.data) {
  console.log(item.index, item.embedding.length, item.embedding.slice(0, 3));
}
