
import streamlit as st

from langchain_core.messages import HumanMessage, AIMessage
from src.rag_pipeline import rag_chain


# 1. Page Configuration
st.set_page_config(
    page_title="Conversational RAG Chatbot",
    page_icon="🤖",
    layout="centered"
)


# 2. Custom Styling
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .stChatMessage {
        border-radius: 12px;
    }

    h1 {
        color: #2563eb;
        text-align: center;
    }

    .subtitle {
        text-align: center;
        color: gray;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)


# 3. Application Header
st.title("🤖 Conversational RAG Chatbot")

st.markdown(
    '<p class="subtitle">Ask questions about your company policy documents</p>',
    unsafe_allow_html=True
)

st.divider()


# 4. Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "messages" not in st.session_state:
    st.session_state.messages = []


# 5. Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    st.write("**Knowledge Base:**")
    st.success("Company Policy PDF")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.messages = []
        st.rerun()

    st.caption("Powered by LangChain + FAISS")


# 6. Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# 7. User Input
question = st.chat_input("Ask something about company policies...")

if question:

    # Display user question
    st.chat_message("user").markdown(question)

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Searching documents and generating answer..."):

            try:
                answer = rag_chain.invoke({
                    "input": question,
                    "chat_history": st.session_state.chat_history[-10:]
                })

                st.markdown(answer)

                # Store conversation history
                st.session_state.chat_history.append(
                    HumanMessage(content=question)
                )

                st.session_state.chat_history.append(
                    AIMessage(content=answer)
                )

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")
