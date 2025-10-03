from typing import List
from my_project.auth.dao import customerDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Customer

class CustomerService(GeneralService):
    _dao = customerDao

    def create(self, customer: Customer) -> None:
        self._dao.create(customer)

    def get_all_customers(self) -> List[Customer]:
        return self._dao.find_all()

    def get_customer_by_email(self, email: str) -> Customer:
        return self._dao.find_by_email(email)
