from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import adress_controller
from my_project.auth.domain.orders.Adress import Adress

adress_bp = Blueprint('adress', __name__, url_prefix='/adress')


@adress_bp.get('')
def get_all_adresses() -> Response:
    adresses = adress_controller.find_all()
    adresses_dto = [adress.put_into_dto() for adress in adresses]
    return make_response(jsonify(adresses_dto), HTTPStatus.OK)

@adress_bp.post('')
def create_adress() -> Response:
    content = request.get_json()
    adress = Adress.create_from_dto(content)
    adress_controller.create(adress)
    return make_response(jsonify(adress.put_into_dto()), HTTPStatus.CREATED)

@adress_bp.get('/<int:adress_id>')
def get_adress(adress_id: int) -> Response:
    adress = adress_controller.find_by_id(adress_id)
    if adress:
        return make_response(jsonify(adress.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Adress not found"}), HTTPStatus.NOT_FOUND)

@adress_bp.put('/<int:adress_id>')
def update_adress(adress_id: int) -> Response:
    content = request.get_json()
    adress = Adress.create_from_dto(content)
    adress_controller.update(adress_id, adress)
    return make_response("Adress updated", HTTPStatus.OK)

@adress_bp.delete('/<int:adress_id>')
def delete_adress(adress_id: int) -> Response:
    adress_controller.delete(adress_id)
    return make_response("Adress deleted", HTTPStatus.NO_CONTENT)
