from typing import List
from my_project.auth.dao import reviewDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Review

class ReviewService(GeneralService):
    _dao = reviewDao

    def create(self, review: Review) -> None:
        self._dao.create(review)

    def get_all_reviews(self) -> List[Review]:
        return self._dao.find_all()

    def get_reviews_by_product_id(self, product_id: int) -> List[Review]:
        return self._dao.find_by_product_id(product_id)
