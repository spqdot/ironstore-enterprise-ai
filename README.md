# 🤖 IronStore Enterprise AI Assistant

An end-to-end **Retrieval-Augmented Generation (RAG) application** that enables users to ask natural-language questions about IronStore's internal business documents and receive context-aware answers with source references.

The system combines **FastAPI, LangChain, OpenAI, Pinecone, React, and Vite** to create a modern enterprise knowledge assistant. It includes PDF ingestion, regex-based text preprocessing, improved document chunking, vector embeddings, semantic retrieval, LLM-based answer generation, source attribution, and full-stack cloud deployment.

🌐 **Live Application:**  
https://ironstore-enterprise-ai-79ya.vercel.app

⚙️ **Backend API:**  
https://ironstore-enterprise-ai.onrender.com

📚 **FastAPI Documentation:**  
https://ironstore-enterprise-ai.onrender.com/docs

---

## 📌 Project Overview

Organizations often store important information across large collections of internal documents, policies, product catalogs, and operational files.

Finding a specific answer manually can be slow and inefficient.

The **IronStore Enterprise AI Assistant** solves this problem using Retrieval-Augmented Generation.

Instead of asking an LLM to answer purely from its pretrained knowledge, the application first searches IronStore's indexed documents for relevant information and then provides that retrieved context to the language model.

This allows the chatbot to produce answers grounded in the organization's own documents.

---

## ✨ Key Features

- 💬 Modern conversational chatbot interface
- 📄 PDF document ingestion
- 🧹 Regex-based text preprocessing
- ✂️ Structure-aware document chunking
- 🧠 OpenAI embeddings
- 🔎 Semantic vector search with Pinecone
- 🤖 Retrieval-Augmented Generation (RAG)
- 📚 Source and page attribution
- ⚡ FastAPI REST backend
- ⚛️ React + Vite frontend
- 🔐 Environment-variable based secret management
- ☁️ Backend deployment with Render
- ▲ Frontend deployment with Vercel
- 🔄 GitHub-based deployment workflow

---

# 🏗️ System Architecture

```text
                        USER
                          │
                          ▼
                ┌──────────────────┐
                │ React / Vite UI  │
                │     Vercel       │
                └────────┬─────────┘
                         │
                         │ POST /chat
                         ▼
                ┌──────────────────┐
                │ FastAPI Backend  │
                │      Render      │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   RAG Pipeline   │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Query Embedding  │
                │      OpenAI      │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Pinecone Vector  │
                │      Search      │
                └────────┬─────────┘
                         │
                         ▼
                Relevant document chunks
                         │
                         ▼
                ┌──────────────────┐
                │  Prompt + LLM    │
                │      OpenAI      │
                └────────┬─────────┘
                         │
                         ▼
                 Answer + Sources
                         │
                         ▼
                ┌──────────────────┐
                │ React Chatbot UI │
                └──────────────────┘
```

---

# 🧠 How the RAG Pipeline Works

The application uses two main workflows:

## 1. Document Ingestion

```text
PDF Documents
      │
      ▼
PyPDFLoader
      │
      ▼
Regex Text Cleaning
      │
      ▼
Metadata Enrichment
      │
      ▼
Recursive Character Splitting
      │
      ▼
OpenAI Embeddings
      │
      ▼
Pinecone Vector Database
```

The current document corpus contains:

- **2,308 loaded PDF pages**
- **2,256 non-empty processed pages**
- **4,247 indexed document chunks**

---

## 2. Question Answering

When a user asks a question:

```text
User Question
      │
      ▼
FastAPI /chat
      │
      ▼
Embedding Generation
      │
      ▼
Pinecone Similarity Search
      │
      ▼
Relevant Document Chunks
      │
      ▼
Context + Prompt
      │
      ▼
OpenAI Language Model
      │
      ▼
Generated Answer
      │
      ▼
Sources + Page Numbers
```

This approach allows the model to answer questions using retrieved enterprise information rather than relying only on general model knowledge.

---

# 🧹 Regex-Based Text Preprocessing

PDF extraction often introduces formatting problems that can reduce retrieval quality.

The ingestion pipeline includes custom regex preprocessing to clean the extracted text before embedding.

The preprocessing handles:

### Line-ending normalization

Different line-ending formats are converted into a consistent structure.

### Null-character removal

Unexpected null characters introduced during PDF extraction are removed.

### Hyphenated line-break repair

For example:

```text
employ-
ment
```

becomes:

```text
employment
```

### Whitespace normalization

Repeated spaces and tabs are reduced while meaningful newline structure is preserved.

### Punctuation cleanup

Unnecessary whitespace before punctuation is removed.

### Blank-line normalization

Excessive blank lines are reduced while retaining useful document structure.

The preprocessing intentionally avoids aggressive transformations that could corrupt legitimate terminology such as:

