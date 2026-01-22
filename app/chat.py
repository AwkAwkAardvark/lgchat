from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/chat")
def chat(message: str = Body(...)):
    return {"you_said": message}
