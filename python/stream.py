"""Потоковый ответ (stream=True) через Heli.

    export HELI_API_KEY=sk-heli-...
    python stream.py "Расскажи коротко про SSE"
"""
import os
import sys

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["HELI_API_KEY"],
    base_url=os.getenv("HELI_BASE_URL", "https://getheli.ru/v1"),
)

prompt = sys.argv[1] if len(sys.argv) > 1 else "Посчитай от 1 до 5 словами."

stream = client.chat.completions.create(
    model=os.getenv("HELI_MODEL", "deepseek/deepseek-v4-flash"),
    messages=[{"role": "user", "content": prompt}],
    stream=True,
)

for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
