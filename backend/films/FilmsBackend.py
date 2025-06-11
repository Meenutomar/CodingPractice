from typing import List
from sqlmodel import SQLModel, Session, select, Field
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from errors.TechnicalException import TechnicalException
from models.film_model import Film, Category, Film_Category


def get_all_films(session: Session):
    try:
        statement = select(Film)
        return session.exec(statement).all()
    except Exception as e:
        raise TechnicalException(str(e))

def getFilmById(session: Session, id):
    #statement = select(Film).where(Film.film_id == id)
    #return session.exec(statement).one()

    statement = (
        select(Film).where(Film.film_id == id).options(selectinload(Film.film_category).selectinload(Film_Category.category))

    )
    return session.exec(statement).first()

def create_film(session: Session, film):
    # Create a film
    return ""

# def fetch_category_by_name(session: Session, categories: List[str]):
#     statement = select(Category).where(Category.category_name.in_(categories))
#     return session.exec(statement).all()