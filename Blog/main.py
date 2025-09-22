from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models, hashing
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from .models import User, Blog
from .routers import blog, user

app = FastAPI()


# User.__table__.drop(engine)
# Blog.__table__.drop(engine)
models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)

