from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import product_controller
from my_project.auth.domain.orders.Product import Product

product_bp = Blueprint('product', __name__, url_prefix='/product')

@product_bp.get('')
def get_all_products() -> Response:
    products = product_controller.find_all()
    products_dto = [product.put_into_dto() for product in products]
    return make_response(jsonify(products_dto), HTTPStatus.OK)

@product_bp.post('')
def create_product() -> Response:
    content = request.get_json()
    product = Product.create_from_dto(content)
    product_controller.create(product)
    return make_response(jsonify(product.put_into_dto()), HTTPStatus.CREATED)

@product_bp.get('/<int:product_id>')
def get_product(product_id: int) -> Response:
    product = product_controller.find_by_id(product_id)
    if product:
        return make_response(jsonify(product.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Product not found"}), HTTPStatus.NOT_FOUND)

@product_bp.put('/<int:product_id>')
def update_product(product_id: int) -> Response:
    content = request.get_json()
    product = Product.create_from_dto(content)
    product_controller.update(product_id, product)
    return make_response("Product updated", HTTPStatus.OK)

@product_bp.delete('/<int:product_id>')
def delete_product(product_id: int) -> Response:
    product_controller.delete(product_id)
    return make_response("Product deleted", HTTPStatus.NO_CONTENT)
