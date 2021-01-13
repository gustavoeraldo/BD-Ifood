from sqlalchemy.orm import Session
from typing import Optional, List

from schemas.foodSchema import FoodBase, FoodInDB
from models.food import Food

'''
[] - read
  [] - by name
  [] - by description
  [] - low price -> less than a fix value
[] - add
[] - edit
[] - remove
'''

class CRUDFood():
  def add_food(self, db: Session, food_in: FoodInDB, owner_id: int) -> Food:
    db_food = Food(name)
    db.add(db_food)
    db.commit()
    db.refresh(db_food)

    return db_food 

  
  def get_by_name(self, db: Session, food_name: str) -> List[Food]:
    return db.query(Food).filter(Food.name.like(f'%{food_name}%'))

  
  def get_by_description(self, db: Session, description: str) -> List[Food]:
    return db.query(Food).filter(Food.name.like(f'%{description}%'))

  # method only for admin or Restaurant
  def edit_food(self, db: Session, food_id: int, new_values: FoodBase) -> Food:
    db_food = db.update().where(Food.id == food_id).values(new_values)
    db.commit()
    db.refresh(db_food)
    return db_food

  # method only for admin or Restaurant users
  def delete_food(self, db: Session, food_id: int, new_values: FoodBase):
    db_food = db.delete().where(Food.id == food_id).values(new_values)
    db.commit()
    db.refresh(db_food)
    return db_food

food = CRUDFood()