from pydantic import BaseModel

class Token(BaseModel):
  access_token: str
  token_type: str
  user_type: str

class TokenPayload(Token):
  username: str = None
  user_type: str = None