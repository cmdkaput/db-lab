from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Order import Order  # Імпортуйте модель Order

class OrderDAO(GeneralDAO):
    _domain_type = Order

    def create(self, order: Order) -> None:
        self._session.add(order)
        self._session.commit()

    def find_all(self) -> List[Order]:
        return self._session.query(Order).all()

    def find_by_customer_id(self, customer_id: int) -> List[Order]:
        return self._session.query(Order).filter(Order.customer_id == customer_id).all()
