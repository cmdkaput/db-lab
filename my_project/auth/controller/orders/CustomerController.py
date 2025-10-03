from typing import List
from my_project.auth.dao.orders.CustomerDao import CustomerDAO
from my_project.auth.domain.orders.Customer import Customer

class CustomerController:
    _dao = CustomerDAO()

    def find_all(self) -> List[Customer]:
        return self._dao.find_all()

    def create(self, customer: Customer) -> None:
        self._dao.create(customer)

    def find_by_id(self, customer_id: int) -> Customer:
        return self._dao.find_by_id(customer_id)

    def update(self, customer_id: int, customer: Customer) -> None:
        self._dao.update(customer_id, customer)

    def delete(self, customer_id: int) -> None:
        self._dao.delete(customer_id)

    def find_by_email(self, email: str) -> Customer:
        return self._dao.get_customer_by_email(email)
