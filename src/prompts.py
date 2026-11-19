from langchain_core.prompts import(
    ChatPromptTemplate,
    MessagesPlaceholder
)


intent_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an intent classification assistant.

        Classify the latest user question into exactly one category.

        DOCUMENT:
        Question requiring information from PDF documents.

        HISTORY:
        Question about previous user questions,
        AI responses, or conversation details.

        GENERAL:
        Greetings, small tasks, and general conversation.

        Use conversation history to understand follow-up questions.

        Examples:
        What is the leave policy? -> DOCUMENT
        What about others? -> DOCUMENT
        What was my last question? -> HISTORY
        How are you? -> GENERAL
        Hello -> GENERAL

        Return ONLY:
        DOCUMENT, HISTORY, or GENERAL.
        """
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])



contextualize_prompt=ChatPromptTemplate.from_messages([
    (
        "system",
    """
    Rewrite the latest user question into a standalons questions using conversation history.
    
    Rules:
    1. Do not answer the question.
    2. Do not explain anything.
    3. Do not invent information.
    4. Presrve the original meaning.
    5. If the question is already clear, return it.
    6. Return only the rewritten question.
    
    
    Example:
    
    Conversation:
    user: What is the leave policy?
    
    
    Latest Question:
    What about others?
    
    
    
    Rewritten Question?
    What other leave types are mentioned in the company policy?
    
    
    """
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{input}")
    
])

answer_prompt=ChatPromptTemplate.from_messages([
    (
        "system",
    """
    You are a document-based AI assistant.
    
    Answer using ONLY  the provided document context.
    
    Rules:
    
    1. Do not use outside knowledge.
    2. Do not assume or invent information.
    3. If information is unavailable , say:
        I Don't know based on the provided documents.
    4. Present the answer clearly.
    
    Context:
    {context}
    
    """
    ),
    ("human","{input}")
    
])


# History Answer Prompt
history_prompt=ChatPromptTemplate.from_messages([
    (
        
        "system",
    """
    You are a conversational assistant.
    
    Answer Question using conversation history.
    
    If the user asks for their last question,
    Identify the most recent previous HumanMessages.
    
    If the user what you answered earlier,
    Identify the relevent previous AIMessage.
    
    
    Do not confuse the current question with the previous questions.
    
    Do not invent conversation details.
    Answer in simple english.
    
    """
        
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{input}")
])


# General Conversation Prompt 

general_prompt=ChatPromptTemplate.from_messages([(
    "system",
    """
    You are a Friendly AI Assistent.
    
    respond naturally to greetings and small talk.
    
    keep your responce simple,polite, and conversational.
    
    Do not retrieve documents for these questions.
    
    """
    

                                                 
                                                 
),
MessagesPlaceholder(variable_name="chat_history"),
("human","{input}")

])
