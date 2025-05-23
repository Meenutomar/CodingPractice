from backend.payment.PaymentBackend import getPaymentById, get_all_payments
from models.payment_model import PaymentListView,PaymentDetailView
from models.customer_model import CustomersListView
from sqlmodel import Session

def fetchPaymentById(session: Session, id):
    payment = getPaymentById(session,id)
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

def fetchPayment(session: Session):
    payments = get_all_payments(session)

    payment_list: List[PaymentListView] = [PaymentListView(
        payment_id = payment.payment_id,
        customer_id= payment.customer_id,
       
     #   amount = payment.amount,
      #  payment_date = payment.payment_date,
        
        rental_id= payment.rental_id,
        staff_id= payment.staff_id,
    )
    for payment in payments]

    return payment_list

