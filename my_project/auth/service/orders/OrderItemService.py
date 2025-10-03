from typing import List
from my_project.auth.dao import orderItemDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import OrderItem

class OrderItemService(GeneralService):
    _dao = orderItemDao

    def create(self, order_item: OrderItem) -> None:
        self._dao.create(order_item)

    def get_all_order_items(self) -> List[OrderItem]:
        return self._dao.find_all()

    def get_order_item_by_product_id(self, product_id: int) -> List[OrderItem]:
        return self._dao.find_by_product_id(product_id)
