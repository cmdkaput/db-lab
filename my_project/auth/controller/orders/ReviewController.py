from typing import List
from my_project.auth.dao.orders.ReviewDao import ReviewDAO
from my_project.auth.domain.orders.Review import Review

class ReviewController:
    _dao = ReviewDAO()

    def find_all(self) -> List[Review]:
        return self._dao.find_all()

    def create(self, review: Review) -> None:
        self._dao.create(review)

    def find_by_id(self, review_id: int) -> Review:
        return self._dao.find_by_id(review_id)

    def update(self, review_id: int, review: Review) -> None:
        self._dao.update(review_id, review)

    def delete(self, review_id: int) -> None:
        self._dao.delete(review_id)

    def find_by_product_id(self, product_id: int) -> List[Review]:
        return self._dao.find_by_product_id(product_id)
