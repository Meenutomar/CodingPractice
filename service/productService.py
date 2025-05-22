from backend.products.ProductsBackend import get_all_products, getProductById
from sqlmodel import Session
from models.product_model import ProductsListView, ProductsDetailView
from typing import List

def fetchProducts(session: Session) -> List[ProductsListView]:
    productData = get_all_products(session)

    # Convert DB models to read models
    products: List[ProductsListView] = [
        ProductsListView(
            ProductID=product.ProductID,
            ProductName=product.ProductName,
            Price=product.Price
        )
        for product in productData
    ]

    return products


def fetchProductById(session: Session, id):
    product = getProductById(session, id)
    product_read = ProductsDetailView(
            ProductID=product.ProductID,
            ProductName=product.ProductName,
            Description=product.Description,
            Price=product.Price
    )
    return product_read