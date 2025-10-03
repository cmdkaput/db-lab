from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Store import Store  # Імпортуйте модель Store

class StoreDAO(GeneralDAO):
    _domain_type = Store

    def create(self, store: Store) -> None:
        self._session.add(store)
        self._session.commit()

    def find_all(self) -> List[Store]:
        return self._session.query(Store).all()

    def find_by_brand_id(self, brand_id: int) -> List[Store]:
        return self._session.query(Store).filter(Store.brand_id == brand_id).all()
