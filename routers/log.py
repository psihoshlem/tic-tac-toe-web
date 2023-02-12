import os
import hashlib

from fastapi import APIRouter
from pydantic import BaseModel

from databases.bases import add_new_user, is_user_exist

router = APIRouter()

class User(BaseModel):
    login: str
    password: str

users = []

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
    login = user.login
    password = user.password
    id=-1
    for i in range(0, len(users)):
        if login==users[i]['login']:
            id=i
    if id==-1:
        return False
    if hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), users[id]['salt'], 100000)==users[id]['password']:
        return True
    else:
        return False