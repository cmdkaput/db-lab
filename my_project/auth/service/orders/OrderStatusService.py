from typing import List
from my_project.auth.dao import orderStatusDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import OrderStatus

class OrderStatusService(GeneralService):
    _dao = orderStatusDao

    def create(self, status: OrderStatus) -> None:
        self._dao.create(status)

    def get_all_order_statuses(self) -> List[OrderStatus]:
        return self._dao.find_all()

    def get_status_by_name(self, status: str) -> List[OrderStatus]:
        return self._dao.find_by_status(status)
