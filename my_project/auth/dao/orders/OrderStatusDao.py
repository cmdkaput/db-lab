from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.OrderStatus import OrderStatus  # Імпортуйте модель OrderStatus

class OrderStatusDAO(GeneralDAO):
    _domain_type = OrderStatus

    def create(self, order_status: OrderStatus) -> None:
        self._session.add(order_status)
        self._session.commit()

    def find_all(self) -> List[OrderStatus]:
        return self._session.query(OrderStatus).all()

    def find_by_status(self, status: str) -> List[OrderStatus]:
        return self._session.query(OrderStatus).filter(OrderStatus.status == status).all()
