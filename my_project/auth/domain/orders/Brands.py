from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Brand(db.Model, IDto):
    __tablename__ = "brands"
    brand_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_name = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(255), nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"brand_id": self.brand_id, "brand_name": self.brand_name, "website": self.website}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Brand:
        return Brand(**dto_dict)
