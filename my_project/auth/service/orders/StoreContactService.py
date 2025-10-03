from typing import List
from my_project.auth.dao import storeContactDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import StoreContact

class StoreContactService(GeneralService):
    _dao = storeContactDao

    def create(self, contact: StoreContact) -> None:
        self._dao.create(contact)

    def get_all_store_contacts(self) -> List[StoreContact]:
        return self._dao.find_all()

    def get_contacts_by_store_id(self, store_id: int) -> List[StoreContact]:
        return self._dao.find_by_store_id(store_id)
