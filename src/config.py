
import os
from dotenv import load_dotenv

from supabase import create_client
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore


# Load environment variables
load_dotenv()


# 1. Initialize HuggingFace Embeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# 2. Get Supabase Credentials

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase credentials are missing in .env")

if not GROQ_API_KEY:
    raise ValueError("Groq API key is missing in .env")


# 3. Connect to Supabase

supabase_client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


# 4. Initialize Supabase Vector Store

vectorstore = SupabaseVectorStore(
    client=supabase_client,
    embedding=embeddings,
    table_name="documents",
    query_name="match_documents"
)


# 5. Create Retriever

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


# 6. Initialize Groq LLM

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=GROQ_API_KEY
)


print("Supabase Vector Database connected successfully!")
