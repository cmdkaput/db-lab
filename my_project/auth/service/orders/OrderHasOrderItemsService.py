from typing import List
from my_project.auth.dao import ordersHasOrderItemsDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import OrdersHasOrderItems

class OrdersHasOrderItemsService(GeneralService):
    _dao = ordersHasOrderItemsDao

    def create(self, order_item: OrdersHasOrderItems) -> None:
        self._dao.create(order_item)

    def get_all_orders_has_orderitems(self) -> List[OrdersHasOrderItems]:
        return self._dao.find_all()

    def get_by_order_id(self, order_id: int) -> List[OrdersHasOrderItems]:
        return self._dao.find_by_order_id(order_id)
