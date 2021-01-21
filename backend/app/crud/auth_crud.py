from sqlalchemy.orm import Session
from typing import Optional
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from pydantic import ValidationError
from fastapi.security import OAuth2PasswordBearer

# Local imports
from core.config import settings
from api.api_v1.deps import get_db
from db.models import User
from core.config import settings
from schemas.token import TokenPayload
from crud.user import user

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
usable_oauth2 = OAuth2PasswordBearer(tokenUrl='api/v1/login')

class AuthController():
  def create_access_token(
    data: dict, expires_delta: Optional[timedelta]= None)->str:
    if expires_delta:
      expire = datetime.utcnow() + expires_delta
    else:
      expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
      )
    
    to_encode = data.copy()
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, 'HS256')
    
    return encoded_jwt

  
  def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)
    
  
  def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


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
