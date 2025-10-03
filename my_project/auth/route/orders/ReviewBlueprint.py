from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import review_controller
from my_project.auth.domain.orders.Review import Review

review_bp = Blueprint('review', __name__, url_prefix='/review')

@review_bp.get('')
def get_all_reviews() -> Response:
    reviews = review_controller.find_all()
    reviews_dto = [review.put_into_dto() for review in reviews]
    return make_response(jsonify(reviews_dto), HTTPStatus.OK)

@review_bp.post('')
def create_review() -> Response:
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)

@review_bp.get('/<int:review_id>')
def get_review(review_id: int) -> Response:
    review = review_controller.find_by_id(review_id)
    if review:
        return make_response(jsonify(review.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Review not found"}), HTTPStatus.NOT_FOUND)

@review_bp.put('/<int:review_id>')
def update_review(review_id: int) -> Response:
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.update(review_id, review)
    return make_response("Review updated", HTTPStatus.OK)

@review_bp.delete('/<int:review_id>')
def delete_review(review_id: int) -> Response:
    review_controller.delete(review_id)
    return make_response("Review deleted", HTTPStatus.NO_CONTENT)
