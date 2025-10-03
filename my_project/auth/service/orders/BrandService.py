from typing import List
from my_project.auth.dao import brandDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Brands

class BrandService(GeneralService):
    _dao = brandDao

    def create(self, brand: Brands) -> None:
        self._dao.create(brand)

    def get_all_brands(self) -> List[Brands]:
        return self._dao.find_all()

    def get_brand_by_name(self, brand_name: str) -> List[Brands]:
        return self._dao.find_by_name(brand_name)
