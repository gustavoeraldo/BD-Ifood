from sqlalchemy.orm import Session

from models.user import UserBase
from db import models

def get():
  return {
    "Name": "Fake user 1"
  }

def get_multi():
  return [{'Name':'User 1'}, {'Name':'User 2'}]

def create_user(db:Session, user_in: UserBase):
  db_user = models.User(name=user_in.name,email=user_in.email)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)

  return db_user
