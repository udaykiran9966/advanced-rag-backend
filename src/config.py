import os       
from langchain_groq import ChatGroq
from dotenv import load_dotenv 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS 





# Load environment variables 

load_dotenv()

# Initial Embeddings 
embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

# Load FAISS vector database 

vectorstore=FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)


# Create the Retriver 

retriever=vectorstore.as_retriever(
    search_kwargs={"k":3}
)



# Initialize The LLM

llm=ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
    
)
