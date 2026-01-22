# Work Log: a081127@naver.com

## Preferences
*(Reserved for future use: languages, formatting, etc.)*

## Current Task
- [2026-01-22]: Verified `python-dotenv` installation.
    - User reported VS Code resolving issue.
    - Confirmed `python-dotenv` is in `requirements.txt` and installed in `.venv_wsl`.


## History
*(Move completed tasks here - Newest on top)*

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
