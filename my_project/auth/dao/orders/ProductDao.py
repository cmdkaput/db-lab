from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Product import Product  # Імпортуйте модель Product

class ProductDAO(GeneralDAO):
    _domain_type = Product

    def create(self, product: Product) -> None:
        self._session.add(product)
        self._session.commit()

    def find_all(self) -> List[Product]:
        return self._session.query(Product).all()

    def find_by_name(self, product_name: str) -> List[Product]:
        return self._session.query(Product).filter(Product.product_name == product_name).all()
