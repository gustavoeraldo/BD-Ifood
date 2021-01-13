from sqlalchemy.orm import Session
from typing import Optional, List

from schemas.userSchema import UserBase, UserUpdate
from db import models
from core.security import verify_password, get_password_hash
from .base import CRUDBase

class CRUDUser(CRUDBase[models.User, UserBase, UserUpdate]):
  def get_user(self, db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


  def create_user(self, db:Session, user_in: UserBase):
    db_user = models.User(
      name=user_in.name, 
      email=user_in.email, 
      cpf_cnpj=user_in.cnpj_cpf,
      hashed_password=get_password_hash(user_in.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


  def get_by_email(self, db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()


  def authenticate(self, db: Session, email: str, password: str
  ) -> Optional[models.User]:
    # verify if the email is in db & check the password
    user = self.get_by_email(db, email)

    if not user:
      return None
    if not verify_password(password, user.hashed_password):
      return None
    
    return user 


user = CRUDUser(models.User)
