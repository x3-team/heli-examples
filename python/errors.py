"""Обработка ошибок Heli: 402 — закончился баланс, 401 — неверный или отозванный ключ.

    export HELI_API_KEY=sk-heli-...
    python errors.py
"""
import os

import openai
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["HELI_API_KEY"],
    base_url=os.getenv("HELI_BASE_URL", "https://getheli.ru/v1"),
)

try:
    response = client.chat.completions.create(
        model=os.getenv("HELI_MODEL", "openai/gpt-4.1-mini"),
        messages=[{"role": "user", "content": "ping"}],
    )
    print(response.choices[0].message.content)
except openai.AuthenticationError:
    print("401: проверьте ключ sk-heli- во вкладке «Ключи» кабинета")
except openai.APIStatusError as e:
    if e.status_code == 402:
        print("402: баланс Heli равен нулю — пополните его в кабинете getheli.ru")
    else:
        raise
