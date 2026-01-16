from fastapi import Body, APIRouter

router = APIRouter()

@router.post("/chat")
def chat(message: str = Body(...)):
    return {"you_said": message}