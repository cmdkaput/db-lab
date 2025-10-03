from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Review import Review  # Імпортуйте модель Review

class ReviewDAO(GeneralDAO):
    _domain_type = Review

    def create(self, review: Review) -> None:
        self._session.add(review)
        self._session.commit()

    def find_all(self) -> List[Review]:
        return self._session.query(Review).all()

    def find_by_product_id(self, product_id: int) -> List[Review]:
        return self._session.query(Review).filter(Review.product_id == product_id).all()
