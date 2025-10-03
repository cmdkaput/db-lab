from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class OrdersHasOrderItems(db.Model, IDto):
    __tablename__ = "orders_has_orderitems"
    orders_order_id = db.Column(db.Integer, db.ForeignKey("orders.order_id"), primary_key=True)
    orderitems_order_item_id = db.Column(db.Integer, db.ForeignKey("orderitems.order_item_id"), primary_key=True)

    order = db.relationship("Order", backref="order_has_items")
    order_item = db.relationship("OrderItem", backref="item_has_orders")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "orders_order_id": self.orders_order_id,
            "orderitems_order_item_id": self.orderitems_order_item_id,
        }

    def put_into_large_dto(self) -> Dict[str, Any]:
        return {
            "order": self.order.put_into_dto() if self.order else None,
            "order_item": self.order_item.put_into_dto() if self.order_item else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> OrdersHasOrderItems:
        return OrdersHasOrderItems(**dto_dict)
