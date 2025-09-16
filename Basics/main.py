from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None): # Query parameters
    if published:
        return {"data" : f"{limit} published  Blog list from the database"}
    else:
        return {"data" : f"{limit} Blog list from the database"}

@app.get("/blog/unpublished")
def unpublished():
    return {'data' : 'unpublished'}



@app.get("/blog/{id}")
def show(id: int):
    return {"data": id
    }


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {"1", "2"}}


class Blog(BaseModel):
    title:str
    body: str
    published: Optional[bool]




@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog is created as the title {request.title}"}