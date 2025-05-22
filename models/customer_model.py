from datetime import date
from sqlmodel import SQLModel, Field
from typing import Optional

class Customer(SQLModel, table=True,):
    customer_id: Optional[int] = Field(default=None, primary_key=True)
    store_id: int
    first_name: str
    last_name: str
    email: str
    address_id: int
    activebool: bool
    create_date: date
    last_update: date
    active: int



   

class CustomersListView(SQLModel):
    customer_id: Optional[int]
    store_id: int
    first_name: str
    last_name: str
    email: str
   

class CustomersDetailView(SQLModel):
    customer_id: Optional[int]
    store_id: int
    first_name: str
    last_name: str
    email: str
    address_id: int
    activebool: bool
    creat_date: date
    last_update: date
    active: int





    