from typing import Generator
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import ValidationError

from db.database import SessionLocal, engine
from db.models import User
from core.config import settings
from schemas.token import TokenPayload
from crud.user import user

usable_oauth2 = OAuth2PasswordBearer(
  tokenUrl=f'api/v1/login')

# Dependency
def get_db() -> Generator:
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

def get_current_user(
  db: Session = Depends(get_db), token: str = Depends(usable_oauth2)
  ) -> User:
  try:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    token_data = TokenPayload(**payload)
  except (JWTError, ValidationError):
    raise HTTPException(
      status_code = status.HTTP_403_FORBIDDEN,
      detail = f'Could not validate user credentials.'
    )

  user_db = user.get_user(db, user_id=token_data.id)
  if not user_db:
    raise HTTPException(
      status_code = 404,
      detail = 'User not found.' 
    )

  return user_db