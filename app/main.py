from fastapi import Body, FastAPI
from app.users import router as users_router

app = FastAPI()

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