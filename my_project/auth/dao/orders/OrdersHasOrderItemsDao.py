from typing import List
from sqlalchemy.orm import joinedload
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.OrdersHasOrderItems import OrdersHasOrderItems

class OrdersHasOrderItemsDAO(GeneralDAO):
    _domain_type = OrdersHasOrderItems

    def create(self, order_item: OrdersHasOrderItems) -> None:
        self._session.add(order_item)
        self._session.commit()

    def find_all(self) -> List[OrdersHasOrderItems]:
        return self._session.query(OrdersHasOrderItems).all()

    def find_all_with_related_data(self) -> List[OrdersHasOrderItems]:
        return (
            self._session.query(OrdersHasOrderItems)
            .options(
                joinedload(OrdersHasOrderItems.order),
                joinedload(OrdersHasOrderItems.order_item),
            )
            .all()
        )

    def find_by_order_id(self, order_id: int) -> List[OrdersHasOrderItems]:
        return self._session.query(OrdersHasOrderItems).filter(OrdersHasOrderItems.orders_order_id == order_id).all()
