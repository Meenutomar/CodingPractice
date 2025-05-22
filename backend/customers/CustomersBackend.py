from sqlmodel import SQLModel, Session, select, Field


# def read_users(session: Session = Depends(get_session)):
   
#     return session.exec(select(Users)).all()


from sqlmodel import Session, select
from models.customer_model import Customer


def get_all_customers(session: Session):
    statement = select(Customer)
    return session.exec(statement).all()

def getCustomerById(session: Session, id):
    statement = select(Customer).where(Customer.customer_id == id)
    return session.exec(statement).one()