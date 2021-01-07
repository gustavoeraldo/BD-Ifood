from pydantic import BaseModel

class Token(BaseModel):
  access_token: str
  token_type: str # restaurant or costumer

class TokenPayload(BaseModel):
  username: str = None