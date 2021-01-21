from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Any

from schemas.token import Token 
from crud.auth_crud import AuthController
from ..deps import get_db
from crud.user import user
from db.models import User

router = APIRouter()

@router.post('', response_model=Token)
async def login_access_token(
  form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
  ) -> Any:
  user_db = user.authenticate(
    db=db, 
    email=form_data.username, 
    password=form_data.password
  )
  if not user_db:
    raise HTTPException(
      status_code= status.HTTP_401_UNAUTHORIZED, 
      detail= 'Incorrect username or password',
      headers= {'WWW-Authenticate': 'Bearer'}
    )

  access_token = AuthController.create_access_token(data={'id': user_db.id})
  return {
    'access_token': access_token,
    'token_type': 'bearer',
    'user_type': 'costumer',
  }

# password-recovery (to do)
# reset-password (to do)
