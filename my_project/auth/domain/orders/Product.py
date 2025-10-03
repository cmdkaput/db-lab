from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Product(db.Model, IDto):
    __tablename__ = "products"
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.brand_id'), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "description": self.description,
            "price": self.price,
            "brand_id": self.brand_id,
            "category_id": self.category_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Product:
        return Product(**dto_dict)
