from fastapi import APIRouter, Depends ,HTTPException
from sqlalchemy.orm import Session
from typing import List

from models.user import UserBase, UserCreate
from db.database import SessionLocal, engine
import crud 
from db import models

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/", response_model=List[UserBase])
def read_users():
  """
  Return all users
  """
  users = crud.user.get_multi()
  return users


@router.post("/", response_model=UserBase)
def create_user(user_in: UserBase, db: Session = Depends(get_db)):
  """
  Create User
  """
  db_user = crud.user.create_user(db=db, user_in=user_in)
  if db_user:
    raise HTTPException(
      status_code = 400,
      detail = "The user already exist in the system."
    )

  return db_user
