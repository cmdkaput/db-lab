from typing import List
from my_project.auth.dao.orders.OrderItemDao import OrderItemDAO
from my_project.auth.domain.orders.OrderItem import OrderItem

class OrderItemController:
    _dao = OrderItemDAO()

    def find_all(self) -> List[OrderItem]:
        return self._dao.find_all()

    def create(self, order_item: OrderItem) -> None:
        self._dao.create(order_item)

    def find_by_id(self, order_item_id: int) -> OrderItem:
        return self._dao.find_by_id(order_item_id)

    def update(self, order_item_id: int, order_item: OrderItem) -> None:
        self._dao.update(order_item_id, order_item)

    def delete(self, order_item_id: int) -> None:
        self._dao.delete(order_item_id)

    def find_by_product_id(self, product_id: int) -> List[OrderItem]:
        return self._dao.find_by_product_id(product_id)
