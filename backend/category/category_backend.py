from sqlmodel import Session, select
from errors.TechnicalException import TechnicalException
from models.category_model import CategoryView
from models.film_model import Category
import logging as LOG

def get_all_category(session:Session):
    try:
        statement = select(Category)
        return session.exec(statement).all()
    except Exception as e:
        raise TechnicalException(str(e))
    
def get_category_by_id(session:Session,id:int):
    try:
        statement = select(Category).where(Category.category_id == id)
        return session.exec(statement).first()
    except Exception as e:
        raise TechnicalException(str(e))
    
def create_category(session: Session, category: Category):
    try:
        session.add(category)
    except Exception as e:
        session.rollback()
        LOG.error("Error occurred: ", e)
        raise TechnicalException("Error creating category")

def get_category_by_name(session:Session,name: str):
    LOG.info(f"{__name__} fetching name: {name}")
    try:
        statement = select(Category).where(Category.name == name)
        return session.exec(statement).first()
    except Exception as e:
        raise TechnicalException(str(e))