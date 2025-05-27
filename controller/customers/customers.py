from fastapi import APIRouter, Depends
from service.CustomerService import CustomerService
from sqlmodel import Session
from backend.databasepaglu import get_session_pagli
from typing import List
from models.customer_model import CustomersListView
        


router = APIRouter()
customerService =  CustomerService()

@router.get("/customers", response_model=List[CustomersListView])
def read_customer(session: Session = Depends(get_session_pagli)):
    return customerService.fetchCustomers(session)

@router.get("/customers/{id}")
def getCustomerById(id: int, session: Session = Depends(get_session_pagli)):
    return customerService.fetchCustomerById(session, id)


