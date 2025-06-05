from flask_sqlalchemy import SQLAlchemy

# Создаём единый объект db
db = SQLAlchemy()

# Импортируем модели после создания db
from .user import User
from .tour import Tour
from .review import Review
from .booking import Booking

