from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from pydantic import BaseModel

from db.base_class import Base

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchematype = TypeVar('UpdateSchematype', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchematype]):
  def __init__(self, model: Type[ModelType]):
    '''
    CRUD object with default methods to Create, Read, Update, Delete (CRUD).
    **Parameters**
    * `model`: A SQLAlchemy model class
    * `schema`: A Pydantic model (schema) class
    '''

    self.model = model
