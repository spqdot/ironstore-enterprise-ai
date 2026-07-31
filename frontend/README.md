# 🤖 IronStore Enterprise AI Assistant

An Enterprise Retrieval-Augmented Generation (RAG) application that allows employees to ask questions about internal company documents using natural language.

The system retrieves the most relevant document chunks from a Pinecone vector database and generates accurate, source-grounded answers using OpenAI's language models.

---

## 🚀 Features

- Enterprise RAG pipeline
- React frontend
- FastAPI backend
- OpenAI GPT integration
- Pinecone vector database
- Semantic document retrieval
- PDF document ingestion
- Source citation with page numbers
- REST API
- Interactive web interface

---

## 🏗️ Project Architecture

```
React Frontend
       │
       ▼
Axios API Requests
       │
       ▼
FastAPI Backend
       │
       ▼
RAG Pipeline
       │
 ┌─────┴─────┐
 ▼           ▼
Pinecone   OpenAI GPT
(Vector DB)   (LLM)
       │
       ▼
Answer + Sources
```

---

## 📂 Project Structure

```text
ironstore-enterprise-ai/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── routers/
│   ├── services/
│   ├── models/
│   ├── documents/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json
│
├── README.md
└── LICENSE
```

---

## ⚙️ Technologies Used

### Backend

- Python
- FastAPI
- LangChain
- OpenAI API
- Pinecone
- Pydantic

### Frontend

- React
- Vite
- Axios

### Vector Database

- Pinecone

### Embedding Model

- OpenAI text-embedding-3-small

### Language Model

- GPT-4.1-mini

---

## 📖 How It Works

1. PDF documents are loaded.
2. Documents are split into chunks.
3. Chunks are converted into embeddings.
4. Embeddings are stored in Pinecone.
5. User submits a question.
6. Similar document chunks are retrieved.
7. Retrieved context is sent to OpenAI.
8. AI generates an answer with source references.

---

## 🖥️ Running the Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

Backend runs at

```
http://localhost:8000
```

Swagger documentation

```
http://localhost:8000/docs
```

---

## 💻 Running the Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

## 📷 Demo

### Example Question

```
How do employees request leave?
```

### Example Answer

Employees should submit annual leave requests through PeopleHub at least 10 calendar days before leave of one to five working days...

The response includes the source document and page number used to generate the answer.

---

## 🔮 Future Improvements

- Chat history
- Authentication
- Streaming responses
- Better chunking strategy
- Regex-based preprocessing
- Metadata filtering
- Modern chatbot interface
- Deployment on Render and Vercel

---

## 👤 Author

**Shrabani Panigrahi**

GitHub: https://github.com/YOUR_GITHUB_USERNAME

LinkedIn: YOUR_LINKEDIN_URL