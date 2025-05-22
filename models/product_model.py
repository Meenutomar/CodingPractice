from sqlmodel import SQLModel, Field
from typing import Optional

class Products(SQLModel, table=True,):
    ProductID: Optional[int] = Field(default=None, primary_key=True)
    
    ProductName: str
    Description: str
    Price: float
   

class ProductsListView(SQLModel):
    ProductID: Optional[int]
    ProductName: str
    Price: float

class ProductsDetailView(SQLModel):
    ProductID: Optional[int]
    ProductName: str
    Description: str
    Price: float


    