from typing import List
from my_project.auth.dao import orderDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Order

class OrderService(GeneralService):
    _dao = orderDao

    def create(self, order: Order) -> None:
        self._dao.create(order)

    def get_all_orders(self) -> List[Order]:
        return self._dao.find_all()

    def get_orders_by_customer_id(self, customer_id: int) -> List[Order]:
        return self._dao.find_by_customer_id(customer_id)
