from typing import Optional
from sqlmodel import Field, SQLModel


class Staff(SQLModel,table = True):
    staff_id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    address_id: int
    email: str
    store_id: int
    active: bool
    username: str
    password: str

class StaffsListView(SQLModel):
    staff_id: int
    first_name: str
    last_name: str
    address_id: int
    email: str

class StaffsDetailView(SQLModel):
    staff_id: int
    first_name: str
    last_name: str
    address_id: int
    email: str
    store_id: int
    active: bool
    username: str
   # password: str

