from fastapi import Body, FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from app.users import router as users_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_root():
    return FileResponse('app/static/index.html')

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "Hello, meatbag."}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}"}

@app.get("/add")
def add(a: int, b: int):
    return {"sum": a + b}

@app.post("/chat")
def chat(message: str = Body(...)):
    return {"you_said": message}

app.include_router(users_router)
