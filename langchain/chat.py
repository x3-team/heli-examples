"""LangChain + Heli: ChatOpenAI с base_url https://getheli.ru/v1.

    pip install -r requirements.txt
    export HELI_API_KEY=sk-heli-...
    python chat.py
"""
import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model=os.getenv("HELI_MODEL", "openai/gpt-4.1-mini"),
    api_key=os.environ["HELI_API_KEY"],
    base_url=os.getenv("HELI_BASE_URL", "https://getheli.ru/v1"),
    temperature=0.3,
)

print(llm.invoke("Объясни в двух предложениях, что такое embedding.").content)

# Потоковый вывод
for chunk in llm.stream("Назови три идеи для pet-проекта с LLM."):
    print(chunk.content, end="", flush=True)
print()
