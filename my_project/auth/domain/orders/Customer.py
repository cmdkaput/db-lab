from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Customer(db.Model, IDto):
    __tablename__ = "customers"
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone_number = db.Column(db.String(25), nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"customer_id": self.customer_id, "customer_name": self.customer_name, "email": self.email, "phone_number": self.phone_number}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Customer:
        return Customer(**dto_dict)
