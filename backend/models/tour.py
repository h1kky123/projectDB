from . import db  # Импортируем db из models/__init__.py

class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100))
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(255))
    days = db.Column(db.Integer)
    groupSize = db.Column(db.Integer)
    type = db.Column(db.String(50))
    reviews = db.relationship('Review', backref='tour', lazy=True)
    bookings = db.relationship('Booking', backref='tour', lazy=True)
