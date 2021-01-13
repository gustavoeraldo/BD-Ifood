from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
  name : str
  email: EmailStr
  cnpj_cpf : str
  password : str
  
  class Config:
    orm_mode = True
    schema_extra = {
      "example": {
        "name": "Fake user 1",
        "email": "fakeuser@example.com",
        "cnpj_cpf": "111.111.111-11",
        "password": "123"
      }
    }


class UserInDB(UserBase):
  id: int
  hashed_password: str


class UserToken(BaseModel):
  username: str
  email: EmailStr
  full_name: Optional[str] = None
  active: Optional[bool] = False


class UserUpdate(UserBase):
  pass