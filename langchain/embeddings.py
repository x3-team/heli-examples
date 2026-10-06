"""LangChain + Heli: OpenAIEmbeddings для RAG и векторного поиска.

    export HELI_API_KEY=sk-heli-...
    python embeddings.py
"""
import os

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="openai/text-embedding-3-small",
    api_key=os.environ["HELI_API_KEY"],
    base_url=os.getenv("HELI_BASE_URL", "https://getheli.ru/v1"),
    # Heli принимает текст; не даём LangChain заранее превращать его в токены tiktoken
    check_embedding_ctx_length=False,
)

vectors = embeddings.embed_documents(["Оплата API в рублях", "OpenAI-совместимый шлюз"])
print(len(vectors), len(vectors[0]))
