# LangChain + Heli

`ChatOpenAI` и `OpenAIEmbeddings` из `langchain-openai` работают с Heli: передайте
`base_url="https://getheli.ru/v1"` и ключ `sk-heli-...`. Цепочки, агенты, tool calling,
retriever и RAG-пайплайны менять не нужно.

```bash
pip install -r requirements.txt
export HELI_API_KEY=sk-heli-ВАШ_КЛЮЧ
python chat.py
python embeddings.py
```

Через переменные окружения (без явных параметров в коде):

```bash
export OPENAI_API_KEY=sk-heli-ВАШ_КЛЮЧ
export OPENAI_BASE_URL=https://getheli.ru/v1
```
