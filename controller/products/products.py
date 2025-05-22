from fastapi import APIRouter, Depends
from service.productService import fetchProducts, fetchProductById
from sqlmodel import Session
from backend.database import get_session
from typing import List
from models.product_model import ProductsListView

router = APIRouter()

@router.get("/products", response_model=List[ProductsListView])
def read_users(session: Session = Depends(get_session)):
    return fetchProducts(session)

@router.get("/products/{id}")
def getProductById(id: int, session: Session = Depends(get_session)):
    return fetchProductById(session, id)


