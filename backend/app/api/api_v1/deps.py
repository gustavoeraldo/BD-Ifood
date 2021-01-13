from typing import Generator
from sqlalchemy.orm import Session

from db.database import SessionLocal, engine

# Dependency
def get_db() -> Generator:
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
