from typing import Optional 
from pydantic import BaseModel

class FoodBase(BaseModel):
  name : str
  price : float
  description : Optional[str] = None

class FoodInDB(FoodBase):
  id : int
  owner_id : int
  class Config:
    orm_mode : True
