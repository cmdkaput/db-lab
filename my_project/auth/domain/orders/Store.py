from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Store(db.Model, IDto):
    __tablename__ = "stores"
    store_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_website = db.Column(db.String(255), nullable=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.brand_id'), nullable=False)
    adress_adress_id = db.Column(db.Integer, db.ForeignKey('adress.adress_id'), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "store_id": self.store_id,
            "store_website": self.store_website,
            "brand_id": self.brand_id,
            "adress_adress_id": self.adress_adress_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Store:
        return Store(**dto_dict)
