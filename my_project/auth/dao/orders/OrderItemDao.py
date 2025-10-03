from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.OrderItem import OrderItem  # Імпортуйте модель OrderItem

class OrderItemDAO(GeneralDAO):
    _domain_type = OrderItem

    def create(self, order_item: OrderItem) -> None:
        self._session.add(order_item)
        self._session.commit()

    def find_all(self) -> List[OrderItem]:
        return self._session.query(OrderItem).all()

    def find_by_product_id(self, product_id: int) -> List[OrderItem]:
        return self._session.query(OrderItem).filter(OrderItem.product_id == product_id).all()
