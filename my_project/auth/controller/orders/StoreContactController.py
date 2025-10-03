from typing import List
from my_project.auth.dao.orders.StoreContactDao import StoreContactDAO
from my_project.auth.domain.orders.StoreContact import StoreContact

class StoreContactController:
    _dao = StoreContactDAO()

    def find_all(self) -> List[StoreContact]:
        return self._dao.find_all()

    def create(self, contact: StoreContact) -> None:
        self._dao.create(contact)

    def find_by_id(self, contact_id: int) -> StoreContact:
        return self._dao.find_by_id(contact_id)

    def update(self, contact_id: int, contact: StoreContact) -> None:
        self._dao.update(contact_id, contact)

    def delete(self, contact_id: int) -> None:
        self._dao.delete(contact_id)

    def find_by_store_id(self, store_id: int) -> List[StoreContact]:
        return self._dao.find_by_store_id(store_id)
