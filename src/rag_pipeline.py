from src.config import retriever
from langchain_core.runnables import RunnableLambda

from src.chains import(
    contextualize_chain,
    document_answer_chain,
    intent_chain,
    history_answer_chain,
    general_chain 
)


def retrieve_documents(inputs):
    
    
    # 1. Rewrite the questions 
    
    standalone_question=contextualize_chain.invoke(
        {
            
            "input":inputs["input"],
            "chat_history":inputs["chat_history"]
        }
    
    )
    print("\n Rewritten Question:", standalone_question)
    
    #  1. Retrieve relevant documents 
    
    documents=retriever.invoke(standalone_question)
    
    
    # Combine document chunks 
    
    context="\n\n".join(
        [doc.page_content for doc in documents ]
        
    )
    
    # 4. Handle Empty Retrieval 
    
    if not context.strip():
        return "I dont know based on the provided document."
    
    # 5. Generate The document based Answer 
    
    answer=document_answer_chain.invoke(
        {
        "input":standalone_question,
        "context":context
        }
        
    )
    return answer 


def route_request(inputs):
    
    # 1. Get the user question
    
    question=inputs["input"]
    history=inputs["chat_history"]
    
    
    # 2. Identifying the Intent 
    
    intent=intent_chain.invoke(
        {
            
            "input":question,
            "chat_history":history
        }
    ).strip().upper()
    
    print("\nDetected Intent:",intent)
    
    # Document Route 
    
    if intent=="DOCUMENT":
        return retrieve_documents(inputs)
    
    elif intent=="HISTORY":
        return history_answer_chain.invoke(
            {
                
                "input":question,
                "chat_history":history 
                    
            }
        )
        
    elif intent=="GENERAL":
        return general_chain.invoke(
            {
                
                "input":question,
                "chat_history":history
                
            }
        )

rag_chain=RunnableLambda(route_request)


   
   