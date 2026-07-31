from rag import ask_question

result = ask_question("How do employees request leave?")

print("\nAnswer:\n")
print(result["answer"])

print("\nSources:")

for source in result["sources"]:
    print(f"{source['source']} (Page {source['page']})")