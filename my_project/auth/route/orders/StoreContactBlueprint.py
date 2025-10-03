from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import store_contact_controller
from my_project.auth.domain.orders.StoreContact import StoreContact

store_contact_bp = Blueprint('store_contact', __name__, url_prefix='/store_contact')

@store_contact_bp.get('')
def get_all_store_contacts() -> Response:
    contacts = store_contact_controller.find_all()
    contacts_dto = [contact.put_into_dto() for contact in contacts]
    return make_response(jsonify(contacts_dto), HTTPStatus.OK)

@store_contact_bp.post('')
def create_store_contact() -> Response:
    content = request.get_json()
    contact = StoreContact.create_from_dto(content)
    store_contact_controller.create(contact)
    return make_response(jsonify(contact.put_into_dto()), HTTPStatus.CREATED)

@store_contact_bp.get('/<int:contact_id>')
def get_store_contact(contact_id: int) -> Response:
    contact = store_contact_controller.find_by_id(contact_id)
    if contact:
        return make_response(jsonify(contact.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Store contact not found"}), HTTPStatus.NOT_FOUND)

@store_contact_bp.put('/<int:contact_id>')
def update_store_contact(contact_id: int) -> Response:
    content = request.get_json()
    contact = StoreContact.create_from_dto(content)
    store_contact_controller.update(contact_id, contact)
    return make_response("Store contact updated", HTTPStatus.OK)

@store_contact_bp.delete('/<int:contact_id>')
def delete_store_contact(contact_id: int) -> Response:
    store_contact_controller.delete(contact_id)
    return make_response("Store contact deleted", HTTPStatus.NO_CONTENT)
