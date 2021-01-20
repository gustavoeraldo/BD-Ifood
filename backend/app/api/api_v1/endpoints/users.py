from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from jose import JWTError, jwt
from passlib.context import CryptContext 
import sqlalchemy

from models.user import UserBase, UserToken, UserTokenInDB
from models.token import Token
from db.database import SessionLocal, engine
from crud.user import user
from db import models
from core import security
from ..deps import get_db, get_current_user

metadata = sqlalchemy.MetaData()

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Functions for test
def fake_hased_password(password: str):
  return f'fakehashed{password}' 

@router.post('/login-user', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
  user_db = fake_users_db.get(form_data.username)
  
  if not user_db:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED, 
      detail='Incorrect username or password',
      headers={'WWW-Authenticate': 'Bearer'}
    )

  access_token = security.create_access_token(data={'sub': user.username})
  return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/token')
async def get_token(token: str = Depends(oauth2_scheme)):
  return {'token': token}


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

@router.get('/mesasa/test', response_model=UserBase)
async def get_user_info(current_user: UserBase = Depends(get_current_user)):
  return current_user
