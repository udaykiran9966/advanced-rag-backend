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
- **Groq LLM Integration:** Generate fast AI responses using `openai/gpt-oss-20b`.
- **Streamlit Interface:** Interactive chatbot interface.
- **Terminal Chatbot:** Run the conversational chatbot directly from the terminal.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| LangChain | RAG workflow and chain orchestration |
| Groq | Large Language Model |
| Hug
