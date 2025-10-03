from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class OrderStatus(db.Model, IDto):
    __tablename__ = "orderstatus"
    orderstatus_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(20), nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "orderstatus_id": self.orderstatus_id,
            "status": self.status
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> OrderStatus:
        return OrderStatus(**dto_dict)
