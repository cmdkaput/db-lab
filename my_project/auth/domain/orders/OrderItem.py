from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class OrderItem(db.Model, IDto):
    __tablename__ = "orderitems"
    order_item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"order_item_id": self.order_item_id, "product_id": self.product_id, "quantity": self.quantity, "price": self.price}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> OrderItem:
        return OrderItem(**dto_dict)
