from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import order_item_controller
from my_project.auth.domain.orders.OrderItem import OrderItem

order_item_bp = Blueprint('order_item', __name__, url_prefix='/order_item')

@order_item_bp.get('')
def get_all_order_items() -> Response:
    order_items = order_item_controller.find_all()
    order_items_dto = [item.put_into_dto() for item in order_items]
    return make_response(jsonify(order_items_dto), HTTPStatus.OK)

@order_item_bp.post('')
def create_order_item() -> Response:
    content = request.get_json()
    order_item = OrderItem.create_from_dto(content)
    order_item_controller.create(order_item)
    return make_response(jsonify(order_item.put_into_dto()), HTTPStatus.CREATED)

@order_item_bp.get('/<int:order_item_id>')
def get_order_item(order_item_id: int) -> Response:
    order_item = order_item_controller.find_by_id(order_item_id)
    if order_item:
        return make_response(jsonify(order_item.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Order item not found"}), HTTPStatus.NOT_FOUND)

@order_item_bp.put('/<int:order_item_id>')
def update_order_item(order_item_id: int) -> Response:
    content = request.get_json()
    order_item = OrderItem.create_from_dto(content)
    order_item_controller.update(order_item_id, order_item)
    return make_response("Order item updated", HTTPStatus.OK)

@order_item_bp.delete('/<int:order_item_id>')
def delete_order_item(order_item_id: int) -> Response:
    order_item_controller.delete(order_item_id)
    return make_response("Order item deleted", HTTPStatus.NO_CONTENT)
