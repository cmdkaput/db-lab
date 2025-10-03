from typing import List
from my_project.auth.dao.orders.OrderStatusDao import OrderStatusDAO
from my_project.auth.domain.orders.OrderStatus import OrderStatus

class OrderStatusController:
    _dao = OrderStatusDAO()

    def find_all(self) -> List[OrderStatus]:
        return self._dao.find_all()

    def create(self, order_status: OrderStatus) -> None:
        self._dao.create(order_status)

    def find_by_id(self, order_status_id: int) -> OrderStatus:
        return self._dao.find_by_id(order_status_id)

    def update(self, order_status_id: int, order_status: OrderStatus) -> None:
        self._dao.update(order_status_id, order_status)

    def delete(self, order_status_id: int) -> None:
        self._dao.delete(order_status_id)

    def find_by_status(self, status: str) -> List[OrderStatus]:
        return self._dao.find_by_status(status)
