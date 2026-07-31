from langchain_openai import OpenAIEmbeddings

from config import EMBEDDING_MODEL

embeddings = OpenAIEmbeddings(
    model=EMBEDDING_MODEL,
    dimensions=512
)