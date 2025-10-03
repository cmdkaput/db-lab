from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Review(db.Model, IDto):
    __tablename__ = "reviews"
    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating = db.Column(db.Integer, nullable=True)
    comment = db.Column(db.Text, nullable=True)
    review_date = db.Column(db.Date, nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "review_id": self.review_id,
            "rating": self.rating,
            "comment": self.comment,
            "review_date": self.review_date,
            "product_id": self.product_id,
            "customer_id": self.customer_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Review:
        return Review(**dto_dict)
