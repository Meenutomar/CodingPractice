import datetime
from backend.customers.CustomersBackend import get_all_customers, getCustomerById
from sqlmodel import Session
from models.customer_model import CustomersListView, CustomersDetailView
from typing import List

class CustomerService:
    def __init__(self):
        self.customer_cache_data = {}


    def fetchCustomers(self,session: Session) -> List[CustomersListView]:
        self.checkAndUpdateCache(session)
        

        # Convert DB models to read models
        customer: List[CustomersListView] = [
            CustomersListView(

                customer_id = customer.customer_id,
                store_id = customer.store_id,


                first_name = customer.first_name,
                last_name = customer.last_name,
                email = customer.email,
            )
            for key,customer in self.customer_cache_data.items()
        ]

        return customer


    def fetchCustomerById(self,session: Session, id):
        startTime = datetime.datetime.now()
        print("-------------------------------Enter DB call", startTime )
        self.checkAndUpdateCache(session)
        customer = self.customer_cache_data.get(id)
        print("Fetched from Cache....", customer)
            
        if (customer == None):
            customer = getCustomerById(session,id)
            self.customer_cache_data.append(customer)
        
        print("-------------------------------Exit DB call", (datetime.datetime.now()-startTime).total_seconds())

        customer = getCustomerById(session, id)
        customer_read = CustomersListView(
            customer_id = customer.customer_id,
            store_id = customer.store_id,
            first_name = customer.first_name,
            last_name = customer.last_name,
            email = customer.email,
            )
        return customer_read
    
    def cacheCustomer(self,customer):
        for customer in customer:
            key = customer.customer_id
            value = customer
            self.customer_cache_data.setdefault(key,value)

        print("Data cached......", len(self.customer_cache_data))

    def checkAndUpdateCache(self, session):
        if(len(self.customer_cache_data) == 0):
            print("Caching Data.....")
            customer= get_all_customers(session)
            print("Cache Data:", self.customer_cache_data)
            self.cacheCustomer(customer)
        else:
            print("Data already cached.....", len(self.customer_cache_data))
    