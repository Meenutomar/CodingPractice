from sqlmodel import Session, select
from models.store_model import Store

def get_all_store(session: Session):
    """Get all stores from the database."""
    statement = select(Store)

    return session.exec(statement).all()

def get_StoreById(session:Session,id):
    """Get a store by its id from the database."""
    statement = select(Store).where(Store.store_id == id)
    return session.exec(statement).first()


