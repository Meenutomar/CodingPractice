from typing import List, Optional
from sqlmodel import Session
from backend.staff.staff_backend import get_all_staffs, getStaffById
from models.staff_model import Staff, StaffsDetailView, StaffsListView


class StaffService:
    def __init__(self):
        self.staff_cache_data = {}

    def fetchStaffs(self,session: Session) -> List[StaffsDetailView]: 
        # Fetch staffs from database
        self.checkAndUpdateCache(session)
        #print(session)

        staff_list: List[StaffsDetailView] = [
            StaffsDetailView(
                staff_id=staff.staff_id,
                first_name=staff.first_name,
                last_name=staff.last_name,
                email=staff.email,
                address_id=staff.address_id,
                store_id = staff.store_id,
                active = staff.active,
                username= staff.username,

   

            )
            for staff in self.staff_cache_data.values()
        ]
        return staff_list

    def fetchStaffsById(self, session: Session, id: int) -> Optional[StaffsListView]:
        # Fetch staff by id from cache or database
        self.checkAndUpdateCache(session)
        staff = self.staff_cache_data.get(id)
        print("mujhe mila staff",staff)
        if staff is None:
            staff = getStaffById(session, id)
            if staff:
                self.staff_cache_data[staff.staff_id] = staff

        if staff:
            return StaffsListView(
                staff_id=staff.staff_id,
                first_name=staff.first_name,
                last_name=staff.last_name,
                email=staff.email,
                address_id=staff.address_id
            )
        return None

    def cacheStaff(self, staff_list: List[Staff]):
        # Cache staff data
        for staff in staff_list:
            self.staff_cache_data[staff.staff_id] = staff
    
    def checkAndUpdateCache(self, session: Session):
        if len(self.staff_cache_data) == 0:
            staff_list = get_all_staffs(session)
            self.cacheStaff(staff_list)
        else:
            print("Data already cached.....", len(self.staff_cache_data))
