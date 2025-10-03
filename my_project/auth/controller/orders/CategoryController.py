from typing import List
from my_project.auth.dao.orders.CategoryDao import CategoryDAO
from my_project.auth.domain.orders.Category import Category

class CategoryController:
    _dao = CategoryDAO()

    def find_all(self) -> List[Category]:
        return self._dao.find_all()

    def create(self, category: Category) -> None:
        self._dao.create(category)

    def find_by_id(self, category_id: int) -> Category:
        return self._dao.find_by_id(category_id)

    def update(self, category_id: int, category: Category) -> None:
        self._dao.update(category_id, category)

    def delete(self, category_id: int) -> None:
        self._dao.delete(category_id)

    def find_by_name(self, name: str) -> List[Category]:
        return self._dao.find_by_name(name)
