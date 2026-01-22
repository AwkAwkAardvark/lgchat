# Project Context

## Project Description
A chatbot application built with LangChain and FastAPI, capable of RAG (Retrieval Augmented Generation) using CSV data.

## Tech Stack
*   **Backend:** Python 3.10+, FastAPI
*   **AI/ML:** LangChain, OpenAI (GPT-4/Embeddings), ChromaDB (Vector Store)
*   **Frontend:** HTML/CSS (Static files serving)
*   **Environment:** Linux (WSL), Git

## Recent Progress
*(Newest summaries should be added immediately below this line)*

- **2026-01-22**: Implemented persistent, stateful chat module (`app/chat.py`) using `ConversationChain` and in-memory session storage. Updated frontend to match API schema.
- **2026-01-22**: Refactored documentation to support individual agent logs (`docs/logs/`) keyed by git credentials, enabling concurrent work and user preferences while maintaining a shared project context.
- **2026-01-22**: Initial setup of agent documentation and workflow structure.
- **2026-01-22**: Added CSV loader functionality (`app/csvloader.py`), refactored `main.py` for path safety and router inclusion, and cleaned up `chat.py`.