```text
IronStore
DisplayPort
macOS
microSD
mAh
USB-C
```

---

# ✂️ Improved Document Chunking

The application uses LangChain's `RecursiveCharacterTextSplitter`.

Current configuration:

```python
chunk_size = 900
chunk_overlap = 150
```

The splitter prioritizes meaningful structural boundaries:

```python
separators = [
    "\n\n",
    "\n",
    ". ",
    "? ",
    "! ",
    "; ",
    ", ",
    " ",
    "",
]
```

This helps preserve semantic context while still producing chunks suitable for vector retrieval.

Chunk overlap also allows important context near chunk boundaries to appear in neighboring chunks.

---

# 🏷️ Metadata Enrichment

Each processed document chunk includes useful metadata.

Examples include:

```text
source
filename
page
page_number
department
chunk_index
```

This metadata supports source attribution and makes retrieved results more interpretable.

For example, the chatbot can show the document and page associated with information used in an answer.

---

# 🔎 Vector Search

The cleaned document chunks are converted into embeddings and stored in **Pinecone**.

Current Pinecone index:

```text
Vector count: 4,247
Dimensions:   512
Metric:       Cosine Similarity
Vector type:  Dense
```

When a question is submitted, the query is embedded using the same embedding configuration and compared with the stored vectors.

Pinecone returns the most semantically relevant document chunks for the RAG pipeline.

---

# 💬 Example Questions

The assistant can answer questions such as:

### HR / Internal Policy

```text
What is the process for requesting annual leave?
```

```text
What is IronStore's policy for employees reporting sick leave?
```

### Product Information

```text
What is the price and availability of the IronStore 24" Full HD Office Monitor?
```

```text
What are the specifications, price, and availability of the IronStore USB-C Docking Station 8-in-1?
```

### Enterprise Knowledge

Users can also ask questions about other information contained in the indexed IronStore documents.

---

# 🖥️ Frontend

The frontend is built with:

- React
- Vite
- Axios
- CSS

The chatbot interface includes:

- Question input
- Conversation-style messages
- AI-generated responses
- Source references
- Page information
- Responsive modern UI

The frontend communicates with the FastAPI backend through:

```text
POST /chat
```

The production backend URL is configured using:

```javascript
import.meta.env.VITE_API_URL
```

This avoids hard-coding local or production API URLs into the application.

---

# ⚙️ Backend

The backend is built with **FastAPI**.

Its responsibilities include:

- Receiving user questions
- Running document retrieval
- Communicating with Pinecone
- Constructing RAG context
- Calling the language model
- Returning answers
- Returning source metadata
- Managing CORS between frontend and backend

Example API request:

```json
{
  "question": "What is the process for requesting annual leave?"
}
```

Example response structure:

```json
{
  "answer": "Generated answer based on retrieved documents...",
  "sources": [
    {
      "source": "document.pdf",
      "page": 3
    }
  ]
}
```

---

# 📂 Project Structure

```text
ironstore-enterprise-ai/
│
├── backend/
│   │
│   ├── app.py
│   ├── config.py
│   ├── ingest.py
│   ├── rag.py
│   ├── reset_index.py
│   ├── requirements.txt
│   ├── utils.py
│   │
│   ├── documents/
│   ├── models/
│   ├── prompts/
│   ├── routers/
│   ├── services/
│   ├── tests/
│   └── logs/
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatBox.jsx
│   │   │   ├── Message.jsx
│   │   │   └── SourceList.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.css
│   │
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
├── LICENSE
└── README.md
```

---

# 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React |
| Build Tool | Vite |
| HTTP Client | Axios |
| Backend API | FastAPI |
| RAG Framework | LangChain |
| LLM | OpenAI |
| Embeddings | OpenAI Embeddings |
| Vector Database | Pinecone |
| PDF Processing | PyPDFLoader |
| Text Splitting | RecursiveCharacterTextSplitter |
| Text Preprocessing | Python Regex |
| Backend Hosting | Render |
| Frontend Hosting | Vercel |
| Version Control | Git + GitHub |

---

# 🚀 Local Installation

## 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ironstore-enterprise-ai
```

---

## 2. Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows Git Bash

```bash
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create:

```text
backend/.env
```

Configure the required environment variables:

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name

