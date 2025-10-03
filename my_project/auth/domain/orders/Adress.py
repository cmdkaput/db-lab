from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Adress(db.Model, IDto):
    __tablename__ = "adress"
    adress_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(60), nullable=True)
    street = db.Column(db.String(60), nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"adress_id": self.adress_id, "country": self.country, "city": self.city, "street": self.street}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Adress:
        return Adress(**dto_dict)
