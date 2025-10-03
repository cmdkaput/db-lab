from typing import List
from my_project.auth.dao import storeDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Store

class StoreService(GeneralService):
    _dao = storeDao

    def create(self, store: Store) -> None:
        self._dao.create(store)

    def get_all_stores(self) -> List[Store]:
        return self._dao.find_all()

    def get_stores_by_brand_id(self, brand_id: int) -> List[Store]:
        return self._dao.find_by_brand_id(brand_id)
