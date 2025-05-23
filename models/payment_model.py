from datetime import date
from typing import Optional
from sqlmodel import SQLModel, Field


class payment(SQLModel, table = True):

    payment_id: Optional[int] = Field(default = None, primary_key = True)
   # customer_id : Optional[ int] = Field(foreign_key=True)
    customer_id: int
   # staff_id : Optional[ int] = Field(foreign_key=True)
    staff_id: int
   # rental_id :  Optional[ int] = Field(foreign_key=True)
    rental_id: int
  #  payment_date:  Optional[ date] 
    amount: float

class PaymentListView(SQLModel):
    payment_id: int
    customer_id: int
    staff_id: int
    rental_id: int


class PaymentDetailView(SQLModel):
    payment_id: int
    customer_id: int
    staff_id: int
    rental_id: int
   # payment_date: date
    amount: float
