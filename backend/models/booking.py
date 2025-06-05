from . import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False)
    booking_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    payment_status = db.Column(db.String(20), default='pending')
