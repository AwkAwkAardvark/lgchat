import logging
import os
from pathlib import Path

from fastapi import APIRouter, Body, HTTPException
from langchain_community.document_loaders import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

router = APIRouter()

DEFAULT_CSV_PATH = "sample.csv"
DEFAULT_PERSIST_DIR = "chroma_db"

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_ROOT = Path(os.getenv("CSV_ROOT", str(BASE_DIR))).resolve()
PERSIST_ROOT = Path(os.getenv("PERSIST_ROOT", str(BASE_DIR / "chroma_db"))).resolve()
MAX_CSV_BYTES = int(os.getenv("MAX_CSV_BYTES", "5000000"))

logger = logging.getLogger(__name__)


def _resolve_under(base: Path, candidate: str) -> Path:
    if candidate is None or str(candidate).strip() == "":
        raise HTTPException(status_code=400, detail="Path is required")
    raw = Path(candidate)
    path = raw if raw.is_absolute() else (base / raw)
    path = path.resolve()
    try:
        path.relative_to(base)
    except ValueError:
        raise HTTPException(status_code=400, detail="Path must be within allowed directory")
    return path


@router.post("/csv/build")
def build_vector_db(
    csv_path: str = Body(DEFAULT_CSV_PATH, embed=True),
    persist_dir: str = Body(DEFAULT_PERSIST_DIR, embed=True),
):
    if not csv_path:
        raise HTTPException(status_code=400, detail="csv_path is required")
    try:
        csv_file = _resolve_under(CSV_ROOT, csv_path)
        if not csv_file.exists():
            raise HTTPException(status_code=404, detail="CSV not found")
        if not csv_file.is_file():
            raise HTTPException(status_code=400, detail="csv_path must be a file")
        if csv_file.suffix.lower() != ".csv":
            raise HTTPException(status_code=400, detail="Only .csv files are allowed")
        if csv_file.stat().st_size > MAX_CSV_BYTES:
            raise HTTPException(status_code=413, detail="CSV file is too large")

        if persist_dir in (None, "", DEFAULT_PERSIST_DIR, str(PERSIST_ROOT), PERSIST_ROOT.name):
            persist_path = PERSIST_ROOT
        else:
            persist_path = _resolve_under(PERSIST_ROOT, persist_dir)
        persist_path.mkdir(parents=True, exist_ok=True)

        loader = CSVLoader(str(csv_file))
        documents = loader.load()
        if not documents:
            raise HTTPException(status_code=400, detail="No documents loaded")
        embeddings = OpenAIEmbeddings()
        Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=str(persist_path),
        )
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Failed to build vector DB")
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"loaded": len(documents), "persist_dir": str(persist_path)}
