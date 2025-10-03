from typing import List
from my_project.auth.dao import categoryDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders import Category

class CategoryService(GeneralService):
    _dao = categoryDao

    def create(self, category: Category) -> None:
        self._dao.create(category)

    def get_all_categories(self) -> List[Category]:
        return self._dao.find_all()

    def get_category_by_name(self, category_name: str) -> List[Category]:
        return self._dao.find_by_name(category_name)
