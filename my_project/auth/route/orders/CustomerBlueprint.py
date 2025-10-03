from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import customer_controller
from my_project.auth.domain.orders.Customer import Customer

customer_bp = Blueprint('customer', __name__, url_prefix='/customer')

@customer_bp.get('')
def get_all_customers() -> Response:
    customers = customer_controller.find_all()
    customers_dto = [customer.put_into_dto() for customer in customers]
    return make_response(jsonify(customers_dto), HTTPStatus.OK)

@customer_bp.post('')
def create_customer() -> Response:
    content = request.get_json()
    customer = Customer.create_from_dto(content)
    customer_controller.create(customer)
    return make_response(jsonify(customer.put_into_dto()), HTTPStatus.CREATED)

@customer_bp.get('/<int:customer_id>')
def get_customer(customer_id: int) -> Response:
    customer = customer_controller.find_by_id(customer_id)
    if customer:
        return make_response(jsonify(customer.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Customer not found"}), HTTPStatus.NOT_FOUND)

@customer_bp.put('/<int:customer_id>')
def update_customer(customer_id: int) -> Response:
    content = request.get_json()
    customer = Customer.create_from_dto(content)
    customer_controller.update(customer_id, customer)
    return make_response("Customer updated", HTTPStatus.OK)

@customer_bp.delete('/<int:customer_id>')
def delete_customer(customer_id: int) -> Response:
    customer_controller.delete(customer_id)
    return make_response("Customer deleted", HTTPStatus.NO_CONTENT)
