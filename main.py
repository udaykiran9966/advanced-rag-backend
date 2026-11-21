
from langchain_core.messages import HumanMessage, AIMessage

from src.rag_pipeline import rag_chain


# 1. Conversation History Storage

storage = {}


# 2. Get Session History

def get_session_history(session_id):

    if session_id not in storage:
        storage[session_id] = []

    return storage[session_id]


# 3. Create User Session

session_id = "user_1"

chat_history = get_session_history(session_id)


# 4. Start the Chatbot

print("\nWelcome To Conversational RAG Chatbot")
print("\nType 'exit' or 'quit' to stop the chatbot")


# 5. Chat Loop

while True:

    question = input("\nYou: ").strip()

    # Exit chatbot

    if question.lower() in ["exit", "quit"]:
        print("\nExiting Conversational RAG Chatbot...")
        break

    # Handle empty input

    if not question:
        print("Please enter a question.")
        continue

    try:

        # 6. Invoke RAG Chain

        answer = rag_chain.invoke({
            "input": question,
            "chat_history": chat_history[-10:]
        })

        print("\nAI:", answer)

        # 7. Store Human Message

        chat_history.append(
            HumanMessage(content=question)
        )

        # 8. Store AI Message

        chat_history.append(
            AIMessage(content=answer)
        )

    except Exception as e:

        print("\nError:", str(e))
