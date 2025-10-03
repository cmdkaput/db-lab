from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import category_controller
from my_project.auth.domain.orders.Category import Category

category_bp = Blueprint('category', __name__, url_prefix='/category')

@category_bp.get('')
def get_all_categories() -> Response:
    categories = category_controller.find_all()
    categories_dto = [category.put_into_dto() for category in categories]
    return make_response(jsonify(categories_dto), HTTPStatus.OK)

@category_bp.post('')
def create_category() -> Response:
    content = request.get_json()
    category = Category.create_from_dto(content)
    category_controller.create(category)
    return make_response(jsonify(category.put_into_dto()), HTTPStatus.CREATED)

@category_bp.get('/<int:category_id>')
def get_category(category_id: int) -> Response:
    category = category_controller.find_by_id(category_id)
    if category:
        return make_response(jsonify(category.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Category not found"}), HTTPStatus.NOT_FOUND)

@category_bp.put('/<int:category_id>')
def update_category(category_id: int) -> Response:
    content = request.get_json()
    category = Category.create_from_dto(content)
    category_controller.update(category_id, category)
    return make_response("Category updated", HTTPStatus.OK)

@category_bp.delete('/<int:category_id>')
def delete_category(category_id: int) -> Response:
    category_controller.delete(category_id)
    return make_response("Category deleted", HTTPStatus.NO_CONTENT)
