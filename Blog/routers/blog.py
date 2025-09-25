from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models
from typing import List
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user


router = APIRouter(
    tags=['blogs'],
    prefix="/blog"
)


@router.get("/", status_code=200, response_model=List[schemas.ShowBlog])
def all(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user)
):
    return blog.all(db)


@router.post("/", status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):        
    return blog.create(db, request)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog.show(id,db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session=Depends(get_db)):
    return blog.update_blog(id, request)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.delete_blog(id, db)
