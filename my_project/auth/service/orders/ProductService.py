from typing import List
from my_project.auth.dao import productDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Product

class ProductService(GeneralService):
    _dao = productDao

    def create(self, product: Product) -> None:
        self._dao.create(product)

    def get_all_products(self) -> List[Product]:
        return self._dao.find_all()

    def get_product_by_name(self, product_name: str) -> List[Product]:
        return self._dao.find_by_name(product_name)
