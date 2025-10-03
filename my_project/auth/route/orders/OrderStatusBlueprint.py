from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import order_status_controller
from my_project.auth.domain.orders.OrderStatus import OrderStatus

order_status_bp = Blueprint('order_status', __name__, url_prefix='/order_status')

@order_status_bp.get('')
def get_all_order_statuses() -> Response:
    statuses = order_status_controller.find_all()
    statuses_dto = [status.put_into_dto() for status in statuses]
    return make_response(jsonify(statuses_dto), HTTPStatus.OK)

@order_status_bp.post('')
def create_order_status() -> Response:
    content = request.get_json()
    status = OrderStatus.create_from_dto(content)
    order_status_controller.create(status)
    return make_response(jsonify(status.put_into_dto()), HTTPStatus.CREATED)

@order_status_bp.get('/<int:status_id>')
def get_order_status(status_id: int) -> Response:
    status = order_status_controller.find_by_id(status_id)
    if status:
        return make_response(jsonify(status.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Order status not found"}), HTTPStatus.NOT_FOUND)

@order_status_bp.put('/<int:status_id>')
def update_order_status(status_id: int) -> Response:
    content = request.get_json()
    status = OrderStatus.create_from_dto(content)
    order_status_controller.update(status_id, status)
    return make_response("Order status updated", HTTPStatus.OK)

@order_status_bp.delete('/<int:status_id>')
def delete_order_status(status_id: int) -> Response:
    order_status_controller.delete(status_id)
    return make_response("Order status deleted", HTTPStatus.NO_CONTENT)
