from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Category(db.Model, IDto):
    __tablename__ = "categories"
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(100), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"category_id": self.category_id, "category_name": self.category_name}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Category:
        return Category(**dto_dict)
