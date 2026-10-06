"""Chat Completions через Heli (OpenAI-совместимый API, оплата в рублях).

    pip install -r requirements.txt
    export HELI_API_KEY=sk-heli-...
    python chat.py "Напиши функцию сортировки на Python"
"""
import os
import sys

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["HELI_API_KEY"],
    base_url=os.getenv("HELI_BASE_URL", "https://getheli.ru/v1"),
)

prompt = sys.argv[1] if len(sys.argv) > 1 else "Привет! Ответь одним предложением."

response = client.chat.completions.create(
    # Любой слаг из https://getheli.ru/models, например
    # anthropic/claude-sonnet-4.6, deepseek/deepseek-v4-flash, google/gemini-2.5-flash
    model=os.getenv("HELI_MODEL", "openai/gpt-4.1-mini"),
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
