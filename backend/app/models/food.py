from typing import List, Optional, Union, 
from pydantic import BaseModel, EmailStr

class FoodBase(BaseModel):
  id = int
  name = str
  price = float
  description = Optional[str] = None
  owner_id = int

  class Config:
    orm_mode = True
