from typing import Optional
from sqlmodel import SQLModel
from pydantic import BaseModel


class Store(SQLModel, table = True):
    store_id = Optional[int](default = None, primarykey = True)
    manager_staff_id = int
    address_id = int

class StoreView(BaseModel):
    store_id = int
    manager_staff_id = int
    address_id = int
    