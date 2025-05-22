from sqlmodel import SQLModel, Field
from typing import Optional

class Users(SQLModel, table=True,):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    gender: str
    age: int

class UserRead(SQLModel):
    id: Optional[int]
    name: str
    email: str
    gender: str
    age: int

class UserListView(SQLModel):
    id: Optional[int]
    name: str
