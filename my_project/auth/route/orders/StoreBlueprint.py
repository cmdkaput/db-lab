from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import store_controller
from my_project.auth.domain.orders.Store import Store

store_bp = Blueprint('store', __name__, url_prefix='/store')

@store_bp.get('')
def get_all_stores() -> Response:
    stores = store_controller.find_all()
    stores_dto = [store.put_into_dto() for store in stores]
    return make_response(jsonify(stores_dto), HTTPStatus.OK)

@store_bp.post('')
def create_store() -> Response:
    content = request.get_json()
    store = Store.create_from_dto(content)
    store_controller.create(store)
    return make_response(jsonify(store.put_into_dto()), HTTPStatus.CREATED)

@store_bp.get('/<int:store_id>')
def get_store(store_id: int) -> Response:
    store = store_controller.find_by_id(store_id)
    if store:
        return make_response(jsonify(store.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Store not found"}), HTTPStatus.NOT_FOUND)

@store_bp.put('/<int:store_id>')
def update_store(store_id: int) -> Response:
    content = request.get_json()
    store = Store.create_from_dto(content)
    store_controller.update(store_id, store)
    return make_response("Store updated", HTTPStatus.OK)

@store_bp.delete('/<int:store_id>')
def delete_store(store_id: int) -> Response:
    store_controller.delete(store_id)
    return make_response("Store deleted", HTTPStatus.NO_CONTENT)
