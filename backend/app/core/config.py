import secrets
from pydantic import BaseSettings, PostgresDsn
from typing import Optional


class Settings(BaseSettings):
  API_V1_STR: str = "/api/v1"
  SECRET_KEY: str = 'u3iVLzL_A7vBurgiOksFMzg4RTKzp8GEVzQkBW1gUe0SRb2-01aRVor4HUsYe6TjoTAjEzACuna55KLysHVP2A'#secrets.token_urlsafe(32)
  ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8# expires in 8 days

  # Database server
  POSTGRES_SERVER: str = None
  POSTGRES_USER: str = None
  POSTGRES_PASSWORD: str = None
  POSTGRES_DB: str = None
  SQLALCHEMY_DATABASE_URI: Optional[str] = None

settings = Settings()