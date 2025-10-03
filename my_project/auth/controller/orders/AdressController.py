from typing import List
from my_project.auth.dao.orders.AdressDao import AdressDAO
from my_project.auth.domain.orders.Adress import Adress

class AdressController:
    _dao = AdressDAO()

    def find_all(self) -> List[Adress]:
        return self._dao.find_all()

    def create(self, adress: Adress) -> None:
        self._dao.create(adress)

    def find_by_id(self, adress_id: int) -> Adress:
        return self._dao.find_by_id(adress_id)

    def update(self, adress_id: int, adress: Adress) -> None:
        self._dao.update(adress_id, adress)

    def delete(self, adress_id: int) -> None:
        self._dao.delete(adress_id)

    def find_by_city(self, city: str) -> List[Adress]:
        return self._dao.find_by_city(city)
