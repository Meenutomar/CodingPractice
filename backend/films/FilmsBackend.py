from sqlmodel import SQLModel, Session, select, Field
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from models.film_model import Film, Category, Film_Category


def get_all_films(session: Session):
    statement = select(Film)
    return session.exec(statement).all()

def getFilmById(session: Session, id):
    #statement = select(Film).where(Film.film_id == id)
    #return session.exec(statement).one()

    statement = (
        select(Film).where(Film.film_id == id).options(selectinload(Film.film_category).selectinload(Film_Category.category))

    )
    return session.exec(statement).first()