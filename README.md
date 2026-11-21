# 🤖 Advanced Conversational RAG Chatbot

An intelligent, document-based conversational chatbot built using **LangChain, Groq LLM, Hugging Face Embeddings, Supabase Vector Database, and Streamlit**.

The chatbot allows users to ask questions about uploaded PDF documents and provides context-aware answers using Retrieval-Augmented Generation (RAG). It also supports conversation history, follow-up questions, and intent-based routing.

## 🚀 Features

- **PDF Document Loading:** Extract information from PDF documents.
- **Text Splitting:** Split documents into smaller chunks for efficient retrieval.
- **Hugging Face Embeddings:** Convert text into vector embeddings using `all-MiniLM-L6-v2`.
- **Supabase Vector Database:** Store and retrieve document embeddings using PostgreSQL and pgvector.
- **Conversational RAG:** Answer questions using relevant document context.
- **Intent Classification:** Identify user queries as DOCUMENT, HISTORY, or GENERAL.
- **Contextual Question Rewriting:** Convert follow-up questions into standalone questions.
- **Conversation Memory:** Maintain previous questions and AI responses.
- **Groq LLM Integration:** Generate AI responses using `openai/gpt-oss-20b`.
- **Streamlit Interface:** Interactive chatbot interface.
- **Terminal Chatbot:** Run the conversational chatbot directly from the terminal.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| LangChain | RAG workflow and chain orchestration |
| Groq | Large Language Model |
| Hugging Face | Text embeddings |
| Supabase | Vector database |
| PostgreSQL | Database |
| pgvector | Vector similarity search |
| Streamlit | Frontend interface |
| PyPDF | PDF document loading |

## 🏗️ Project Architecture

```text
PDF Documents
     |
     v
PyPDFLoader
     |
     v
Text Splitter
     |
     v
Hugging Face Embeddings
     |
     v
Supabase Vector Database
     |
     v
User Question
     |
     v
Intent Classification
     |
     +-------------------+
     |         |         |
  DOCUMENT   HISTORY   GENERAL
     |         |         |
     v         v         v
 Retrieval   History   General
     |       Response  Response
     v
 Contextual Question
 Rewriting
     |
     v
 Relevant Documents
     |
     v
 Groq LLM
     |
     v
 AI Response
```

## 📁 Project Structure

```text
advanced-rag-backend/
│
├── data/
│   └── company_policy.pdf
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── prompts.py
│   ├── chains.py
│   └── rag_pipeline.py
│
├── app.py
├── main.py
├── ingest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/udaykiran9966/advanced-rag-backend.git
```

### 2. Navigate to the Project Directory

```bash
cd advanced-rag-backend
```

### 3. Create a Virtual Environment

```bash
python -m venv advance_rag
```

### 4. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\advance_rag\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root directory.

Add the following credentials:

```env
GROQ_API_KEY=your_groq_api_key
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
```

**Important:** Never upload your `.env` file or expose your API keys on GitHub.

## 🗄️ Supabase Database Setup

1. Create a Supabase project.
2. Enable the pgvector extension.
3. Create a `documents` table with the following columns:

| Column | Data Type |
|---|---|
| id | BIGINT |
| content | TEXT |
| metadata | JSONB |
| embedding | VECTOR(384) |

4. Create the `match_documents` PostgreSQL function for similarity search.
5. Configure the appropriate database permissions.

## 📥 Document Ingestion

Place your PDF file inside the `data/` directory.

Run:

```bash
python ingest.py
```

This process:
- Loads the PDF document.
- Splits the document into smaller chunks.
- Generates embeddings using Hugging Face.
- Stores document chunks and embeddings in Supabase.

## ▶️ Run the Application

### Streamlit Web Application

```bash
streamlit run app.py
```

### Terminal Chatbot

```bash
python main.py
```

## 💡 Example Questions

- What is the company leave policy?
- What are the different types of leave?
- What is the IT policy?
- What was my previous question?
- What did you answer earlier?

## 🔮 Future Improvements

- Support multiple PDF documents.
- Add user authentication.
- Improve document retrieval accuracy.
- Add source citations in AI responses.
- Deploy the application on Streamlit Cloud.
- Add support for more document formats.

## 👨‍💻 Author

**Uday Kiran**

B.Tech – Computer Science and Engineering

GitHub: [udaykiran9966](https://github.com/udaykiran9966)

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with Python, LangChain, Groq, Hugging Face, and Supabase.**
