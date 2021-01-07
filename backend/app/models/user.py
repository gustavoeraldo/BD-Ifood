from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
  name : str
  email: EmailStr
  class Config:
    orm_mode = True

class UserCreate(BaseModel):
  name : str
  email: EmailStr
  cnpj_cpf : str
  password : str
  adress : str
  phone1 : str
  phone2 : Optional[str]

  class Config:
    orm_mode = True

class UserBaseInDB(UserBase):
  username : Optional[str] = None