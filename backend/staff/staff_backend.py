from sqlmodel import Session, select
from models.staff_model import Staff


def get_all_staffs(sessin:Session):
    """Get all staffs from the database."""
    statement = select(Staff)
    return sessin.exec(statement).all()

def getStaffById(session:Session,id):
    """Get staff by id from the database."""
    statement = select(Staff).where(Staff.staff_id == id)
    return session.exec(statement).one()
    
    