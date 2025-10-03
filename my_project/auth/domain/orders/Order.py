from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Order(db.Model, IDto):
    __tablename__ = "orders"
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.Date, nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=True)
    orderstatus_id = db.Column(db.Integer, db.ForeignKey('orderstatus.orderstatus_id'), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "order_id": self.order_id,
            "order_date": self.order_date,
            "customer_id": self.customer_id,
            "orderstatus_id": self.orderstatus_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Order:
        return Order(**dto_dict)