OPENAI_MODEL=your_openai_model
EMBEDDING_MODEL=your_embedding_model
```

> **Never commit `.env` or API keys to GitHub.**

The repository's `.gitignore` excludes environment files.

---

# 📥 Document Ingestion

Place the required PDF documents inside:

```text
backend/documents/
```

Then run:

```bash
python ingest.py
```

The ingestion process:

1. Loads PDFs
2. Cleans extracted text
3. Removes empty pages
4. Adds metadata
5. Creates structured chunks
6. Generates embeddings
7. Uploads vectors to Pinecone

> `ingest.py` uploads vectors to Pinecone. Avoid repeatedly running it against an existing populated index unless duplicate-vector behavior is intentionally handled.

A maintenance utility is also provided for resetting the index:

```bash
python reset_index.py
```

This script requires explicit confirmation before deleting vectors.

---

# ▶️ Run the Backend

From the `backend` directory:

```bash
uvicorn app:app --reload
```

Local backend:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run the Frontend

Open another terminal:

```bash
cd frontend
npm install
```

For local development, configure the frontend API URL using a Vite environment variable.

Example:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Then run:

```bash
npm run dev
```

Open the local URL shown by Vite.

---

# 🧪 Testing

The backend contains dedicated test scripts for different parts of the RAG pipeline.

Examples include:

```bash
python test_pinecone.py
```

Used to verify Pinecone connectivity and index statistics.

```bash
python test_retrieval.py
```

Used to inspect document retrieval quality.

```bash
python test_rag.py
```

Used to test the complete RAG response pipeline.

Testing retrieval independently from generation is particularly useful because it helps distinguish retrieval problems from LLM-generation problems.

---

# ☁️ Deployment

## Backend — Render

The FastAPI backend is deployed using Render.

Production backend:

```text
https://ironstore-enterprise-ai.onrender.com
```

Render configuration:

```text
Root Directory: backend
Build Command:  pip install -r requirements.txt
Start Command:  uvicorn app:app --host 0.0.0.0 --port $PORT
Python Version: 3.12.4
```

Required environment variables are configured securely through Render rather than stored in GitHub.

---

## Frontend — Vercel

The React/Vite frontend is deployed using Vercel.

Production application:

```text
https://ironstore-enterprise-ai-79ya.vercel.app
```

Vercel configuration:

```text
Framework:        Vite
Root Directory:   frontend
Build Command:    npm run build
Output Directory: dist
```

Production environment variable:

```env
VITE_API_URL=https://ironstore-enterprise-ai.onrender.com
```

---

# 🔐 Security

Sensitive configuration is stored using environment variables.

The following files are excluded from Git:

```text
.env
.env.*
.venv/
venv/
__pycache__/
frontend/node_modules/
frontend/dist/
```

API keys should never be stored directly in source code.

CORS is configured in FastAPI to restrict browser access to approved frontend origins.

---

# 📈 Improvements Made During Development

Several iterations were made to improve retrieval quality and deployment readiness.

### Initial ingestion

The original pipeline used basic recursive chunking.

### Improved preprocessing

Regex-based text cleaning was introduced to repair common PDF extraction issues.

### Structure preservation

Instead of flattening all document text into a single line, meaningful newline boundaries were preserved.

This improved the representation of content such as:

```text
Price
Availability
Warehouse Location
Key Specifications
```

### Improved chunking

Chunking was refined to:

```text
chunk_size = 900
chunk_overlap = 150
```

with structural separators.

### Metadata enrichment

Filename, page number, department, and chunk information were added to improve traceability.

### Vector index rebuild

The previous vector index was safely reset and rebuilt using the improved ingestion pipeline.

Final index:

```text
4,247 vectors
```

### Production deployment

The complete application was deployed using:

```text
Frontend → Vercel
Backend  → Render
Vectors  → Pinecone
LLM      → OpenAI
```

---

# 🔮 Future Improvements

Potential future improvements include:

- Hybrid semantic + keyword search
- Retrieval reranking
- Query rewriting
- Conversation memory
- Streaming responses
- Authentication and role-based access control
- Department-specific retrieval filters
- Stable deterministic vector IDs
- Incremental document ingestion
- Automated document synchronization
- Retrieval evaluation metrics
- RAG observability and tracing
- Improved citations
- Admin document-management interface
- Automated CI/CD testing

---

# 🎯 Project Goal

The goal of this project is to demonstrate how modern Generative AI technologies can be combined to create a practical enterprise knowledge assistant.

The project covers the complete AI application lifecycle:

```text
Enterprise Documents
        ↓
Data Preprocessing
        ↓
Chunking
        ↓
Embeddings
        ↓
Vector Database
        ↓
Semantic Retrieval
        ↓
Prompt Engineering
        ↓
LLM Generation
        ↓
FastAPI
        ↓
React
        ↓
Cloud Deployment
```

It demonstrates not only LLM integration, but also **document engineering, retrieval design, backend API development, frontend development, vector database integration, testing, security practices, and cloud deployment**.

---

# 👩‍💻 Author

**Shrabani Panigrahi**

Data Science / AI Engineering Project

---

## 🌐 Live Demo

👉 **https://ironstore-enterprise-ai-79ya.vercel.app**

---

## 📄 License

This project includes a `LICENSE` file. Refer to it for the applicable licensing terms.
