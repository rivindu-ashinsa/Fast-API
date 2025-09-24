from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, hashing
from typing import List
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
     tags=['users'],
     prefix='/user'
)

@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db : Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def show_user(id : int, db: Session = Depends(get_db)): 
    return user.show(id, db)
