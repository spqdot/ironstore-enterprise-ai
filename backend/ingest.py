import re
from pathlib import Path

from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

from services.vectorstore import vectorstore


# ============================================================
# 1. REGEX TEXT PREPROCESSING
# ============================================================

def clean_text(text: str) -> str:
    """
    Clean text extracted from PDF documents while preserving
    useful document structure for RAG retrieval.
    """

    if not text:
        return ""

    # --------------------------------------------------------
    # Normalize line endings
    # --------------------------------------------------------
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # --------------------------------------------------------
    # Remove null characters that may appear during
    # PDF text extraction
    # --------------------------------------------------------
    text = text.replace("\x00", "")

    # --------------------------------------------------------
    # Repair words broken by PDF line wrapping
    #
    # Example:
    #
    # employ-
    # ment
    #
    # becomes:
    #
    # employment
    # --------------------------------------------------------
    text = re.sub(
        r"(\w)-\n(\w)",
        r"\1\2",
        text
    )

    # --------------------------------------------------------
    # Normalize repeated spaces and tabs
    #
    # We deliberately preserve newline characters because
    # they contain useful document structure.
    # --------------------------------------------------------
    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    # --------------------------------------------------------
    # Remove unnecessary spaces before punctuation
    #
    # Example:
    #
    # PeopleHub , IronStore
    #
    # becomes:
    #
    # PeopleHub, IronStore
    # --------------------------------------------------------
    text = re.sub(
        r"[ \t]+([,.;:!?])",
        r"\1",
        text
    )

    # --------------------------------------------------------
    # Remove unnecessary spaces around line breaks
    # --------------------------------------------------------
    text = re.sub(
        r" *\n *",
        "\n",
        text
    )

    # --------------------------------------------------------
    # Reduce excessive blank lines
    # --------------------------------------------------------
    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    return text.strip()


# ============================================================
# 2. LOAD PDF DOCUMENTS
# ============================================================

print("Loading PDF documents...")

loader = DirectoryLoader(
    "documents",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader,
)

documents = loader.load()

print(f"Loaded {len(documents)} pages.")


# ============================================================
# 3. CLEAN DOCUMENTS + ADD METADATA
# ============================================================

print("Cleaning document text...")

cleaned_documents = []

for doc in documents:

    # --------------------------------------------------------
    # Apply regex preprocessing
    # --------------------------------------------------------
    doc.page_content = clean_text(
        doc.page_content
    )

    # --------------------------------------------------------
    # Skip completely empty pages
    # --------------------------------------------------------
    if not doc.page_content:
        continue

    # --------------------------------------------------------
    # Get source file
    # --------------------------------------------------------
    source = doc.metadata.get(
        "source",
        ""
    )

    source_path = Path(source)

    # --------------------------------------------------------
    # Add filename metadata
    #
    # Example:
    # IronStore_Leave_and_Absence_Policy.pdf
    # --------------------------------------------------------
    doc.metadata["filename"] = (
        source_path.name
    )

    # --------------------------------------------------------
    # Add human-readable page number
    #
    # PyPDFLoader uses:
    #
    # page = 0
    #
    # for the first page.
    #
    # We additionally store:
    #
    # page_number = 1
    # --------------------------------------------------------
    page = doc.metadata.get("page")

    if page is not None:
        doc.metadata["page_number"] = (
            int(page) + 1
        )

    # --------------------------------------------------------
    # Extract department / business area from folder structure
    #
    # Example:
    #
    # documents/
    #   internal_docs_by_area/
    #       HR_policies/
    #           policy.pdf
    #
    # department = HR_policies
    # --------------------------------------------------------
    parts = source_path.parts

    if "internal_docs_by_area" in parts:

        position = parts.index(
            "internal_docs_by_area"
        )

        if position + 1 < len(parts):

            doc.metadata["department"] = (
                parts[position + 1]
            )

    cleaned_documents.append(doc)


print(
    f"Cleaned {len(cleaned_documents)} "
    f"non-empty pages."
)


# ============================================================
# 4. IMPROVED DOCUMENT CHUNKING
# ============================================================

print("Splitting documents into chunks...")

text_splitter = RecursiveCharacterTextSplitter(

    # Maximum approximate chunk size
    chunk_size=900,

    # Preserve some context between adjacent chunks
    chunk_overlap=150,

    # Prefer structural boundaries before falling
    # back to smaller boundaries
    separators=[
        "\n\n",
        "\n",
        ". ",
        "? ",
        "! ",
        "; ",
        ", ",
        " ",
        "",
    ],

    length_function=len,
)


chunks = text_splitter.split_documents(
    cleaned_documents
)


print(f"Created {len(chunks)} chunks.")


# ============================================================
# 5. ADD CHUNK METADATA
# ============================================================

print("Adding chunk metadata...")

for index, chunk in enumerate(chunks):

    chunk.metadata["chunk_index"] = index


# ============================================================
# 6. UPLOAD CHUNKS TO PINECONE
# ============================================================

print("Uploading chunks to Pinecone...")

vectorstore.add_documents(
    chunks
)


# ============================================================
# 7. COMPLETE
# ============================================================

print(
    "✅ Ingestion completed successfully!"
)

print(
    f"Indexed {len(chunks)} chunks."
)