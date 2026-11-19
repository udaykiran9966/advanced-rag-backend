from langchain_core.messages import(
    HumanMessage,AIMessage
)

from src.rag_pipeline import rag_chain

# 1. Conversation History Storage 

storage={}


# 2. Get Session History 
def get_session_history(session_id):
    
    if session_id not in storage:
        storage[session_id]=[]
    return storage[session_id] # Chat History of that particular  session/user 

# 3. Create user session 

session_id="user_1"

chat_history=get_session_history(session_id)

#. Start the chatbot 

print("\n Welcome To Conversational RAG Chatbot")
print("\n Type Exist to stop the Chatbot")

# 5. Chat Loop

while True:
    question=input("\nYou:")
    
    if question.lower()=="exist":
        print("Existing free Chatbot...")
        break 
    
    # 6. Initiate the RAG Chain 
    
    answer=rag_chain.invoke({
        
        "input":question,
        "chat_history":chat_history[-10:]
    })
    print("\nAI:",answer) 
    
    
    # 7. Store the HumanMessage in chat history 
    chat_history.append (
        HumanMessage(content=question),
        
        
    )
    
    # 8. Store the AI Message 
    
    chat_history.append(
        AIMessage(content=answer)
    )
    
