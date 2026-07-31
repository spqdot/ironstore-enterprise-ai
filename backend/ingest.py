from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from services.vectorstore import vectorstore

print("Loading PDF documents...")

loader = DirectoryLoader(
    "documents",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()

print(f"Loaded {len(documents)} pages.")

print("Splitting documents into chunks...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks.")

print("Uploading chunks to Pinecone...")

vectorstore.add_documents(chunks)

print("✅ Ingestion completed successfully!")
print(f"Indexed {len(chunks)} chunks.")