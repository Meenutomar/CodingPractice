from backend.payment.PaymentBackend import getPaymentById, get_all_payments
from models.payment_model import PaymentListView,PaymentDetailView
from models.customer_model import CustomersListView
from sqlmodel import Session
import datetime

class PaymentService:
    def __init__(self):
        self.payment_cache_data = {}
        


    def fetchPaymentById(self, session: Session, id):

        startTime = datetime.datetime.now()
        print("-------------------------------Enter DB call", startTime )
        self.checkAndUpdateCache(session)
        

        
        payment = self.payment_cache_data.get(id)
        print("Fetched from Cache....", payment)
            
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
        self.checkAndUpdateCache(session)
    
        payment_list: List[PaymentListView] = [PaymentListView(
            payment_id = payment.payment_id,
            customer_id= payment.customer_id,
        
        #   amount = payment.amount,
        #  payment_date = payment.payment_date,
            
            rental_id= payment.rental_id,
            staff_id= payment.staff_id,
        )
        for key, payment in  self.payment_cache_data.items()]
        print("-------------------------------Exit DB call", (datetime.datetime.now()-startTime).total_seconds())

        return payment_list


    def cachePayments(self, payments):
        for payment in payments:
            #print("Payment::", i, type(i))
            key = payment.payment_id
            value =  payment
            print("Key::", key, " Value::", value)
            self.payment_cache_data.setdefault(key,value)

        print("Data cached.....", len(self.payment_cache_data))

    def checkAndUpdateCache(self, session):
        if(len(self.payment_cache_data) == 0):
            print("Caching Data.....")
            payments = get_all_payments(session)
            #self.payment_cache_data = {payments[i]: payments[i+1] for i in range(0,len(payments))}
            print("Cache Data:", self.payment_cache_data)
            self.cachePayments(payments)
        else:
            print("Data already cached.....", len(self.payment_cache_data))
       
        