from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.review import Review, db
from models.tour import Tour

reviews_bp = Blueprint('reviews', __name__)

@ reviews_bp.route('/reviews', methods=['POST'])
@ jwt_required()
def create_review():
    identity = get_jwt_identity()
    data = request.get_json()
    tour_id = data.get('tourId')
    rating = data.get('rating')
    comment = data.get('comment')
    if not (1 <= rating <= 5):
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400
    tour = Tour.query.get_or_404(tour_id)
    review = Review(
        tour_id=tour_id,
        user_id=identity['id'],
        rating=rating,
        comment=comment
    )
    db.session.add(review)
    db.session.commit()
    return jsonify({'message': 'Review created successfully'}), 201

@ reviews_bp.route('/reviews/<int:tour_id>', methods=['GET'])
def get_reviews(tour_id):
    reviews = Review.query.filter_by(tour_id=tour_id).all()
    result = [{
        'id': r.id,
        'tourId': r.tour_id,
        'userId': r.user_id,
        'rating': r.rating,
        'comment': r.comment
    } for r in reviews]
    return jsonify(result), 200