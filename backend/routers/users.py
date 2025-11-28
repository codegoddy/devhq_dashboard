from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from .auth import get_current_user

router = APIRouter()

class User(BaseModel):
    id: int
    username: str
    email: str
    role: str = "user"
    is_active: bool = True

# Mock users data - in production, fetch from main DevHQ backend
MOCK_USERS = [
    {"id": 1, "username": "user1", "email": "user1@example.com", "role": "user", "is_active": True},
    {"id": 2, "username": "user2", "email": "user2@example.com", "role": "user", "is_active": True},
]

@router.get("/", response_model=List[User])
async def get_users(current_user: str = Depends(get_current_user)):
    # In production, proxy request to main DevHQ backend
    return MOCK_USERS

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int, current_user: str = Depends(get_current_user)):
    user = next((u for u in MOCK_USERS if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=User)
async def create_user(user: User, current_user: str = Depends(get_current_user)):
    # In production, proxy to main backend
    new_user = user.dict()
    new_user["id"] = len(MOCK_USERS) + 1
    MOCK_USERS.append(new_user)
    return new_user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: User, current_user: str = Depends(get_current_user)):
    # In production, proxy to main backend
    for i, u in enumerate(MOCK_USERS):
        if u["id"] == user_id:
            MOCK_USERS[i] = user.dict()
            MOCK_USERS[i]["id"] = user_id
            return MOCK_USERS[i]
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
async def delete_user(user_id: int, current_user: str = Depends(get_current_user)):
    # In production, proxy to main backend
    for i, u in enumerate(MOCK_USERS):
        if u["id"] == user_id:
            del MOCK_USERS[i]
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")