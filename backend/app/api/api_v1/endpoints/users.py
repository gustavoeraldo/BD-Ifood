from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import sqlalchemy

from models.user import UserBase
from db.database import engine
from crud.user import user
from db import models
from ..deps import get_db
from crud.auth_crud import AuthController

metadata = sqlalchemy.MetaData()

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get("/{user_id}")
async def read_users(user_id, db: Session = Depends(get_db)):
  """
  Return all users
  """
  return user.get_user(db=db, user_id=user_id) 


@router.post("/", response_model=UserBase)
async def create_user(user_in: UserBase, db: Session = Depends(get_db))->UserBase:
  """
  Create User
  """
  db_user = user.create_user(db=db, user_in=user_in)
  if db_user:
    raise HTTPException(
      status_code = 400,
      detail = "The user already exist in the system."
    )

  return db_user

# Next endpoint that I must work
@router.post('/restaurant')
async def create_restaurant_user():
  return {'restaurant_user': 'Created successfully'}


@router.get('/mesasa/test', response_model=UserBase)
async def get_user_info(current_user: UserBase = Depends(AuthController.get_current_user)):
  return current_user
