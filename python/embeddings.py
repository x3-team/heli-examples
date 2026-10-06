"""Эмбеддинги через Heli: POST /v1/embeddings.

    export HELI_API_KEY=sk-heli-...
    python embeddings.py
"""
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["HELI_API_KEY"],
    base_url=os.getenv("HELI_BASE_URL", "https://getheli.ru/v1"),
)

result = client.embeddings.create(
    model="openai/text-embedding-3-small",  # алиас text-embedding-3-small тоже принимается
    input=["Оплата API в рублях", "OpenAI-совместимый шлюз"],
)

for item in result.data:
    print(item.index, len(item.embedding), item.embedding[:3])
