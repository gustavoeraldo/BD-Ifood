from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
  access_token: str
  token_type: str
  user_type: str

class TokenPayload(BaseModel):
  id: Optional[int] = None