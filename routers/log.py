from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    login: str
    password: str

users = []

@router.post("/reg")
async def reg(user: User):
    users.append(user.login)
    return users