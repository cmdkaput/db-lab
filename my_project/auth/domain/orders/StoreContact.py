from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class StoreContact(db.Model, IDto):
    __tablename__ = "storecontacts"
    contact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(100), nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "contact_id": self.contact_id,
            "store_id": self.store_id,
            "phone_number": self.phone_number,
            "email": self.email
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> StoreContact:
        return StoreContact(**dto_dict)
