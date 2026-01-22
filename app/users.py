from fastapi import APIRouter, Body, HTTPException

router = APIRouter()

@router.post("/users")
def get_user(user_id: int = Body(..., embed=True)):
    users = {
        1: "Alice",
        2: "Bob",
        3: "Charlie",
    }
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, "name": users[user_id]}
