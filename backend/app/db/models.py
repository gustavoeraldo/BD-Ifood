from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from models.food import FoodBase
from models.user import UserBase

class User(User):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  email = Column(String)

  food = relationship('Food', back_populates='owner')

class Food(FoodBase):
  __tablename__ = 'food'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  price = Column(Float, index=True)
  description = Column(String, index=True)
  owner_id = Column(Integer, ForeignKey=('users.id'))

  owner = relationship('User', back_populates='food')