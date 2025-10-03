from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Customer import Customer  # Імпортуйте модель Customer

class CustomerDAO(GeneralDAO):
    _domain_type = Customer

    def create(self, customer: Customer) -> None:
        self._session.add(customer)
        self._session.commit()

    def find_all(self) -> List[Customer]:
        return self._session.query(Customer).all()

    def find_by_email(self, email: str) -> Customer:
        return self._session.query(Customer).filter(Customer.email == email).first()

