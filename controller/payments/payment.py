from fastapi import APIRouter, Depends
from backend.databasepaglu import get_session_pagli
from models.payment_model import PaymentListView,PaymentDetailView
from service.paymentService import fetchPaymentById, fetchPayment
from sqlmodel import Session
from typing import List
from models.payment_model import PaymentDetailView,PaymentListView

router = APIRouter()

@router.get("/payments", response_model=List[PaymentListView])
def read_payments(session: Session = Depends(get_session_pagli)):
    return fetchPayment (session)

@router.get("/payments/{id}")
def getPaymentByID(id: int, session: Session = Depends(get_session_pagli)):
    return fetchPaymentById(session, id)


