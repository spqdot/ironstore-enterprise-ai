from services.vectorstore import vectorstore

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

query = "What is the leave policy?"

results = retriever.invoke(query)

print(f"Retrieved {len(results)} documents\n")

for i, doc in enumerate(results, 1):
    print(f"----- Result {i} -----")
    print("Source:", doc.metadata.get("source"))
    print("Page:", doc.metadata.get("page"))
    print(doc.page_content[:500])
    print()