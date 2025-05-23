from datetime import date
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
from models.customer_model import CustomersListView

if TYPE_CHECKING:
    from models.customer_model import Customer


class payment(SQLModel, table = True):

    payment_id: Optional[int] = Field(default = None, primary_key = True)
    customer_id : Optional[int] = Field(foreign_key="customer.customer_id")
   # customer_id: int
   # staff_id : Optional[ int] = Field(foreign_key=True)
    staff_id: int
   # rental_id :  Optional[ int] = Field(foreign_key=True)
    rental_id: int
  #  payment_date:  Optional[ date] 
    amount: float

    # Relationships
    customer: Optional["Customer"] = Relationship(back_populates="payments")

class PaymentListView(SQLModel):
    payment_id: int
    customer_id: int
    customer: Optional[CustomersListView] = None
    staff_id: int
    rental_id: int

    class Config:
        orm_mode = True


class PaymentDetailView(SQLModel):
    payment_id: int
    customer: Optional[CustomersListView] = None
    staff_id: int
    rental_id: int
   # payment_date: date
    amount: float

    class Config:
        orm_mode = True
