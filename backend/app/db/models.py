from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

# from models.food import FoodBase
from .database import Base
from models.food import Food

class User(Base):
  __tablename__ = 'users_t'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  email = Column(String, index= True)
  cpf_cnpj = Column(String, unique=True, index=True)
  hashed_password = Column(String)

  food = relationship('Food', back_populates='owner')
