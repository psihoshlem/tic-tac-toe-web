from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from routers import log
from routers import game

# from gamelogic import app

class User(BaseModel):
    login: str
    password: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(log.router)
app.include_router(game.router)

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)