from sqlmodel import Session, select
from models.actor_model import Actor, Film_Actor
from models.film_model import Film
from sqlalchemy.orm import selectinload

def get_all_actors(session: Session):
    """Get all actors from the database."""
    statement = select(Actor)
    return session.exec(statement).all()

def getActorById(session: Session, id: int):
    """Get actor by id from the database."""
    #statement = select(Actor).where(Actor.actor_id == id)#.options(selectinload(Film_Actor.actor))
    statement = (
        select(Actor).where(Actor.actor_id == id).options(selectinload(Actor.film_actors).selectinload(Film_Actor.film))
        )
    return session.exec(statement).first()
