from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta

from core.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_access_token(
  data: dict, expires_delta: Optional[timedelta] = None 
) -> str:
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
  