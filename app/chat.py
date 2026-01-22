import logging
from typing import Dict

from fastapi import APIRouter, Body, HTTPException
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from app.settings import get_settings

router = APIRouter()
logger = logging.getLogger(__name__)

# Global store for active conversations to persist memory
# Key: session_id, Value: ConversationChain
CONVERSATIONS: Dict[str, ConversationChain] = {}

@router.post("/chat")
def chat(
    query: str = Body(..., embed=True),
    session_id: str = Body("default", embed=True)
):
    settings = get_settings()

    try:
        # Get or create the chain for this session
        if session_id not in CONVERSATIONS:
            # 1. LLM
            llm = ChatOpenAI(
                model_name=settings.openai_model,
                openai_api_key=settings.openai_api_key,
                temperature=settings.openai_temperature
            )

            # 2. Memory
            memory = ConversationBufferMemory(return_messages=True)

            # 3. Prompt
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are an expert on this topic. Be professional and concise."),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}")
            ])

            # 4. Chain
            chain = ConversationChain(
                llm=llm,
                memory=memory,
                prompt=prompt
            )
            
            CONVERSATIONS[session_id] = chain
        
        # Retrieve existing chain
        chain = CONVERSATIONS[session_id]

        # 5. Run
        response = chain.invoke({"input": query})
        
        return response["response"]

    except Exception as e:
        logger.exception("Chat processing failed")
        raise HTTPException(status_code=500, detail=str(e))
