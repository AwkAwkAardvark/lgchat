from fastapi import Body, APIRouter
import pandas as pd
import numpy as np
import os
import sqlite3
from datetime import datetime

import openai

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryBufferMemory

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

router = APIRouter()

@router.post("/chat")
def chat(message: str = Body(...)):
    return {"you_said": message}
