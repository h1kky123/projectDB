from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from routes.auth import auth_bp
from routes.tours import tours_bp
from routes.bookings import bookings_bp
from routes.reviews import reviews_bp
from models import db

# Инициализация приложения
app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_object(Config)
CORS(app)
db.init_app(app)
JWTManager(app)

# Регистрация blueprints
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(tours_bp, url_prefix='/api')
app.register_blueprint(bookings_bp, url_prefix='/api')
app.register_blueprint(reviews_bp, url_prefix='/api')

# Создание таблиц
with app.app_context():
    db.create_all()

# Отдача статических файлов (JS, CSS, изображения и т.д.)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

# Отдача index.html для корневого маршрута и вложенных путей SPA
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
