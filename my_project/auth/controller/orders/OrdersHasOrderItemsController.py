from typing import List
from my_project.auth.dao.orders.OrdersHasOrderItemsDao import OrdersHasOrderItemsDAO
from my_project.auth.domain.orders.OrdersHasOrderItems import OrdersHasOrderItems

class OrdersHasOrderItemsController:
    _dao = OrdersHasOrderItemsDAO()

    def find_all(self) -> List[OrdersHasOrderItems]:
        return self._dao.find_all()

    def find_all_with_related_data(self) -> List[OrdersHasOrderItems]:
        return self._dao.find_all_with_related_data()

    def create(self, order_item: OrdersHasOrderItems) -> None:
        self._dao.create(order_item)

    def find_by_order_id(self, order_id: int) -> List[OrdersHasOrderItems]:
        return self._dao.find_by_order_id(order_id)

    def delete(self, order_id: int, order_item_id: int) -> None:
        self._dao.delete(order_id, order_item_id)
