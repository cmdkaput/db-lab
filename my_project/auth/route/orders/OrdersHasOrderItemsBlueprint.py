from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import orders_has_order_items_controller
from my_project.auth.domain.orders.OrdersHasOrderItems import OrdersHasOrderItems
from my_project.auth.controller.orders.OrdersHasOrderItemsController import OrdersHasOrderItemsController

orders_has_order_items_bp = Blueprint('orders_has_order_items', __name__, url_prefix='/orders_has_order_items')
controller = OrdersHasOrderItemsController()

@orders_has_order_items_bp.post('')
def create_order_item() -> Response:
    content = request.get_json()
    orders_item = OrdersHasOrderItems.create_from_dto(content)
    orders_has_order_items_controller.create(orders_item)
    return make_response(jsonify(orders_item.put_into_dto()), HTTPStatus.CREATED)

@orders_has_order_items_bp.delete('')
def delete_order_item() -> Response:
    content = request.get_json()
    order_id = content.get("order_id")
    order_item_id = content.get("order_item_id")
    if order_id and order_item_id:
        orders_has_order_items_controller.delete_by_composite_key(order_id, order_item_id)
        return make_response("Order item relation deleted", HTTPStatus.NO_CONTENT)
    return make_response(
        jsonify({"error": "Invalid request data. 'order_id' and 'order_item_id' are required."}),
        HTTPStatus.BAD_REQUEST
    )

@orders_has_order_items_bp.get('')
def get_all_orders_items_and_details() -> Response:
    orders_items = orders_has_order_items_controller.find_all_with_related_data()
    orders_items_dto = [item.put_into_large_dto() for item in orders_items]
    return make_response(jsonify(orders_items_dto), HTTPStatus.OK)

