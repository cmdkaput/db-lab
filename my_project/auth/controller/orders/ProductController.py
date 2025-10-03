from typing import List
from my_project.auth.dao.orders.ProductDao import ProductDAO
from my_project.auth.domain.orders.Product import Product

class ProductController:
    _dao = ProductDAO()

    def find_all(self) -> List[Product]:
        return self._dao.find_all()

    def create(self, product: Product) -> None:
        self._dao.create(product)

    def find_by_id(self, product_id: int) -> Product:
        return self._dao.find_by_id(product_id)

    def update(self, product_id: int, product: Product) -> None:
        self._dao.update(product_id, product)

    def delete(self, product_id: int) -> None:
        self._dao.delete(product_id)

    def find_by_name(self, name: str) -> List[Product]:
        return self._dao.find_by_name(name)
