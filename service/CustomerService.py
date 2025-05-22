from backend.customers.CustomersBackend import get_all_customers, getCustomerById
from sqlmodel import Session
from models.customer_model import CustomersListView, CustomersDetailView
from typing import List

def fetchCustomers(session: Session) -> List[CustomersListView]:
    curtomerData = get_all_customers(session)

    # Convert DB models to read models
    curtomer: List[CustomersListView] = [
        CustomersListView(

            customer_id = customer.customer_id,
            store_id = customer.store_id,


            first_name = customer.first_name,
            last_name = customer.last_name,
            email = customer.email,
            

         


        )
        for customer in curtomerData
    ]

    return curtomer


def fetchCustomerById(session: Session, id):
    customer = getCustomerById(session, id)
    customer_read = CustomersListView(
        customer_id = customer.customer_id,
        store_id = customer.store_id,
        first_name = customer.first_name,
        last_name = customer.last_name,
        email = customer.email,
        )
            

    return customer_read