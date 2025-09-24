from sqlalchemy.orm import Session
from .. import schemas
from .. import models
from fastapi import HTTPException, status

def all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(db: Session, request: schemas.Blog):        
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id, db: Session, ):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with the id {id} is not available")
    return blog


def update_blog(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"id {id} is not found")
    db.commit()
    return "updated"


def delete_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Done"}

