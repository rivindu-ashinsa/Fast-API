from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models
from typing import List
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/blog", status_code=200, response_model=List[schemas.ShowBlog], tags=['blogs'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post("/blog", status_code = status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schemas.Blog, db: Session = Depends(get_db)):        
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with the id {id} is not available")
    return blog


@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update_blog(id: int, request: schemas.Blog, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"id {id} is not found")
    db.commit()
    return "updated"


@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Done"}
