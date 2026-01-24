# Project Context

## Project Description
A chatbot application built with LangChain and FastAPI, capable of RAG (Retrieval Augmented Generation) using CSV data.

## Tech Stack
*   **Backend:** Python 3.10+, FastAPI
*   **AI/ML:** LangChain, OpenAI (GPT-4/Embeddings), ChromaDB (Vector Store)
*   **Frontend:** HTML/CSS (Static files serving)
*   **Environment:** Linux (WSL), Git

## Roadmap / Active Tasks
- [ ] **Dockerization**
    - [x] Create `Dockerfile` (Python 3.11-slim, multi-stage if needed).
    - [x] Create `docker-compose.yml` (Volume mounts for persistence).
    - [x] Build local image (Success).
    - [ ] Launch container (`docker compose up`) and verify.
- [ ] **Remote Access (Post-Docker)**
    - [ ] Set up Cloudflare Tunnel (sidecar container).
    - [ ] Configure Cloudflare Access for authentication.

## Recent Progress
*(Newest summaries should be added immediately below this line)*

- **2026-01-24**: Implemented Docker infrastructure (`Dockerfile`, `docker-compose.yml`) and successfully built the image after resolving WSL integration issues. Ready for initial launch.
- **2026-01-22**: Finalized session: Modern chat UI (`chat.html`) is live, `python-dotenv` environment issues resolved, and default model updated to `gpt-o4-mini`. Evaluated `sample.csv` for future RAG implementation.
- **2026-01-22**: Updated default OpenAI model to `gpt-o4-mini` in `app/settings.py`.
- **2026-01-22**: Added `app/static/chat.html`, a dedicated, modern UI for the chat functionality with message history and session management. Resolved `python-dotenv` environment issues.
- **2026-01-22**: Synchronized frontend and backend:
    - Updated `app/static/index.html` to support `session_id` input for stateful chat.
    - Updated `app/chat.py` to return standard JSON objects.
    - Resolved WSL/Windows environment conflicts by establishing a Linux-native workflow.
- **2026-01-22**: Implemented persistent, stateful chat module (`app/chat.py`) using `ConversationChain` and in-memory session storage. Updated frontend to match API schema.
- **2026-01-22**: Refactored documentation to support individual agent logs (`docs/logs/`) keyed by git credentials, enabling concurrent work and user preferences while maintaining a shared project context.
- **2026-01-22**: Initial setup of agent documentation and workflow structure.
- **2026-01-22**: Added CSV loader functionality (`app/csvloader.py`), refactored `main.py` for path safety and router inclusion, and cleaned up `chat.py`.
