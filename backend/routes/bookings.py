from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.booking import Booking, db
from models.tour import Tour

bookings_bp = Blueprint('bookings', __name__)

@ bookings_bp.route('/bookings', methods=['GET'])
@ jwt_required()
def get_bookings():
    identity = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=identity['id']).all()
    result = []
    for booking in bookings:
        tour = Tour.query.get(booking.tour_id)
        result.append({
            'id': booking.id,
            'tourId': booking.tour_id,
            'tourName': tour.name,
            'bookingDate': booking.booking_date.isoformat(),
            'paymentStatus': booking.payment_status
        })
    return jsonify(result), 200

@ bookings_bp.route('/bookings', methods=['POST'])
@ jwt_required()
def create_booking():
    identity = get_jwt_identity()
    data = request.get_json()
    tour_id = data.get('tourId')
    tour = Tour.query.get_or_404(tour_id)
    booking = Booking(user_id=identity['id'], tour_id=tour_id)
    db.session.add(booking)
    db.session.commit()
    return jsonify({'message': 'Booking created successfully'}), 201