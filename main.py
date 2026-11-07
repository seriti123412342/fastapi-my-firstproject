from fastapi import FastAPI, HTTPException
import endpoints
import uvicorn
from schemas import *
from datetime import timezone, datetime
from db import setup_database, async_engine
from contextlib import asynccontextmanager
from models import Base

app = FastAPI()

app.include_router(endpoints.router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await setup_database()
    yield





if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
