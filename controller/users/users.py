from fastapi import APIRouter, Depends
from service.UserService import fetchUsers, fetchUserById

from sqlmodel import Session
from backend.database import get_session
from typing import List
from models.user_model import UserListView


router = APIRouter()

@router.get("/users", response_model=List[UserListView])
def read_users(session: Session = Depends(get_session)):
    return fetchUsers(session)

@router.get("/users/{id}")
def get_userById(id: int, session: Session = Depends(get_session)):
    return fetchUserById(session, id)






