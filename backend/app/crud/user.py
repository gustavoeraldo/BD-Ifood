from sqlalchemy.orm import Session

from models.user import UserBase

def get():
  return {
    "Name": "Fake user 1"
  }

def get_multi():
  return [{'Name':'User 1'}, {'Name':'User 2'}]

def create_user(db:Session, user_in: UserBase):
  db.add(user_in)
  db.commit()
  db.refresh(user_in)

  return user_in
