from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Category import Category  # Імпортуйте модель Category

class CategoryDAO(GeneralDAO):
    _domain_type = Category

    def create(self, category: Category) -> None:
        self._session.add(category)
        self._session.commit()

    def find_all(self) -> List[Category]:
        return self._session.query(Category).all()

    def find_by_name(self, category_name: str) -> List[Category]:
        return self._session.query(Category).filter(Category.category_name == category_name).all()
