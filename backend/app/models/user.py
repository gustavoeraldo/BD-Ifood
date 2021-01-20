from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
  name : str
  email: EmailStr
  cpf_cnpj : str
  hashed_password : str
  
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

class UserToken(BaseModel):
  username: str
  email: EmailStr
  full_name: Optional[str] = None
  active: Optional[bool] = False

class UserTokenInDB(UserToken):
  hashed_password: str