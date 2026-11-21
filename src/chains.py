
from langchain_core.output_parsers import StrOutputParser

from src.config import llm

from src.prompts import (
    intent_prompt,
    contextualize_prompt,
    answer_prompt,
    history_prompt,
    general_prompt
)


# 1. Intent Classification Chain

intent_chain = (
    intent_prompt
    | llm
    | StrOutputParser()
)


# 2. Question Contextualization Chain

contextualize_chain = (
    contextualize_prompt
    | llm
    | StrOutputParser()
)


# 3. Document Answer Chain

document_answer_chain = (
    answer_prompt
    | llm
    | StrOutputParser()
)


# 4. History Answer Chain

history_answer_chain = (
    history_prompt
    | llm
    | StrOutputParser()
)


# 5. General Conversation Chain

general_chain = (
    general_prompt
    | llm
    | StrOutputParser()
)
