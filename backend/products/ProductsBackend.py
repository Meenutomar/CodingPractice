from sqlmodel import SQLModel, Session, select, Field


# def read_users(session: Session = Depends(get_session)):
   
#     return session.exec(select(Users)).all()


from sqlmodel import Session, select
from models.product_model import Products


def get_all_products(session: Session):
    statement = select(Products)
    return session.exec(statement).all()

def getProductById(session: Session, id):
    statement = select(Products).where(Products.ProductID == id)
    return session.exec(statement).one()