"""Список моделей, доступных по вашему ключу: GET /v1/models.

    export HELI_API_KEY=sk-heli-...
    python list_models.py claude
"""
import os
import sys

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["HELI_API_KEY"],
    base_url=os.getenv("HELI_BASE_URL", "https://getheli.ru/v1"),
)

needle = sys.argv[1].lower() if len(sys.argv) > 1 else ""

for model in client.models.list():
    if needle in model.id.lower():
        print(model.id)
