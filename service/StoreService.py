from typing import List
from sqlmodel import Session
from controller.staffs import store
from models.store_model import StoreView
from backend.staff.store_backend import get_StoreById, get_all_store

def fetchStore(session: Session):
    # Fetch all stores from the database
    stores = get_all_store(session)
    store_list : List[StoreView] = [
        StoreView(
            id=store.store_id,
            manager_staff_id =store.manager_staff_id ,
            address_id=store.address_id
           
            
        )
        for store in stores
        
    ]
    return store_list



