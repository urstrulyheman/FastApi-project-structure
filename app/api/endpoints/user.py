from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.schemas.user import User, UserCreate
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=User)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user = crud.user.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud.user.create_user(db=db, user=user_in)
    return user
