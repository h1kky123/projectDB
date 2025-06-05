from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.tour import Tour, db
from models.review import Review

tours_bp = Blueprint('tours', __name__)

@ tours_bp.route('/tours', methods=['GET'])
def get_tours():
    tours = Tour.query.all()
    result = []
    for tour in tours:
        reviews = Review.query.filter_by(tour_id=tour.id).all()
        avg_rating = sum(r.rating for r in reviews) / len(reviews) if reviews else 0
        result.append({
            'id': tour.id,
            'name': tour.name,
            'destination': tour.destination,
            'country': tour.country,
            'city': tour.city,
            'price': tour.price,
            'description': tour.description,
            'image': tour.image,
            'days': tour.days,
            'groupSize': tour.groupSize,
            'type': tour.type,
            'rating': round(avg_rating, 1),
            'reviews': len(reviews)
        })
    return jsonify(result), 200

@ tours_bp.route('/tours', methods=['POST'])
@ jwt_required()
def create_tour():
    identity = get_jwt_identity()
    if identity['role'] != 'admin':
        return jsonify({'error': 'Admin access required'}), 403
    data = request.get_json()
    tour = Tour(
        name=data['title'],
        destination=data['city'],
        country=data['country'],
        city=data['city'],
        price=float(data['price']),
        description=data['description'],
        type=data['type'],
        image=data.get('image', '/images/default.png'),
        days=data.get('days', 1),
        groupSize=data.get('groupSize', 10)
    )
    db.session.add(tour)
    db.session.commit()
    return jsonify({'message': 'Tour created successfully'}), 201

@ tours_bp.route('/tours/<int:tour_id>', methods=['DELETE'])
@ jwt_required()
def delete_tour(tour_id):
    identity = get_jwt_identity()
    if identity['role'] != 'admin':
        return jsonify({'error': 'Admin access required'}), 403
    tour = Tour.query.get_or_404(tour_id)
    db.session.delete(tour)
    db.session.commit()
    return jsonify({'message': 'Tour deleted successfully'}), 200