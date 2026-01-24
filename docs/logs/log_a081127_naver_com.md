# Work Log: a081127@naver.com

## Preferences
*(Reserved for future use: languages, formatting, etc.)*

## Current Task

*(Record individual code changes and steps here as they happen)*



## History

*(Move completed tasks here - Newest on top)*

### 2026-01-24: Dockerization (Part 1)
- **Infrastructure**: Created `Dockerfile` (Python 3.11-slim) and `docker-compose.yml` with persistent volume mounts for data.
- **Environment**: Diagnosed and resolved WSL 2 Docker permission issues (requires enabling WSL integration in Docker Desktop).
- **Build**: Successfully built the Docker image `langchat-app`.
- **Status**: Ready to launch (`docker compose up`).

### 2026-01-22: Session Wrap-up

- **UI**: Delivered `chat.html` and verified static file serving.

- **Model**: Switched default to `gpt-o4-mini`.

- **RAG Prep**: Inspected `sample.csv` and identified cleaning requirements for future work.



### 2026-01-22: Model Configuration Update



- **Backend**: Updated default model to `gpt-o4-mini` in `app/settings.py`.



### 2026-01-22: Chat UI & Environment



- **UI**: Created `app/static/chat.html` with responsive design, session control, and message history.

- **Environment**: Fixed broken `python-dotenv` installation in Windows `.venv` using PowerShell.



### 2026-01-22: UI & Environment Fixes


- **Frontend**: Added `session_id` input to `index.html` and updated `postChat` payload to match backend.
- **Backend**: Updated `app/chat.py` to return consistent JSON object `{"response": ...}`.
- **Environment**: Resolved `uvicorn` path/process issues by switching to a WSL-native virtual environment (`.venv_wsl`).

### 2026-01-22: Chat Module Implementation
- **Frontend**: Updated `app/static/index.html` to send correct JSON payload `{query: ...}`.
- **Backend**: 
    - Implemented `ConversationChain` with `ConversationBufferMemory`.
    - Added global `CONVERSATIONS` dict for session persistence.
    - Updated `app/chat.py` to use `langchain_openai` and correct project settings.
    - Removed RAG dependencies (Chroma) for now as requested.

### 2026-01-22: Documentation Refactor (Individual Logs)
- Renamed generic `WORK_LOG.md` to `docs/logs/log_a081127_naver_com.md`.
- Updated `docs/AGENT_INSTRUCTIONS.md` to define the individual logging workflow and file naming conventions.
- Updated `docs/PROJECT_CONTEXT.md` to reflect the new structure.

### 2026-01-22: Setup Documentation
- Created `docs/` directory.
- Created `docs/AGENT_INSTRUCTIONS.md` with workflow definition.
- Created `docs/PROJECT_CONTEXT.md` with project overview and initial progress.
- Created `docs/WORK_LOG.md` (now this file).

### 2026-01-22: Add CSV Loader & Refactor
- Created `app/csvloader.py` for handling CSV ingestion into ChromaDB.
- Modified `app/main.py`:
    - Added `pathlib` for robust path handling.
    - Renamed hello endpoints to avoid shadowing.
    - Mounted `csv_router`.
- Modified `app/chat.py`: Removed unused imports (pandas, numpy, sqlite3, etc.) and legacy code.
- Updated `.gitignore` to exclude `sample.csv`.
- Updated `requirements.txt`.
