from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Adress import Adress

class AdressDAO(GeneralDAO):
    _domain_type = Adress

    def create(self, adress: Adress) -> None:
        self._session.add(adress)
        self._session.commit()

    def find_all(self) -> List[Adress]:
        return self._session.query(Adress).all()

    def find_by_city(self, city: str) -> List[Adress]:
        return self._session.query(Adress).filter(Adress.city == city).all()