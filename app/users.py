from fastapi import APIRouter

router = APIRouter()

@router.post("/users")
def list_users():
    return [{"id":1, "name":"Alice"},
           {"id":2, "name":"Bob"},
           {"id":3, "name":"Charlie"}]