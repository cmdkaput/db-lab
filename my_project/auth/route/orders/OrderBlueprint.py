from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import order_controller
from my_project.auth.domain.orders.Order import Order

order_bp = Blueprint('order', __name__, url_prefix='/order')

@order_bp.get('')
def get_all_orders() -> Response:
    orders = order_controller.find_all()
    orders_dto = [order.put_into_dto() for order in orders]
    return make_response(jsonify(orders_dto), HTTPStatus.OK)

@order_bp.post('')
def create_order() -> Response:
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.create(order)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.CREATED)

@order_bp.get('/<int:order_id>')
def get_order(order_id: int) -> Response:
    order = order_controller.find_by_id(order_id)
    if order:
        return make_response(jsonify(order.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Order not found"}), HTTPStatus.NOT_FOUND)

@order_bp.put('/<int:order_id>')
def update_order(order_id: int) -> Response:
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.update(order_id, order)
    return make_response("Order updated", HTTPStatus.OK)

@order_bp.delete('/<int:order_id>')
def delete_order(order_id: int) -> Response:
    order_controller.delete(order_id)
    return make_response("Order deleted", HTTPStatus.NO_CONTENT)
