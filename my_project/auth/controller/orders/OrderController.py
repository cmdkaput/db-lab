from typing import List
from my_project.auth.dao.orders.OrderDao import OrderDAO
from my_project.auth.domain.orders.Order import Order

class OrderController:
    _dao = OrderDAO()

    def find_all(self) -> List[Order]:
        return self._dao.find_all()

    def create(self, order: Order) -> None:
        self._dao.create(order)

    def find_by_id(self, order_id: int) -> Order:
        return self._dao.find_by_id(order_id)

    def update(self, order_id: int, order: Order) -> None:
        self._dao.update(order_id, order)

    def delete(self, order_id: int) -> None:
        self._dao.delete(order_id)

    def find_by_customer_id(self, customer_id: int) -> List[Order]:
        return self._dao.find_by_customer_id(customer_id)
