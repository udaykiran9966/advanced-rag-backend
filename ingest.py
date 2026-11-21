
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import SupabaseVectorStore

from src.config import embeddings, supabase_client

# 1. Load the PDF
loader = PyPDFLoader("data/company_policy.pdf")
documents = loader.load()

print(f"Total PDF pages loaded: {len(documents)}")

# 2. Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Total chunks created: {len(chunks)}")

# 3. Connect to Supabase Vector Store
vectorstore = SupabaseVectorStore(
    client=supabase_client,
    embedding=embeddings,
    table_name="documents",
    query_name="match_documents"
)

# 4. Insert chunks and embeddings into Supabase
print("Starting ingestion to Supabase...")

vectorstore.add_documents(chunks)

print("PDF data successfully stored in Supabase!")
