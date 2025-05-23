from sqlmodel import SQLModel, Session, select, Field


# def read_users(session: Session = Depends(get_session)):
   
#     return session.exec(select(Users)).all()


from sqlmodel import Session, select
from models.payment_model import payment


def get_all_payments(session: Session):
    statement = select(payment)
    return session.exec(statement).all()

def getPaymentById(session: Session, id):
    statement = select(payment).where(payment.payment_id == id)
    return session.exec(statement).one()