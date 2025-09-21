from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List


app = FastAPI()


models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog", status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):        
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog", status_code=200, response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with the id {id} is not available")
    return blog


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"id {id} is not found")
    db.commit()
    return "updated"


@app.delete("/blog/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Done"}


@app.post("/user", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db : Session = Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email, password = request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
