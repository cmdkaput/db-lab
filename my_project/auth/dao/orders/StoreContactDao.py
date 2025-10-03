from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.StoreContact import StoreContact  # Імпортуйте модель StoreContact

class StoreContactDAO(GeneralDAO):
    _domain_type = StoreContact

    def create(self, contact: StoreContact) -> None:
        self._session.add(contact)
        self._session.commit()

    def find_all(self) -> List[StoreContact]:
        return self._session.query(StoreContact).all()

    def find_by_store_id(self, store_id: int) -> List[StoreContact]:
        return self._session.query(StoreContact).filter(StoreContact.store_id == store_id).all()
