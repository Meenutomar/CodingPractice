from backend.payment.PaymentBackend import getPaymentById, get_all_payments
from models.payment_model import PaymentListView,PaymentDetailView
from models.customer_model import CustomersListView
from sqlmodel import Session
import datetime

class PaymentService:
    def __init__(self):
        self.payment_cache_data = []
        

    def fetchPaymentById(self, session: Session, id):

        startTime = datetime.datetime.now()
        print("-------------------------------Enter DB call", startTime )
        
        if(len(self.payment_cache_data) == 0):
            print("Load Cache.....")
            self.payment_cache_data = get_all_payments(session)
        
        print("######################### 1 ############::", len(self.payment_cache_data))

        
        payment = None
        for i in range(len(self.payment_cache_data)):
            if(self.payment_cache_data[i].payment_id == id):
                print("######################### 2 ############")
                payment = self.payment_cache_data[i] 
            
        print("######################### 3 ############")    
        if (payment == None):
            payment = getPaymentById(session,id)
            self.payment_cache_data.append(payment)
        
        print("-------------------------------Exit DB call", (datetime.datetime.now()-startTime).total_seconds())

                

        payment_read = PaymentDetailView(
            payment_id = payment.payment_id,
            amount = payment.amount,
        #   payment_date = payment.payment_date,
            customer_id= payment.customer_id,
            customer=CustomersListView(  # ✅ This line was missing
                    customer_id=payment.customer.customer_id,
                    store_id=payment.customer.store_id,
                    first_name=payment.customer.first_name,
                    last_name=payment.customer.last_name,
                    email=payment.customer.email,
                ) if payment.customer else None,  # Avoids error if customer is None
            rental_id= payment.rental_id,
            staff_id= payment.staff_id,
            
        )
        return payment_read

    def fetchPayment(self, session: Session):
        startTime = datetime.datetime.now()
        print("-------------------------------Enter DB call", startTime )
        if(len(self.payment_cache_data) == 0):
            print("Caching Data.....")
            payments = get_all_payments(session)
            self.payment_cache_data = payments
            print("Data cached.....", len(self.payment_cache_data))
        else:
            print("Data already cached.....", len(self.payment_cache_data))
            payments =  self.payment_cache_data
        
    
        payment_list: List[PaymentListView] = [PaymentListView(
            payment_id = payment.payment_id,
            customer_id= payment.customer_id,
        
        #   amount = payment.amount,
        #  payment_date = payment.payment_date,
            
            rental_id= payment.rental_id,
            staff_id= payment.staff_id,
        )
        for payment in payments]
        print("-------------------------------Exit DB call", (datetime.datetime.now()-startTime).total_seconds())

        return payment_list

