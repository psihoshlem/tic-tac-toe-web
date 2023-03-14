import os
import hashlib

from fastapi import APIRouter
from pydantic import BaseModel

from databases.bases import add_new_user, is_user_exist, get_user_data

router = APIRouter()

class User(BaseModel):
    login: str
    password: str


@router.post("/reg")
async def reg(user: User):
    login = user.login
    password = user.password
    if not is_user_exist(login):
        salt = os.urandom(32)
        password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        data={
            'login':login,
            'password':password,
            'salt':salt
        }
        add_new_user(data)
        return True
    else:
        return False

@router.post("/log")
async def log(user: User):
    if not is_user_exist(user.login):
        return False
    else:
        password_from_db, salt = get_user_data(user.login)
        return hashlib.pbkdf2_hmac('sha256', user.password.encode('utf-8'), salt, 100000) == password_from_db