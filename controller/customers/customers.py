from fastapi import APIRouter, Depends
from service.CustomerService import fetchCustomers, fetchCustomerById
from sqlmodel import Session
from backend.databasepaglu import get_session_pagli
from typing import List
from models.customer_model import CustomersListView

router = APIRouter()

@router.get("/customers", response_model=List[CustomersListView])
def read_customer(session: Session = Depends(get_session_pagli)):
    return fetchCustomers(session)

@router.get("/customers/{id}")
def getCustomerById(id: int, session: Session = Depends(get_session_pagli)):
    return fetchCustomerById(session, id)


