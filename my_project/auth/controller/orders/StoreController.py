from typing import List
from my_project.auth.dao.orders.StoreDao import StoreDAO
from my_project.auth.domain.orders.Store import Store

class StoreController:
    _dao = StoreDAO()

    def find_all(self) -> List[Store]:
        return self._dao.find_all()

    def create(self, store: Store) -> None:
        self._dao.create(store)

    def find_by_id(self, store_id: int) -> Store:
        return self._dao.find_by_id(store_id)

    def update(self, store_id: int, store: Store) -> None:
        self._dao.update(store_id, store)

    def delete(self, store_id: int) -> None:
        self._dao.delete(store_id)

    def find_by_brand_id(self, brand_id: int) -> List[Store]:
        return self._dao.find_by_brand_id(brand_id)
