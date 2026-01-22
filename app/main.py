from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from app.users import router as users_router
from app.chat import router as chat_router
from app.csvloader import router as csv_router

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "app" / "static"
INDEX_FILE = STATIC_DIR / "index.html"

app = FastAPI()

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/")
def read_root():
    return FileResponse(str(INDEX_FILE))

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello_default():
    return {"message": "Hello, meatbag."}

@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"Hello, {name}"}

@app.get("/add")
def add(a: int, b: int):
    return {"sum": a + b}

app.include_router(users_router)
app.include_router(chat_router)
app.include_router(csv_router)
