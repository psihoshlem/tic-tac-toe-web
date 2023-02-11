import os
import hashlib

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    login: str
    password: str

users = []

@router.post("/reg")
async def reg(user: User):
    login = user.login
    password = user.password
    for user in users:
        if login==user['login']:
            return False
    
    salt = os.urandom(32)
    password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    data={
        'login':login,
        'password':password,
        'salt':salt
    }
    users.append(data)
    print(users)
    return True

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