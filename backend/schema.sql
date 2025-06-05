CREATE DATABASE IF NOT EXISTS travel_db;
USE travel_db;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    role ENUM('admin', 'user') NOT NULL DEFAULT 'user'
);

CREATE TABLE tour (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    price FLOAT NOT NULL,
    description TEXT,
    image VARCHAR(255),  -- URL изображения
    days INT,           -- Количество дней
    groupSize INT,      -- Размер группы
    type VARCHAR(50)    -- Тип тура (например, "спокойный")
);

CREATE TABLE review (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tour_id INT NOT NULL,
    user_id INT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT NOT NULL,
    FOREIGN KEY (tour_id) REFERENCES tour(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE booking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    tour_id INT NOT NULL,
    booking_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_status VARCHAR(20) DEFAULT 'pending',  -- pending, paid, failed
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (tour_id) REFERENCES tour(id)
);

-- Тестовые данные для туров
INSERT INTO tour (name, destination, country, city, price, description, image, days, groupSize, type)
VALUES
    ('Пляжный отдых', 'Мальдивы', 'Мальдивы', 'Мале', 1200.00, 'Отдых на белоснежных пляжах.', '/images/maldives.png', 7, 10, 'спокойный'),
    ('Городское приключение', 'Париж', 'Франция', 'Париж', 900.00, 'Исследуйте город огней.', '/images/paris.png', 4, 15, 'активный'),
    ('Бали', 'Бали', 'Индонезия', 'Денпасар', 45000.00, 'Тур на Бали.', '/images/bali.png', 4, 10, 'спокойный'),
    ('Швейцарские Альпы', 'Альпы', 'Швейцария', 'Церматт', 23000.00, 'Горный тур.', '/images/alps.png', 6, 13, 'активный');

-- Тестовые данные для пользователей
INSERT INTO user (username, password, email, role)
VALUES
    ('admin', '$2b$12$8Xz5Qz6t5z7Y6X8Y9Z0A1e2B3C4D5E6F7G8H9I0J', 'admin@example.com', 'admin'),
    ('user', '$2b$12$8Xz5Qz6t5z7Y6X8Y9Z0A1e2B3C4D5E6F7G8H9I0J', 'user@example.com', 'user');

-- Тестовые данные для отзывов
INSERT INTO review (tour_id, user_id, rating, comment)
VALUES
    (1, 1, 5, 'Потрясающий отдых! Рекомендую всем!'),
    (2, 1, 4, 'Хороший тур, но дороговато.');

-- Тестовые данные для бронирований
INSERT INTO booking (user_id, tour_id, payment_status)
VALUES
    (2, 1, 'paid'),
    (2, 2, 'pending');