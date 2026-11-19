from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# 1. Load The PDF

loader=PyPDFLoader("data/company_policy.pdf")
documents=loader.load()


# step 2: Split Text into Chunks 
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
    
)

chunks=text_splitter.split_documents(documents)
print(len(chunks))

# Step 3: Embeddings 
embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Vectorstore DataBase

vectorstore=FAISS.from_documents(
    chunks,
    embeddings
)

# Save the vectorstore DB
vectorstore.save_local("vectorstore")

print("vector database save Sucessfully.")