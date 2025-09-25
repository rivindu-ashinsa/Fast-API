from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from ..import schemas, database, models, hashing
from ..token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Authentication']
)

@router.post("/login") #, response_model=schemas.ShowUser
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No username Found")
    
    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password")
    access_token = create_access_token(
        data={"sub": user.email}
    )    
    return {"access_token": access_token, "token_type": "bearer"}
 
