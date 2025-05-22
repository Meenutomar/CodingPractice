from sqlmodel import SQLModel, Session, select, Field


# def read_users(session: Session = Depends(get_session)):
   
#     return session.exec(select(Users)).all()


from sqlmodel import Session, select
from models.user_model import Users

def get_all_users(session: Session):
    statement = select(Users)
    return session.exec(statement).all()

def getuserById(session: Session,id):
    statement = select(Users).where(Users.id == id)
    return session.exec(statement).one()



