from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "dialect+driver://username:password@host:port/database"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:docker@localhost:5435/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()