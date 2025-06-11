from dataclasses import Field
from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel


# class Category(SQLModel, table = True):
#     category_id:Optional[int] = Field(default = None, primarykey = True)
#     name: str

class CategoryView(BaseModel):
    category_id: Optional[int]
    name: str

class CategoryCreateModel(BaseModel):
    category_id: Optional[int]= None
    name: str

