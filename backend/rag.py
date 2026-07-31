from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config import OPENAI_MODEL
from services.vectorstore import vectorstore

llm = ChatOpenAI(
    model=OPENAI_MODEL,
    temperature=0
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

prompt = ChatPromptTemplate.from_template(
    """
You are IronStore's Enterprise AI Assistant.

Answer ONLY using the information provided in the context.

If the answer is not in the context, reply:
"I couldn't find that information in the company documents."

Context:
{context}

Question:
{question}
"""
)

def ask_question(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    messages = prompt.format_messages(
        context=context,
        question=question
    )

    response = llm.invoke(messages)

    sources = []

    for doc in docs:
        sources.append({
            "source": doc.metadata.get("source"),
            "page": int(doc.metadata.get("page", 0))
        })

    return {
        "answer": response.content,
        "sources": sources
    }