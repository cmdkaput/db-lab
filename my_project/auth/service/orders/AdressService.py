from typing import List
from my_project.auth.dao import adressDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Adress

class AdressService(GeneralService):
    _dao = adressDao

    def create(self, adress: Adress) -> None:
        self._dao.create(adress)

    def get_all_adresses(self) -> List[Adress]:
        return self._dao.find_all()

    def get_adress_by_city(self, city: str) -> List[Adress]:
        return self._dao.find_by_city(city)
