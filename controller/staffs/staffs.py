from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session
from backend.databasepaglu import get_session_pagli
from models.staff_model import StaffsListView,StaffsDetailView
from service.StaffService import StaffService


router = APIRouter()
service = StaffService()

@router.get("/staffs",response_model= List[StaffsDetailView])
def read_staff(session: Session = Depends(get_session_pagli)):
    return service.fetchStaffs(session)

@router.get("/staffs/{id}")
def getStaffByID(id: int, session: Session = Depends(get_session_pagli)):
    print("this is id: ",id)
    return service.fetchStaffsById(session, id)