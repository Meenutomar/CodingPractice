from backend.users.UsersBackend import get_all_users, getuserById
from sqlmodel import Session
from models.user_model import UserRead,UserListView
from typing import List



def fetchUsers(session: Session) :
    userData = get_all_users(session)
    # Convert Users to UserReadWithName
    user_list: List[UserRead] = [
        UserRead(
            id=user.id,
            email=user.email,
            gender=user.gender,
            age=user.age,
            name=f"{user.first_name} {user.last_name}"
        )
        for user in userData
    ]
    return user_list

def fetchUserById(session: Session,id):
    user = getuserById(session, id)
    return user


    




