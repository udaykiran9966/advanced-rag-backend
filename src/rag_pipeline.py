
from src.config import retriever
from langchain_core.runnables import RunnableLambda

from src.chains import (
    contextualize_chain,
    document_answer_chain,
    intent_chain,
    history_answer_chain,
    general_chain
)


# 1. Document Retrieval Function

def retrieve_documents(inputs):

    # Rewrite the follow-up question

    standalone_question = contextualize_chain.invoke(
        {
            "input": inputs["input"],
            "chat_history": inputs["chat_history"]
        }
    )

    print("\nRewritten Question:", standalone_question)

    # Retrieve relevant documents

    documents = retriever.invoke(standalone_question)

    # Combine document chunks

    context = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    # Handle empty retrieval

    if not context.strip():
        return "I don't know based on the provided documents."

    # Generate document-based answer

    answer = document_answer_chain.invoke(
        {
            "input": standalone_question,
            "context": context
        }
    )

    return answer


# 2. Intent Routing Function

def route_request(inputs):

    # Validate input

    question = inputs.get("input", "").strip()
    history = inputs.get("chat_history", [])

    if not question:
        return "Please enter a question."

    # Identify user intent

    intent = intent_chain.invoke(
        {
            "input": question,
            "chat_history": history
        }
    ).strip().upper()

    print("\nDetected Intent:", intent)

    # Document Route

    if intent == "DOCUMENT":
        return retrieve_documents(inputs)

    # History Route

    elif intent == "HISTORY":
        return history_answer_chain.invoke(
            {
                "input": question,
                "chat_history": history
            }
        )

    # General Conversation Route

    elif intent == "GENERAL":
        return general_chain.invoke(
            {
                "input": question,
                "chat_history": history
            }
        )

    # Handle unexpected intent

    else:
        return "Sorry, I couldn't understand your request. Please try again."


# 3. Create RAG Chain

rag_chain = RunnableLambda(route_request)
