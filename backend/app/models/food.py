from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

# from db.models import User
from db.database import Base

class Food(Base):
  __tablename__ = 'food'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  price = Column(Float, index=True)
  description = Column(String, index=True)
  owner_id = Column(Integer, ForeignKey('users_t.id'))

  owner = relationship('User', back_populates='food')