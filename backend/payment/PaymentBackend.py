from sqlmodel import SQLModel, Session, select, Field


# def read_users(session: Session = Depends(get_session)):
   
#     return session.exec(select(Users)).all()


from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from models.payment_model import payment


def get_all_payments(session: Session):
    statement = (
        select(payment)
        .options(selectinload(payment.customer))  # This loads the customer relationship
    )
    return session.exec(statement).all()

def getPaymentById(session: Session, id):
    statement = select(payment).where(payment.payment_id == id).options(selectinload(payment.customer))  # Add this!)
    return session.exec(statement).one()